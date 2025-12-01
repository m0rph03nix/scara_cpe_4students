import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import ExecuteProcess, DeclareLaunchArgument, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.conditions import IfCondition, UnlessCondition

from launch_ros.actions import Node


import xacro


def generate_launch_description():

    # Specify the name of the package and path to xacro file within the package
    pkg_name = 'scara_cpe_description'
    file_subpath = 'urdf/scara_cpe.urdf.gazebo.xacro'

    world_subpath = 'config/coins.world'


    # Use xacro to process the file
    xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    
    use_sim_time_declaration = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true')

    # Configure the node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw,
        'use_sim_time': use_sim_time}] # add other parameters here if required
    )

    # Get world for Gazebo
    world_file = os.path.join(get_package_share_directory(pkg_name),world_subpath)
    
    world = LaunchConfiguration('world')

    declare_world_cmd = DeclareLaunchArgument(
        name='world',
        default_value=world_file,
        description='Full path to the world model file to load'
    )

    declare_headless_cmd = DeclareLaunchArgument(
        name='headless',
        default_value='False',
        description='Run Gazebo in headless mode (no GUI)'
    )

    # Logic to determine gz_args
    headless = LaunchConfiguration('headless')

    # If headless is True, we want '-r -s'. If False, '-r'.
    gz_args = LaunchConfiguration('gz_args', default='-r')

    # We will default it to '-r'. User can override with '-r -s'.
    declare_gz_args_cmd = DeclareLaunchArgument(
        'gz_args',
        default_value='-r',
        description='Arguments for gz_sim'
    )

    gazebo = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('ros_gz_sim'), 'launch'), '/gz_sim.launch.py']),
            launch_arguments={'gz_args': [LaunchConfiguration('gz_args'), ' ', world]}.items()
        )


    spawn_entity = Node(package='ros_gz_sim', executable='create',
                    arguments=['-topic', 'robot_description',
                                '-name', 'scara_cpe'],
                    output='screen')

    # Bridge
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
                   ],
        output='screen'
    )

    load_joint_state_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster'],
        output='screen'
    )

    load_joint_trajectory_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['scara_cpe_group_controller'],
        output='screen'
    )



    # Run the node
    return LaunchDescription([

        use_sim_time_declaration,
        
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=spawn_entity,
                on_exit=[load_joint_state_controller],
            )
        ),
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=load_joint_state_controller,
                on_exit=[load_joint_trajectory_controller],
            )
        ),     
        declare_world_cmd,
        declare_headless_cmd,
        declare_gz_args_cmd,
        gazebo,
        node_robot_state_publisher,
        spawn_entity,
        bridge
    ])



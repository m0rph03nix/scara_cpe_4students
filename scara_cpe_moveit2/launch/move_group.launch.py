from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import SetParameter

def generate_launch_description():
    # Declare the launch argument for use_sim_time
    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='false',
        description='Use simulation (Gazebo) clock if true')

    # Create a LaunchConfiguration for use_sim_time
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Build MoveIt Configurations
    moveit_config = MoveItConfigsBuilder("scara_cpe", package_name="scara_cpe_moveit2").to_moveit_configs()

    # Set the use_sim_time parameter
    set_use_sim_time = SetParameter(name='use_sim_time', value=use_sim_time)

    # Generate and return the launch description
    return LaunchDescription([
        use_sim_time_arg,
        set_use_sim_time,
        generate_move_group_launch(moveit_config)
    ])

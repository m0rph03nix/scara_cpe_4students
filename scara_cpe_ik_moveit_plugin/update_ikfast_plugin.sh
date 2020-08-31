search_mode=OPTIMIZE_MAX_JOINT
srdf_filename=scara_cpe.srdf
robot_name_in_srdf=scara_cpe
moveit_config_pkg=scara_cpe_moveit_config
robot_name=scara_cpe
planning_group_name=scara_cpe_group
ikfast_plugin_pkg=scara_cpe_scara_cpe_group_ikfast_plugin
base_link_name=base_link
eef_link_name=end_link
ikfast_output_path=/home/raph/catkin_dir/tuto/src/scara_cpe_4students/scara_cpe_description/urdf/scara_cpe_scara_cpe_group_ikfast_plugin/src/scara_cpe_scara_cpe_group_ikfast_solver.cpp

rosrun moveit_kinematics create_ikfast_moveit_plugin.py\
  --search_mode=$search_mode\
  --srdf_filename=$srdf_filename\
  --robot_name_in_srdf=$robot_name_in_srdf\
  --moveit_config_pkg=$moveit_config_pkg\
  $robot_name\
  $planning_group_name\
  $ikfast_plugin_pkg\
  $base_link_name\
  $eef_link_name\
  $ikfast_output_path

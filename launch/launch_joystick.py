import os

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros.actions
from launch_ros.actions import Node

"""
To be used with launch_robot.py
Run this on the remote computer with the joystick
"""

# Taken from https://github.com/ros2/teleop_twist_joy/blob/foxy/launch/teleop-launch.py
def generate_launch_description():
    joy_config = launch.substitutions.LaunchConfiguration('joy_config')
    joy_dev = launch.substitutions.LaunchConfiguration('joy_dev')
    config_filepath = launch.substitutions.LaunchConfiguration('config_filepath')

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument('joy_config', default_value='xbox'),
        launch.actions.DeclareLaunchArgument('joy_dev', default_value='/dev/input/js3'),
        launch.actions.DeclareLaunchArgument('config_filepath', default_value=[
            launch.substitutions.TextSubstitution(text=os.path.join(
                get_package_share_directory('teleop_twist_joy'), 'config', '')),
            joy_config, launch.substitutions.TextSubstitution(text='.config.yaml')]),

        Node(
            package='joy', node_executable='joy_node', name='joy_node',
            parameters=[{
                'dev': joy_dev,
                'deadzone': 0.3,
                'autorepeat_rate': 20.0,
            }]),
        Node(
            package='teleop_twist_joy', node_executable='teleop_node',
            name='teleop_joy_to_cmdvel', parameters=[config_filepath])
    ])

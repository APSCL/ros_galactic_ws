from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
    	# LIDAR Node
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            name='rplidar_composition'
        ),
        
        # Transform from base_link > laser
        # Required by laser_scan_matcher
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='transform_base_link_laser',
            arguments="0 0 0 0 0 0 base_link laser".split(' ')
        ),
        
        # Transform from base_footprint > base_link
        # Required by slam_toolbox
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='transform_base_footprint_base_link',
            arguments="0 0 0 0 0 0 base_footprint base_link".split(' ')
        ),
    ])


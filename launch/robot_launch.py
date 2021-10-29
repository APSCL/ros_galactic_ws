from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
    	# rplidar Node
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
            name='transform_base_link_laser_frame',
            arguments="0 0 0 0 0 0 base_link laser_frame".split(' ')
        ),
        
        # Transform from base_link > base_footprint
        # Required by slam_toolbox
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='transform_base_link_base_footprint',
            arguments="0 0 0 0 0 0 base_link base_footprint".split(' ')
        ),
        
        # laser_scan_matcher Node
        Node(
            package='ros2_laser_scan_matcher',
            executable='laser_scan_matcher',
            name='laser_scan_matcher',
            parameters=[
		{'publish_tf': True},
		{'laser_frame': 'laser_frame'}
		]
        ),
    ])


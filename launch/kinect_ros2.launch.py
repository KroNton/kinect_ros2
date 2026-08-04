import os

import launch_ros
from launch_ros.actions.node import Node

from launch.actions.declare_launch_argument import DeclareLaunchArgument
from launch.launch_description import LaunchDescription
from launch.substitutions.launch_configuration import LaunchConfiguration


def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package="kinect_ros2").find(
        "kinect_ros2"
    )


    kinect_node=Node(
                package="kinect_ros2",
                executable="kinect_ros2_node",
                name="kinect_ros2",
                namespace="kinect",
            )
    
    static_frame_node= Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='camera_base_to_optical',
            arguments=[
                '--x', '0', '--y', '0', '--z', '1.0', 
                '--yaw', '1.5708', '--pitch', '0', '--roll', '-1.5708',
                '--frame-id', 'kinect_camera_link',
                '--child-frame-id', 'kinect_depth'
            ]
        )
    return LaunchDescription([
            static_frame_node,
            kinect_node
        ])

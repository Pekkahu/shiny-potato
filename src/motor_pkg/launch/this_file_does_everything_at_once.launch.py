from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_pkg",
            executable="controller.py",
            name="controller",
            parameters=[{"wheel_radius":75.00}]
        ),
        Node(
            package="motor_pkg",
            executable="motor_encoder.py",
            name="motor_encoder"
        ),  
        ExecuteProcess(
            cmd=['ros2', 'topic', 'list'], 
            output="screen"
        )
        ])


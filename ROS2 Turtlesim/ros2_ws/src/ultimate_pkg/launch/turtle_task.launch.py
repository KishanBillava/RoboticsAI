from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtle'
        ),
        Node(
        package='ultimate_pkg',
        # namespace='',
        executable='turtle_driver',
        name='turtle_driver'
        )
        ])


# ros2 launch pckage_name file_name :  ros2 launch ultimate_pkg turtle_task.launch.py
# ensure to update the stup.py file 



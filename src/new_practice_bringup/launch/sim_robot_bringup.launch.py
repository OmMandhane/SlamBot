from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
import os
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.conditions import UnlessCondition, IfCondition


def generate_launch_description():
    joystick = DeclareLaunchArgument("joystick",
    default_value="True")

    use_joystick = LaunchConfiguration("joystick")

    gazebo_sim = IncludeLaunchDescription(
        os.path.join(get_package_share_directory("new_robot_description"),
        "launch",
        "gazebo.launch.py")
    )

    controller =  IncludeLaunchDescription(
    os.path.join(
        get_package_share_directory("new_robot_controller"),
        "launch",
        "simple_controller.launch.py")
    )

    joystick_teleop = IncludeLaunchDescription(
        os.path.join(
        get_package_share_directory("new_robot_controller"),
        "launch",
        "joystick_teleop.launch.py"
        ),
        condition=IfCondition(use_joystick)
    )

    keyboard_node = Node(package="new_robot_controller",
                            executable="keyboard_control",
                            condition=UnlessCondition(use_joystick))

    return LaunchDescription([gazebo_sim,controller,joystick_teleop, keyboard_node])

    
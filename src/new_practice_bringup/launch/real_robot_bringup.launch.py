import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    hardware_interface = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("new_robot_firmware"),
            "launch",
            "hardware_interface.launch.py"
        ),
    )
    
    controller = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("new_robot_controller"),
            "launch",
            "simple_controller.launch.py"
        ),
        launch_arguments={
            "use_simple_controller": "True",
            "use_python": "False"
        }.items(),
    )
    
    joystick = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("new_robot_controller"),
            "launch",
            "joystick_teleop.launch.py"
        ),
    )
    
    return LaunchDescription([
        hardware_interface,
        controller,
        joystick,
    ])
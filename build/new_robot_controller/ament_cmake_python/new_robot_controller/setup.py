from setuptools import find_packages
from setuptools import setup

setup(
    name='new_robot_controller',
    version='0.0.0',
    packages=find_packages(
        include=('new_robot_controller', 'new_robot_controller.*')),
)

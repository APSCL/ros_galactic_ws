# ROS 2 Galactic Workspace
This is a developmental workspace based on previous work on Foxy intended to explore performance and stability enhancements.

## Update for environment setup
Please first install Ubuntu 20.04 (dual system or virtual machine) and [ros2 galactic](https://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Debians.html), then install the necessary packages as follows.
1. [colcon](https://docs.ros.org/en/foxy/Tutorials/Colcon-Tutorial.html)
2. [Navigation2](https://navigation.ros.org/build_instructions/index.html)
3. [Slam_toolbox](https://navigation.ros.org/tutorials/docs/navigation2_with_slam.html)
Please note that the ros2 distribution is **galactic**, it may be needed in some commands.

## Getting Started
1. Clone this project and navigate to root.
2. Build the workspace: ```colcon build --symlink-install```
3. Source the workspace: ```source ./install/setup.bash```

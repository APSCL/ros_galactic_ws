# ROS 2 Galactic Workspace
This is a developmental workspace based on previous work on Foxy intended to explore performance and stability enhancements.

## Update for environment setup
Please first install Ubuntu 20.04 (dual system or virtual machine) and [ros2 galactic](https://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Debians.html), then install the necessary packages as follows.
1. [colcon](https://docs.ros.org/en/foxy/Tutorials/Colcon-Tutorial.html)
2. [Navigation2](https://navigation.ros.org/build_instructions/index.html)
3. [Slam_toolbox](https://navigation.ros.org/tutorials/docs/navigation2_with_slam.html)

Please note that the ros2 distribution is **galactic**, it may be needed in some commands.

## Getting Started
### On Raspberry Pi
1. Clone this project and navigate to root.
2. Source the workspace: ```source ./install/setup.bash```
3. Start running ROS: ```ros2 launch ./launch/robot_launch.py```

### On Ubuntu Desktop
1. Clone this project and navigate to root.
2. (For the first time) Build the workspace: ```colcon build --symlink-install```
3. Make sure to source the command by ```source /opt/ros/galactic/setup.bash``` (```setup.zsh``` if running in zsh)
4. Running SLAM command by: ```./launch/slam_launch.sh```
5. Running Nav2 command by: ```./launch/nav2_launch.sh``` (if running mecnaum wheel agv please directly use command ```ros2 launch nav2_bringup navigation_launch.py params_file:=nav2_mecnaum.yaml```)
7. Open ROS Visualizer by: ```rviz2```
8. Select File -> Open Config -> Select ```./launch/nav2.rviz```

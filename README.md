# RecoDrone Workspace
This folder includes all the modified packages used in the recodrone project. Below is a step by step guide to recreating it.
## Virtual Machine Configuration
Download the latest VM image from [here](https://github.com/CopterExpress/clover_vm/releases). For reference, this project uses the v1.3 release. I recommend increasing the memory usage to at least 4 GB (2 CPU cores) and storage to 40 GB and enable 3D acceleration. When you are ready to connect to a real drone configure the bridge network option in the virtual machine settings.
## Gazebo simulator
1. First update all the outdated packages indicies in the virtual machine.
```
    sudo apt-get update
```
2. Add the hokuyo lidar to the drone by copying the `hokuyo_utm30lx.urdf.xacro` file in the following folder: `clover/clover_description/urdf/sensors/`
3. Replace `clover4.xacro` file in the `clover/clover_description/urdf/clover/` folder with the one provided.
4. Replace the launch file `mavros.launch` in `clover/clover/launch/` with the one provided.
## Mapping
1. Download the gmapping package
```
    sudo apt install ros-noetic-gmapping
```
2. Download the package from source in `catkin_ws/src` to edit the launch file.
```
    git clone https://github.com/ros-perception/slam_gmapping.git
```
3. Replace the gmapping launch file in `slam_gmapping/gmapping/launch/` and comment out the following lines to test it.
```
    <arg name="map_name" value="/home/clover/catkin_ws/src/clover_navigation/map/map"/>
    <node pkg="map_server" type="map_saver" name="map_saver" args="-f $(arg map_name)" output="screen"/>
```
4. Add the `setup.rviz` file in `catkin_ws/src` which provides customized configurations for Rviz.
5. Revert back to the `catkin_ws` folder and execute this command to build the workspace:
```
    catkin_make
```
5. Open gazebo and place the drone in an enclosed space. Launch the gmapping node along with rviz with this command:
```
    roslaunch gmapping slam_gmapping_pr2.launch
```
## Navigation
1. Install the following packages:
```
    sudo apt install ros-noetic-move-base
    sudo apt install ros-noetic-amcl
    sudo apt install ros-noetic-map-server
    sudo apt install ros-noetic-dwa-local-planner
    sudo apt install python-is-python3
```
2. Copy the `clover_navigation` package in the workspace source folder.
3. Copy the `takeoff.py` file in the same folder.
4. Execute the `catkin_made` command.
5. uncomment the two lines in the `slam_gmapping_pr2.launch` file.
6. Run the following commands in three different terminals
```
    roslaunch gmapping slam_gmapping_pr2.launch
    roslaunch clover_navigation move_base.launch
    python takeoff.py
```
7. Place a 2D nav goal in Rviz to test the move_base package.
## Web Application
1. Download the Rviz camera stream plug-in ROS package into the src directory of your workspace.
```
    git clone https://github.com/lucasw/rviz_camera_stream
```
2. Download the RecoDrone Web Application in your home folder:
```
    git clone 
```
# RecoDrone Workspace
This folder includes all the modified packages used in the recodrone project. Below is a step by step guide to recreating it.
## Virtual Machine Configuration
Download the latest VM image from [here](https://github.com/CopterExpress/clover_vm/releases). For reference, this project uses the v1.3 release. I recommend increasing the memory usage to at least 4 GB (2 CPU cores) and storage to 40 GB and enable 3D acceleration. When you are ready to connect to a real drone configure the bridge network option in the virtual machine settings.
## Gazebo simulator
1. First update all the outdated packages indicies in the virtual machine.
```
    sudo apt-get update
```
2. Add the hokuyo lidar to the drone by copying the ```hokuyo_utm30lx.urdf.xacro``` file in the following folder: ```clover/clover_description/urdf/sensors/```
3. Replace ```clover4.xacro``` file in the ```clover/clover_description/urdf/clover/``` folder with the one provided.
4. Replace the launch file ```mavros.launch``` in ```clover/clover/launch/``` with the one provided.
## Mapping
1. Download the gmapping package
```
    sudo apt install ros-noetic-gmapping
```
2. Download the package from source in ```catkin_ws/src``` to edit the launch file
```
    git clone https://github.com/ros-perception/slam_gmapping.git
```
3. 
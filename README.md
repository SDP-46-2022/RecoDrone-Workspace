# RecoDrone Workspace
This folder includes all the modified packages used in the recodrone project. Below is a step by step guide to recreating it.
## Virtual Machine Configuration
Download the latest VM image from [here](https://github.com/CopterExpress/clover_vm/releases). For reference, this project uses the v1.3 release. I recommend increasing the memory usage to at least 4 GB (2 CPU cores) and storage to 40 GB and enable 3D acceleration. When you are ready to connect to a real drone configure the bridge network option in the virtual machine settings.
## Gazebo simulator
1. first update all the outdated packages indicies in the virtual machine.
```sudo apt-get update```
2. replace clover.xacro file in the `````` with the one provided.

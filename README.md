ROS2 installation process on Ubuntu 22.04
====

Ros2 is also available on Windows, but we recommend that you install it on a virtual machine so that you can use all the Ros functionality.


Click on the following link shown [here](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html) and follow the procedure to install ROS.


Please note that it will tell you that,

***you're reading the documentation for an older, but still supported, version of ROS 2. For information on the latest version, please take a look at Iron.***

Even though it says that this is an older version of Ros, but Ros Humble is a long-lasting package supported up to 2027, while Ros Iron is only supported for one year.

And finally once you have runned the example file please source the ros setup.bash file to home directory by using this command
```bash
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
```
if you have't installed a virtual machine then i recommened you to install [VMware](https://www.vmware.com/in/products/workstation-player.html) and a [desktop image of ubuntu](https://releases.ubuntu.com/jammy/) and follow the setup wizarde to run ubuntu on your windows machine.

How to create ROS2 workspace 
====

Before creating ROS package you should be familare with file structure where we create our package, normally the user should create following folders to run ROS build package.

```bash
Home
├── Ros-workspace             # should be created manually
│   ├── Robots_name           # should be created manually
|      | build                # auto genrated while building package
|      | log                  # auto genrated while building package
|      | install              # auto genrated while building package
|      | src                  # should be created manually
|           ├── pacakage      # package folder build by ROS
|               | scripts     # this is where our python scripts go     | 
|               | src         # this is where our c++ file goes         |  
|               | msg         # custom message files                    | All this file's are to be created manually
|               | launch      # luanch scripts                          |
|               | camke.txt   # complier instruction                    
|               | xmal file
```

## step1: Create files which are to be created manually and change the directory 
```bash
mkdir Ros-workspace
mkdir Ros-workspace/src
cd ~/Ros-workspace/src
```
## step2: Build the package by using the following command
```bash
ros2 pkg build package_name --build-type ament_cmake
cd ../
colcon build
```
Create your file inside the package folder according to your scripting language (actual script)
## step3: source the setup.bash file
```bash
source install/setup.bash
```
## step4: run ros by using the following command
``` bash
ros2 run package_name file_name
```
This process comes with its own disadvantage that your changes in the scripts folder will not be recorded once you run colcon build. To avoid this, you have to link your changes to colcon build so that you don't have to run colcon build again and again. For that, you have to customize the cmake file within your package folder. Don't ask why you have to do those things because CMake is not my level of game.

## setp1: adding dependency in your CmakeLists.txt file

```cmake
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
```

## step2: telling cmake where your excutable scripts are 

```cmake
ament_python_install_package(scripts)
```
Once you execute this, make sure that you create an empty folder named __init__.py in the scripts folder.

## step3: creating a lib folder where your executable files are clone and linked

```cmake
install(PROGRAMS
  scripts/my_file_where_my_code_is.py 
  scripts/you can_add_as_many_folder_you_want.py
  DESTINATION lib/${PROJECT_NAME}
  )
```

## step4: go in terminal and run the following command

```bash
cd ~/Ros-workspace/your_file/
colcon build --symlink-install 
```
Now carry the previous process from step 3 every time you save your file in vs. code, but you may come in to an error of permission or that file is not found. Don't worry, just give permission to your files using the following command:

```bash
chmod +x filename1, filename2, filename3 ...
```
This will fix your problem, Just run the following command once you create your file or may just have to create a tasks.json file in vs code soo you don't have to go through this long process

launch file setup and execution 
====
Launch files are those files that can run multiple nodes with just one command rather than putting commands again and again. There is nothing more to explain here, but you will understand it's use once you go through the code itself.
```python
from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_pkg",
            executable="controller.py",
            name="controller"
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
```
you can have as many nodes and execution tubles you want and to run this type this command
```bash
ros2 launch package_name file_name_used_in_launch_file
```


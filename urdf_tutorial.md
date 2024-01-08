Exploring URDF with Ros by using Rviz
===

As I am learning Ros, my biggest question is how am I going to use my design skills from other CAD software to create an URDF? It's pretty interesting that I don't have to write a xacro file to make an urdf version of my robot; all I need is a plug-in called Fusion360 to urdf, which does the work for me to covert my design to urdf model, which is pretty easy and I can skip the tedious task of writing and xacro file, but this time I am continuing on both paths. This blog will cover both ways, even if you might not need it for small projects, but sometimes small things lead to huge disasters.

Before that, if you are new to Ros, I have to give you a tour of Rviz so that we are on the same page.

So follow along with this blog and do what I am doing by running this following command, and I will explain exactly what is going on here. I am assuming you have sourced the ros library to your home directory; if not, run this following command.

```bash
cd /opt/ros/humble/share/urdf_tutorial/urdf/
ls 
```
I won't be explaining all the commands, but here we are changing our directory where all the Ros packages are stored within the share folder (this doesn't include packages built by us).
and if you encounter a error that file not found then don't worry run this following command to fix error of missing files.

```bash
cd ~
sudo apt install ros-humble-urdf-tutorial
```
once you downloaded and changed the directory run this following command 

```bash
ros2 launch urdf_tutorial display.launch.py model:=/opt/ros/humble/share/urdf_tutorial/urdf/08-macroed.urdf.xacro
```
Now you will see a window where Rviz is launched, and you can see a robot in a 3D plane where we are going to work in the future to build our robot. For now, I will explain what all these arrows are all about.

RobotModel: this window is used to set the topic and also the visual display such as link and opcacity within the Rviz window

TF: This option shows the vectorized position of links and their respective motions to the base link in the form of an axis.

this vectors are then transformed into matrices which is done by joint_state publisher or TF topic.

```bash
aditya@aditya-virtual-machine:/opt/ros/humble/share/urdf_tutorial/urdf$ ros2 topic list
/joint_states
/parameter_events
/robot_description
/rosout
/tf
/tf_static
```

Try to change the value by moving the slider within the joint state publisher. Before that, run this command in the other shell and observe the values while sliding the joint state publisher in the parallel window.

```bash
ros2 topic echo \tf
```
so if you observe tf topic keeps track of time and position of link but the joint_state publisher is used to change the vectorized position based on the constrained defined for that tf.

Now that you know what is going on behind the Rviz, you may have concluded that TF is the most important when it comes to simulation and tracking the robot's state within the Rviz.

but you don't have to because we rarely take a look at this topic because Ros handles this for us, so we can ignore it for timing.




#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32
import math

wheel_radius = 0.5 # parameter varaiables can only be defined for global instance 

# to change parameter run this following command 
# ros2 param set /node_name parameter_name value 

# to check the value of parameter run this command
# ros2 param get /node_name parameter_name 

# to check the list of parameter currently run by the ros use the following command 
# ros2 param list

class Controller(Node):
    def __init__(self):
        super().__init__('controller') # this line asigns name to our node
        self.pub = self.create_subscription(Float32, 'rpm', self.calculate_velocity, 10) # creates a subscriber where we define what data it can accept, topic name to which it is going to subscribe , what fuction it should do everytime it recieves a message , quality of service(will explain it latter).
        self.declare_parameter("wheel_radius", wheel_radius ) # this only works for global variable 

    def calculate_velocity(self, msg):    # while defining this type of fuction make sure that you add a argument for msg 
        velocity = (2 * math.pi * msg.data * wheel_radius/ 60 )
        print('velocity of wheel = ' + str(velocity))
        



def main():
    rclpy.init() # intialize the library
    my_sub = Controller() # define a node
    print("publishing rpm node...")

    try :
        rclpy.spin(my_sub) # keep your DDS open for the topic 
    except KeyboardInterrupt:
        my_sub.destroy_node()
        print("stopping the transmission")



if __name__ == '__main__':
    main()

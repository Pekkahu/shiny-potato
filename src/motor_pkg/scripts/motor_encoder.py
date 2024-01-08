#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32

class Encoder(Node):
    def __init__(self):
        super().__init__('motor_encoder')
        self.pub = self.create_publisher(Float32, 'rpm', 10)
        self.timer = self.create_timer(1, self.rpm_data)
        self.counter = float()

    def rpm_data(self):
        msg = Float32()
        msg.data = self.counter
        print("rpm = "+ str(msg.data) )
        self.pub.publish(msg)
        self.counter +=float(1)

def main():
    rclpy.init()
    my_node = Encoder()
    print("publishing rpm node...")

    try :
        rclpy.spin(my_node)
    except KeyboardInterrupt:
        my_node.destroy_node()
        print("stopping the transmission")



if __name__ == '__main__':
    main()
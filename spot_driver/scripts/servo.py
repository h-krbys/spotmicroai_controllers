#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
import Adafruit_PCA9685

class Servo:

    def __init__(self):
        # Subscribe 12 joint angles [rad]
        self.sub = rospy.Subscriber("angle", Float32MultiArray, self.jointCallback, queue_size=10)

        # Initialise the PCA9685 using desired address & bus
        self.driver = Adafruit_PCA9685.PCA9685(address = 0x40, busnum = 1)
        self.driver.set_pwm_freq(60)

        # Load joint config from parameter server
        self.limit = rospy.get_param('joint')

    def jointCallback(self, msg):
        # print(msg.data[0])
        for i in range(12):
            self.driver.set_pwm(i, 0, int(self.limit[i]['center']) + int(450 * msg.data[i] / 3.14159))

if __name__ == '__main__':
    rospy.init_node('servo')
    Servo()
    rospy.spin()

#!/usr/bin/env python
import rospy
from test_my_srv.srv import Average, AverageResponse

def averageTwoNum(req):
    value = (req.num1+req.num2)/2.0
    return AverageResponse(value)
    
def main():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('average_server', anonymous=True)

    a_server = rospy.Service("/average", Average, averageTwoNum)
    print("The average server is ready")
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()

#!/usr/bin/env python
import rospy
from my_srv.srv import Average, AverageResponse

def averageTwoNum(req):
    value = (req.num1+req.num2)/2.0
    return AverageResponse(value)
    
def main():

    #Initialize the node
    rospy.init_node('average_server', anonymous=True)
    #Define the server that calculates the average
    a_server = rospy.Service("/average", Average, averageTwoNum)
    print("The average server is ready")
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()

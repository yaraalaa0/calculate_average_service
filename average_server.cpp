#include "ros/ros.h"
#include "test_my_srv/Average.h"

bool averageTwoNum(test_my_srv::Average::Request &req, test_my_srv::Average::Response &res){
    res.result= (req.num1+req.num2)/2.0;
    return true;
}

int main(int argc, char **argv)
{
  /**
   * Initialize the ROS node
   */
  ros::init(argc, argv, "average_server");
  ros::NodeHandle n;
  
  ros::ServiceServer a_server = n.advertiseService("/average", averageTwoNum);
  ros::spin();
  return 0;
}

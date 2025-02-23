#include "ros/ros.h"
#include "my_srv/Average.h"

bool averageTwoNum(my_srv::Average::Request &req, my_srv::Average::Response &res){
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

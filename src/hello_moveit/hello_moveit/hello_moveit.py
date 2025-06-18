# my_moveit_pkg/moveit_example.py
import os
import sys
import yaml
import rclpy
import numpy as np

# message libraries
from geometry_msgs.msg import PoseStamped, Pose

# moveit_py
from moveit.planning import MoveItPy
from moveit.core.robot_state import RobotState

# config file libraries
from moveit_configs_utils import MoveItConfigsBuilder
from ament_index_python.packages import get_package_share_directory

class MoveItExampleNode(Node):
    def __init__(self):
        super().__init__('moveit_example_node')

        # Initialize MoveIt
        moveit_commander.roscpp_initialize([])
        self.robot = RobotCommander()
        self.scene = PlanningSceneInterface()
        self.group = MoveGroupCommander("arm")

        self.get_logger().info('MoveIt Example Node Initialized')

    def move_to_goal(self, joint_values):
        self.group.set_joint_value_target(joint_values)
        plan = self.group.plan()
        self.group.go(wait=True)

    def shutdown(self):
        moveit_commander.roscpp_shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = MoveItExampleNode()
    rclpy.spin(node)
    node.shutdown()

if __name__ == '__main__':
    main()

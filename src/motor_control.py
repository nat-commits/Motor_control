#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan, Imu, Image
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller_node')
        
        # Исправлено: все имена топиков обернуты в кавычки
        self.lidar_sub = self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)
        self.imu_sub = self.create_subscription(Imu, '/imu', self.imu_callback, 10)
        self.cam_sub = self.create_subscription(Image, '/camera/image_raw', self.camera_callback, 10)
        self.custom_sensor_sub = self.create_subscription(Float64, '/custom_sensor/data', self.custom_callback, 10)
        
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_loop)
        self.obstacle_detected = False
        
        self.get_logger().info('=== Система управления роботом успешно инициализирована ===')

    def lidar_callback(self, msg: LaserScan):
        if len(msg.ranges) > 0 and min(msg.ranges) < 0.5:
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

    def imu_callback(self, msg: Imu): pass
    def camera_callback(self, msg: Image): pass
    def custom_callback(self, msg: Float64): pass

    def control_loop(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.0 if self.obstacle_detected else 0.2
        twist_msg.angular.z = 0.5 if self.obstacle_detected else 0.0
        self.cmd_vel_pub.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

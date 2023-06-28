import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleDriver(Node):

    def __init__(self):
        super().__init__('turtle_drive_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel',10)
        timer_period = 1 # second 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        # msg.linear.y = 2.0
        msg.angular.z = 3.0
        self.publisher_.publish(msg)

        # self.get_logger().info(f'Publishing {msg.data}')
        self.i +=1


def main(args=None):
    rclpy.init(args=args)
    talker_node = TurtleDriver()

    rclpy.spin(talker_node)
    talker_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

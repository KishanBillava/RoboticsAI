
const Config = {
    ROSBRIDGE_SERVER_IP: "192.168.0.145",
    ROSBRIDGE_SERVER_PORT: "9090",
    RECONNECTION_TIMER: 5000,
    CMD_VEL_TOPIC:"/cmd_vel", // /turtle1/cmd_vel
    ODOM_TOPIC: "/odom",
    POSE_TOPIC: "/amcl_pose",
}

export default Config;
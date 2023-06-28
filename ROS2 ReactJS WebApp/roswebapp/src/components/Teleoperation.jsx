import React, { Component } from 'react';
import {Joystick} from "react-joystick-component"
import Config from "../scripts/Config"

class Teleoperation extends Component {
    state = { ros:null };

    // ---- same code as connection --- 
    constructor(){
        super();
        this.init_connection(); 

        this.handleMove = this.handleMove.bind(this)
        this.handleStop = this.handleStop.bind(this)
    }  

    init_connection(){
        this.state.ros = new window.ROSLIB.Ros();
            console.log(this.state.ros);

        this.state.ros.on("connection", ()=> {
            console.log("Connection established");
            this.setState({connected:true});
        });
        this.state.ros.on("close",()=>{
            console.log("Connection closed");
            this.setState({connected:false});

            setTimeout(function (){
                try{
                    this.state.ros.connect("ws://"+Config.ROSBRIDGE_SERVER_IP+":"+Config.ROSBRIDGE_SERVER_PORT+"");
                } catch (error) {
                    console.log("connection problem") 
                }    
            }, Config.RECONNECTION_TIMER);
        
        });
        try{
            this.state.ros.connect("ws://"+Config.ROSBRIDGE_SERVER_IP+":"+Config.ROSBRIDGE_SERVER_PORT+"");
        } catch (error) {
            console.log("connection problem") 
        }
        
    }

    // ---- same code as connection --- 

    handleMove(event){
        // ROS publish on topic cmd_vel
        let cmd_vel = new window.ROSLIB.Topic({
            ros: this.state.ros,
            name:Config.CMD_VEL_TOPIC,
            messageType: "geometry_msgs/Twist"
        });

        // twist message to publish to ros_bridge
        let twist = new window.ROSLIB.Message({
            linear:{
                x: event.y,
                y:0,
                z:0,
            },
            angular:{
                x:0,
                y:0,
                z: -event.x,
            }
        });

        // publish message on cmd_vel topic
        cmd_vel.publish(twist)
    };
    handleStop(event){

        let cmd_vel = new window.ROSLIB.Topic({
            ros: this.state.ros,
            name:Config.CMD_VEL_TOPIC,
            messageType: "geometry_msgs/Twist"
        });

        let twist = new window.ROSLIB.Message({
            linear:{
                x:0,
                y:0,
                z:0,
            },
            angular:{
                x:0,
                y:0,
                z:0,
            }
        });

        cmd_vel.publish(twist)
    };

    render() { 
        return ( 
        <div>

            <Joystick 
            size={100} 
            sticky={false} 
            baseColor="red" 
            stickColor="blue" 
            move={this.handleMove} 
            stop={this.handleStop}
            ></Joystick>

        </div> );
    }
}
 
export default Teleoperation ;
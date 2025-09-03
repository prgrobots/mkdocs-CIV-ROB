"""line_following_behavior controller."""
# This program implements a state-machine based line-following behavior
# for the e-puck robot. 

# Author: Felipe N. Martins
# Date: 7th of April, 2020
# Update: 17 September 2021 - add comments and adjust variable names

from controller import Robot, DistanceSensor, Motor
import numpy as np

#-------------------------------------------------------
# Initialize variables

TIME_STEP = 64
MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())   # [ms]

# states
states = ['forward', 'turn_right', 'turn_left']
current_state = states[0]

# counter: used to maintain an active state for a number of cycles
counter = 0
COUNTER_MAX = 5

#-------------------------------------------------------
# Initialize devices

# distance sensors
ps = []
psNames = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']
for i in range(8):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(timestep)

# ground sensors
gs = []
gsNames = ['gs0', 'gs1', 'gs2']
for i in range(3):
    gs.append(robot.getDevice(gsNames[i]))
    gs[i].enable(timestep)


# motors    
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)


#-------------------------------------------------------
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Update sensor readings
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())

    gsValues = []
    for i in range(3):
        gsValues.append(gs[i].getValue())

    # Process sensor data
    line_right = gsValues[0] > 600
    line_left = gsValues[2] > 600

    # Implement the line-following state machine
    if current_state == 'forward':
        # Action for the current state: update speed variables
        leftSpeed = MAX_SPEED
        rightSpeed = MAX_SPEED

        # check if it is necessary to update current_state
        if line_right and not line_left:
            current_state = 'turn_right'
            counter = 0
        elif line_left and not line_right:
            current_state = 'turn_left'
            counter = 0
            
    if current_state == 'turn_right':
        # Action for the current state: update speed variables
        leftSpeed = 0.8 * MAX_SPEED
        rightSpeed = 0.4 * MAX_SPEED

        # check if it is necessary to update current_state
        if counter == COUNTER_MAX:
            current_state = 'forward'

    if current_state == 'turn_left':
        # Action for the current state: update speed variables
        leftSpeed = 0.4 * MAX_SPEED
        rightSpeed = 0.8 * MAX_SPEED

        # check if it is necessary to update current_state
        if counter == COUNTER_MAX:
            current_state = 'forward'        

    # increment counter
    counter += 1
    
    #print('Counter: '+ str(counter), gsValues[0], gsValues[1], gsValues[2])
    print('Counter: '+ str(counter) + '. Current state: ' + current_state)

    # Set motor speeds with the values defined by the state-machine
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)

    # Repeat all steps while the simulation is running.
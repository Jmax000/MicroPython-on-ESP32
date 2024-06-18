"""################################################################################################
  ECEN 240/301 Lab Code
  Light-Following Robot

  The approach of this code is to use an architecture that employs
  three different processes:
    Perception
    Planning
    Action

  By separating these processes, this allows one to focus on the
  individual elements needed to do these tasks that are general
  to most robotics.


  Version History
  1.1.3       11 January 2023   Creation by Dr. Mazzeo and TAs from 2022 version
  2.0.0       07 June 2024      Creation by Jacob Ackroyd translating 2023 version into MircoPython

################################################################################################"""

# These initial includes allow you to use necessary libraries for your sensors and servos.
import machine
from machine import Pin
from enum import Enum
import sys

###################################################################################################
# Pin definitions
# Replace the pin numbers with those you connect to your robot

# IMPORTANT DO NOT CHANGE
repl_button = Pin(0, Pin.IN, Pin.PULL_UP)
DebugStateOutput = False

# LED pins
led_1 = Pin(14, Pin.OUT)
led_2 = Pin(27, Pin.OUT)
led_3 = Pin(26, Pin.OUT)
led_4 = Pin(25, Pin.OUT)
led_5 = Pin(32, Pin.OUT)

# Button pins. These will be replaced with the photodiode variables in lab 5
button_1 = Pin(4, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(16, Pin.IN, Pin.PULL_DOWN)
button_3 = Pin(17, Pin.IN, Pin.PULL_DOWN)
button_4 = Pin(5, Pin.IN, Pin.PULL_DOWN)
button_5 = Pin(18, Pin.IN, Pin.PULL_DOWN)

# Motor enable pins - Lab 3
# These will replace LEDs 2 and 4

# Photodiode pins - Lab 5
# These will replace buttons 1, 2, 4, 5

# Capacitive sensor pins - Lab 4


# Ultrasonic sensor pin - Lab 6
# This will replace button 3 and LED 3 will no longer be needed

# Servo pin - Lab 6
# This will replace LEDs 1 and 5

###################################################################################################
# Configuration parameter definitions
# Replace the parameters with those that are appropriate for your robot

# Voltage at which a button is considered to be pressed
BUTTON_THRESHOLD = 2.5


# Voltage at which a photodiode voltage is considered to be present - Lab 5


# Number of samples that the capacitor sensor will use in a measurement - Lab 4


# Parameters for servo control as well as instantiation - Lab 6


# Parameters for ultrasonic sensor and instantiation - Lab 6


# Parameter to define when the ultrasonic sensor detects a collision - Lab 6

###################################################################################################
# Definitions that allow one to set states
# Sensor state definitions
class Detection(Enum):
    NO = 0
    YES = 1


# Motor speed definitions - Lab 4


# Collision definitions
class Collision(Enum):
    ON = 0
    OFF = 1


# Driving direction definitions
class Drive(Enum):
    STOP = 0
    LEFT = 1
    RIGHT = 2
    STRAIGHT = 3


# Servo movement definitions
class ServoMove(Enum):
    STOP = 0
    UP = 1
    DOWN = 2


###################################################################################################
# Global variables that define PERCEPTION and initialization

# Global finite state machine Variables that keep track of states
collisionDetectionState = 0
steerRobotState = 0
moveServoState = 0

# Collision (using Definitions)
SensedCollision = Detection.NO

# Photodiode inputs (using Definitions) - The button represent the photodiodes for lab 2
SensedLightRight = Detection.NO
SensedLightLeft = Detection.NO
SensedLightUp = Detection.NO
SensedLightDown = Detection.NO

# Capacitive sensor input (using Definitions) - Lab 4
# SensedCapacitiveTouch = DETECTION_NO;

###################################################################################################
# Global variables that define ACTION and initialization

# Collision Actions (using Definitions)
ActionCollision = Collision.OFF

# Main motors Action (using Definitions)
ActionRobotDrive = Drive.STOP
# Add speed action in Lab 4

# Servo Action (using Definitions)
ActionServoMove = ServoMove.STOP

'''################################################################################################
    Robot PERCEPTION - all of the sensing
################################################################################################'''


def RobotPerception():
    # This function polls all the sensors and then assigns sensor outputs
    # that can be used by the robot in subsequent stages
    global SensedLightUp
    global SensedLightDown
    global SensedLightRight
    global SensedLightLeft
    global SensedCollision

    # Photodiode Sensing
    if isButtonPushed(button_1):
        SensedLightUp = Detection.YES
    else:
        SensedLightLeft = Detection.NO
    if isButtonPushed(button_2):
        SensedLightRight = Detection.YES
    else:
        SensedLightRight = Detection.NO
    if isButtonPushed(button_4):
        SensedLightLeft = Detection.YES
    else:
        SensedLightLeft = Detection.NO
    if isButtonPushed(button_5):
        SensedLightDown = Detection.YES
    else:
        SensedLightDown = Detection.NO

    # Add code to detect if light is up or down. Lab 2 milestone 3

    # Capacitive Sensor
    ''' Add code in lab 4 '''

    # Collision Sensor
    if isCollision():
        SensedCollision = Detection.YES
    else:
        SensedCollision = Detection.NO


#####################################################################
# Function to read pin voltage
#####################################################################
def getPinVoltage(pin):
    # FIXME
    return


#####################################################################
# Function to determine if a button is pushed or not
#####################################################################
def isButtonPushed(button_pin):
    if button_pin.value() == 0:
        return True
    else:
        return False


#####################################################################
# Function that detects if there is an obstacle in front of robot
#####################################################################
def isCollision():
    # This is where you add code that tests if the collision button
    # was pushed (BUTTON_3)
    # In lab 6 you will add a sonar sensor to detect collision and
    # the code for the sonar sensor will go in this function.
    # Until then, we will use a button to model the sensor.

    if isButtonPushed(button_3):  # Add code to detect if the collision button was pressed
        return True
    else:
        return False


#####################################################################
# Function that detects if the capacitive sensor is being touched
#####################################################################
def isCapacitiveSensorTouched():
    # In lab 4 you will add a capacitive sensor, and
    # you will need to modify this function accordingly.
    return


'''################################################################################################
    Robot PLANNING - using the sensing to make decisions
################################################################################################'''


def RobotPlanning():
    # The planning FSMs that are used by the robot to assign actions
    # based on the sensing from the Perception stage.
    fsmCollisionDetection()  # Milestone 1
    fsmMoveServoUpAndDown()  # Milestone 3
    # Add Speed Control State Machine in lab 4


#####################################################################
# State machine for detecting collisions, and stopping the robot
# if necessary.
#####################################################################
def fsmCollisionDetection():
    global ActionCollision
    global collisionDetectionState

    match collisionDetectionState:
        case 0:  # collision detected
            # There is an obstacle, stop the robot
            ActionCollision = Collision.ON  # Sets the action to turn on the collision LED

            '''Add code in milestone 2 to stop the robot's wheels - Hint: ActionRobotDrive = ________'''
            ActionCollision = Drive.STOP

            # State transition logic
            if SensedCollision == Detection.NO:
                collisionDetectionState = 1

        case 1:  # no collision
            # There is no obstacle, drive the robot
            ActionCollision = Collision.OFF  # Sets action to turn off the collision LED

            fsmSteerRobot()  # Milestone 2

            # State transition logic
            if isCollision():  # Add code to determine when you need to go back to state 0
                collisionDetectionState = 0  # if collision, go to collision state

        case _:  # error handling
            collisionDetectionState = 0


#####################################################################
# State machine for detecting if light is to the right or left,
# and steering the robot accordingly.
#####################################################################
def fsmSteerRobot():
    global steerRobotState
    global ActionRobotDrive

    match steerRobotState:
        case 0:  # light is not detected
            ActionRobotDrive = Drive.STOP

            # State transition logic
            if SensedLightLeft == Detection.YES:
                steerRobotState = 1  # if light on left of robot, go to left state
            elif SensedLightRight == Detection.YES:
                steerRobotState = 2  # if light on right of robot, go to right state

        case 1:  # light is to the left of robot
            # The light is on the left, turn left
            ActionRobotDrive = Drive.LEFT  # Add appropriate variable to set the action to turn left

            # State transition logic
            if SensedLightRight == Detection.YES:  # Add code: If light is also to the right, the light is in front
                steerRobotState = 3 # if light is on right, then go straight
            elif SensedLightLeft == Detection.NO:  # Add code: no longer light to the left
                steerRobotState = 0 # if light is not on left, go back to stop state

        case 2:  # light is to the rig ht of robot
            # The light is on the right, turn right
            ActionRobotDrive = Drive.RIGHT  # Add code to set the action

            # State transition logic
            if SensedLightLeft == Detection.YES:  # Add code: If light is also to the right, the light is in front
                steerRobotState = 3 # if light is on left, then go straight
            elif SensedLightRight == Detection.NO:  # Add code: no longer light to the left
                steerRobotState = 0 # if light is not on right, go back to stop state

        case 3:  # light is on both right and left
            ActionRobotDrive = Drive.STRAIGHT  # Add code to set the action

            # State transition logic
            if SensedLightLeft == Detection.NO:  # Add code: If light is also to the right, the light is in front
                steerRobotState = 2  # if light is on left, then go straight
            elif SensedLightRight == Detection.NO:  # Add code: no longer light to the left
                steerRobotState = 1  # if light is not on right, go back to stop state

        case _: # error handling
            steerRobotState = 0


#####################################################################
# State machine for detecting if light is above or below center,
# and moving the servo accordingly.
#####################################################################
def fsmMoveServoUpAndDown():
    global moveServoState
    global ActionServoMove

    # Milestone 3
    # Create a state machine modeled after the ones in milestones 1 and 2
    # to plan the servo action based off of the perception of the robot
    # Remember no light or light in front = servo doesn't move
    # Light above = servo moves up
    # Light below = servo moves down

    match moveServoState:
        case 0: # light is not detected
            ActionServoMove = ServoMove.STOP

            # State transition logic
            if SensedLightUp == Detection.YES and SensedLightDown == Detection.NO:
                moveServoState = 1 # if light is above the robot and not below, go to up state
            elif SensedLightUp == Detection.NO and SensedLightDown == Detection.YES:
                moveServoState = 2 # if light is below the robot and not above, go to down state

        case 1: # light is to the above of robot
            # The light is above, move up
            ActionServoMove = ServoMove.UP

            # State transition logic
            if SensedLightDown == Detection.YES:
                moveServoState = 0 # if light is on above and below, go back to stop state
            elif SensedLightUp == Detection.NO:
                moveServoState = 0 # if light is below, move down

        case 2: # light is below the robot
            # The light is below, move down
            ActionServoMove = ServoMove.DOWN

            # State transition logic
            if SensedLightUp == Detection.YES:
                moveServoState = 0 # if light is on above and below, go back to stop state
            elif SensedLightDown == Detection.NO:
                moveServoState = 0 # if light is not below, go back to stop state

        case _:
            moveServoState = 0


#####################################################################
# State machine for detecting when the capacitive sensor is
# touched, and changing the robot's speed.
#####################################################################
def fsmCapacitiveSensorSpeedControl():
    # Implement in lab 4
    return


#####################################################################
# State machine for cycling through the robot's speeds.
#####################################################################
def fsmChangeSpeed():
    # Implement in lab 4
    return


'''################################################################################################
    Robot ACTION - implementing the decisions from planning to specific actions
################################################################################################'''


def RobotAction():
    # Here the results of planning are implemented so the robot does something
    global ActionCollision
    global ActionRobotDrive

    # This turns the collision LED on and off
    match ActionCollision:
        case Collision.OFF:
            led_3.off()
        case Collision.ON:
            led_3.on()

    match ActionRobotDrive:
        case Drive.STOP:
            led_2.off()
            led_4.off()
        case Drive.LEFT:
            led_4.off()
            led_2.on()
        case Drive.RIGHT:
            led_2.off()
            led_4.on()
        case Drive.STRAIGHT:
            led_2.on()
            led_4.on()

    # This calls a function to move the servo
    MoveServo()


#####################################################################
# Function that causes the servo to move up or down.
#####################################################################
def MoveServo():
    global ActionServoMove

    # Note that there needs to be some logic in the action of moving
    # the servo so that it does not exceed its range
    # /* Add CurrentServoAngle in lab 6 */
    match ActionServoMove:
        case ServoMove.STOP:
            led_1.off()
            led_5.off()
        case ServoMove.UP:
            led_1.on()
            led_5.off()
        case ServoMove.DOWN:
            led_5.on()
            led_1.off()


'''################################################################################################
    Main LOOP function - this gets executed in an infinite loop until power off or reset. 
    - Notice: PERCEPTION, PLANNING, ACTION
################################################################################################'''

while True:
    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        sys.exit()

    print("HIT")
    DebugStateOutput = True

    RobotPerception()
    if DebugStateOutput:
        print("Perception:")
        print(SensedLightUp)
        print(SensedLightRight)
        print(SensedLightLeft)
        print(SensedLightDown)
        # print(SensedCapacitiveTouch) # Lab 4

    RobotPlanning()
    if DebugStateOutput:
        print("Action:")
        print(ActionCollision)
        print(ActionRobotDrive)
        print(ActionServoMove)
        # print(ActionRobotSpeed) # Lab 4

    RobotAction()

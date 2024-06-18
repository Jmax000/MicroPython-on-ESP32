#####################################################################
# State machine for detecting collisions, and stopping the robot
# if necessary.
#####################################################################
collisionDetectionState = 0


def fsmCollisionDetection():
    match collisionDetectionState:
        case 0:
            ActionCollision = COLLISION_ON

from controller import Robot, DistanceSensor, Motor

MAX_SPEED = 6.28
SPEED_DIFF = 0.5

# Initialize the robot
robot = Robot()

# Initialize motors
left_motor = robot.getMotor("left wheel motor")
right_motor = robot.getMotor("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(MAX_SPEED)
right_motor.setVelocity(MAX_SPEED)

# Initialize distance sensors
left_sensor = robot.getDistanceSensor("ps5")
right_sensor = robot.getDistanceSensor("ps6")
left_sensor.enable(64)
right_sensor.enable(64)

# Main loop
while robot.step(64) != -1:
    left_value = left_sensor.getValue()
    right_value = right_sensor.getValue()

    speed_left = MAX_SPEED
    speed_right = MAX_SPEED

    # Adjust speed based on sensor readings
    if left_value > 600 and right_value > 600:
        # Both sensors see white (off the line)
        speed_left -= SPEED_DIFF
        speed_right += SPEED_DIFF
    elif left_value < 600 and right_value < 600:
        # Both sensors see black (on the line)
        speed_left += SPEED_DIFF
        speed_right -= SPEED_DIFF
    elif left_value > right_value:
        # Only left sensor sees black
        speed_left -= SPEED_DIFF
        speed_right += SPEED_DIFF
    else:
        # Only right sensor sees black
        speed_left += SPEED_DIFF
        speed_right -= SPEED_DIFF

    # Apply calculated speeds to motors
    left_motor.setVelocity(speed_left)
    right_motor.setVelocity(speed_right)

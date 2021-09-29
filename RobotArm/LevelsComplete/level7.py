i = 1

from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:

while i < 6:
    for n in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    robotArm.moveRight()
    robotArm.moveRight()
    if i == 5:
        break
    i += 1



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
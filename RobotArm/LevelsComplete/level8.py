i = 1

from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
while i < 7:
    robotArm.grab()
    for k in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for k in range(8):
        robotArm.moveLeft()
    if i == 7:
        break
i += 1 
        





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
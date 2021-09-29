i = 1
m = 1 
from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

while i < 4:
    for n in range(m):
        robotArm.grab()
        for n in range (5):
            robotArm.moveRight()
        robotArm.drop()
        for n in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
    m += 1

    if i == 4:
        break
i += 1 
        


        



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
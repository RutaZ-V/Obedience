from functions import *

# Define area parameters:
xMax = int(input("Define the width of the field in meters: "))
yMax = int(input("Define the length of the field in meters: "))

# Define number of turns:
xTurns = int(input("How many turns you need? "))

# Define start and finish
start = generateCoordinates("start")
points.append(start)
finish = generateCoordinates("finish")

generateTurns(xTurns, xMax, yMax)

points.append(finish)
# In-process control
for i in points:
    print("points", i)

generateIntermediates(xTurns)
# In-process control
for i in intrm:
    print("int", i)

generateCourse(points, intrm, xTurns)

plotCourse(course, xTurns)

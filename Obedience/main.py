from functions import *

# Define area parameters
xMax = int(input("Define the width of the field in meters: "))
yMax = int(input("Define the length of the field in meters: "))

# Define number of extra points
xTurns = int(input("How many extra points you need? "))

# Define start and finish
start = generateCoordinates("start")
points.append(start)
finish = generateCoordinates("finish")

# Generate turning points
generateTurns(xTurns, xMax, yMax)

points.append(finish)
# In-process control
print("Initial points:")
for point in points:
    print(point)

generateIntermediates(xTurns)

generateCourse(points, intrm, xTurns)

plotCourse(course, xTurns)

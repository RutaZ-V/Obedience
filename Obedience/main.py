from functions import *

generateTurns(xTurns)

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

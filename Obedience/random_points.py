import numpy
import random


points = []
intrm = []

# Define area parameters:
xMax = 5
yMax = 5

# Define number of turns:
xTurns = 2

# Define start and finish:
start = numpy.array([1, 1])
points.append(start)
finish = numpy.array([3, 3])

# Generate turning points:


def generateTurns(xTurns):
    i = 1
    while i <= xTurns:
        x = random.randint(0, xMax)
        y = random.randint(0, yMax)
        points.append(numpy.array([x, y]))
        i += 1


generateTurns(xTurns)
points.append(finish)

for i in points:
    print("points", i)

# Generate intermediate turns


def generateIntermediates(xTurns):
    i = 0
    while i <= xTurns:
        x = numpy.array([points[i][0], points[i + 1][1]])
        print("x", x)
        intrm.append(x)
        i += 1


for i in intrm:
    print(i)
generateIntermediates(xTurns)

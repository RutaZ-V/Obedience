import numpy
import random


points = []

# Define area parameters:
xMax = 5
yMax = 5

# Define number of turns:
xTurns = 4

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
print(points)

# Generate intermediate turns

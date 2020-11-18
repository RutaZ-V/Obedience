import numpy
import random
from matplotlib import pyplot


points = []
intrm = []
course = []

# Define area parameters:
xMax = 10
yMax = 8

# Define number of turns:
xTurns = 4

# Define start and finish:
start = numpy.array([1, 3])
points.append(start)
finish = numpy.array([4, 2])

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
        y = numpy.array([points[i + 1][0], points[i][1]])
        print("y", y)
        temp = []
        temp.append(x)
        temp.append(y)

        for item in temp:
            print("temp", item)

        intrm.append(temp[random.randint(0, 1)])
        i += 1


generateIntermediates(xTurns)
for i in intrm:
    print("int", i)


def generateCourse(points, intrm, xTurns):

    i = 0
    while i <= xTurns:
        course.append(points[i])
        course.append(intrm[i])
        i += 1
    course.append(points[xTurns + 1])

    for i in course:
        print("course", i)


generateCourse(points, intrm, xTurns)


def plotCourse(course, xTurns):
    x, y = zip(*course)
    pyplot.plot(x, y)
#     pyplot.show()
    pyplot.scatter(x[0], y[0])
    pyplot.scatter(x[xTurns * 2 + 2], y[xTurns * 2 + 2])
    pyplot.show()


plotCourse(course, xTurns)

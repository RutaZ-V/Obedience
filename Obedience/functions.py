import numpy
import random
from matplotlib import pyplot

points = []
intrm = []
course = []

# Define point coordinates:
def generateCoordinates(name):
    coord_x, coord_y = input(f"Define {name} coordinates in format \"x,y\": ").split(sep=",")
    coord_x = int(coord_x)
    coord_y = int(coord_y)
    name = numpy.array([coord_x, coord_y])
    return name

# Generate turning points:
def generateTurns(xTurns, xMax, yMax):
    i = 1
    while i <= xTurns:
        x = random.randint(0, xMax)
        y = random.randint(0, yMax)
        points.append(numpy.array([x, y]))
        i += 1

# Generate intermediate turns
def generateIntermediates(xTurns):
    i = 0
    while i <= xTurns:
        x = numpy.array([points[i][0], points[i + 1][1]])
        y = numpy.array([points[i + 1][0], points[i][1]])
        
        temp = []
        temp.append(x)
        temp.append(y)
        
        # In-process control
        print("x", x)
        print("y", y)
        for item in temp:
            print("temp", item)

        intrm.append(temp[random.randint(0, 1)])
        i += 1

#Generate whole course
def generateCourse(points, intrm, xTurns):

    i = 0
    while i <= xTurns:
        course.append(points[i])
        course.append(intrm[i])
        i += 1
    course.append(points[xTurns + 1])

    for i in course:
        print("course", i)

#Plot the course
def plotCourse(course, xTurns):
    x, y = zip(*course)
    pyplot.plot(x, y)
    pyplot.scatter(x[0], y[0])
    pyplot.scatter(x[xTurns * 2 + 2], y[xTurns * 2 + 2])
    pyplot.show()


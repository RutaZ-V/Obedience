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

# Generate extra points:
def generateTurns(xTurns, xMax, yMax):
    i = 1
    # Selects random points in the field
    while i <= xTurns:
        coord_x = random.randint(0, xMax)
        coord_y = random.randint(0, yMax)
        points.append(numpy.array([coord_x, coord_y]))
        i += 1

# Generate intermediate turns
def generateIntermediates(xTurns):
    i = 0
    while i <= xTurns:
        option1 = numpy.array([points[i][0], points[i + 1][1]])
        option2 = numpy.array([points[i + 1][0], points[i][1]])
        
        temp = []
        temp.append(option1)
        temp.append(option2)
        selectedPoint = temp[random.randint(0, 1)]
        
        intrm.append(selectedPoint)
        i += 1
        
        # In-process control
        print("Selecting intermediate points:")
        print("option 1", option1)
        print("option 2", option2)
        print("Selected point: ",selectedPoint)
        

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


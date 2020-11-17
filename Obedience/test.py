from abc import abstractmethod
import numpy
import random
from pip._vendor.webencodings.mklabels import generate


class newTrack:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.drxn = 1


obd = newTrack()
print("Initial direction:", obd.drxn)
print("Initial position:", obd.X, obd.Y)


class Element:
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def turn(self):
        pass

    def assignMatrix(self):
        if obd.drxn == 1:
            matrix = numpy.array([[1, 0], [0, 1]])
            print("matrix assigned")
            return(matrix)
        elif obd.drxn == 2:
            matrix = numpy.array([[0, 1], [-1, 0]])
            print("matrix assigned")
            return(matrix)
        elif obd.drxn == 3:
            matrix = numpy.array([[-1, 0], [0, -1]])
            print("matrix assigned")
            return(matrix)
        elif obd.drxn == 4:
            matrix = numpy.array([[0, -1], [1, 0]])
            print("matrix assigned")
            return(matrix)

    step = numpy.array([[0, ], [0, ]])


class Right(Element):

    def move(self, step):
        print("no movement")

    def turn(self):
        if obd.drxn < 4:
            obd.drxn += 1
            print("direction updated and now is:", obd.drxn)
            return(obd.drxn)
        else:
            obd.drxn = 1
            print("direction updated and now is:", obd.drxn)
            return(obd.drxn)


class Left(Element):

    def move(self, step):
        print("no movement")

    def turn(self):
        if obd.drxn > 1:
            obd.drxn -= 1
            print("Turning Left. Direction updated and now is:", obd.drxn)
            return(obd.drxn)
        else:
            obd.drxn = 4
            print("Turning Left. Direction updated and now is:", obd.drxn)
            return(obd.drxn)


class StepFwd(Element):

    step = numpy.array([[0, ], [1, ]])

    def move(self, step):
        change = self.assignMatrix().dot(step)
        obd.X += int(change[0])
        obd.Y += int(change[1])
        print("moved one step forward")

    def turn(self):
        print("no turning")


step1 = StepFwd()
turn1 = Right()
turn2 = Left()
selection = []
selection.append(step1)
selection.append(turn1)
selection.append(turn2)

# Number of elements in the course
numEl = 4
course = []

for i in range(0, numEl):
    course.append(random.choice(selection))

for i in course:
    print(i)
    i.turn()
    i.move(i.step)

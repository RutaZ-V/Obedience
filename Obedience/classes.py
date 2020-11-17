from abc import abstractmethod
import numpy
import random


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
            print("Turning Right. Direction updated and now is:", obd.drxn)
            return(obd.drxn)
        else:
            obd.drxn = 1
            print("Turning Right. Direction updated and now is:", obd.drxn)
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


class About(Element):

    def move(self, step):
        print("no movement")

    def turn(self):
        if obd.drxn < 3:
            obd.drxn += 2
            print("Turning around. Direction updated and now is:", obd.drxn)
            return(obd.drxn)
        else:
            obd.drxn = obd.drxn - 2
            print("Turning around. Direction updated and now is:", obd.drxn)
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


class LineFwd(Element):

    step = numpy.array([[0, ], [5, ]])

    def move(self, step):
        change = self.assignMatrix().dot(step)
        obd.X += int(change[0])
        obd.Y += int(change[1])
        print("moved forward")

    def turn(self):
        print("no turning")


steps = []
step1 = StepFwd()
step2 = LineFwd()
steps.append(step1)
steps.append(step2)

turns = []
turn1 = Right()
turn2 = Left()
turn3 = About()
turns.append(turn1)
turns.append(turn2)
turns.append(turn3)
selection = []
selection.append(step1)
selection.append(step2)
selection.append(turn1)
selection.append(turn2)
selection.append(turn3)

# Number of elements in the course
numEl = 4
course = []

for i in range(0, numEl):
    course.append(random.choice(selection))

for i in course:
    i.turn()
    i.move(i.step)
    print("current position: ", obd.X, obd.Y)

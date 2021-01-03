import numpy


def rightTurn(drxn):
    if drxn < 4:
        drxn += 1
        return(drxn)
    else:
        drxn = 1
        return(drxn)


def leftTurn(drxn):
    if drxn > 1:
        drxn -= 1
        return(drxn)
    else:
        drxn = 4
        return(drxn)


def assignMatrix(drxn):
    if drxn == 1:
        matrix = 1
        return(matrix)
    elif drxn == 2:
        matrix = numpy.array([[0, 1], [-1, 0]])
        return(matrix)
    elif drxn == 3:
        matrix = numpy.array([[-1, 0], [0, -1]])
        return(matrix)
    elif drxn == 4:
        matrix = numpy.array([[0, -1], [1, 0]])
        return(matrix)
    else:
        print("direction is wrong")


def apply_func(L, x):
    #   Applies function given by each element in L to x
    #   Parameters
    #   ----------
    #   L : list containing the operations
    #   x : the operand

    for f in L:
        x = f(x)
#   Returns the result after all function applications
    return x


class Element:
    def __init__(self, dX, dY, dDrxn):
        self.dX = dX
        self.dY = dY
        self.dDrxn = dDrxn


def main():
    #   Starting direction
    direction = 1
    X = 0
    Y = 0
#   Elements of the course
    straight = Line(0, 5)
    oneStepFwd = Line(0, 1)
    oneStepBck = Line(0, -1)

    turns = [rightTurn, leftTurn, rightTurn, rightTurn]
    direction = apply_func(turns, direction)
    print(direction)

    matrix = assignMatrix(direction)
    print(matrix)


main()

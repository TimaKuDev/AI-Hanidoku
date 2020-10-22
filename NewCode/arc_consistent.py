from matrices import getSharedIndicesArray
from matrices import printMat

from gameLogic import indicesArrayToValuesArray
from gameLogic import inRangeArray
from gameLogic import calculateDomainSetMat
from gameLogic import updateNeighborsDomainSetMat
from gameLogic import varNeighborsSetOfVar




def find2zeros(arr):
    """

    :param arr: a whole number arr in the range [1 , hanidokuFactor] that have at least 2 zeroes in it.
    :return: two indices that have zeores
    """
    index1 = arr.index(0)
    try:
        index2 = arr.index(0, index1 + 1)
    except ValueError:
        return None, None
    return index1, index2


def makeArcConsistent(sudoku, x , y, domainSetMat):
    """
    The function updates domain of var x in arc ( x , r <x,y> )
    :param x: indices tuple of var x
    :param y: indices tuple of var y
    :param domainSetMat:
    :return: nothing
    """

    sharedIndeciesArr = getSharedIndicesArray(x, y)
    if sharedIndeciesArr is None or sudoku[x[0]][x[1]] != 0 or sudoku[y[0]][y[1]] != 0:
        return None # ERROR
    sharedArr = indicesArrayToValuesArray(sudoku, sharedIndeciesArr)
    indexX, indexY = find2zeros(sharedArr)
    if indexX is None:
        return None
    xDomain = domainSetMat[x[0]][x[1]]
    yDomain = domainSetMat[y[0]][y[1]]
    toDiscard = set()

    for valX in xDomain:
        sharedArr[indexX] = valX
        i = 0
        for valY in yDomain:
            if valY != valX and inRangeArray(sharedArr, valY):
                break
            i += 1
        if i == len(yDomain):
            toDiscard.add(valX)
    xDomain -= toDiscard


def ac3(sudoku, VariablesSet, domainSetMat):
    tda = set()


    for var in VariablesSet:
        neighborsSet = varNeighborsSetOfVar(sudoku, var[0], var[1])
        for neighbor in neighborsSet:
            tda.add((var, neighbor))

    while tda:
        arc = tda.pop()
        x = arc[0]
        y = arc[1]
        domainLengthOfX = len(domainSetMat[x[0]][x[1]])
        makeArcConsistent(sudoku, x, y, domainSetMat)
        newDomainLengthOfX = len(domainSetMat[x[0]][x[1]])
        if newDomainLengthOfX == 0:
            return False
        if domainLengthOfX != newDomainLengthOfX:
            toAdd = set()
            for var in varNeighborsSetOfVar(sudoku, x[0], x[1]):
                toAdd.add((var, x))
            toAdd.remove((y, x))
            tda = tda.union(toAdd)


def updateDomainSetMat(sudoku, i, j, domainSetMatNew, variablesSetNew):
    updateNeighborsDomainSetMat(sudoku, i, j, domainSetMatNew)
    checkSuccess = ac3(sudoku, variablesSetNew, domainSetMatNew)
    if checkSuccess is False:
        return False







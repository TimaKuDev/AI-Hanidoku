from matrices import hanidokuFactor
from matrices import getLineByIndex
from matrices import getLineByVar
from matrices import getInclineByVar
from matrices import getDeclineByVar
from matrices import getInclineByIndex
from matrices import getDeclineByIndex
from matrices import getLineInclineDeclineSetByVar
from matrices import middleRawIndex

def indicesArrayToValuesArray(sudoku, indicesArray):
    arr = []
    for i,j in indicesArray:
        arr.append(sudoku[i][j])
    return arr

def positiveMin(arr, arrLength):
    """
    returns the minimum positive integer in an array that has at least one value > 0
    """
    i = 0
    while arr[i] == 0:
        i += 1
    mini = arr[i]
    for x in range(i + 1, arrLength):
        if arr[x] != 0 and arr[x] < mini:
            mini = arr[x]
    return mini


def inRangeArray(arr, num):
    length = len(arr)
    maxi = max(arr)
    if maxi == 0:
        return True
    mini = positiveMin(arr, length)
    if maxi - length < num < mini + length:
        return True
    else:
        return False

def inRange(sudoku, indicesArray, num):
    """
    Check if num can be in a continuous array indicesArray.
    if num is already in the array -> return True
    """
    # Creates an actual values array (arr) according to the indices array (indicesArray)
    arr = indicesArrayToValuesArray(sudoku, indicesArray)
    return inRangeArray(arr,num)


def notInRange(sudoku, indicesArray):
    """
    For a given array returns set = {1 <= k <= hanidokuFactor : k is not in range of array (k is not consistent)}
    """
    length = len(indicesArray)
    arr = indicesArrayToValuesArray(sudoku, indicesArray)
    maxi = max(arr)
    if maxi == 0:
        return set()
    mini = positiveMin(arr, length)
    inf = maxi - length + 1
    if inf <= 0:
        inf = 1
    sup = mini + length - 1
    return set(range(1, hanidokuFactor + 1)) - set(range(inf , sup + 1))


def value_is_consistent(sudoku, var_i, var_j, val):
    # Check row
    line = getLineByVar(var_i, var_j)  # create list of indices of line i
    for var in line:
        if var != 0 and var == val:
            return False
    if not (inRange(sudoku, line, val)):
        return False

    # Check incline
    incline = getInclineByVar(var_i, var_j)
    for index in incline:
        element = sudoku[index[0]][index[1]]
        if element != 0 and element == val:
            return False
    if not inRange(sudoku, incline, val):
        return False

    # Check decline
    decline = getDeclineByVar(var_i, var_j)
    for index in decline:
        element = sudoku[index[0]][index[1]]
        if element != 0 and element == val:
            return False
    if not (inRange(sudoku, decline, val)):
        return False

    return True


# Domains:
def createDomainSetMat(sudoku):
    """
    :param sudoku:
    :return: matrix mat with hanidoku dimensions such that:
        if sudoku[i][j] has value -> mat[i][j] == -1
        if sudoku[i][j] empty ->  mat[i][j] == {1,2,... , hanidokuFactor}
    """
    mat = []
    for i in range(len(sudoku)):
        arr = []
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                arr.append(set(range(1, hanidokuFactor + 1)))
            else:
                arr.append(-1)
        mat.append(arr)
    return mat



def updateNeighborsDomainSetMat(sudoku, i, j, domainSetMatNew):
    for var in getLineInclineDeclineSetByVar(i, j):
        if type(domainSetMatNew[var[0]][var[1]]) is set:
            domainSetMatNew[var[0]][var[1]].discard(sudoku[i][j])

    toDiscard = notInRange(sudoku, getLineByVar(i, j))
    for I,J in getLineByVar(i,j):
        if type(domainSetMatNew[I][J]) is set:
            domainSetMatNew[I][J] -= toDiscard

    toDiscard = notInRange(sudoku, getInclineByVar(i, j))
    for I,J in getInclineByVar(i, j):
        if type(domainSetMatNew[I][J]) is set:
            domainSetMatNew[I][J] -= toDiscard

    toDiscard = notInRange(sudoku, getDeclineByVar(i, j))
    for I, J in getDeclineByVar(i, j):
        if type(domainSetMatNew[I][J]) is set:
            domainSetMatNew[I][J] -= toDiscard



def calculateDomainSetMat(sudoku):
    """

    :param sudoku:
    :return: matrix mat with hanidoku dimensions such that:
        if sudoku[i][j] has value -> mat[i][j] == -1
        if sudoku[i][j] empty ->  mat[i][j] == {n : n is a legitimate consistent value to assign to sudoku[i][j]}
    """
    domainSetMat = createDomainSetMat(sudoku)

    # calculate the number already in use in each line and discard them from the domains of vars in said line
    for i in range(len(sudoku)):
        toDiscard = set()
        for val in sudoku[i]:
            if val != 0:
                toDiscard.add(val)
        for j in range(len(domainSetMat[i])):
            if type(domainSetMat[i][j]) is set:
                domainSetMat[i][j] -= toDiscard

    # calculate the number already in use in each incline and discard them from the domains of vars in said line
    for i in range(hanidokuFactor):  # hanidokuFacor == number of inclines
        toDiscard = set()
        for var in getInclineByIndex(i):
            if sudoku[var[0]][var[1]] != 0:
                toDiscard.add(sudoku[var[0]][var[1]])
        for var in getInclineByIndex(i):
            if type(domainSetMat[var[0]][var[1]]) is set:
                domainSetMat[var[0]][var[1]] -= toDiscard

    # calculate the number already in use in each decline and discard them from the domains of vars in said line
    for i in range(hanidokuFactor):  # hanidokuFacor == number of declines
        toDiscard = set()
        for var in getDeclineByIndex(i):
            if sudoku[var[0]][var[1]] != 0:
                toDiscard.add(sudoku[var[0]][var[1]])
        for var in getDeclineByIndex(i):
            if type(domainSetMat[var[0]][var[1]]) is set:
                domainSetMat[var[0]][var[1]] -= toDiscard

    # Discarding numbers that cannot be assigned in each line due to not inRange
    for i in range(len(sudoku)):
        toDiscard = notInRange(sudoku, getLineByIndex(i))
        for j in range(len(domainSetMat[i])):
            if type(domainSetMat[i][j]) is set:
                domainSetMat[i][j] -= toDiscard

    # Discarding numbers that cannot be assigned into each incline due to not inRange
    for i in range(hanidokuFactor):  # hanidokuFacor == number of inclines
        toDiscard = notInRange(sudoku, getInclineByIndex(i))
        for var in getInclineByIndex(i):
            if type(domainSetMat[var[0]][var[1]]) is set:
                domainSetMat[var[0]][var[1]] -= toDiscard

    # Discarding numbers that cannot be assigned into each decline due to not inRange
    for i in range(hanidokuFactor):  # hanidokuFacor == number of declines
        toDiscard = notInRange(sudoku, getDeclineByIndex(i))
        for var in getDeclineByIndex(i):
            if type(domainSetMat[var[0]][var[1]]) is set:
                domainSetMat[var[0]][var[1]] -= toDiscard

    return domainSetMat


def calculateDomainOfVar(sudoku,i,j):
    toDiscard = set()
    for val in sudoku[i]:
        if val != 0:
            toDiscard.add(val)

    for var in getInclineByVar(i,j):
        if sudoku[var[0]][var[1]] != 0:
            toDiscard.add(sudoku[var[0]][var[1]])

    for var in getDeclineByVar(i,j):
        if sudoku[var[0]][var[1]] != 0:
            toDiscard.add(sudoku[var[0]][var[1]])

    toDiscard = toDiscard.union(notInRange(sudoku, getLineByIndex(i)))
    toDiscard = toDiscard.union(notInRange(sudoku, getInclineByVar(i,j)))
    toDiscard = toDiscard.union(notInRange(sudoku, getDeclineByVar(i,j)))

    return set(range(1, hanidokuFactor + 1)) - toDiscard


# Correctness:

def sudoku_is_complete(sudoku):
    for row in sudoku:
        for var in row:
            if var == 0:
                return False
    return True

def allDifferent(sudoku, array):
    arr = indicesArrayToValuesArray(sudoku, array)
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            return False
    return True


def continuousArray(sudoku, array):
    arr = indicesArrayToValuesArray(sudoku, array)
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] != 1:
            return False
    return True


def sudoku_is_correct(sudoku):
    if sudoku_is_complete(sudoku) is False:
        return False
    numOfLines = len(sudoku)
    numOfInclines = hanidokuFactor
    numOfDeclines = hanidokuFactor

    for i in range(numOfLines):
        if allDifferent(sudoku, getLineByIndex(i)) is False or continuousArray(sudoku, getLineByIndex(i)) is False:
            return False
    for i in range(numOfInclines):
        if allDifferent(sudoku, getInclineByIndex(i)) is False or continuousArray(sudoku, getInclineByIndex(i)) is False:
            return False
    for i in range(numOfDeclines):
        if allDifferent(sudoku, getDeclineByIndex(i)) is False or continuousArray(sudoku, getDeclineByIndex(i)) is False:
            return False

    return True


def arrayNoDuplicate(arr):
    if max(arr) == 0:
        return True
    arr.sort()
    i = 0
    while arr[i] == 0:
        i += 1
    for k in range(i,len(arr) - 1 ):
        if arr[k] == arr[k+1]:
            return False
    return True



def arrayHasRange(arr):
    length = len(arr)
    maxi = max(arr)
    if maxi == 0:
        return True
    check = range(positiveMin(arr,length) + 1 , maxi)
    missing = 0
    for val in check:
        if val not in arr:
            missing += 1
    numofzeroes = 0
    for val in arr:
        if val == 0:
            numofzeroes += 1
    if numofzeroes >= missing:
        return True
    return False

def arrIsValid(arr):
    if arrayNoDuplicate(arr) is True and arrayHasRange(arr) is True:
        return True
    else:
        return False


def sudokuDimentionsCorrect(sudoku):
    if hanidokuFactor % 2 == 1:
        if hanidokuFactor != len(sudoku):
            return False
    else:
        if hanidokuFactor != len(sudoku) + 1:
            return False
    for i in range(0, middleRawIndex):
        if len(sudoku[i]) + 1 != len(sudoku[i+1]):
            return False
    for i in range(middleRawIndex , len(sudoku) - 1):
        if len(sudoku[i]) - 1 != len(sudoku[i+1]):
            return False
    return True


def inputSudokuIsVaild(sudoku):
    if sudokuDimentionsCorrect(sudoku) is False:
        print("dimentions are wrong")
        return False
    for i in range(0, len(sudoku)):
        indicesLine = getLineByIndex(i)
        line = indicesArrayToValuesArray(sudoku, indicesLine)
        if arrIsValid(line) is False:
            print("line: ",i, " is Wrong")
            return False

    for i in range(0,hanidokuFactor):
        indicesIncline = getInclineByIndex(i)
        incline = indicesArrayToValuesArray(sudoku, indicesIncline)
        if arrIsValid(incline) is False:
            print("incline: ",i, " is Wrong")
            return False

    for i in range(0,hanidokuFactor):
        indicesDecline = getDeclineByIndex(i)
        decline = indicesArrayToValuesArray(sudoku, indicesDecline)
        if arrIsValid(decline) is False:
            print("decline: ",i, " is Wrong")
            return False

    return True


def varNeighborsSetOfVar(sudoku, i, j):
    """

    :param sudoku:
    :param i: i'th index of var
    :param j: j'th index of var
    :return: A set of tuples representing all variables!! that in the same line / incline / decline with var
             not including var itself!
    """
    neighborsSet = getLineInclineDeclineSetByVar(i, j)  # set of indices
    varNeighbors = set()
    for neighbor in neighborsSet:
        if sudoku[neighbor[0]][neighbor[1]] != 0 or neighbor == (i, j):
            continue
        varNeighbors.add(neighbor)
    return varNeighbors


def calculateDomainOfVarsInRelation(sudoku, i, j):
    domainDict = {}
    Vars = varNeighborsSetOfVar(sudoku, i, j)
    for var in Vars:
        if sudoku[var[0]][var[1]] != 0:
            continue
        domainDict[var] = calculateDomainOfVar(sudoku, var[0], var[1])
    return domainDict

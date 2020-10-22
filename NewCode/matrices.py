from input import hanidoku

sudokuLength = len(hanidoku)
middleRawIndex = (sudokuLength - 1) // 2
middleRaw = hanidoku[middleRawIndex]
hanidokuFactor = len(middleRaw)


##########################################################################################################
##########################################################################################################
# Utility Functions:

def zeroes(mat):
    """
    Counts the amount of 0's in a mat
    :param mat:
    :return:
    """
    counter = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                counter += 1
    return counter



def printMat(mat):
    for line in mat:
        print(line)


def printSudoku(sudoku):
    print("Result:")
    for row in sudoku:
        print(row)

##########################################################################################################
##########################################################################################################
# initializing Functions:
# NOT TO BE CALLED OR IMPORTED!!!

# Inclines AND Declines:
def _getIncline(sudoku, i):
    """
    :param sudoku:
    :param i: the number of the diagonal incline: 0<= i <= n-1
    :return: all values in the i'th incline as an array
    """
    if hanidokuFactor % 2 == 0:
        k = 1
    else:
        k = 0
    answer = []
    n = len(sudoku) + k
    m = (n - 1) // 2
    n = n - k
    if i <= m:
        for j in range(0, i+1):
            answer.append((m+(i-j), j))
        for j in range(1, m+1):
            answer.append((m-j, i))
    else:
        for j in range(1, ((n+1)//2)+1):
            answer.append((n-j, i-m+j-1))
        for j in range(1, (n-1-i)+1+k):
            answer.append((m-j, i))
    return answer


def _getDecline(sudoku, i): # not to be used other than creating declineMAT
    """
        :param sudoku:
        :param i: the number of the diagonal decline: 0<= i <= n-1
        :return: all values in the i'th decline as an array
    """
    n = len(sudoku)
    m = (n - 1) // 2
    answer = []
    inclineArray = _getIncline(sudoku,i) #NOT an ERROR it's incline on purpose
    for i in range(len(inclineArray)):
        temp = list(inclineArray[i])
        temp[0] = 2*m - temp[0]
        temp = tuple(temp)
        answer.append(temp)
    return answer


def _createInclineMat(sudoku):
    if hanidokuFactor % 2 == 0:
        k = 1
    else:
        k = 0
    mat = []
    for i in range(len(sudoku) + k):
        mat.append(_getIncline(sudoku, i))
    return mat


def _createDeclineMat(sudoku):
    if hanidokuFactor % 2 == 0:
        k = 1
    else:
        k = 0
    mat = []
    for i in range(len(sudoku) + k):
        mat.append(_getDecline(sudoku, i))
    return mat


inclineMat = _createInclineMat(hanidoku)  # inclineMat[i] == incline i indices of hanidoku
declineMat = _createDeclineMat(hanidoku)  # declineMat[i] == decline i indices of hanidoku


# Lines:
def _createLineMat(sudoku):
    mat = []
    for i in range(len(sudoku)):
        lineOfElement = [(i, k) for k in range(0, len(sudoku[i]))]  # create list of indices of line i
        mat.append(lineOfElement)
    return mat


lineMat = _createLineMat(hanidoku)  # lineMat[i] == line i indices of hanidoku



def getInclineIndexByVar(i,j):
    """
    Recieve the index of a variable in sudoku
    :param sudoku:
    :param i: i value of the variable in question
    :param j: j value of the variable in question
    :return: the incline index that value belongs to (there is only one)
    """
    if i <= middleRawIndex:
        return j
    else:
        return i - middleRawIndex + j


def getDeclineIndexByVar(i,j):
    """
        Recieve the index of a variable in sudoku
        :param sudoku:
        :param i: i value of the variable in question
        :param j: j value of the variable in question
        :return: the incline that value belongs to (there is only one)
    """
    if i <= middleRawIndex:
        return middleRawIndex - i + j
    else:
        return j


# Belongs To Matrix:
def _createBelongToMat(sudoku):
    mat=[]
    for i in range(len(sudoku)):
        arr=[]
        for j in range(len(sudoku[i])):
            tup = (getInclineIndexByVar(i, j), getDeclineIndexByVar(i, j))
            arr.append(tup)
        mat.append(arr)
    return mat


belongTo = _createBelongToMat(hanidoku)  # belongsTo[i][j] == (incline index of hanidoku[i][j] , decline index of hanidoku[i][j])
##########################################################################################################
##########################################################################################################


# Callable Functions:



def getInclineByIndex(i):
    return inclineMat[i]


def getDeclineByIndex(i):
    return declineMat[i]


def getInclineByVar(i, j):
    return getInclineByIndex(belongTo[i][j][0])


def getDeclineByVar(i, j):
    return getDeclineByIndex(belongTo[i][j][1])


def getLineByIndex(i):
    return lineMat[i]


def getLineByVar(i,j):
    return lineMat[i]

def getSharedIndicesArray(var1, var2):
    """

    :param var1: indices tuple of var1
    :param var2: indices tuple of var1
    :return: indices array of the line / incline / decline both variables are in.
    """
    i1 = var1[0]
    j1 = var1[1]
    i2 = var2[0]
    j2 = var2[1]

    if i1 == i2:
        return getLineByIndex(i1)
    if getInclineIndexByVar(i1, j1) == getInclineIndexByVar(i2, j2):
        return getInclineByVar(i1, j1)
    if getDeclineIndexByVar(i1, j1) == getDeclineIndexByVar(i2, j2):
        return getDeclineByVar(i1, j1)

    return None


def getLineInclineDeclineSetByVar(i,j):
    answer = set()
    answer = answer.union(getLineByVar(i,j))
    answer = answer.union(getInclineByVar(i,j))
    answer = answer.union(getDeclineByVar(i,j))
    return answer







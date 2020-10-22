import copy

from backtracking import backtracking_search
from backtracking_memory import backtracking_search_memory
from matrices import hanidokuFactor
from matrices import getLineByIndex
from matrices import getInclineByVar
from matrices import getDeclineByVar

from gameLogic import notInRange
from gameLogic import calculateDomainSetMat

from arc_consistent import ac3


def nonNegativeMinIndex(arr):
    """
    returns the minimum Non-Negative integer in an arr that has at least one value > -1
    """
    i=0
    while (arr[i] == -1):
        i+=1
    mini = i
    for x in range(i+1, len(arr)):
        if arr[x] != -1 and arr[x] < arr[mini]:
            mini = x
    return mini


def lcv_values(sudoku, i, j, domainMat):
    """

    :param sudoku:
    :param i: line index of selected var
    :param j: column index of selected var
    :param domainMat: Mat[x][y] = set -> set hold domain of var (x,y)
    :return: ordered list of var's ( var == (i,j) ) values in order (according to heuristic logic) of selection
    """
    valueSet = domainMat[i][j]  # must not be empty
    if valueSet == set():
        return None
    orderedList = [-1] * (hanidokuFactor + 1)
    for value in valueSet:
        sudoku[i][j] = value
        counter = 0

        toDiscardFromLine = notInRange(sudoku, getLineByIndex(i))
        lineDomains = {}
        for var in getLineByIndex(i):
            if var == (i, j) or sudoku[var[0]][var[1]] != 0:
                continue
            lineDomains[var] = copy.deepcopy(domainMat[var[0]][var[1]])
            lineDomains[var] -= {value}
            lineDomains[var] -= toDiscardFromLine
            counter += len(domainMat[var[0]][var[1]] - lineDomains[var])

        toDiscardFromIncline = notInRange(sudoku, getInclineByVar(i,j))
        inclineDomains = {}
        for var in getInclineByVar(i,j):
            if var == (i, j) or sudoku[var[0]][var[1]] != 0:
                continue
            inclineDomains[var] = copy.deepcopy(domainMat[var[0]][var[1]])
            inclineDomains[var] -= {value}
            inclineDomains[var] -= toDiscardFromIncline
            counter += len(domainMat[var[0]][var[1]] - inclineDomains[var])

        toDiscardFromDecline = notInRange(sudoku, getDeclineByVar(i, j))
        declineDomains = {}
        for var in getDeclineByVar(i, j):
            if var == (i, j) or sudoku[var[0]][var[1]] != 0:
                continue
            declineDomains[var] = copy.deepcopy(domainMat[var[0]][var[1]])
            declineDomains[var] -= {value}
            declineDomains[var] -= toDiscardFromDecline
            counter += len(domainMat[var[0]][var[1]] - declineDomains[var])

        sudoku[i][j] = 0
        orderedList[value] = counter

    answer = []
    for k in valueSet:
        minIndex = nonNegativeMinIndex(orderedList)
        answer.append(minIndex)
        orderedList[minIndex] = -1

    return answer




def var_selector_no_ac3(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                domainSetMat = calculateDomainSetMat(sudoku)
                domain = lcv_values(sudoku, i, j, domainSetMat)
                return i, j, domain

def var_selector_ac3(sudoku, domainSetMat):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                domain = lcv_values(sudoku,i,j, domainSetMat)
                return i, j, domain


def search(sudoku, useAc3=False):
    if useAc3 is False:
        return backtracking_search(sudoku, var_selector_no_ac3)
    else:
        variables = set()
        for i in range(len(sudoku)):
            for j in range(len(sudoku[i])):
                if sudoku[i][j] == 0:
                    variables.add((i, j))
        domainSetMat = calculateDomainSetMat(sudoku)
        check = ac3(sudoku, variables, domainSetMat)
        if check is False:
            return None
        return backtracking_search_memory(sudoku, var_selector_ac3, domainSetMat, variables)


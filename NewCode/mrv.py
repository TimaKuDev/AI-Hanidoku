"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""

from backtracking import backtracking_search
from backtracking_memory import backtracking_search_memory
from matrices import hanidokuFactor
from gameLogic import calculateDomainSetMat
from arc_consistent import ac3


def minDomainArray(domainMat):
    arr = []
    min = hanidokuFactor
    for i in range(len(domainMat)):
        for j in range(len(domainMat[i])):
            if type(domainMat[i][j]) is set:
                length = len(domainMat[i][j])
                if length > min:
                    continue
                if length == min:
                    arr.append((i, j))
                elif length < min:
                    min = length
                    if min == 0:
                        return []
                    arr = []
                    arr.append((i, j))
    return arr


def mrv_domains(sudoku, allMinDomainVars, returnDomainSetMat, domainMat=None):
    if domainMat is None:
        domainSetMat = calculateDomainSetMat(sudoku)
    else:
        domainSetMat = domainMat
    minDomainsVariablesArray = minDomainArray(domainSetMat)

    if len(minDomainsVariablesArray) == 0:
        if returnDomainSetMat is True:
            return None, None
        else:
            return None

    if allMinDomainVars is True:  # return all the variables that have minimum domain length
        min_domains = {var: domainSetMat[var[0]][var[1]] for var in minDomainsVariablesArray}

    else:  # return just one variable that have minimum domain length
        var = minDomainsVariablesArray[0]
        min_domains = {var: domainSetMat[var[0]][var[1]]}

    if returnDomainSetMat is True:
        return min_domains, domainSetMat
    else:
        return min_domains



def var_selector_no_ac3(sudoku):
    min_domains = mrv_domains(sudoku, False, False)

    if not min_domains:
        return None, None, None
    var = min_domains.popitem()
    return var[0][0], var[0][1], var[1]


def var_selector_ac3(sudoku, domainSetMat):
    minDomainsVariablesArray = minDomainArray(domainSetMat)
    var = minDomainsVariablesArray[0]
    return var[0],var[1], domainSetMat[var[0]][var[1]]


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


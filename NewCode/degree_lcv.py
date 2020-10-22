from backtracking import backtracking_search
from backtracking_memory import backtracking_search_memory
from degree import maxDegreeVar
from gameLogic import calculateDomainSetMat
from lcv import lcv_values
from arc_consistent import ac3


def var_selector_no_ac3(sudoku):
    var = maxDegreeVar(sudoku)
    domainSetMat = calculateDomainSetMat(sudoku)
    orderedDomain = lcv_values(sudoku, var[0], var[1], domainSetMat)
    return var[0], var[1], orderedDomain


def var_selector_ac3(sudoku, domainSetMat):
    var = maxDegreeVar(sudoku)
    orderedDomain = lcv_values(sudoku, var[0], var[1], domainSetMat)
    return var[0], var[1], orderedDomain


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


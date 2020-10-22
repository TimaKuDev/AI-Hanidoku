"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""
from copy import deepcopy

from gameLogic import sudoku_is_complete
from arc_consistent import updateDomainSetMat

iteration = 0



def backtracking_search_memory(sudoku, var_selector, domainSetMat, variablesSet):
    global iteration
    iteration += 1
    if sudoku_is_complete(sudoku):
        return sudoku
    var_i, var_j, domain = var_selector(sudoku, domainSetMat)
    if domain is None:
        return None
    for val in domain:
        sudoku[var_i][var_j] = val
        variablesSetNew = deepcopy(variablesSet)
        variablesSetNew.remove((var_i, var_j))
        domainSetMatNew = deepcopy(domainSetMat)
        domainSetMatNew[var_i][var_j] = -1
        checkSuccess = updateDomainSetMat(sudoku, var_i, var_j, domainSetMatNew,variablesSetNew)
        if checkSuccess is False:
            sudoku[var_i][var_j] = 0
            continue
        result = backtracking_search_memory(sudoku, var_selector, domainSetMatNew, variablesSetNew)
        if result:
            return result
        sudoku[var_i][var_j] = 0
    return None


def resetIterationM():
    global iteration
    iteration = 0
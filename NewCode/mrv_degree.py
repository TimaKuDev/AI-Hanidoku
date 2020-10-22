"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""

from mrv import mrv_domains
from backtracking import backtracking_search
from backtracking_memory import backtracking_search_memory
from degree import maxDegreeVar

from gameLogic import calculateDomainSetMat
from arc_consistent import ac3



def var_selector_no_ac3(sudoku):
    min_domains = mrv_domains(sudoku, True, False)

    if not min_domains:
        return None, None, None

    if len(min_domains) == 1:
        var = min_domains.popitem()
        return var[0][0], var[0][1], var[1]

    var = maxDegreeVar(sudoku, min_domains.keys())
    return var[0], var[1], min_domains[var]


def var_selector_ac3(sudoku, domainSetMat):
    min_domains = mrv_domains(sudoku, True, False, domainSetMat)

    if len(min_domains) == 1:
        var = min_domains.popitem()
        return var[0][0], var[0][1], var[1]

    var = maxDegreeVar(sudoku, min_domains.keys())
    return var[0], var[1], min_domains[var]



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


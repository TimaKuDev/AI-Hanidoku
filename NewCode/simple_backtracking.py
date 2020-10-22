"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""
from backtracking import backtracking_search
from backtracking_memory import backtracking_search_memory

from gameLogic import calculateDomainOfVar
from gameLogic import calculateDomainSetMat
from arc_consistent import ac3




def var_selector_no_ac3(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                domain = calculateDomainOfVar(sudoku, i, j)
                return i, j, domain


def var_selector_ac3(sudoku, domainSetMat):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                domain = domainSetMat[i][j]
                return i, j, domain


def search(sudoku,useAc3=False):
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



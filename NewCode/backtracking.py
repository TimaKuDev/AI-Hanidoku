"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""

from gameLogic import sudoku_is_complete
from gameLogic import value_is_consistent


iteration = 0


def backtracking_search(sudoku, var_selector, check=False):
    global iteration
    iteration += 1
    if sudoku_is_complete(sudoku):
        return sudoku
    var_i, var_j, domain = var_selector(sudoku)
    if domain is None:
        return None
    for val in domain:
        if check is True:  # Simple BackTracking
            if not value_is_consistent(sudoku, var_i, var_j, val):
                continue
        sudoku[var_i][var_j] = val
        result = backtracking_search(sudoku, var_selector, check)
        if result:
            return result
        sudoku[var_i][var_j] = 0
    return None


def resetIteration():
    global iteration
    iteration = 0
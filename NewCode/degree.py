from matrices import getInclineByIndex
from matrices import getDeclineByIndex
from backtracking import backtracking_search
from backtracking_memory import backtracking_search_memory
from matrices import hanidokuFactor
from gameLogic import varNeighborsSetOfVar
from gameLogic import calculateDomainOfVar
from gameLogic import calculateDomainSetMat
from arc_consistent import ac3

def degreeOfVar(sudoku, var):
    return len(varNeighborsSetOfVar(sudoku, var[0], var[1]))


def degreeDictOfVars(sudoku, vars):
    degree_dict = {}
    for var in vars:
        degree_dict[var[0], var[1]] = degreeOfVar(sudoku, var)
    return degree_dict



def degreeDictOfAllVars(sudoku):
    """
    :param sudoku:
    :return: domains_dict[i,j] = x  -> var (i,j) has degree of x
    """
    degree_dict = {}
    length = len(sudoku)

    for i in range(length):
        counter = 0
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                counter += 1
                degree_dict[i, j] = 0
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                degree_dict[i, j] = counter  # numbre of 0's in line i

    for i in range(hanidokuFactor):
        incline = getInclineByIndex(i)
        counter = 0
        for pair in incline:
            if sudoku[pair[0]][pair[1]] == 0:
                counter += 1
        for pair in incline:
            if sudoku[pair[0]][pair[1]] == 0:
                degree_dict[pair] += counter

    for i in range(hanidokuFactor):
        decline = getDeclineByIndex(i)
        counter = 0
        for pair in decline:
            if sudoku[pair[0]][pair[1]] == 0:
                counter += 1
        for pair in decline:
            if sudoku[pair[0]][pair[1]] == 0:
                degree_dict[pair] += counter

    return degree_dict



def maxDegreeVar(sudoku, vars=None):
    """

    :param sudoku:
    :param vars: set of variables
    :param allMaxDegreeVars:
    :return:
        if vars is none -> var with maximum degree out of all possible variables in sudoku
        else -> var with maximum degree out of vars set.
    """
    if vars is None:
        degree_dict = degreeDictOfAllVars(sudoku)
    else:
        degree_dict = degreeDictOfVars(sudoku, vars)
    max_degree_val = max(degree_dict.values())

    for var in degree_dict.keys():
        if degree_dict[var] == max_degree_val:
            max_degree_var = var
            break
    return max_degree_var


def var_selector_no_ac3(sudoku):
    max_degree_var = maxDegreeVar(sudoku)
    if not max_degree_var:
        return None, None, None
    i = max_degree_var[0]
    j = max_degree_var[1]
    return i, j, calculateDomainOfVar(sudoku, i, j)


def var_selector_ac3(sudoku, domainSetMat):
    return var_selector_no_ac3(sudoku)




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


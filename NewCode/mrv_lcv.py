from backtracking import backtracking_search
from backtracking_memory import backtracking_search_memory
from lcv import lcv_values
from mrv import mrv_domains
from mrv import minDomainArray

from gameLogic import calculateDomainSetMat
from arc_consistent import ac3

def var_selector_no_ac3(sudoku):
    min_domains, domainSetMat = mrv_domains(sudoku, False, True)

    if not min_domains:
        return None, None, None
    var = min_domains.popitem()
    orderedDomain = lcv_values(sudoku, var[0][0], var[0][1], domainSetMat)

    return var[0][0], var[0][1], orderedDomain


def var_selector_ac3(sudoku, domainSetMat):
    minDomainsVariablesArray = minDomainArray(domainSetMat)
    var = minDomainsVariablesArray[0]
    i = var[0]
    j = var[1]
    return i, j, lcv_values(sudoku, i, j, domainSetMat)


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


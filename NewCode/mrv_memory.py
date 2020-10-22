#from backtracking_memory import backtracking_search
from matrices import hanidokuFactor
from gameLogic import calculateDomainSetMat


def mrv_domains_memory(sudoku, domainSetSizeMat):

 #   minDomainsVariablesArray = minDomainSizeArray(domainSetSizeMat)
    if len(minDomainsVariablesArray) == 0:
        return None

    min_domains = {var : domainSetSizeMat[var[0]][var[1]] for var in minDomainsVariablesArray}
    return min_domains



def var_selector(sudoku, domainSetSizeMat):
    min_domains = mrv_domains_memory(sudoku, domainSetSizeMat)

    if not min_domains:
        return None, None, None
    var = min_domains.popitem()
    return var[0][0], var[0][1], var[1]


def search(sudoku):
    domainSetMat = calculateDomainSetMat(sudoku)
  #  domainSetSizeMat = calculateDomainSizeMat(domainSetMat)
   # return backtracking_search(sudoku, var_selector, 2, domainSetSizeMat)




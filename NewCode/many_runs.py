import os
import platform
import time

from copy import copy, deepcopy
from random import randrange
from matrices import hanidokuFactor

import simple_backtracking

import mrv
import degree
import lcv

import mrv_degree
import mrv_lcv
import degree_lcv

import mrv_degree_lcv

import winsound

from input import hanidoku
from backtracking import resetIteration
from backtracking_memory import resetIterationM


platform_system = platform.system()
def clear_screen():
    if platform_system == 'Linux':
        os.system('clear')
    elif platform_system == 'Windows':
        os.system('cls')


a = "Simple backtracking"
b = "MRV"
c = "Degree"
d = "LCV"
e = "MRV and Degree"
f = "MRV and LCV"
g = "Degree and LCV"
h = "MRV and Degree and LCV"


choosen = ""
theTime = "The time it took: "
anwser = ""
Hanidoku = "The Hanidoku is:\n"
resultHanidoku = "The result is:\n"
applyAC3 = ""


copiedHanidoku = deepcopy(hanidoku)
currentZeros = 0
amountOfIndices = 0


otherHanidoku=""
justTime = 0

result = None

for i in range(len(hanidoku)):
    for j in range(len(hanidoku[i])):
        amountOfIndices += 1


while currentZeros != amountOfIndices + 1:
    for useAc3 in range(2):
        if useAc3 < 0 or useAc3 > 1:
            raise Exception
        if useAc3 == 0:
            useAc3 = False
        else:
            useAc3 = True

        for option in range(6):
            starting_time = time.time()
            if option == 0:
                choosen += a
                result = simple_backtracking.search(deepcopy(copiedHanidoku), useAc3)
            elif option == 1:
                choosen += b
                result = mrv.search(deepcopy(copiedHanidoku), useAc3)
            elif option == 2:
                choosen += c
                result = degree.search(deepcopy(copiedHanidoku), useAc3)
            elif option == 2:
                choosen += d
                result = lcv.search(deepcopy(copiedHanidoku), useAc3)
            elif option == 3:
                choosen += e
                result = mrv_degree.search(deepcopy(copiedHanidoku), useAc3)
            elif option == 4:
                choosen += f
                result = mrv_lcv.search(deepcopy(copiedHanidoku), useAc3)
            elif option == 6:
                choosen += g
                result = degree_lcv.search(deepcopy(copiedHanidoku), useAc3)
            elif option == 5:
                choosen += h
                result = mrv_degree_lcv.search(deepcopy(copiedHanidoku), useAc3)

            ending_time = time.time()
            theTime += str(ending_time - starting_time)
            justTime = ending_time - starting_time

            if useAc3 is True:
                from backtracking_memory import iteration
                reset = resetIterationM()
            else:
                from backtracking import iteration
                reset = resetIteration()

            if result is None:
                anwser += "This sudoku is not solvable!\nNumber of Steps: " + str(iteration)

            else:
                anwser += "This sudoku is solvable!\nNumber of Steps: " + str(iteration) + "\n"
                str_lines = []
                for row in result:
                    str_lines.append(str(row))
                    resultHanidoku += str(row) + ",\n"

            Hanidoku += "[\n"
            resultHanidoku += "[\n"
            for row in copiedHanidoku:
                Hanidoku += str(row) + ",\n"
            Hanidoku += "]\n"

            try:
                with open(r"C:\Users\libxp\Desktop\NewCode\Giladushka\Anwser"+str(hanidokuFactor)+".txt", "a") as ff:
                    if useAc3 is True:
                        applyAC3 = "Using AC3 "
                    toWrite = applyAC3 + choosen + "\n" + theTime + "\n" + anwser + "\n" + str(currentZeros) + "\n" + str(amountOfIndices) + "\n" + Hanidoku + "\n" + resultHanidoku + "\n" + "################################################################################" + "\n" + "\n"
                    ff.write(toWrite)
                    ff.close()
            except:
                pass
            finally:
                applyAC3 =''
                anwser = ""
                Hanidoku = "The Hanidoku is:\n"
                choosen = ""
                theTime = "The time it took: "
                resultHanidoku = "The result is:\n"


            try:
                with open(r"C:\Users\libxp\Desktop\NewCode\Giladushka\AnwserCSV"+str(hanidokuFactor)+".txt", "a") as ff:
                    toWrite = str(justTime) + "\n" + str(iteration) + "\n"
                    ff.write(toWrite)
                    ff.close()
            except:
                pass
            reset

    try:
        with open(r"C:\Users\libxp\Desktop\NewCode\Giladushka\AnwserCSV"+str(hanidokuFactor)+".txt", "a") as ff:
            toWrite ="\n"
            ff.write(toWrite)
            ff.close()
    except:
        pass

    rangeList = range(len(copiedHanidoku))
    lastNumber = rangeList[len(rangeList) - 1:][0] + 1
    i = randrange(lastNumber)
    rangeList = range(len(copiedHanidoku[i]))
    lastNumber = rangeList[len(rangeList) - 1:][0] + 1
    j = randrange(lastNumber)


    while copiedHanidoku[i][j] == 0:
        rangeList = range(len(copiedHanidoku))
        lastNumber = rangeList[len(rangeList) - 1:][0] + 1
        i = randrange(lastNumber)
        rangeList = range(len(copiedHanidoku[i]))
        lastNumber = rangeList[len(rangeList) - 1:][0] + 1
        j = randrange(lastNumber)

        if currentZeros == amountOfIndices:
            break

    copiedHanidoku[i][j] = 0

    currentZeros += 1

# duration = 1000  # milliseconds
# freq = 540  # Hz
# winsound.Beep(freq, duration)



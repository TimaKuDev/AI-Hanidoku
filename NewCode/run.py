# !/usr/bin/env python3
"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""
from copy import deepcopy

from input import hanidoku


#print(getInclineByIndex(1))

import os
import platform
import sys
import time
#######################################################################################################
import simple_backtracking

import mrv
import degree
import lcv

import mrv_degree
import mrv_lcv
import degree_lcv
import mrv_degree_lcv

from gameLogic import inputSudokuIsVaild
from gameLogic import sudoku_is_correct
from matrices import middleRawIndex

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
indexx = middleRawIndex
while True:
    option = -1
    choosen = "The Algorithm that we used is: "
    theTime = "The time it took: "
    anwser = ""
    Hanidoku = "The Hanidoku is:\n"
    resultHanidoku = "The result is:\n"
    applyAC3 = ""

    Hanidoku += "[\n"
    resultHanidoku += "[\n"
    for row in hanidoku:
        Hanidoku += str(row) + ",\n"
    Hanidoku += "]\n"

    if inputSudokuIsVaild(hanidoku) is False:
        print("input Sudoku is Wrong!")
        sys.exit(1)

    while True:
        # clear_screen()
        print("    Choose Algorithm:")
        print("    0- No AC-3")
        print("    1- AC-3")
        print("    To exit -1")

        try:
            useAc3 = int(input("Enter a number: "))
            if useAc3 == -1:
                break
            if useAc3 < 0 or useAc3 > 1:
                raise Exception
            if useAc3 == 0:
                useAc3 = False
            else:
                useAc3 = True
        except:
            continue
        print()
        print("Algorithms :")
        print("    0-", a)
        print("    1-", b)
        print("    2-", c)
        print("    3-", d)
        print("    4-", e)
        print("    5-", f)
        print("    6-", g)
        print("    7-", h)

        print("    -1- Exit")
        try:
            option = int(input("Enter a number: "))
            if option < 0 or option > 7:
                raise Exception
        except:
            continue

        break

    if option == -1:
        break

    result = None
    ###############################################################################

    starting_time = time.time()

    if option == 0:
        choosen += a
        result = simple_backtracking.search(deepcopy(hanidoku), useAc3)
    elif option == 1:
        choosen += b
        result = mrv.search(deepcopy(hanidoku), useAc3)
    elif option == 2:
        choosen += c
        result = degree.search(deepcopy(hanidoku), useAc3)
    elif option == 3:
        choosen += d
        result = lcv.search(deepcopy(hanidoku), useAc3)
    elif option == 4:
        choosen += e
        result = mrv_degree.search(deepcopy(hanidoku), useAc3)
    elif option == 5:
        choosen += f
        result = mrv_lcv.search(deepcopy(hanidoku), useAc3)
    elif option == 6:
        choosen += g
        result = degree_lcv.search(deepcopy(hanidoku), useAc3)
    elif option == 7:
        choosen += h
        result = mrv_degree_lcv.search(deepcopy(hanidoku), useAc3)

    if useAc3 is True:
        from backtracking_memory import iteration
    else:
        from backtracking import iteration

    ending_time = time.time()
    print("\n" + theTime, ending_time - starting_time)
    theTime += str(ending_time - starting_time)
    if result is None:

        print("This sudoku is not solvable!\nNumber of Steps: " + str(iteration))
        anwser += "This sudoku is not solvable!\nNumber of Steps: " + str(iteration)

    else:
        anwser += "This sudoku is solvable!\nNumber of Steps: " + str(iteration)
        str_lines = []
        print("Result:\nNumber of Steps: " + str(iteration))

        i = 0
        spacee = ""

        for row in result:
            for x in range(abs(indexx - i)):
                spacee += " "
            str_lines.append(spacee + str(row))
            i += 1
            spacee = ""
            resultHanidoku += str(row) + ",\n"
        stri = '\n'.join(str_lines)
        print(stri)
        print("")

        if sudoku_is_correct(result) is True:
            print("The result sudoku is correct!\n")
        else:
            print("The result sudoku is Incorrect!!\n")
        try:
            with open('output.txt', 'w') as file:
                file.write(stri)
        except:
            pass
    resultHanidoku += "]\n"
    try:
        with open("Anwser.txt", "a") as ff:
            if useAc3 is True:
                applyAC3 = "Using AC3 "
            toWrite = applyAC3 + choosen + "\n" + theTime + "\n" + anwser + "\n" + Hanidoku + "\n" + resultHanidoku + "\n" + "################################################################################" + "\n" + "\n"
            ff.write(toWrite)
            ff.close()
    except:
        pass

input("Press Enter to exit")
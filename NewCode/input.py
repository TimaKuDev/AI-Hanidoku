hanidoku10 = [
    [5, 4, 6, 3, 2, 7],
    [4, 3, 9, 5, 7, 6, 8],
    [3, 6, 7, 8, 10, 4, 5, 9],
    [2, 7, 5, 10, 3, 8, 9, 4, 6],
    [1, 5, 8, 9, 4, 2, 7, 6, 3, 10],
    [2, 4, 6, 8, 9, 10, 3, 5, 7],
    [3, 7, 9, 10, 6, 5, 4, 8],
    [4, 6, 5, 3, 8, 7, 9],
    [5, 3, 4, 7, 2, 6],
]

hanidoku6 = [[2, 5, 3, 4],
             [3, 4, 1, 2, 5],
             [1, 2, 5, 3, 4, 6],
             [3, 4, 6, 2, 5],
             [2, 5, 3, 4]]

hanidoku9 = [
    [4, 2, 6, 3, 5],
    [6, 1, 5, 2, 4, 3],
    [5, 3, 8, 4, 7, 6, 2],
    [3, 4, 2, 9, 8, 5, 7, 6],
    [2, 5, 3, 7, 6, 9, 1, 8, 4],
    [6, 7, 8, 1, 2, 3, 4, 5],
    [4, 6, 9, 8, 5, 7, 3],
    [5, 2, 7, 4, 3, 6],
    [3, 4, 6, 5, 7]
]

hanidoku = []




def addZerosToHanidoku(amountOfZeros, zeroArray):
    global hanidoku
    for i in range(amountOfZeros):
        hanidoku[zeroArray[i][0]][zeroArray[i][1]] = 0


doku6 = [(2, 3), (4, 0), (2, 4), (4, 3), (1, 2), (1, 4), (3, 2), (2, 5), (0, 3), (1, 1), (0, 2), (3, 1), (0, 1), (0, 0),
         (2, 1), (3, 4), (2, 0), (4, 1), (2, 2), (3, 0), (4, 2), (1, 3), (1, 0), (3, 3)]

doku9 = [(5, 0), (6, 5), (6, 2), (8, 1), (7, 4), (1, 2), (2, 1), (8, 3), (7, 1), (3, 0), (5, 7), (3, 2), (5, 2), (5, 4),
         (3, 6), (3, 5), (6, 6), (2, 6), (0, 4), (6, 4),
         (0, 1), (5, 1), (1, 5), (2, 5), (2, 0), (4, 6), (4, 1), (0, 3), (1, 1), (3, 3), (7, 2), (6, 0), (8, 2), (4, 0),
         (6, 1), (6, 3), (2, 3), (1, 3), (0, 0), (4, 5),
         (2, 2), (7, 3), (7, 5), (5, 6), (7, 0), (0, 2), (5, 3), (3, 4), (1, 0), (2, 4), (1, 4), (3, 1), (5, 5), (8, 4),
         (8, 0), (4, 7), (4, 2), (3, 7), (4, 3), (4, 8), (4, 4)]

doku10 = [(5, 4), (5, 0), (0, 0), (0, 2), (6, 6), (3, 5), (7, 1), (2, 2), (3, 7), (3, 1), (1, 0), (8, 3), (6, 7),
          (6, 2), (8, 4), (1, 5), (4, 7), (4, 8), (3, 2), (4, 2), (1, 3), (1, 6), (6, 4), (6, 3), (6, 5),
          (5, 5), (3, 4), (7, 6), (7, 3), (5, 6), (2, 7), (3, 8), (2, 0), (4, 3), (7, 4), (8, 2), (3, 3), (8, 0),
          (0, 5), (0, 3), (4, 4), (6, 0), (1, 4), (2, 1), (0, 4), (1, 2), (0, 1), (3, 6), (6, 1), (8, 5),
          (2, 3), (4, 0), (4, 1), (1, 1), (2, 6), (3, 0), (7, 0), (8, 1), (5, 1), (5, 7), (4, 6), (4, 9), (7, 2),
          (2, 4), (5, 2), (4, 5), (5, 3), (7, 5), (5, 8), (2, 5)]

str_lines = []
space = ""
hanidokuMat = ""
i = 0
hanidokuOption = 0
zerosOption = 0
index = 4

while True:
    print("Please Choose Which Hanidoku u would like to test:")

    print("\nPress 1 to choose this Hanidoku(size 6, indices 24)")
    for row in hanidoku6:
        for x in range(abs(2 - i)):
            space += " "
        str_lines.append(space + str(row))
        i += 1
        space = ""
    hanidokuMat = '\n'.join(str_lines)
    print(hanidokuMat)

    space = ""
    hanidokuMat = ""
    str_lines = []
    i = 0
    print("\nPress 2 to choose this Hanidoku(size 9, indices 61)")
    for row in hanidoku9:
        for x in range(abs(4 - i)):
            space += " "
        str_lines.append(space + str(row))
        i += 1
        space = ""
    hanidokuMat = '\n'.join(str_lines)
    print(hanidokuMat)

    space = ""
    hanidokuMat = ""
    str_lines = []
    i = 0
    print("\nPress 3 to choose this Hanidoku(size 10, indices 70)")
    for row in hanidoku10:
        for x in range(abs(4 - i)):
            space += " "
        str_lines.append(space + str(row))
        i += 1
        space = ""
    hanidokuMat = '\n'.join(str_lines)
    print(hanidokuMat)
    space = ""
    hanidokuMat = ""
    str_lines = []
    i = 0

    hanidokuOption = int(input("\nEnter Your Choice:"))
    if not (0 < hanidokuOption < 4):
        print("\nPlease Enter Correct Number Between 1 - 3\n")
        continue
    zerosOption = int(input("\nPlease Enter the Amount of Zeros u want inisde the Hanidoku:"))

    if hanidokuOption == 1:
        index = 2
        hanidoku = hanidoku6
        if zerosOption > 24 or zerosOption < 0:
            zerosOption = 24
        addZerosToHanidoku(zerosOption, doku6)
    elif hanidokuOption == 2:
        hanidoku = hanidoku9
        if zerosOption > 61 or zerosOption < 0:
            zerosOption = 61
        addZerosToHanidoku(zerosOption, doku9)
    elif hanidokuOption == 3:
        hanidoku = hanidoku10
        if zerosOption > 70 or zerosOption < 0:
            zerosOption = 70
        addZerosToHanidoku(zerosOption, doku10)

    break

print("\nThe Hanidoku that given is:")
for row in hanidoku:
    for x in range(abs(index - i)):
        space += " "
    str_lines.append(space + str(row))
    i += 1
    space = ""
hanidokuMat = '\n'.join(str_lines)
print(hanidokuMat)
print("")
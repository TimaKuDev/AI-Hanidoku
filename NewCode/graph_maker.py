import matplotlib.pyplot as plt
import numpy as np
from matrices import hanidokuFactor
amountOfIndices = 25

SimpleBacktracking = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
MRV = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
Degree = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
LCV = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
MRVandDegree = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
MRVandLCV = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
DegreeandLCV = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
MRVandDegreeandLCV = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
AC3SimpleBacktracking = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
AC3MRV = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
AC3Degree = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
AC3LCV = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
AC3MRVandDegree = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
AC3MRVandLCV = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
AC3DegreeandLCV = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)
AC3MRVandDegreeandLCV = np.zeros(2*amountOfIndices).reshape(2,amountOfIndices)

arrayZeros = np.arange(0,amountOfIndices)



i = 0
j = 0
counter = 0

line =""

try:
    with open("F:\\AI\\Final Project\\NewCode\\Giladushka\\AnwserCSV6.txt", "r") as f:
        for line in f:
            if line == "\n":
                continue

            if(counter == 0):
                SimpleBacktracking[i, j] = float(line)
            if(counter == 1):
                MRV[i,j] = float(line)
            if(counter == 2):
                Degree[i,j] = float(line)
            if(counter == 3):
                LCV[i,j] = float(line)
            if(counter == 4):
                MRVandDegree[i,j] = float(line)
            if(counter == 5):
                MRVandLCV[i,j] = float(line)
            if (counter == 6):
                DegreeandLCV[i, j] = float(line)
            if (counter == 7):
                MRVandDegreeandLCV[i, j] = float(line)
            if (counter == 8):
                AC3SimpleBacktracking[i, j] = float(line)
            if (counter == 9):
                AC3MRV[i, j] = float(line)
            if (counter == 10):
                AC3Degree[i, j] = float(line)
            if (counter == 11):
                AC3LCV[i, j] = float(line)
            if (counter == 12):
                AC3MRVandDegree[i, j] = float(line)
            if (counter == 13):
                AC3MRVandLCV[i, j] = float(line)
            if (counter == 14):
                AC3DegreeandLCV[i, j] = float(line)
            if (counter == 15):
                AC3MRVandDegreeandLCV[i, j] = float(line)

            i += 1
            if(i == 2):
                counter += 1
            i = i % 2
            if counter == 16:
                j += 1
            counter = counter % 16


except:
    pass


plt.plot(arrayZeros,SimpleBacktracking[0],label="SimpleBacktracking")
plt.plot(arrayZeros,MRV[0],label="MRV")
plt.plot(arrayZeros,Degree[0],label="Degree")
plt.plot(arrayZeros,LCV[0],label="LCV")
plt.plot(arrayZeros,MRVandDegree[0],label="MRVandDegree")
plt.plot(arrayZeros,MRVandLCV[0],label="MRVandLCV")
plt.plot(arrayZeros,DegreeandLCV[0],label="DegreeandLCV")
plt.plot(arrayZeros,MRVandDegreeandLCV[0],label="MRVandDefreeandLCV")
plt.plot(arrayZeros,AC3SimpleBacktracking[0],label="AC3SimpleBacktracking")
plt.plot(arrayZeros,AC3MRV[0],label="AC3MRV")
plt.plot(arrayZeros,AC3Degree[0],label="AC3Degree")
plt.plot(arrayZeros,AC3LCV[0],label="AC3LCV")
plt.plot(arrayZeros,AC3MRVandDegree[0],label="AC3MRVandDegree")
plt.plot(arrayZeros,AC3MRVandLCV[0],label="AC3MRVandLCV")
plt.plot(arrayZeros,AC3DegreeandLCV[0],label="AC3DegreeandLCV")
plt.plot(arrayZeros,AC3MRVandDegreeandLCV[0],label="AC3MRVandDefreeandLCV")
plt.xlabel ("amount of zeros")
plt.ylabel ("time it took")
plt.legend()
plt.show()

print(AC3SimpleBacktracking[1])

plt.plot(arrayZeros,SimpleBacktracking[1],label="SimpleBacktracking")
plt.plot(arrayZeros,MRV[1],label="MRV")
plt.plot(arrayZeros,Degree[1],label="Degree")
plt.plot(arrayZeros,LCV[1],label="LCV")
plt.plot(arrayZeros,MRVandDegree[1],label="MRVandDegree")
plt.plot(arrayZeros,MRVandLCV[1],label="MRVandLCV")
plt.plot(arrayZeros,DegreeandLCV[1],label="DegreeandLCV")
plt.plot(arrayZeros,MRVandDegreeandLCV[1],label="MRVandDefreeandLCV")
plt.plot(arrayZeros,AC3SimpleBacktracking[1],label="AC3SimpleBacktracking")
plt.plot(arrayZeros,AC3MRV[1],label="AC3MRV")
plt.plot(arrayZeros,AC3Degree[1],label="AC3Degree")
plt.plot(arrayZeros,AC3LCV[1],label="AC3LCV")
plt.plot(arrayZeros,AC3MRVandDegree[1],label="AC3MRVandDegree")
plt.plot(arrayZeros,AC3MRVandLCV[1],label="AC3MRVandLCV")
plt.plot(arrayZeros,AC3DegreeandLCV[1],label="AC3DegreeandLCV")
plt.plot(arrayZeros,AC3MRVandDegreeandLCV[1],label="AC3MRVandDefreeandLCV")
plt.xlabel ("amount of zeros")
plt.ylabel ("iteration")
plt.legend()
plt.show()

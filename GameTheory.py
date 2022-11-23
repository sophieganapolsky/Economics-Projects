import numpy as np


def isFloat(var):
    try:
        float(var)
        return True
    except ValueError:
        return False

def isInt(var):
    try:
        int(var)
        return True
    except ValueError:
        return False


def numCheck(type,negative):
    while(True):
        var = input("")
        if type == "int":
            if not isInt(var):
                print("Please enter a number.")
            elif int(var) < 1:
                print("Please enter a positive number.")
            else:
                return var
        elif type == "float":
            if not isFloat(var):
                print("Please enter a number.")
            elif not negative and float(var) < 0:
                print("Please enter a number greater than or equal to 0.")
            else:
                return var

def maxInRow(arr,row,col):
    maxCol = 0
    for i in range(col):
        if arr[row][i] > arr[row][maxCol]:
            maxCol = i
    return arr[row][maxCol]

def maxInCol(arr,row,col):
    maxRow = 0
    for i in range(row):
        if arr[i][col] > arr[maxRow][col]:
            maxRow = i
    return arr[maxRow][col]

def nashEq():
    dim1 = 0
    dim2 = 0
    print("Start by creating the square payoff matrix.")
    print("Enter the number of prices for each firm: ")
    dim1 = numCheck("int", False)
    dim1 = int(dim1)
    dim2 = int(dim1)
    pricesA = []
    pricesB = []
    matA = [[0 for x in range(dim1)] for y in range(dim2)]
    matB = [[0 for x in range(dim1)] for y in range(dim2)]

    #entering and sorting prices
    print("Enter the prices for firm 1: ")
    for i in range(dim1):
        pricesA.append(float(numCheck("float", False)))
    print("Enter the prices for firm 2: ")
    for i in range(dim2):
        pricesB.append(float(numCheck("float", False)))
    print("Enter the profit for company 1 where...")
    for i in range(dim1):
        for j in range(dim2):
            print("firm 1 price = " + str(pricesA[i]) + ", firm 2 price = " + str(pricesB[j]) + ": ")
            matA[i][j] = float(numCheck("float", True))

    print("Enter the profit for company 2 where...")
    for j in range(dim2):
        for i in range(dim1):
            print("firm 1 price = " + str(pricesA[i]) + ", firm 2 price = " + str(pricesB[j]) + ": ")
            matB[i][j] = float(numCheck("float", True))

    #finding equilibria
    #max pairs for A
    maxA = []
    for i in range(dim2):
        max = maxInCol(matA, dim1, i)
        for j in range(dim1):
            if matA[j][i] == max:
                pair = (float(pricesA[j]), float(pricesB[i]))
                maxA.append(pair)

    #max pairs for B
    maxB = []
    for i in range(dim1):
        max = maxInRow(matB, i, dim2)
        for j in range(dim2):
            if matB[i][j] == max:
                pair = (float(pricesA[i]), float(pricesB[j]))
                maxB.append(pair)

    #finding shared pairs
    equilibria = []
    for i in range(len(maxA)):
        if maxA[i] in maxB:
            equilibria.append(maxA[i])

    if len(equilibria) == 0:
        print("There are no Nash equilibria.")
    elif len(equilibria) == 1:
        print("The Nash equilibrium is: ")
        print((equilibria[0]))
        print("where the first price is for firm 1 and the second price is for firm 2.")
    else:
        print("The Nash equilibria are: ")
        for i in range(len(equilibria)):
            print(equilibria[i])
        print("where the first price is for firm 1 and the second price is for firm 2.")

print("This program calculates the pure strategy Nash equilibria for 2 firms.")
nashEq()

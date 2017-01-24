import sys

# Assignment 1: Implement a solution to the knapsack problem using dynamic programming.
# This script can read in data from a file with entries separated by new lines and tabs.
# Each entry should have its own line; each data point in each entry should be separated by a tab.


# Formats an entry / item from the list of items to be considered for the knapsack
def formatEntry (name, weight, value):
    return 'name: ' + name + ', weight: ' + str(weight) + ', value: ' + str(value)

# Function to print the matrix with an optional statement
def printMatrix (matrix, statement=''):
    print statement
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            print matrix[x][y], '\t',
        print ''
    print ''

# Function to solve the knapsack problem
def solveKnapsack (nameList, weightList, valueList, maxWeight):
    # Horizontal: Choosing what items to take
    horizontal = len(weightList)

    # Vertical: Room in the knapsack
    vertical = maxWeight + 1

    matrix = [[-1 for y in range(vertical)] for x in range(horizontal)]

    # Initialize first row and column with zeroes
    for x in range(horizontal):
        matrix[x][0] = 0
    for y in range(vertical):
        matrix[0][y] = 0

    # Now that the first row / column are initialized, I can begin solving the knapsack problem...
    for y in range(1, len(matrix[0])):
        for x in range(1, len(matrix)):
            if weightList[x] <= y:
                matrix[x][y] = max(valueList[x] + matrix[x-1][y-weightList[x]], matrix[x-1][y])
            else:
                matrix[x][y] = matrix[x-1][y]

    printMatrix(matrix, 'Solving knapsack problem via dynamic programming...')

    # Trace back through the matrix to find which items were selected
    knapsack = []
    x = horizontal - 1
    y = vertical - 1
    totalWeight = 0

    while x > 0 and y > 0:
        if matrix[x][y] != matrix[x-1][y]:
            totalWeight += weightList[x]
            item = formatEntry(nameList[x], weightList[x], valueList[x])
            # item = nameList[x] + ' weight: ' + str(weightList[x]) + ' value: ' + str(valueList[x])
            knapsack.insert(0, item)
            y = y - weightList[x]
        x = x - 1

    print "Items in final knapsack:"
    for item in knapsack:
        print item
    print ''
    print "Total weight: ", totalWeight
    print "Total value: ", matrix[horizontal-1][vertical-1]


# Initialize lists with the first item in each list as 0 / essentially null (makes it easier for finding the solution)
nameList = [0]
weightList = [0]
valueList = [0]
print ''
print "Items from which to select:"

# Read in the list of items, their weights, and their values from a file. Put them in the separate lists.
with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in open(sys.argv[1])]
    for line in lines:
        entry = line.split('\t')

        # print line
        # print entry
        print formatEntry(entry[0], entry[1], entry[2])

        nameList.append(entry[0])
        weightList.append(int(entry[1]))
        valueList.append(int(entry[2]))
print ''
print "Max weight allowed in the knapsack: ", sys.argv[2]
print ''

solveKnapsack(nameList, weightList, valueList, int(sys.argv[2]))

print ''

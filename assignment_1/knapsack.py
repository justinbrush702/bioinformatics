import sys

# Assignment 1: Implement a solution to the knapsack problem using dynamic programming.
# This script can read in data from a file with entries separated by new lines and tabs.
# Each entry should have its own line; each data point in each entry should be separated by a tab.

errorAlert = '*****'

# Error trapping for input parameters

# If there are not enough parameters
if len(sys.argv) < 3:
    print errorAlert, 'To run this script, you must pass the following two arguments in order:'
    print '\tThe .tsv file containing the data'
    print '\tThe size of the knapsack.'
    print errorAlert, 'For example:'
    print '\tpython knapsack.py data.tsv 10'
    print errorAlert, 'Check the README file for more information.'
    sys.exit()

# Check to see if the file can be located
try:
    f = open(sys.argv[1])
except IOError as e:
    print errorAlert, 'Your file was not found. Make sure you properly enter the path to the file.'
    # print errorAlert, 'Here was the error given by the system:'
    # print "\tI/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit()
else:
    f.close()

# If the data file is not a .tsv file
if sys.argv[1][-4:] != '.tsv':
    print errorAlert, 'Make sure the data file you pass in is a .tsv file.'
    sys.exit()

knapsackSize = sys.argv[2]

try:
    knapsackSize = int(knapsackSize)
except ValueError:
    print errorAlert, 'The value passed in for the size of the knapsack was invalid. Please try again.'
    sys.exit()

if knapsackSize < 0:
    print errorAlert, 'The size of the knapsack cannot be negative. Please try again.'
    sys.exit()


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

    printMatrix(matrix, 'Creating the dynamic table...')

    # Trace back through the matrix to find which items were selected
    knapsack = []
    x = horizontal - 1
    y = vertical - 1
    totalWeight = 0

    while x > 0 and y > 0:
        if matrix[x][y] != matrix[x-1][y]:
            totalWeight += weightList[x]
            item = formatEntry(nameList[x], weightList[x], valueList[x])
            knapsack.insert(0, item)
            y = y - weightList[x]
        x = x - 1

    print "Items in final knapsack:"
    for item in knapsack:
        print item
    print ''
    print "Total weight of final knapsack: ", totalWeight
    print "Total value of final knapsack: ", matrix[horizontal-1][vertical-1]


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

        nameList.append(entry[0])

        try:
            weightList.append(int(entry[1]))
            valueList.append(int(entry[2]))
        except:
            print errorAlert, 'Your data file is formatted incorrectly. Check the test.tsv file for correct formatting.'
            sys.exit()

        print formatEntry(entry[0], entry[1], entry[2])
print ''
print "Max weight allowed in the knapsack: ", knapsackSize
print ''

solveKnapsack(nameList, weightList, valueList, knapsackSize)

print ''

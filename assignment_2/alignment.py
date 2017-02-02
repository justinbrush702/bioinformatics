import sys
import time

# Write out the results to a file
outputName = "output.txt"

# Read in the data from a file
dataFile = "data_files/transposons.dat"

# Constants
RIGHT_MATCH = 1
WRONG_MATCH = -1
GAP = -2

# Function to print the matrix with an optional statement
def printMatrix (gene, sequence, matrix, statement=''):
    print statement

    # print the gene across the top of the matrix
    print '\t', '\t',
    for char in gene:
        print char, '\t',
    print ''

    # print the matrix, including the sequence down the left side
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            # check to see if a character in the sequence should be printed
            if x == 0:
                if y > 0:
                    print sequence[y-1], '\t',
                else:
                    print '\t',
            if matrix[x][y] >= 0:
                print '',
            print matrix[x][y], '\t',
        print ''
    print ''

# Function to structure the time elapsed between events
def timeElapsed (elapsed):
    if elapsed < 60:
        timeString = str(elapsed) + ' seconds'
    else:
        minutes = int(elapsed / 60)
        seconds = elapsed % 60

        minuteString = 'minute'
        if minutes > 1:
            minuteString = minuteString + 's'

        timeString = str(minutes) + ' ' + minuteString + ', ' + str(seconds) + ' seconds'

    return timeString

# Function to find the value of the match
def matchValue (base1, base2):
    if base1 == base2:
        return RIGHT_MATCH
    return WRONG_MATCH

# Function to solve half semi-global seqence alignment
def solveAlignment (gene, sequence, outputFile):

    width = len(gene) + 1
    height = len(sequence) + 1

    matrix = [[0 for y in range(height)] for x in range(width)]

    # Initialize first row
    for x in range(1, width):
        matrix[x][0] = matrix[x-1][0] - 2

    # printMatrix(gene, sequence, matrix, "Initializing matrix...")

    for y in range(1, height):
        for x in range(1, width):

            match = matchValue(gene[x-1], sequence[y-1])

            # print 'x: ', str(x), 'y: ', str(y), 'gene: ', gene[x-1], 'sequence: ', sequence[y-1]
            matrix[x][y] = max(matrix[x-1][y-1] + match, matrix[x-1][y] + GAP, matrix[x][y-1] + GAP)

    # printMatrix(gene, sequence, matrix, 'Creating the dynamic table...')
    # Trace back through the matrix to find where the gene aligns best in the sequence...

    # Find the best value in the last column
    bestValue = matrix[width-1][0]
    endIndex = 0

    for i in range(height):
        if matrix[width-1][i] > bestValue:
            bestValue = matrix[width-1][i]
            endIndex = i

    # Find the best value in the first column; also, build the alignment strings
    x = width - 1
    y = endIndex
    sequence1 = ''
    sequence2 = ''

    while x > 0:
        if y > 0:
            match = matchValue(gene[x-1], sequence[y-1])

            # Taking the "low road"
            if matrix[x][y] == matrix[x-1][y] + GAP:
                sequence1 = gene[x-1] + sequence1
                sequence2 = '-' + sequence2
                x = x-1
            elif matrix[x][y] == matrix[x-1][y-1] + match:
                sequence1 = gene[x-1] + sequence1
                sequence2 = sequence[y-1] + sequence2
                x = x-1
                y = y-1
            elif matrix[x][y] == matrix[x][y-1] + GAP:
                sequence1 = '-' + sequence1
                sequence2 = sequence[y-1] + sequence2
                y = y-1
            else:
                print 'Error! This else block should be unreachable.'
                sys.exit()
        else:
            sequence1 = gene[x-1] + sequence1
            sequence2 = '-' + sequence2
            x = x-1

        startIndex = y+1

    bestAlignmentString = 'best alignment is from [1,' + str(startIndex) + '] to [' + str(len(gene)) + ',' + str(endIndex) + ']'
    scoreString = 'score is ' + str(bestValue)

    print bestAlignmentString
    print scoreString
    print sequence1
    print sequence2
    print ''

    outputFile.write('\n')
    outputFile.write(bestAlignmentString)
    outputFile.write('\n')
    outputFile.write(scoreString)
    outputFile.write('\n')
    outputFile.write(sequence1)
    outputFile.write('\n')
    outputFile.write(sequence2)
    outputFile.write('\n')


# Script starts here!

overallStart = time.time()

print 'Opening file to write to...', outputName
outputFile = open(outputName, "w")
print outputName, 'opened'

print 'Reading data from', dataFile
print ''
outputFile.write('Results from the data in ' + dataFile)
outputFile.write('\n')

with open(dataFile, "r") as f:
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in open(dataFile)]

    gene = lines[0]

    for i in range(1, len(lines)):
        start = time.time()
        solveAlignment(gene, lines[i], outputFile)
        end = time.time()

        timeString = timeElapsed(end-start)
        timeElapsedString = 'Calculation time: ' + timeString
        print timeElapsedString
        print ''
        outputFile.write(timeElapsedString)
        outputFile.write('\n')

overallEnd = time.time()

timeString = timeElapsed(overallEnd-overallStart)
timeElapsedString = 'OVERALL CALCULATION TIME: ' + timeString
print timeElapsedString
print ''
outputFile.write('\n')
outputFile.write(timeElapsedString)

print 'Closing output file...'
outputFile.close()
print 'Output file closed.'

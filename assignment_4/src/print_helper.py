import color_brush
import tree_helper

colorBrush = color_brush
treeHelper = tree_helper


# Sandwich a print function with a blank line before and after printing
def sandwichPrint(printFunction, printValues):
    print ''
    printFunction(printValues)
    print ''


# Print a line with a given message and color
def printWithColor (values):
    color = values[0] # color or effect
    message = values[1] # text
    newLine = values[2] # True / False value for if you want to make a new line
    colorBrush.setColor(color)
    if newLine:
        print message
    else:
        print message,
    colorBrush.resetColor()


# Error alert
errorAlert = '*****'

# Gives structure to an error message
def printError (message, showReminder=False):
    colorBrush.setColor('FAIL')
    print errorAlert, 'ERROR', errorAlert
    print ''
    print message
    print ''

    if showReminder:
        # Add a reminder for properly running the script with file inputs
        print errorAlert*4
        print ''
        printWithColor(['BOLD', 'Reminder:', True])
        colorBrush.setColor('FAIL')
        print 'To run the script, execute this command from the base of the Assignment 4 directory:'
        print ''
        print '\tpython src/main.py <path of sequences file> <path of structure file [optional]>'
        print ''
        print 'Or from the src folder, run:'
        print ''
        print '\tpyton main.py <path of sequences file> <path of structure file [optional]>'
        print ''
        print '(If you run the script from the src folder, be sure to back track when specifying the data files)'
        print '(E.g. ../data_files/sequences/file.dat)'

    colorBrush.resetColor()
    print ''


# Function to print results of small parsimony
def smallParsimonyResults (results):
    sequences = results.get('sequences')
    structure = results.get('structure')
    beforeP = results.get('beforeP')
    afterP = results.get('afterP')
    score = results.get('score')

    # All the sequences present in the list of example sequences
    sandwichPrint(printWithColor, ['INFO', 'Input sequences:', True])
    for seqIndex in range(len(sequences)):
        print sequences[seqIndex]
    print ''

    # Structure of the tree specified by the file (no sequence data)
    sandwichPrint(printWithColor, ['INFO', 'Input tree string structure:', True])
    print structure
    print ''

    # Structure of tree with leaf nodes in place
    sandwichPrint(printWithColor, ['INFO', 'Tree structure with leaf nodes in place:', True])
    treeHelper.printTree(beforeP)

    # Output final tree and score
    sandwichPrint(printWithColor, ['INFO', 'Final Tree:', True])
    treeHelper.printTree(afterP)
    print ''
    print 'Score: ' + str(score)
    print ''


# Helper to pull and align numbers to the right
def pullRight(number):
    # Arbitrary spacing value
    spacer = 15
    number = str(number)
    if len(number) < spacer:
        return ' '*(spacer - len(number)) + number


# Function to print results of large parsimony
def largeParsimonyResults (treeInfo):
    # Shows how many trees could have possibly been searched
    forest = len(treeInfo.get('sequences')) - 3
    possibilities = 1
    for i in range(forest + 1):
        possibilities *= (1 + (i + 1)*2)

    # Pull out the counts of the number of trees actually searched
    endCount = treeInfo.get('endCount')
    intermediateCount = treeInfo.get('intermediateCount')

    print 'Number of possible trees to search:\t' + pullRight(possibilities)
    print 'Number of intermediate trees searched:\t' + pullRight(intermediateCount)
    print 'Number of end trees searched:\t\t' + pullRight(endCount)
    print 'Number of trees searched in total:\t' + pullRight(endCount + intermediateCount)
    print ''

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
def printError (message):
    colorBrush.setColor('FAIL')
    print errorAlert, 'ERROR', errorAlert
    print ''
    print message
    print ''
    print errorAlert*4
    print ''

    # Add a reminder for properly running the script with file inputs
    printWithColor(['BOLD', 'Reminder:', True])
    colorBrush.setColor('FAIL')
    print 'To run the script, execute this command from the base of the Assignment 4 directory:'
    print ''
    print '\tpython main.py <name of data file [optional]>'
    print ''

    colorBrush.resetColor()
    print ''

# Function to print the results of small parsimony
def printResults (sequences, structure, beforeP, afterP):
    # All the sequences present in the list of example sequences
    sandwichPrint(printWithColor, ['INFO', 'Input sequences:', True])
    for seqIndex in range(len(sequences)):
        print sequences[seqIndex]
    print ''

    # R --> root
    # . --> internal node
    # [number] --> index at which the specified sequence is located in the sequence list
    sandwichPrint(printWithColor, ['INFO', 'Input tree string structure:', True])
    print structure
    print ''

    # Structure of tree with leaf nodes in place
    sandwichPrint(printWithColor, ['INFO', 'Tree structure with leaf nodes in place:', True])
    treeHelper.printTree(beforeP)

    # Output final tree and score
    sandwichPrint(printWithColor, ['INFO', 'Final Tree:', True])
    treeHelper.printTree(afterP.get('root'))
    print ''
    print 'Score: ' + str(afterP.get('score'))
    print ''

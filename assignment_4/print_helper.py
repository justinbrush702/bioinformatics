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
def printResults (sequences, structure, smallP):
    # All the sequences present in the list of example sequences
    print ''
    print 'Input sequence:'
    print ''
    print sequences
    print ''

    # For the example, we have A connected to C, and G connected to T, and their parents connected to each other
    # R --> root
    # . --> internal node
    # [number] --> the index at which the specified sequence is located in the sequence list
    print ''
    print 'Input tree string structure:'
    print ''
    print structure
    print ''

    # Output the final tree and score
    print ''
    print 'Final Tree:'
    print ''
    treeHelper.printTree(smallP.get('root'))
    print ''
    print 'Score: ' + str(smallP.get('score'))
    print ''

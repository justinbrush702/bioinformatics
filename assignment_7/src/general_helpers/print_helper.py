import color_brush

colorBrush = color_brush


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


# Function to print the matrix with an optional statement
def printMatrix (matrix, statement=''):
    print statement
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            print str(matrix[x][y]) + '\t\t',
        print ''
    print ''

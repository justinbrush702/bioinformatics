import color_brush

# Helper methods for printing useful and organized information

# Change color of text in the terminal with these
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
    print 'To run the script, execute this command from the base of the Assignment 3 directory:'
    print ''
    print '\tpython main.py <name of data file [optional]>'
    colorBrush.resetColor()
    print ''

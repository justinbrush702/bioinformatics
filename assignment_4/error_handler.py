import sys
import print_helper

printHelper = print_helper

# Handles errors the same way for each error

# Kills a running program and provides reason
def throwError (message):
    printHelper.printError(message)
    sys.exit()

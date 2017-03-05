import sys
import print_helper

printHelper = print_helper

# Handles errors in a similar fashion for each potential error

# Kills a running program; provides reason
def throwError (message, showReminder=False):
    printHelper.printError(message, showReminder)
    sys.exit()

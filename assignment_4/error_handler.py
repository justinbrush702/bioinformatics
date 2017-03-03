import sys
import os
import print_helper

printHelper = print_helper

# Handles errors in a similar fashion for each potential error

# Kills a running program, and provides reason
def throwError (message):
    printHelper.printError(message)
    os.system('rm *.pyc')
    sys.exit()

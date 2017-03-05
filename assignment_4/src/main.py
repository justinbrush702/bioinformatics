import sys
import file_helper
import print_helper
import tree_helper
import small_parsimony
import large_parsimony

fileHelper = file_helper
printHelper = print_helper
treeHelper = tree_helper
smallParsimony = small_parsimony.smallParsimony
largeParsimony = large_parsimony.largeParsimony


# Main script that runs parsimony, large and small!


# Function to run small parsimony
def runSmall (treeInfo):
    smallP = smallParsimony(treeInfo)
    printHelper.smallParsimonyResults(smallP)


# Function to run large parsimony
def runLarge (treeInfo):
    print ''
    print 'Searching for best tree structure...'
    largeP = largeParsimony(treeInfo)
    print 'Found it.'

    # Run small parsimony with the best tree structure to get more information about the best tree
    print ''
    print 'Result of the best tree:'
    runSmall(largeP)

    # Print results specific to running large parsimony
    printHelper.largeParsimonyResults(largeP)


# Print Assignment 4 header
printHelper.sandwichPrint(printHelper.printWithColor, ['HEADER', 'PARSIMONY OF TREES using SANKOFF\'S ALGORITHM', True])

# Organize tree info from input files
treeInfo = fileHelper.parseData(sys.argv)

# Depending on the input files, run smallP or largeP
if treeInfo.get('structure'):
    # If there are sequence and structure files, run small parsimony
    print 'Running small parsimony on sequences and structure.'
    runSmall(treeInfo)
else:
    # If there is only a sequence file, run large parsimony
    print 'Running large parsimony on sequences without a given structure.'
    runLarge(treeInfo)

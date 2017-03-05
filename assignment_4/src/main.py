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


# Print Assignment 4 header
printHelper.sandwichPrint(printHelper.printWithColor, ['HEADER', 'PARSIMONY OF TREES using SANKOFF\'S ALGORITHM', True])

# Organize tree info from input files
treeInfo = fileHelper.parseData(sys.argv)

# Depending on the input files, run smallP or largeP
if treeInfo.get('structure'):
    # If there are sequence and structure files, run small parsimony
    print 'Running small parsimony on specified sequences and structure...'
    smallP = smallParsimony(treeInfo)
    printHelper.smallParsimonyResults(smallP)
else:
    # If there is only a sequence file, run large parsimony
    print 'Running large parsimony on specified sequences without a given structure...'
    largeP = largeParsimony(treeInfo)
    printHelper.largeParsimonyResults(largeP)

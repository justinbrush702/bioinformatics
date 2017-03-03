import os
import file_helper
import print_helper
import tree_helper
import small_parsimony

fileHelper = file_helper
printHelper = print_helper
treeHelper = tree_helper
smallParsimony = small_parsimony.smallParsimony


# Print Assignment 4 header
printHelper.sandwichPrint(printHelper.printWithColor, ['HEADER', 'PARSIMONY OF TREES using SANKOFF\'S ALGORITHM', True])


# Function to run small parsimony on the data file
def runSmallP (data_file):
    # Read in sequence list and structure
    treeInfo = fileHelper.parseData(data_file)
    sequences = treeInfo.get('sequences')
    structure = treeInfo.get('structure')

    # Decode tree
    root = treeHelper.decode(structure, sequences)

    # Run Sankoff's algorithm on tree
    smallP = smallParsimony(root, len(sequences[0]))

    # Print results
    printHelper.printResults(sequences, structure, root, smallP)


# Call runSmallP on specified data file
# (Hardcoded example data file for testing)
runSmallP('data_files/seq_5_len_100.dat')


# Clear out the .pyc files that are created from compiling and importing python files into each other.
os.system('rm *.pyc')

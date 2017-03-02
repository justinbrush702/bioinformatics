import sys
import os
import file_helper
import print_helper
import base_penalties
import node
import tree_helper
import small_parsimony

fileHelper = file_helper
printHelper = print_helper
bases = base_penalties.bases
Node = node.Node
treeHelper = tree_helper
smallParsimony = small_parsimony.smallParsimony


# Print assignment header
printHelper.sandwichPrint(printHelper.printWithColor, ['HEADER', 'PARSIMONY OF TREES using SANKOFF\'S ALGORITHM', True])

# Read in example sequence list and structure
# Hardcoded for testing
exampleData = fileHelper.parseData('data_files/example.dat')
sequences = exampleData.get('sequences')
structure = str(exampleData.get('structure'))


# All the sequences present in the list of example sequences
# exampleSequences = ['A', 'C', 'T', 'G']

print ''
print 'Input sequence:'
print ''
print sequences
print ''

# For the example, we have A connected to C, and G connected to T, and their parents connected to each other
# R --> root
# . --> internal node
# [number] --> the index at which the specified sequence is located in the sequence list
# exampleTreeString = 'R\n .\n  0\n  1\n .\n  2\n  3'

print ''
print 'Input tree string structure:'
print ''
print structure
print ''


# Decode tree
root = treeHelper.decode(structure, sequences)

# Run Sankoff's algorithm on tree
smallP = smallParsimony(root)


# Output the final tree and score
print ''
print 'Final Tree:'
print ''
treeHelper.printTree(smallP.get('root'))
print ''
print 'Score: ' + str(smallP.get('score'))
print ''


# Clear out the .pyc files that are created from compiling and importing python files into each other.
os.system('rm *.pyc')

import sys
import copy
import tree_helper

treeHelper = tree_helper

# Script to calculate the parsimony of a list of sequences in a given tree structure
# Uses Sankoff's algorithm


# Function to calculate the table values of internal nodes
# Starts from the root; can't calculate tables until the children have calculated theirs.
# Shoot down tree and calculate tables on the way back up.
def calculateTables (node):
    # Only calculate children's tables if node has children
    if len(node.children) == 2:
        calculateTables(node.children[0])
        calculateTables(node.children[1])
        node.calculateTable()
    else:
        # This node is a leaf, so initialize its table
        node.initializeTable()


# Function to name the ancestors (top --> down)
def nameAncestors (node, name):
    node.name = name
    # Only go down a branch if there are children
    if len(node.children) == 2:
        nameAncestors(node.children[0], node.table[name].get('pathL'))
        nameAncestors(node.children[1], node.table[name].get('pathR'))


# Function to build tree of single bases
def buildSingleTrees (root, length):
    # Create a list of trees representing each base in the sequence
    treeList = []
    for index in range(length):
        # Create new tree with only single bases at the leaves
        singleRoot = copy.deepcopy(root)
        renameLeaves(singleRoot, index)
        treeList.append(singleRoot)
    return treeList


# Function to rename leaves based on index
def renameLeaves(node, index):
    if len(node.children) == 2:
        renameLeaves(node.children[0], index)
        renameLeaves(node.children[1], index)
    else:
        node.name = node.name[index]


# Function to calculate the small parsimony of a tree at a particular sequence index, starting at its root
def treeParsimony (root):
    # Calculate all of the tables (bottom --> up)
    calculateTables(root)

    # Rename the tree nodes to specify ancestors (top --> down)
    # In order to recurse down the tree, find the lowest value in the root's table
    lowestKeyRoot = ''
    lowestValueRoot = float('inf')
    for key in root.table:
        if root.table[key].get('value') < lowestValueRoot:
            lowestKeyRoot = key
            lowestValueRoot = root.table[key].get('value')
    # print 'lowest key in root: ' + lowestKeyRoot

    # Call the naming function
    nameAncestors(root, lowestKeyRoot)

    # Return an information object containing the root and score
    return {
        'root': root,
        'score': lowestValueRoot
    }


# Function that combines two trees back together
def combineTrees (mainNode, addNode):
    mainNode.name += addNode.name
    if len(mainNode.children) == 2:
        combineTrees(mainNode.children[0], addNode.children[0])
        combineTrees(mainNode.children[1], addNode.children[1])


# Function that initiates small parsimony on a tree
def smallParsimony (treeInfo):

    # Tree info object --> what shall we do with it???
    sequences = treeInfo.get('sequences')
    structure = treeInfo.get('structure')

    # Decode tree
    root = treeHelper.decode(sequences, structure)

    # Distill the length of the sequences in the tree
    length = len(sequences[0])

    # Break up the tree into individual trees based on the length of the sequences at the leaves
    treeList = buildSingleTrees(root, length)

    # Set up a list for the finished trees
    finishedTreeList = []

    # Run small parsimony at each index of the sequences in the leaves of the tree
    for index in range(len(treeList)):
        finishedTreeList.append(treeParsimony(treeList[index]))
    # print finishedTreeList

    # Set up final tree using first tree in finished tree list
    finalTree = finishedTreeList[0].get('root')
    finalScore = finishedTreeList[0].get('score')

    # Put trees back together
    for index in range(1, len(finishedTreeList)):
        combineTrees(finalTree, finishedTreeList[index].get('root'))
        finalScore += finishedTreeList[index].get('score')

    # Return an information dictionary containing info generated during small parsimony
    return {
        'sequences': sequences,
        'structure': structure,
        'beforeP': root,
        'afterP': finalTree,
        'score': finalScore
    }

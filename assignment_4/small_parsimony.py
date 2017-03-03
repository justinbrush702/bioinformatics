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


# Function to name the ancestors (top --> down)
def nameAncestors (node, name):
    node.name = name
    # Only go down a branch if there are children
    if len(node.children) == 2:
        nameAncestors(node.children[0], node.table[name].get('pathL'))
        nameAncestors(node.children[1], node.table[name].get('pathR'))


# Function that initiates small parsimony on a tree
def smallParsimony (root):
    # Calculate all of the tables (bottom --> up)
    calculateTables(root)

    # Rename the tree nodes to specify ancestors (top --> down)
    # In order to start recursion down the tree, find the lowest value in the root's table
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

import sys
import base_penalties
import node

Node = node.Node
bases = base_penalties.bases

# Script holds functions to encode and decode tree strings


# Recursive function to encode tree string
def buildTreeString (node, visited, depth):
    # Mark down current node as visited
    visited.append(node)

    # Keep track of the local tree string
    treeString = ''

    # Number of spaces to designate depth
    treeString += ' '*depth
    treeString += node.name + '/'

    # Add part of string regarding deeper trees
    for connectedNode in node.connections:
        if connectedNode not in visited:
            treeString += buildTreeString(connectedNode, visited, depth + 1)

    return treeString


# Function to encode tree string from tree structure
def encode (root):
    # Keep track of a list of nodes that have been visited when traversing the tree
    visited = []

    # Recursively build the tree string based on the root
    treeString = buildTreeString(root, visited, 0)

    # Splice off the trailing "/"
    treeString = treeString[:-1]

    return treeString


# Function to decode tree structure from tree string
def decode (sequences, structure):
    # Nodes in the tree
    nodes = structure.split('/')

    # Set up the root node
    root = Node(nodes[0], None, 0)

    # Attach the nodes to the root in the structure of the tree specified by the tree string
    current = root
    for index in range(1, len(nodes)):
        # Remove spaces from name
        name = nodes[index].strip()

        # Depth = number of spaces in the node's original name
        depth = len(nodes[index]) - len(name)

        # Backtrack up to the designated parent of this node
        while current != None:
            if current.depth == depth - 1:
                # If the name can be cast as an int (because it is an index), we have hit a leaf
                try:
                    name = int(name)
                    name = sequences[name]
                except:
                    pass

                newNode = Node(name, current, depth)
                current.children.append(newNode)

                # Set our new node as the potential parent of the next node
                current = newNode
                break
            else:
                current = current.parent

        # This should never happen; if this code gets hit, then there is an error in the code or tree structure
        if current == None:
            print 'ERROR! Current should never be None'
            sys.exit()

    # Returns the root of the tree
    return root


# Prints tree in a way to show its structure
# Takes in a tree in tree form, not string form
def printTree (node):
    # Helpful for spacing
    spacer = 4

    # Show the node's depth in tree
    depthString = ''
    for i in range(node.depth):
        depthString += '|' + ' '*spacer

    print depthString + node.name

    # If the node has children
    if len(node.children) == 2:
        # Highlight lineage in tree
        lineage = depthString + '|' + ' '*(spacer - 1) + '\\'
        print lineage

        # Recurse down through node's children
        printTree(node.children[0])
        printTree(node.children[1])

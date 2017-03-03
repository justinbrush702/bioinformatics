import sys
import base_penalties
import node

Node = node.Node
bases = base_penalties.bases

# Script holds functions to decode tree strings

# Function to decode tree structure from tree string
def decode (structure, sequences):
    # Nodes in the tree
    nodes = structure.split('\n')

    # Set up the root node
    root = Node(nodes[0], None, 0, False)

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
                isLeaf = False
                # If the name can be cast as an int (because it is an index), we have hit a leaf
                try:
                    name = int(name)
                    name = sequences[name]

                    # If the name is present in the list of bases, then this node is a leaf
                    # If the name is not present, then there is an error in the code or tree structure
                    if name in bases:
                        isLeaf = True
                except:
                    pass

                newNode = Node(name, current, depth, isLeaf)
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


# Prints the tree in a way to show its structure
# Takes in a tree in tree form, not string form
def printTree (node):
    print ' '*node.depth,
    print node.name
    # node.printTable()
    if len(node.children) == 2:
        printTree(node.children[0])
        printTree(node.children[1])
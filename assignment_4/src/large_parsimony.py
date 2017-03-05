import copy
import tree_helper
import small_parsimony

treeHelper = tree_helper
smallParsimony = small_parsimony.smallParsimony


# Script to calculate the parsimony of a list of sequences without a given tree structure
# Uses Branch and Bound

# Basic node
class BasicNode:

    def __init__ (self, name):
        self.name = name
        self.connections = []

    def __repr__ (self):
        return self.name + ' # connections: ' + str(len(self.connections))

    # Function to connect this node to another node
    def connect (self, node):
        self.connections.append(node)

    # Function to remove connection between this node the given node
    def remove (self, node):
        self.connections.remove(node)

# Recursive function to find the best tree
def findBestTree (sequences, connections, currentDepth, bestTree):
    # Go through each connection in the list of connections and insert a root for the tree consisting of the given nodes
    for connectionIndex in range(len(connections)):
        # Illustration of how deep large parsimony is currently searching
        print '.'*((currentDepth*3) + 3)

        # Count trees that are actually searched
        if currentDepth < len(sequences) - 3:
            bestTree['intermediateCount'] += 1
        else:
            bestTree['endCount'] += 1

        # Make a deep copy of the connection list
        rootedConnections = copy.deepcopy(connections)

        # Hang onto the connection specified by the connectionIndex
        connection = rootedConnections[connectionIndex]

        # Remove the connection from the list
        del rootedConnections[connectionIndex]

        # Create the root node; the root changes its position based on the tree at this iteration
        root = BasicNode('R')

        # Connect the root to the two nodes its inserting itself between
        root.connect(connection[0])
        root.connect(connection[1])

        # Remove the connections between the two nodes of the given connection
        connection[0].remove(connection[1])
        connection[1].remove(connection[0])

        # Connect those two nodes to the root
        connection[0].connect(root)
        connection[1].connect(root)

        # Add two more connections to the list of connections
        rootedConnections.append([root, connection[0]])
        rootedConnections.append([root, connection[1]])

        # Encode tree based on the root
        structure = treeHelper.encode(root)

        # Create a tree info dictionary to pass into small parsimony
        treeInfo = {
            'sequences': sequences,
            'structure': structure
        }

        # Get the small parsimony score of this tree
        score = smallParsimony(treeInfo).get('score')

        # If the small parsimony score is better than the best one so far
        if score < bestTree.get('score'):
            # If this tree includes all sequences / this is the furthest iteration of the tree
            if currentDepth == len(sequences) - 3:
                # We have a new king
                bestTree['structure'] = structure
                bestTree['score'] = score

            # Otherwise, keep iterating out on this specific tree
            else:
                # Rename the "root" to an inter-node, aka a ".n-number"
                root.name = '.n' + str(currentDepth + 1)

                # Create a new node based on the next sequence in the sequence data, as if to "replace" the root
                nextNode = BasicNode(str(currentDepth + 3))

                # Connect the nextNode and the old root / new inter-node to each other
                nextNode.connect(root)
                root.connect(nextNode)

                # Add this new connection to the connections list
                rootedConnections.append([nextNode, root])

                # Iterate based on new connections
                bestTree = findBestTree(sequences, rootedConnections, currentDepth + 1, bestTree)

    return bestTree


# Function that initiates large parsimony on a list of sequences
def largeParsimony (treeInfo):
    sequences = treeInfo.get('sequences')

    # Set up the inter-connecting node between the first 3 leaf nodes
    interNode = BasicNode('.n0')

    # Create the initial 3 leaf nodes and connect them to the inter-connecting node
    for index in range(3):
        # Create node
        initialNode = BasicNode(str(index))

        # Connect the initial node to the inter node
        initialNode.connect(interNode)

        # Vice versa
        interNode.connect(initialNode)

    # Set up an initial list of connections; this will be used to enumerate trees
    initialConnections = []

    # Only go through the interNode's connections; don't double count by going through the 3 initial nodes as well
    for node in interNode.connections:
        initialConnections.append([interNode, node])

    # Initialize the best tree with the worst tree possible
    worstTree = {
        'score': float('inf'),
        'intermediateCount': 0,
        'endCount': 0
    }

    # Find the best tree
    bestTree = findBestTree(sequences, initialConnections, 0, worstTree)

    # Tack on sequence to return object
    bestTree['sequences'] = sequences

    return bestTree

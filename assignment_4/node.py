import base_penalties

bases = base_penalties.bases
penalties = base_penalties.penalties
lookupPenalty = base_penalties.lookupPenalty


# Node class
class Node:

    def __init__(self, name, parent, depth, isLeaf):
        # Name is the base
        self.name = name

        # Parent to this node
        self.parent = parent

        # How far away this node is from the root
        self.depth = depth

        # The 0 or 2 children of this node
        self.children = []

        # This table will hold all of the data necessary to calculate ancestors
        self.table = {}

        # If this node is a leaf, initialize its table
        self.isLeaf = isLeaf
        if isLeaf:
            # Set up intial information for each base
            for base in bases:

                # At first, give all of the bases a value of infinity
                self.table[base] = {
                    'value': float('inf')
                }

                # Then, replace the base that represents this node with a value of 0
                self.table[self.name] = {
                    'value': 0
                }

    # Function to calculate the table of an ancestral node
    def calculateTable (self):
        # print 'Calculates node: ' + self.name
        if len(self.children) == 2:
            # print '\tLeft Child: ' + self.children[0].name
            # print '\tRight Child: ' + self.children[1].name

            # For each base in the highest level of the table --> The final A, C, G, T values
            for superBase in bases:
                bestRoutes = [] # The best values from the node's children

                # For each of the children nodes
                for child in self.children:
                    # Find the cheapest base this child can pass on
                    bestRoute = {
                        'value': float('inf'),
                        'base': None
                    }
                    # For each base in the child's table
                    for base in bases:
                        table = child.table
                        baseInfo = table.get(base)
                        value = baseInfo.get('value')
                        # print 'base: ' + base + ', value: ' + str(value)

                        if value != float('inf'):
                            value += lookupPenalty(superBase, base)
                        # print 'value after added penalty: ' + str(value)
                        if value < bestRoute.get('value'):
                            bestRoute['value'] = value
                            bestRoute['base'] = base

                    # print 'Best route: ' + str(bestRoute)
                    bestRoutes.append(bestRoute)

                # Add information about this base to the node's table
                self.table[superBase] = {
                    # Value to get to this base
                    'value': bestRoutes[0].get('value') + bestRoutes[1].get('value'),

                    # The base to get to the value (from the left child)
                    'pathL': bestRoutes[0].get('base'),

                    # The base to get to the value (from the right child)
                    'pathR': bestRoutes[1].get('base')
                }

    # Debugging function
    def printTable (self):
        print self.table

    def __repr__(self):
        return self.name + ', ' + 'parent: ' + str(self.parent) + ', depth: ' + str(self.depth)

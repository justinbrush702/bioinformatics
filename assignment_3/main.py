import sys
import os
import print_helper
import cluster

# Helpful print enhancers
printHelper = print_helper

# Class that will hold cluster information
Cluster = cluster.Cluster

# Kills a running program and provides reason
def throwError (message):
    printHelper.printError(message)
    sys.exit()

# Debugging purposes
def printMatrix(clusters, distances, message=''):
    if message:
        printHelper.printWithColor(['UNDERLINE', '_' + message + '__', True])
        print ''

    for cluster in clusters:
        print cluster.clusterName, '\t'*2,
    print ''

    for i in range(len(distances)):
        for j in range(len(distances[i])):
            print '%.2f' % distances[i][j], '\t'*2,
        print ''
    print ''

# Calculate biased distance
def biasedDistance (original, u1, u2):
    return original - u1 - u2

# Calculate distance to parent
def distToParent (original, u1, u2):
    return (float)(original + u1 - u2)/2

# Find the max coord then min coord in the matrix
# This function is needed because we only fill in half of the matrix
def findCoords (a, b):
    small = min(a, b)
    large = max(a, b)
    return [large, small]

# Calculate single u value
def uValues (distances):
    uList = []
    for base in range(len(distances)):
        value = 0
        for variant in range(len(distances)):
            coords = findCoords(base, variant)
            value += distances[coords[0]][coords[1]]
        value /= (float)(len(distances) - 2)
        uList.append(value)
    return uList


# Print assignment header
printHelper.sandwichPrint(printHelper.printWithColor, ['HEADER', 'CONSTRUCTING PHYLOGENETIC TREES via NEIGHBOR JOINING', True])

# Takes in one input, the name of a data file
if len(sys.argv) > 1:
    printHelper.printWithColor(['INFO', 'File specified.', True])
    data_file = sys.argv[1]
    print 'Reading file: ' + data_file
else:
    # Default to the original westnile data file
    data_file = 'data_files/westnile.dat'
    printHelper.printWithColor(['WARNING', 'No file specified.', True])
    print 'Reading from default file: ' + data_file

print ''

# If the data file is not a .dat file
if data_file[-4:] != '.dat':
    throwError('Make sure the data file is a .dat file.')

print 'Verifying location of data file...',
# Check to see if the file can be located
try:
    f = open(data_file)
except IOError as e:
    printHelper.printWithColor(['FAIL', 'FAILED', True])
    print ''
    # print errorAlert, 'Here was the error given by the system:'
    # print "\tI/O error({0}): {1}".format(e.errno, e.strerror)
    throwError('File was not found. Make sure to properly input the file path.')
else:
    f.close()
    printHelper.printWithColor(['SUCCESS', 'SUCCESS!', True])
    print ''


# Ascii value to start naming nodes
nodeNumber = 65
# List of the original clusters
totalClusters = []
# Distance matrix
distances = []

# Read in the data file.
with open(data_file, "r") as f:
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in open(data_file)]

    # First line gives us the names of the taxa
    taxa = lines[0].split('\t')
    for taxon in taxa:
        # Create a cluster for each of these taxa, set priority value (first come, first serve)
        totalClusters.append(Cluster(chr(nodeNumber), taxon))
        totalClusters[len(totalClusters) - 1].index = nodeNumber - 65
        nodeNumber += 1
        distances.append([])

    # The cluster-naming logic currently only works for the length of the uppercase alphabet
    # So, the input file can currently only contain a maximum of 26 taxa
    if len(taxa) > 26:
        throwError('TOO MUCH DATA: program can only handle a maximum of 26 taxa due to its current cluster-naming method.')

    # Get rid of the first line (no longer need it)
    del lines[0]

    # Verify the number of taxa equals the number of lines in the distance matrix
    if len(totalClusters) != len(lines):
        throwError('Data file is improperly formatted. The numbers of taxa and lines in the distance matrix should match.')

    # Take in the original distances of each taxa
    for taxonIndex in range(len(lines)):
        line = lines[taxonIndex].split('\t')
        for distance in line:
            # Make sure data is formatted properly --> check to see if data are ints
            try:
                distVal = int(distance)
            except:
                throwError('Distances are not tab separated values. Check example.dat for correct formatting.')

            distances[taxonIndex].append(distVal)

        # Check the distance matrix has the right amount of data on each line
        if len(distances[taxonIndex]) != taxonIndex + 1:
            throwError('The matrix is not structured properly. Check example.dat for correct matrix distance arrangement.')

# printMatrix(totalClusters, distances, 'Distances of Starting Nodes')

# Keep a reference to the designated outgroup
outgroup = totalClusters[len(totalClusters) - 1]

# Copy the list of clusters; we'll need to see a list of all the clusters and a list of clusters to be calculated
remainingClusters = totalClusters[:]

# While there are at least 2 remaining clusters
while len(remainingClusters) > 2:

    # printMatrix(remainingClusters, distances, 'Distances at top of iteration')

    # Keep track of a list of uValues that correspond to the list of remainingClusters
    uList = uValues(distances)
    # print 'uList: ' + str(uList)

    # Make a biased distance matrix (same structure as the regular distance matrix)
    biasedDistances = []
    for index in range(len(distances)):
        biasedDistances.append([])

    # Create the biased distance matrix while finding the smallest value
    smallestDist = 0
    for i in range(len(biasedDistances)):
        for j in range(i + 1):
            if i != j:
                biasDist = biasedDistance(distances[i][j], uList[i], uList[j])
            else:
                biasDist = 0
            biasedDistances[i].append(biasDist)
            if biasDist < smallestDist:
                smallestDist = biasDist
    # print 'biasedDistances: ' + str(biasedDistances)
    # printMatrix(remainingClusters, biasedDistances, 'Biased Distances')
    # print 'smallest distance: %.2f' % smallestDist

    # Put the cluster groups with the smallest distance to each other into a list.
    smallestDistances = []
    for i in range(len(biasedDistances)):
        for j in range(i + 1):
            if biasedDistances[i][j] == smallestDist:
                # Flip the clusters around when combining them together
                smallestDistances.append([remainingClusters[j], remainingClusters[i]])
    # printHelper.printWithColor(['INFO', 'Cluster Groups with smallest distances', True])
    # for clusterGroup in smallestDistances:
    #     print '\t' + clusterGroup[0].clusterName + ', ' + clusterGroup[1].clusterName
    # print ''


    # # ALTERNATE WAY TO BREAK TIES FOR SMALLEST DISTANCE --> PRIORITY TO CLUSTERS WITH FEWER COMBINATIONS
    # # So, we have a list of cluster groups that tied for smallest distance. How do we break the tie?
    # # Filter the cluster groups in smallestDistances by the length of what could be their new clusterName
    # # This will give priority to those potential new clusters that haven't been combined as many times yet
    # smallestNameLen = len(smallestDistances[0][0].clusterName + smallestDistances[0][1].clusterName)
    # for clusterGroup in smallestDistances:
    #     nameLen = len(clusterGroup[0].clusterName + clusterGroup[1].clusterName)
    #     if nameLen < smallestNameLen:
    #         smallestNameLen = nameLen
    # print 'smallestNameLen: ' + str(smallestNameLen)
    #
    # smallestNames = []
    # for clusterGroup in smallestDistances:
    #     nameLen = len(clusterGroup[0].clusterName + clusterGroup[1].clusterName)
    #     if nameLen == smallestNameLen:
    #         smallestNames.append(clusterGroup)
    # printHelper.printWithColor(['INFO', 'Cluster groups with smallest names', True])
    # for clusterGroup in smallestNames:
    #     print '\t' + clusterGroup[0].clusterName + ', ' + clusterGroup[1].clusterName
    # print ''


    # Pick the two joint clusters from the smallestDistances list to merge based on lowest ranking
    # The first cluster of the two will always be ranked lower
    selectedGroup = smallestDistances[0]

    for clusterGroup in smallestDistances:
        if clusterGroup[0].ranking < selectedGroup[0].ranking:
            selectedGroup = clusterGroup
    # print 'Group selected: ' + str(selectedGroup)

    # I now have the unique group of two clusters to use in the creation of a new cluster

    # Now is the time to create the new cluster
    newClusterName = selectedGroup[0].clusterName + selectedGroup[1].clusterName
    newCluster = Cluster(newClusterName, '')

    # Connect new cluster to its related clusters and vice versa
    # Needs this two-way binding because we don't know how the tree is going to hang yet
    distanceCoords = findCoords(selectedGroup[0].index, selectedGroup[1].index)
    originalDistance = distances[distanceCoords[0]][distanceCoords[1]]
    u0 = uList[selectedGroup[0].index]
    u1 = uList[selectedGroup[1].index]

    # Parent-child 1 and 2
    parChi0 = distToParent(originalDistance, u0, u1)
    parChi1 = distToParent(originalDistance, u1, u0)

    newCluster.connect(selectedGroup[0], parChi0)
    newCluster.connect(selectedGroup[1], parChi1)

    selectedGroup[0].connect(newCluster, parChi0)
    selectedGroup[1].connect(newCluster, parChi1)

    # Add new cluster to the (currently unrooted and unorganized) tree-to-be
    totalClusters.append(newCluster)

    # Update the remaining clusters list
    remainingClusters.remove(selectedGroup[0])
    remainingClusters.remove(selectedGroup[1])

    # Check selected groups distances to the new cluster
    # connectionDistance = selectedGroup[0].connections[0][1]
    # print 'selectedGroup[0]: ' + selectedGroup[0].clusterName + ', distance to new cluster: ' + str(connectionDistance)
    # connectionDistance = selectedGroup[1].connections[0][1]
    # print 'selectedGroup[1]: ' + selectedGroup[1].clusterName + ', distance to new cluster: ' + str(connectionDistance)

    # Build a distance list from the new cluster to the remaining clusters
    clusterDistances = []
    for cluster in remainingClusters:
        # Coordinates of the current cluster vs. the original selected groups
        coords = findCoords(cluster.index, selectedGroup[0].index)
        distanceiz = distances[coords[0]][coords[1]]

        coords = findCoords(cluster.index, selectedGroup[1].index)
        distancejz = distances[coords[0]][coords[1]]

        distancetoi = selectedGroup[0].connections[len(selectedGroup[0].connections) - 1][1]
        distancetoj = selectedGroup[1].connections[len(selectedGroup[1].connections) - 1][1]
        distanceij = distancetoi + distancetoj

        # Rearrangement of the formula used to find distances between clusters
        finalDistance = (float)(distanceiz + distancejz - distanceij) / 2
        clusterDistances.append(finalDistance)

    # Tack on a 0 (to match the distance matrix precedent)
    clusterDistances.append(0)

    # Add the new cluster to the list of remaining clusters to compute
    remainingClusters.append(newCluster)

    # Update the indices of the remainingClusters
    for index in range(len(remainingClusters)):
        remainingClusters[index].index = index

    # Delete the old clusters out of the distance matrix
    # Use findCoords to get high and low rows of distance matrix to delete
    coords = findCoords(selectedGroup[0].index, selectedGroup[1].index)
    del distances[coords[0]]
    del distances[coords[1]]

    # 2nd set of deleting is the deletion of the columns of the selected clusters
    for i in range(len(distances)):
        for j in range(len(distances[i])):
            if j == coords[0]:
                # distances[i][j] = 'x'
                del distances[i][j]
        for j in range(len(distances[i])):
            if j == coords[1]:
                # distances[i][j] = 'x'
                del distances[i][j]

    # Now that the distance matrix has eliminated the selected clusters, add the new cluster's distances
    distances.append(clusterDistances)

# print distances
# printMatrix(remainingClusters, distances, 'Last Distances')

# Distance between the last two clusters
lastDistance = distances[1][0]

# Connect the last two clusters together
remainingClusters[0].connect(remainingClusters[1], lastDistance)
remainingClusters[1].connect(remainingClusters[0], lastDistance)


# Attach a root for the tree to the outgroup and its one connection
root = Cluster('Root', '')
outgroupDist = outgroup.connections[0][1] / 2
root.connect(outgroup, outgroupDist)
root.connect(outgroup.connections[0][0], outgroupDist)

# Function to remove one of the two-way bindings between parent and child clusters
# main cluster is the cluster with connections to other cluster
# connected cluster is the cluster which we are looking for in the main cluster's connections list
def removeConnectedCluster (main, connected):
    for clusterIndex in range(len(main.connections)):
        if main.connections[clusterIndex][0] == connected:
            del main.connections[clusterIndex]
            return True
    throwError('Tried to remove a cluster to which the main cluster was not connected.')


# Connect the outgroup's parent to the root instead of the outgroup
root.connections[1][0].connect(root, outgroupDist)
removeConnectedCluster(root.connections[1][0], outgroup)

# Do the same for the outgroup
outgroup.connections = []
outgroup.connect(root, outgroupDist)

# Add the root to the list of total clusters
totalClusters.append(root)


# Function to recursively print the tree, starting at the root node
# Prints information about each cluster while building the structure of the tree (shows connections)
def printTree (cluster, parent, depth):
    # 'tree' is visual tree structure
    tree = '\n'
    tree += str(' '*depth*2)
    tree += cluster.clusterName

    # Remove the parent of this cluster, so the tree doesn't get stuck in a cycle
    if parent:
        removeConnectedCluster(cluster, parent)

    message = 'Node ' + cluster.clusterName + '\t'

    # Lines up output nicely
    if len(message) < 9:
        message += '\t'

    if cluster.taxonName:
        message += '(' + cluster.taxonName + ')'
    else:
        message += 'connected to '
        for connectedIndex in range(len(cluster.connections)):
            message += cluster.connections[connectedIndex][0].clusterName + ' '
            message += '%.2f' % (cluster.connections[connectedIndex][1]) + ', '
        message = message[:-2]

    print message

    # Recurse down each of this cluster's connections
    # If this clsuter is a leaf, it will not enter this loop
    for connectedIndex in range(len(cluster.connections)):
        tree += str(printTree(cluster.connections[connectedIndex][0], cluster, depth + 1))
    return tree


# Print the tree's information and structure
tree = printTree(root, None, 0)
print ''
printHelper.printWithColor(['INFO', 'Tree Structure', False])
printHelper.printWithColor(['WARNING', '(not to scale)', True])
print tree


# Clear out the .pyc files that are created from compiling and importing python files into each other.
os.system('rm *.pyc')

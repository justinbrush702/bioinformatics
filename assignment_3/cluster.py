# Cluster class
class Cluster:

    def __init__(self, clusterName, taxonName):
        # Name of cluster (concatenated node names)
        self.clusterName = clusterName

        # Name of the taxon (if this cluster is a leaf)
        self.taxonName = taxonName

        # Lowest original node contained in this cluster
        self.lowNode = clusterName[0]
        self.lowValue = ord(self.lowNode)

        # "Ranking" of the cluster based on its lowest node value and number of nodes associated with cluster
        self.ranking = (self.lowValue - 65) + ((len(self.clusterName) - 1)*26)
        # This ranking system should always give each cluster a unique value
        # Subtract 65 because that is where 'A' starts in ASCII
        # This ranking system assumes we will always have less than 26 taxa

        # List of clusters this cluster is connected to (with their distances)
        self.connections = []

        # This value will change based on this cluster's position in the distance matrix
        self.index = -1

    # Use this function to connect this cluster to its element clusters as well as its higher cluster
    def connect(self, cluster, distance):
        self.connections.append([cluster, distance])

    def repConnections(self):
        return self.connections

    def __repr__(self):
        rep = '\n'
        rep += 'clusterName: ' + self.clusterName + '\n'
        rep += 'taxonName: ' + self.taxonName + '\n'
        rep += 'isLeaf? ' + str(self.isLeaf) + '\n'
        rep += 'lowNode: ' + self.lowNode + '\n'
        rep += 'lowValue: ' + str(self.lowValue) + '\n'
        rep += 'ranking: ' + str(self.ranking) + '\n'
        rep += 'number of connections: ' + str(len(self.connections)) + '\n'
        if self.index > -1:
            rep += 'index: ' + str(self.index) + '\n'
        return rep

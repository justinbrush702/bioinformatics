bases = ['A', 'C', 'G', 'T']
matrixLookup = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

# Hardcoded penalties
# A   C   G   T
# 0
# 9   0
# 4   4   0
# 3   4   2   0
penalties = [[0], [9, 0], [4, 4, 0], [3, 4, 2, 0]]

# Function to look up the penalty of changing from one base to another
def lookupPenalty (base1, base2):
    index1 = bases.index(base1)
    index2 = bases.index(base2)
    minBase = min(index1, index2)
    maxBase = max(index1, index2)
    return penalties[maxBase][minBase]

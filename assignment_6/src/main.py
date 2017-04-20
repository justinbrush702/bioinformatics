from general_helpers import file_helper
from general_helpers import print_helper
import markov_model


# Hardcoded data files (no command line input for this assignment)
commonPath = 'data_files/' # common path for data files
commonFile = '.dat' # common file extension for data files

# Function to build data file paths
def buildDataPath (fileName):
    return commonPath + fileName + commonFile

rollsPath = buildDataPath('rolls')
viterbiPath = buildDataPath('viterbi')
diePath = buildDataPath('die')

viterbiData = {}

viterbiData['rolls'] = file_helper.parseData(rollsPath)
viterbiData['die'] = file_helper.parseData(diePath)
viterbiData['viterbi'] = file_helper.parseData(viterbiPath)
# print viterbiData

# Function to standardize data objects placed in the matrix
def formatEntry (value, die, pointer):
    # Set up dictionary
    data = {}
    # Value of the most likely path to this entry
    data['value'] = value
    # Fair or Loaded die
    data['die'] = die
    # Pointer to entry in previous row in which this value was derived
    data['pointer'] = pointer
    return data

# Set up dynamic programming matrix
matrix = [[{} for y in range(len(viterbiData['rolls']) + 1)] for x in range(len(markov_model.states))]

# Initialize first row
matrix[0][0] = formatEntry(markov_model.start_probability['Fair'], None, None)
matrix[1][0] = formatEntry(markov_model.start_probability['Loaded'], None, None)
# print_helper.printMatrix(matrix, 'Matrix, initialized:')

# Loop through matrix, fill in entries
for y in range(1, len(matrix[0])):
    for x in range(len(matrix)):
        # Find the roll at y
        currentRoll = viterbiData['rolls'][y-1]

        # 3 values get multiplied together to determine this entry's value
        # The prev value
        # The probability of transition
        # The probability of emission

        # Calculate value for pointing to the previous fair entry
        fairPrev = matrix[0][y-1]['value']
        # print 'prev fair: ', fairPrev

        if x == 0:
            fairPrev *= markov_model.transition_probability['Fair']['Fair']
        else:
            fairPrev *= markov_model.transition_probability['Fair']['Loaded']
        # print 'prev fair with transition_probability: ', fairPrev

        fairPrev *= markov_model.emission_probability['Fair'][currentRoll]
        # print 'emission_probability: ', markov_model.emission_probability['Fair'][currentRoll]
        # print 'prev fair with emission_probability: ', fairPrev

        # Calculate value for pointing to the previous loaded entry
        loadedPrev = matrix[1][y-1]['value']
        # print 'prev loaded: ', loadedPrev

        if x == 0:
            loadedPrev *= markov_model.transition_probability['Loaded']['Fair']
        else:
            loadedPrev *= markov_model.transition_probability['Loaded']['Loaded']
        # print 'prev loaded with transition_probability: ', loadedPrev

        loadedPrev *= markov_model.emission_probability['Loaded'][currentRoll]
        # print 'prev loaded with emission_probability: ', loadedPrev
        # print 'prev loaded with emission_probability: ', loadedPrev

        currentEntryValue = max(fairPrev, loadedPrev)

        if (fairPrev > loadedPrev):
            matrix[x][y] = formatEntry(currentEntryValue, 'F', matrix[0][y-1])
        else:
            matrix[x][y] = formatEntry(currentEntryValue, 'L', matrix[1][y-1])
# print_helper.printMatrix(matrix, 'Final matrix:')

# Compare the two entries in the bottom row
if (matrix[0][len(matrix[0]) - 1]['value'] > matrix[1][len(matrix[0]) - 1]['value']):
    bestPath = matrix[0][len(matrix[0]) - 1]
else:
    bestPath = matrix[1][len(matrix[0]) - 1]

# Build string of die states used based on the pointers of the best path
mostLikelyDice = ''
while bestPath['pointer'] != None:
    mostLikelyDice = bestPath['die'] + mostLikelyDice
    bestPath = bestPath['pointer']


print 'Rolls observed:'
print viterbiData['rolls']
print ''

print 'Actual die states when rolls occurred:'
print viterbiData['die']
print ''

print 'Die states prediction from the viterbi casino example:'
print viterbiData['viterbi']
print ''

print 'Die states prediction from my algorithm:'
print mostLikelyDice
print ''

print 'Are my predicted die states equal to the viterbi casino example?'
print mostLikelyDice == viterbiData['viterbi']
print ''

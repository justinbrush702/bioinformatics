from general_helpers import file_helper
from general_helpers import print_helper
from general_helpers import error_handler
import markov_model

# Read in 300 die rolls
rolls = file_helper.parseData('data_files/rolls.dat')
# print rolls

# Function to convert die rolls from string to int (currently not used)
def intRoll(roll):
    try:
        roll = int(roll)
        if (roll < 1 or roll > 6):
            error_handler.throwError('Die roll from data file did not come from a 6-sided die.')
        return roll
    except ValueError:
        error_handler.throwError('Die roll from data file is not an int.')

# Initialize matrix
matrix = []
matrix.append([markov_model.start_probability['Fair'], markov_model.start_probability['Loaded']])

# Find all probabilities
for i in range(len(rolls)):
    roll = rolls[i]

    # Find the probability of this roll if coming from both fair and loaded dice
    fair = ((matrix[i - 1][0] * markov_model.transition_probability['Fair']['Fair']) + (matrix[i - 1][1] * markov_model.transition_probability['Loaded']['Fair'])) * markov_model.emission_probability['Fair'][roll]
    loaded = ((matrix[i - 1][0] * markov_model.transition_probability['Fair']['Loaded']) + (matrix[i - 1][1] * markov_model.transition_probability['Loaded']['Loaded'])) * markov_model.emission_probability['Loaded'][roll]

    row =  [fair, loaded]
    matrix.append(row)


print 'Final probabilities in the matrix:'
for i in range(len(matrix)):
    print matrix[i]

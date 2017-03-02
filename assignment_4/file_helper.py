import sys
import error_handler
import print_helper

throwError = error_handler.throwError
printHelper = print_helper

# Script to read in data files


# Function to parse the data out of a single file
def parseData (data_file):

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


    # Read in the data file.
    with open(data_file, "r") as f:
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in open(data_file)]

        # First line gives us the structure of the tree
        # Maybe put a check here to see if the first char is an R
        # That would signal if the problem is small parsimony or large parsimony
        structure = lines[0].replace('/', '\n')

        # Get rid of the first line (no longer need it)
        del lines[0]

        # Build the list of sequences in tree
        sequences = []
        for line in lines:
            sequences.append(line)

    return {
        'structure': structure,
        'sequences': sequences
    }

# Function that takes in one or more files specified
# def readFiles (sysArgs):
#     # Takes in one input, the name of a data file
#     if len(sys.argv) > 1:
#         printHelper.printWithColor(['INFO', 'File specified.', True])
#         data_file = sys.argv[1]
#         print 'Reading file: ' + data_file
#     else:
#         # Default to the original westnile data file
#         data_file = 'data_files/westnile.dat'
#         printHelper.printWithColor(['WARNING', 'No file specified.', True])
#         print 'Reading from default file: ' + data_file
#
#     print ''

import error_handler
import print_helper

throwError = error_handler.throwError
printHelper = print_helper

# Script to read in data files

# Function to read in file; returns the lines in the data file
def verifyFile (data_file):
    printHelper.printWithColor(['INFO', 'Verify data file: ' + data_file, True])
    print ''

    # If the data file is not a .dat file
    if data_file[-4:] != '.dat':
        throwError('Make sure the data file is a .dat file.', True)

    print 'Verifying location of data file...',
    # Check to see if the file can be located
    try:
        f = open(data_file)
    except IOError as e:
        printHelper.printWithColor(['FAIL', 'FAILED', True])
        print ''
        # print errorAlert, 'Here was the error given by the system:'
        # print "\tI/O error({0}): {1}".format(e.errno, e.strerror)
        throwError('File was not found. Make sure to properly input the file path.', True)
    else:
        f.close()
        printHelper.printWithColor(['SUCCESS', 'SUCCESS!', True])
        print ''

    # Read in the data file.
    with open(data_file, "r") as f:
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in open(data_file)]

        return lines


# Function to parse the data from input files
def parseData (sysArgs):

    # Verify there is at least one argument (there can be one or two)
    if len(sysArgs) < 2:
        throwError('No data files specified! Specify a sequences data file along with an optional structure data file.', True)

    # Set up tree info dictionary
    treeInfo = {}

    # Distill the sequences from the sequence file
    sequenceFile = verifyFile(sysArgs[1])

    # Simple check to determine the sequenceFile is filled with sequences, not the structure
    if sequenceFile[0][0] == 'R':
        # If the first character is an 'R', that means this file specifies structure (starting at the root, 'R')
        throwError('The first file passed in appears to contain the structure. The first file must hold the sequences.', True)

    # Build the list of sequences in tree
    sequences = []
    for line in sequenceFile:
        sequences.append(line)

    # Tack the sequences onto the tree info dictionary
    treeInfo['sequences'] = sequences


    # If there is a tree structure file...
    if len(sysArgs) > 2:
        structureFile = verifyFile(sysArgs[2])

        # Simple check to determine the structureFile contains the structure, not the sequences
        if structureFile[0][0] != 'R':
            throwError('The second file passed in appears to contain sequences. The second file must be the structure file.', True)

        # A structure can be ran against a sequenceFile if the structure contains less sequences than the sequenceFile
        # If a structure has more sequences, the program will break
        # If a structure has less, then the sequences not specified in the tree simply don't get included
        # E.g. a sequenceFile with 5 sequences can run small parsimony against a structure with 4 sequences, but not 6
        if str(len(sequences)) in structureFile[0]:
            throwError('There are not enough sequences in the sequence file for the structure in the structure file.')

        # There is only one line in this file
        # R --> root
        # . --> internal node
        # [number] --> index at which the specified sequence is located in the sequence list
        structure = structureFile[0].replace('/', '\n')

        # Tack the structure onto the tree info dictionary
        treeInfo['structure'] = structure


    # Return the treeInfo dictionary
    return treeInfo

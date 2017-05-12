import error_handler
import print_helper

throwError = error_handler.throwError
printHelper = print_helper

# Script to read in data files


# Function to read in file; returns the lines in the data file
def verifyFile (data_file):
    printHelper.printWithColor(['INFO', 'Verify data file: ' + data_file, True])

    # If the data file is not a .dat file
    if data_file[-4:] != '.dat':
        throwError('Make sure the data file is a .dat file.', True)

    print 'Verifying location of data file... ',
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
def parseData (data_file):
    dataLines = verifyFile(data_file)

    # Ensure there is data present in data files
    if (len(dataLines) < 1):
        throwError('No data found in this file!')

    # There's only one line of data in each of these files. That's all we need to return (instead of the array data structure)
    return dataLines[0]

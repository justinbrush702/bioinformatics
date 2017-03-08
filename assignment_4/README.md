This assignment requires me to run both small or large parsimony on sequences and tree structures. The script takes one or two arguments:
  A sequences file,
  A structure file (this file is optional).

If both sequence and structure files are specified, the script runs small parsimony on the data. If only a sequence file is specified, then large parsimony is ran on the data. The small parsimony solution uses Sankoff's algorithm; the large parsimony solution uses Branch and Bound.

Look at the given sequences and structures for data formatting and naming convention.

To run the script from the base of the assignment 4 directory, run:

python src/main.py [path to sequences file] [path to structure file (optional)]

To run the script from the src folder, run:

python main.py [path to sequences file] [path to structure file (optional)]

If you run the script this way, be sure to back track when specifying the paths to the data files. E.g. ../data_files/sequences/file.dat

This assignment is only designed to work with with DNA bases and sequences (so, no amino acid sequences). The penalties for switching from one base to another are hardcoded and are located in base_penalties.py.

All errors are trapped except for improperly formatted data files. I am assuming the data files are formatted correctly.

TODO:

Remove the dot progress print statements.
Replace with a progress update every x amount of minutes, say every 15 or 30 minutes.

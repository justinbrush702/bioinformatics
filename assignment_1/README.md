Assignment 1 is to implement the knapsack problem using dynamic programming. My python script can solve the knapsack problem by reading in a file with data structured as such...

name1 weight1 value1<br/>
name2 weight2 value2<br/>
name3 weight3 value3<br/>

The space between the names, weights, and values are tabs. Each entry has its own line.

In order to run the program, pass in the name of the file along with the size of the knapsack. The program runs from the command line. For example...

python knapsack.py [filename] [knapsack_size]<br/>
python knapsack.py data_files/file.txt 8

The script prints out the initial list of items from which to select, the matrix, and the list of items selected for the knapsack.

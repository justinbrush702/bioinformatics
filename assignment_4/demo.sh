demo-script-prep () {
  echo "(Script will run in 5 seconds)"
  sleep 2
  echo "3..."
  sleep 1
  echo "2..."
  sleep 1
  echo "1..."
  sleep 1
  echo $1
  sleep 1
}

echo
echo "Hello, welcome to the bioinformatics phylogenetic tree reconstruction demo!"
sleep 4
echo
echo "In this demo, I will run python scripts against some collections of DNA sequences and potential structures of their phylogenetic trees."
sleep 8
echo
echo "Here is some context for the assignment I was given in my bioinformatics independent study..."
sleep 4
echo
echo "Sequences of DNA represent organisms have an evolutionary ancestry. Using Sankoff's algorithm, I can score an evolutionary structure from whence the DNA sequences originated. The more accurate the tree, the lower the score."
echo "DNA bases are penalized for mutations, but not every mutation is penalized the same (The penalties are hardcoded into the base_penalties.py file in this assignment's src directory.)."
echo "For example, if I have 5 DNA sequences consisting of 100 bases each, and I have an arbitary tree structure that positions the sequences as leaves, I can score the structure of that tree."
sleep 20
echo

demo-script-prep "Running 'python src/main.py data_files/sequences/5_100.dat data_files/structure/5a.dat'"
python src/main.py data_files/sequences/5_100.dat data_files/structure/5a.dat

sleep 10
echo
echo
echo "As you can see, the structure of the input tree was given a score of 650. This doesn't give us much information, unless we compare this tree structure to others."
sleep 8
echo
echo "Of course, we can run this sequence against every possible tree configuration that exists. However, as the number of sequences increases, the number of tree structures experiences factorial growth."
sleep 10
echo
echo "There is a way to potentially cut down the number of trees required to evaluate. This technique is called 'Branch and Bound'."
sleep 6
echo
echo "The algorithm keeps track of the best scored tree (both structure and score). The algorithm will search other configurations of trees, but trees are looked at via depth first search (DFS), and each tree is scored each time a node is added. That might not make too much sense at face value - and understanding this algorithm might take further research - but when the algorithm finds a poor-performing tree, it can jump ahead to later structures while cutting out huge swaths of trees further down the search of one particular structure."
sleep 20
echo
echo "Here, I will pass in the same 5 sequences, but this time I will not pass in a given tree structure. This signals to the program that it will check for the BEST tree structure and return it."
sleep 6
echo

demo-script-prep "Running 'python src/main.py data_files/sequences/5_100.dat'"
python src/main.py data_files/sequences/5_100.dat

sleep 10
echo "The tree that had the best structure was scored at 450. The Branch and Bound technique will in fact find the best tree, however it is not always the best technique to use. There is a chance that every tree must be checked, and when you have upwards of 20 or 30 sequences, the runtime cost becomes too great."

sleep 15
echo
echo

python src/rainbow_fun.py

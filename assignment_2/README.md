Write a program that will find a certain DNA sequence inside of
several other sequences. You will use this to find antibiotic-
resistance genes within bacteria.

It will input a text file with several lines, each representing a
different sequence. You should align the first line with each of
the others, using a variant of the dynamic programming alignment
algorithm we have been discussing in class.

It should be a half semi-global alignment, such that the entirety
of the first sequence is aligned against a portion of every other
sequence.

When there is a tie in the backtrace, bias it in the following way:

1. Add a gap to the second sequence.
2. Add a gap to neither sequence.
3. Add a gap to the first sequence.

(This is the "low road" if the first sequence is placed on top
of the matrix, or the "high road" if it's placed on the side.)

Assume that the scoring matrix gives a +1 if the bases match, and
a -1 if they don't.  The gap penalty will be -2.

For each pair, you should output where the best alignment is (i.e. its
start and end with respect to both sequences), its score, and the
alignment itself.

For example, let us say the input file has the following data:

AAGGT<br/>
CCCCCCAAGGTCCCCCCC<br/>
AAAGCTAT<br/>
ACACAGGTAA<br/>
CCAAGTCC<br/>

The output should look like this:

best alignment is from [1,7] to [5,11]<br/>
score is 5<br/>
AAGGT<br/>
AAGGT<br/>

best alignment is from [1,2] to [5,6]<br/>
score is 3<br/>
AAGGT<br/>
AAGCT<br/>

best alignment is from [1,4] to [5,8]<br/>
score is 3<br/>
AAGGT<br/>
CAGGT<br/>

best alignment is from [1,3] to [5,6]<br/>
score is 2<br/>
AAGGT<br/>
AAG-T<br/>

The output is written to a file located at the base of this assignment's directory.

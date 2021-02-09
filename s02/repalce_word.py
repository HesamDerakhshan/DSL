
# Write a function which finds and replaces "word 1" with "word 2" in a text file.
# The input will be the file name and the output should be the new file(output) witch in that words replaced.

import sys
import numpy as np

def repalce(f,first,second):
    fin = open(f, "rt")
    fout = open("out.txt", "wt")
    #for each line in the input file
    for line in fin:
    	#read replace the string and write to output file
    	fout.write(line.replace(first, second))
    #close input and output files
    fin.close()
    fout.close()

file        = sys.argv[1]
first_word  = sys.argv[2]
second_word = sys.argv[3]

# opening the text file

repalce(file, first_word, second_word)

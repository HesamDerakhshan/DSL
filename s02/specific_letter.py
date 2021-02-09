
# Write a function which returns all words started with a specific
# letter (for example a) and ended with another specific letter from
# a given text file. The input will be the file name. The function
# should take the file name and make a list of the words.
import sys
import numpy as np

def specific_letter(f,s,e):
    specific = []
    with open(f,'r') as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                if (word[0].lower() == s.lower() and word[-1].lower() == e.lower()):
                    specific.append(word);
    return specific

file        = sys.argv[1]
check_start = sys.argv[2]
check_end   = sys.argv[3]

# opening the text file

print(specific_letter(file, check_start, check_end))

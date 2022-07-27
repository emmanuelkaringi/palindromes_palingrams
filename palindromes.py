"""Find palindromes (letter palingrams) in a dictionary file."""

import load_dictionary

#load the txt file containing the words
word_list= load_dictionary.load('words.txt')

#empty list to hold the palindromes
pali_list = []

#loop through every word comparing te forward slice to the reverse slice
for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
# ------------Problem Statement----------------
# Write a program that takes 2 strings and calculates the jaccard similarity(plagarism) between them. The jaccard similarity is defined as the size of the intersection of the two sets divided by the size of the union of the two sets. 

#-------------Decorator for the project--------------
Project_title = "PLAGARISM CHECKER"
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
print("-"*len(Project_title),Project_title,"-"*len(Project_title),sep = "")
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )

# --------------------Core Logic---------------------

str1 = "Time is the most valuable thing we have, and once lost, it never returns"
str2 = "We never get time back once it's gone, and it is the most valuable thing we have"

import re 
words1 = re.findall(r'\w+', str1.lower()) # This will return a list of all the words in the string, ignoring punctuation and case.
words2 = re.findall(r'\w+', str2.lower()) # This will return a list of all the words in the string, ignoring punctuation and case.

set1 = set(words1) # This will convert the list of words to a set, which will remove duplicates and allow us to perform set operations.
set2 = set(words2) # This will convert the list of words to a set, which will remove duplicates and allow us to perform set operations.

common = set1&set2
all_words = set1|set2
print(common, all_words, len(common), len(all_words), sep = ";")
similarity_ratio = (len(common)/len(all_words))

print(f"similarity Ratio: {similarity_ratio:.2f}") # This will print the similarity ratio as a float with 2 decimal places.
# ------------Problem Statement----------------
# Write a program that takes a set of words and finds all the tuple of words that are anagrams of each other, and return them as a set of tuples. 
# For example, if the input set is {"plea","medical","listen","leap","decimal","silent","pale","enlist"}, the output should be {("plea", "leap"), ("medical", "decimal"), ("listen", "silent", "enlist"), ("pale", "leap")}. etc

#-------------Decorator for the project--------------
Project_title = "SCRAMBLED WORDS"
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
print("-"*len(Project_title),Project_title,"-"*len(Project_title),sep = "")
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )

# --------------------Core Logic---------------------
word_set = {"plea","medical","listen","leap","decimal","silent","pale","enlist"}

result = set()


for i in word_set:
    for j in word_set:
        if i != j and sorted(i) == sorted(j):
            pair = tuple(sorted((i,j))) # Now had we not used this sorted() function here, the output would have contianed both ("plea", "leap") and ("leap", "plea") as separate tuples.
            # But since we have used the sorted() function here, it will always return the tuple in the same order, so only one of them will be added to the result set because a tuple doesn not allow duplicate elements.
            result.add(pair)
    
print(result)
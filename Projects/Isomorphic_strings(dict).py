# ------------Problem Statement----------------
# Write a program that checks if two strings are isomorphic or not. 
# - Two strings are isomorphic if the characters in string A can be replaced to get string B. That is there is a one-to-one mapping possible for every character of string A to every character of string B.
# Example:
# Input: s1 = "abccba", s2 = "gcssce"
# Output: True
# Input: s1 = "add", s2 = "egg"
# Output: True


#-------------Decorator for the project--------------
Project_title = "LOGIN TRACKER"
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
print("-"*len(Project_title),Project_title,"-"*len(Project_title),sep = "")
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )

# --------------------Core Logic---------------------

# -------------- Method-1 ------------------
# Checking mapping is one-to-one for both the strings
s1 = "abccba"
s2 = "gcssce"

flag = True
if len(s1) != len(s2):
    flag = False
else:
    m12 = {}
    m21 = {}
    for c1,c2 in zip(s1,s2):
        if c1 in m12:
            if m12[c1] != c2:
                flag = False
                break
        else:
            m12[c1] = c2
        
        if c2 in m21:
            if m21[c2] != c1:
                flag = False
                break
        else:
            m21[c2] = c1

print(flag)


#--------------- Method-2 --------------
# Finding the numeric patter the 2 strings make and comparing them
s1 = "abccba"
s2 = "gcsscg"

p1, p2 = [], []
count1, count2 = 0, 0
visited1, visited2 = {}, {}

for char in s1:
    if char not in visited1:
        count1 += 1
        visited1[char] = count1

    p1.append(visited1[char])

for char in s2:
    if char not in visited2:
        count2 += 1
        visited2[char] = count2

    p2.append(visited2[char])

if p1 == p2:
    print("The strings are isomorphic!")
else:
    print("The strings are not isomorphic!")
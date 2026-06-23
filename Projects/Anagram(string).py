# whether the given set of strings are anagrams or not.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Data cleaning: First i will remove all the spaces and convert the string to lower case.
cleaned_string1 = string1.replace(" ","").lower().replace("\t","").strip(".")
cleaned_string2 = string2.replace(" ","").lower().replace("\t","").strip(".")

# Now i will iterate through the cleaned string1 and check whether a character present in cleaned_string1 is present in cleaned_string2
# for the same number of times or not. If it is present for the same number of times then i will continue checking for the next character
# but if it is not present for the same number of times then i will break the loop and print that the strings are not anagrams.

for char in cleaned_string1:
    if cleaned_string1.count(char) != cleaned_string2.count(char):
        print("The pair of strings are not Anagrams.")
        break
else: # This else block will be executed only if the for loop is not broken, which means that all the characters in the cleaned_string1 are present in the cleaned_string2 for the same number of times.
    print("The pair of strings are Anagrams.")



# An intersting way of making an anagram :
string1 = input("Enter string1: ")
string2 = input("Enter string2: ")

string1 = string1.lower().strip().replace(" ","")
string2 = string2.lower().strip().replace(" ","")

freq1 = [0]*26
freq2 = [0]*26

for char in string1:
    freq1[ord(char)-ord("a")]+=1
for char in string2:
    freq2[ord(char)-ord("a")]+=1

print(freq1,freq2, sep = '\n')

add1 = ""
add2 = ""

for i in range(26):
    if freq1[i]>freq2[i]:
        add2+=chr(i+ord("a"))*(freq1[i]-freq2[i])
    if freq1[i]<freq2[i]:
        add1+= chr(i+ord("a"))*(freq2[i]-freq1[i])
        
string1 = string1 + add1
string2 = string2 + add2 

print(string1, string2, sep = "\n")

print("Done")

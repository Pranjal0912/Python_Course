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

else:
    print("The pair of strings are Anagrams.")

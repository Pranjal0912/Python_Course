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


# Convert to anagram:
string1 = "sahejbharati"
string2 = "sahejbha"

string1 = string1.lower().strip()
string2 = string2.lower().strip()

high_string = string2 if len(string1)<len(string2) else string1


for char in high_string:
    if string1.count(char)==string2.count(char):
        continue
    else:
        char_1_count = string1.count(char)
        char_2_count = string2.count(char)
        target_string = string1 if char_1_count > char_2_count else string2
        
        char_diff = abs(char_1_count - char_2_count)
        if target_string == string1:
            string1 = string1.replace(char,"",char_diff)
        else:
            string2 = string2.replace(char,"",char_diff)
    
print(string1, string2)
        
        

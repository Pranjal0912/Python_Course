# Input: Raw data with alphabetical characters, special characters and spaces
# - alphabetical characters are important
# - spaces are important
# - special characters are not important and should be replaced by spaces

string = " These+notes#revea19Newton seeking-out$structure to/the*pyramid"

# RULES: 1. if the character is an alphabet or a space keep it in the cleaned string 
#        2. if the character is a special character replace it with a space in the cleaned string
cleaned_string = ""

for char in string:
    if char.isalpha() or char.isspace():
        cleaned_string = cleaned_string + char
    else:
        cleaned_string = cleaned_string + " "
print(cleaned_string)
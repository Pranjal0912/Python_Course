# Task 1:- Checking whether the given string is a palindrom or not.

# Taking input from the user.
string = input("Enter a string: ")

# Data cleaning: First i will remove all the spaces and convert the string to lower case.
cleaned_string = string.replace(" ","").lower().replace("\t","").strip(".")

# Reversing the cleaned string and storing it in another string.
# This can be done by reverse slicing the entire string:
new_string = cleaned_string[::-1]

# Checking for palindrome condition.
if new_string == cleaned_string:
    print("The string is a Palindrom.")
else:
    print("The string is not a Palindrome.")

# -----------------------------------------------------------------------------------------------------

# Task 2:- Making a Palindrome of a given string:

# Taking the input from the user.
string = input("Enter a string: ")

# HOW TO MAKE A PALINDROME FROM A STRING:
#   - 1. Take the string.
#   - 2. Reverse it and store it in another string.
#   - 3. Concatenate these 2 strings 
# The resultant string will be a Palindrome.

rev_string = string[-2::-1] #--> This will reverse the string except the last character, since the last character will be the middle character of the palindrome and it should not be repeated.
palindrome_string = string + rev_string
print("The Palindrome of the given string is: ", palindrome_string)

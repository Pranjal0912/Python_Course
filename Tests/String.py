# 1 Write a Python program to calculate the length of a string.
string = input('Enter a string:')
print(len(string)) 

# 2 Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
string2 = input("Enter a string")
if len(string2) < 2:
    print("")
else:
    start = string2[:2]
    rev = string2[len(string2)-2::1]
    print(start+rev)

# 3 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
string3 = "restart"
firstchar = string3[0]
newstr = string3.replace("r","$")
newstr = firstchar + newstr[1:]
print(newstr)
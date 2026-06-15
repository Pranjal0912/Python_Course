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

# 4 Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1 = input("Enter first string:")
str2 = input("Enter second string:")

str1_first2 = str1[0:2]
str2_first2 = str2[0:2]

str1 = str1.replace(str1_first2,str2_first2)
str2 = str2.replace(str2_first2, str1_first2)

print(f'- String1:- {str1}\n- String2:- {str2}')

# 5 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
string4 = input("Enter a string:")

if len(string4) < 3:
    print(string4)
elif string4.endswith('ing'):
    string4 = string4 + 'ly'
else:
    string4 = string4 + 'ing'

print(string4)    

# 6 Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
string5 = input("Enter a string:")
not_index = string5.find('not')
poor_index = string5.find('poor')

if not_index < poor_index:
    extrastring = string5[not_index:poor_index+4]
    string5 = string5.replace(extrastring,"good")
print(string5)

# 7 Write a Python program to find the first repeated word in a given string.

string = "The Quick Brown fox jumps over the lazy dog"

list1 = string.lower().split()


list2 = []
for char in list1:
    if char in list2:
        print(char)
        break
    else:
        list2.append(char)

# 8 Remove the leading zeros in an IP address

ip_address = "255.024.01.01"
ip_list=ip_address.split(".")
       
for i in range(len(ip_list)):
    ip_list[i] = str(int(ip_list[i]))

print(".".join(ip_list))


# 9 Write a Python program to capitalize the first and last letters of each word in a given string.

string = "The Quick Brown fox jumps over the lazy dog"

list1 = string.split()
i =0
for word in list1:
    word = word.title()
    word = word[0:len(word)-1] + word[-1].upper()
    list1[i] = word
    i+=1    

string = ""
for i in list1:
    string = string + i + " "

print(string)

# Optimal Solution:

string = "The Quick Brown fox jumps over the lazy dog"

new = string[0].upper()
for i in range(1, len(string)-1):
    if string[i+1] == " " or string[i-1]==" ":
        new = new + string[i].upper()
    else:
        new = new + string[i]
new = new + string[len(string)-1].upper()
print(new)


# 8 Write a program to bount the longest susequent substring of 0's in a binary 

string = "1110000100000110"
count = 0
zero = []
for char in string:
    if char == "0":
        count +=1
    else:
        zero.append(count)
        count = 0

print(max(zero))



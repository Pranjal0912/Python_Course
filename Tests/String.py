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

# 9 Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no similar letters print "No common characters".

str1 = "pranjal"
str2 = "angel"
lst = []
for char in str1:
    if char in str2:
        if char not in lst:
            lst.append(char)

print(sorted(lst))

# A very creative method involving set

str1 = "pranjal"
str2 = "angel"
set1 = set(str1)
set2 = set(str2)

# Now to find common elements between 2 sets we can just take the intersection of it 
set3 = set1.intersection(set2)
print(" ".join(set3))

# 10 Write a program to make 2 strings anagram by adding to either or both strings:

str1 = "pranjal"
str2 = "angel"

str1 = str1.strip().replace(" ", "").lower()
str2 = str2.strip().replace(" ", "").lower()

add1 = ""
add2 = ""
checked = ""

for char in str1 + str2:
    if char not in checked:
        checked += char

        count1 = str1.count(char)
        count2 = str2.count(char)

        if count1 < count2:
            add1 += char * (count2 - count1)
        elif count1 > count2:
            add2 += char * (count1 - count2)

str1 += add1
str2 += add2

print(str1, str2)

# Another way of doing it is without using the checked string is by keeping the result of s1 and s2 in a set so that duplicates are not present at all 
str1 = "pranjal"
str2 = "angel"

str1 = str1.strip().replace(" ", "").lower()
str2 = str2.strip().replace(" ", "").lower()

add1=""
add2=""
set = set(str1+str2)
for char in set:
    if str1.count(char) > str2.count(char):
        add2+=char*(str1.count(char)-str2.count(char))
    elif str1.count(char) < str2.count(char):
        add1+=char*(str2.count(char)-str1.count(char))
str1 += add1
str2 += add2

print(str1, str2, sep=" AND " )

# Another way is this :

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


# 11 Remove consecutive duplicates from the string

s1 = "aaebdbgeecdcddccfengpp"
s1 = s1.lower().strip().replace(" ","")
lst=[]
print(s1)
for i in range(len(s1)-1):
        if s1[i]==s1[i+1]:
            lst.append(i+1)    
lst = lst[::-1]
for i in lst:
    s1 = s1[0:i] + s1[i+1:] 

print(s1)

# An out of the box solution:

s1 = "aaebdbgeecdcddccfengpp"
result = ""

for ch in s1:
    if result == "" or result[-1] != ch:
        result += ch

print(result)


# Another brilliant method is this :

s1 = "aaaaebbbdbgeecdcddccfenggppp"
result = s1[0]

for i in range(1,len(s1)):
    if s1[i] != s1[i-1]:
        result += s1[i]

print(result)

# 12 write a program to find the first repeated word in a sentence :(with out using any python specific function like count etc )

str = "There is a good chance that time will reverse its flow and will now run back."
str = str.lower()

result = []
word = ""

for char in str:
    if char != " ":
        word += char
    else:
        result.append(word)
        word = ""

print(result)

# Now we will find the first word that is common:

for word in result:
    result.remove(word)
    if word in result:
        print(f"{word} is the first repeating word")
        break


# 13 Write a Python program to generate two strings from a given string. For the first string, use the characters that occur only once, and for the second, use the characters that occur multiple times in the said string.

string1 = "aabbcceffgh"
one="" 
multiple=""

for char in string1:
    if string1.count(char) > 1:
        if char not in multiple:
            multiple+=char
    else:
        one+=char

print(one, multiple, sep = "\n")

#14 Write a program to print and count the number of substrings from a given string :

# Method 1: First make substring of length 1 then 2, then up until ...substring = len(string)
str = "ABABCA"
substring = []
for length in range(1,len(str)+1):
    for i in range(0,len(str)):
        if length + i <= len(str):
            substring.append(str[i:length+i])
print(substring)

# Method 2: Sliding window select one character and make all possible substring starting from that character:
string = "ABABCA"
substring = []
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
            substring.append(string[i:j])

print(substring)

# 15 Write a program to calculate the longest common substring in 2 given strings 
s1 = "ABABCAB"
s2 = "BABACBA"

substring1= []
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        substring1.append(s1[i:j])

substring2= []
for i in range(len(s2)):
    for j in range(i+1,len(s2)+1):
        substring2.append(s2[i:j])

common_list = set(substring1)&set(substring2)
common_list = list(common_list)

max=""
for i in range(len(common_list)):
    if len(max)<len(common_list[i]):
        max = common_list[i]

print(max)


# This can be done using a DP ( dynamic programming ) approach as well:

s1 = "ABABCAB"
s2 = "BABACBA"

n = len(s1)
m = len(s2)

dp = [[0]*(m+1) for _ in range(n+1)]

max_length = 0
end_index = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1] + 1

            if dp[i][j] > max_length:
                max_length=dp[i][j]
                end_index = i
        else:
            dp[i][j]=0

print(s1[end_index-max_length:end_index])


# Write a program to concatenate uncommon characters from 2 strings and print the result

s1 = " abcdpqr"
s2 = " xabcdyz"

set1 = set(s1)
set2 = set(s2)

set3 = set1^set2
print(set3)
lst = list(set3)

result = "".join(lst)
print(result)


string = "abcdpqr"

# Write a Python program to move all spaces to the front of a given string in a single traversal.

string = " jil jklk klkjk   lkjlk "
non_space = ""
space = ""

for char in string:
    if char != " ":
        non_space+=char
    else:
        space+=" "

print(space,non_space, sep = "")


# Write a program to find Uppercase, Lowercase, Digits and Special Characters in a string

string = "Pranjal@123"
char_count= {"Uppercase":0, "Lowercase":0, "Digits":0, "Special Characters":0}

for char in string:
    if char.isupper():
        char_count["Uppercase"] += 1
    elif char.islower():
        char_count["Lowercase"] += 1
    elif char.isdigit():
        char_count["Digits"] += 1
    else:
        char_count["Special Characters"] += 1
print(char_count)

# Write a Python program to find the minimum window in a given string that will contain all the characters of another given string.

string = "ADOBECODEBANC"
target = "ABC"
bucket = []
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        aim = string[i:j]
        for k in target:
            if k in aim:
                continue
            else:
                break
        else:
            bucket.append(aim)

print(sorted(bucket, key = len)[0])

 # Write a program to check if 2 strings are isomorphic or not.       
s1 = "abccba"
s2 = "gcsscf"

if len(s1) != len(s2):
    print("The strings are not isomorphic!")
else:
    p1,p2 = [],[]
    visited_1,visited_2 = {},{}

    for i in range(len(s1)):
        if s1[i] not in visited_1:
            visited_1[s1[i]]=i

        p1.append(visited_1[s1[i]])

    for i in range(len(s2)):
        if s2[i] not in visited_2:
            visited_2[s2[i]]=i
    
        p2.append(visited_2[s2[i]])
print(p1,p2)
if p1 == p2:
    print("ISOMORPHIC") 
else:
    print("The strings are not isomorphic!")


def check_double_inverse(num):
    """This Function checks if we take the last digit of the number and make it its first digit,
       would it become double the orignal number or not, Based on that this Returns True or False"""    
    text = str(num)
    rotated = int(text[-1] + text[:-1])
    return rotated == 2 * num


def find_double_inverse():
    for digits in range(2, 100):
        for last_digit in range(1, 10):
            numerator = last_digit * (10 ** (digits - 1) - 2)

            if numerator % 19 != 0:
                continue

            prefix = numerator // 19
            number = 10 * prefix + last_digit

            if len(str(number)) == digits:
                return number

    return None


number = find_double_inverse()
print(f"{number} is a Double Inverse.")
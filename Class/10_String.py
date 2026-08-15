# STRING IN PYTHON

#String literals:
s = "hello"
a = 'hello_a'
b = """hello_b"""
c = '''hello_c '''
# So here in all these, what is a literal ?
# => A literal is a notation for representing a fixed value in source code. In the context of strings, a string literal is a sequence of characters enclosed in quotes (single, double, or triple quotes) that represents a string value directly in the code.

#Length of a string:
s = "hello"
length = len(s)
print(s) # Output: hello
print(length) # Output: 5, since the length of the string "hello" is 5 characters long

#Traversal:
print(s[0])#0 --> 1st from start
print(s[4]) #4 --> 5th from start 
print(s[-1]) #-1 --> 1st from last 

# Ways of traversal:
#Method_1: Using for loop
for x in s:
    print(x,end='')
#Method_2: Using for each loop
for x in range(len(s)): # from 0 to len(s) i.e 5 gives 0,1,2,3,4
    print(s[x],end='')

#Slicing : Operator "[]" defined as s[start:stop:step]-> just like a range function

d="hello world"
print(d[0:7]) #--> This will print the substring of 'd' starting from index 0 up to (but not including) index 7, which is "hello w". Output: hello w
print(d[:7])  #--> if no start is given '0' is taken as default. Output: hello w
print(d[3:7]) #--> since it starts from index 3 and goes up to (but not including) index 7. Output: lo w 
#print(d[-5:-9]) --> This is invalid the start should always be less than stop or we say that slicing is always done in the forward direction WHEN steps are positive
print(d[-4:-1])
print(d[0:15:2])#--> If stop > last index in string then its value is set to the last index+1 by default
print(d[::2]) #--> defualt values are taken in case of empty parameters, start = 0, stop = len(d), step = 2
print(d[::])#--> All empty means no slicing so prints the entire string as is 
print(d[::-1])#--> Reverse order 
print(d[-3:-9:-1])#--> Since steps are negative, start > stop 
print(d[7:1:-1])#--> Reverse slicing using positive start/stop


#Sting operations 

a="pranjal"
b="verma"
c = 'tiya'
print(a+b)#--> 1.concatenation using '+'
print(a*10+b)#--> 2.repetion using '*'
print("a" in a)#--> 3.membership using 'in /not in', gives a boolean value
print('z'not in b)
print('ia' in  c)

#--> 4.comparison of string is done in lexical or dictionary order:-
# suppose we have these strings 
a = "apple"
b = "ball"
c = 'cat'
d = 'dog'
p = 'python'
# Now in lexical order this will be the case : apple < ball < cat < dog < python
#->apply>apple because 'y' comes latter than 'e' in the dictionary 
#->cat < catch becasue 'catch' has extra letters 
#->data > Data because in ASCII chart capital letters and numbers come before lowecase letters 
#->2nd < Byte because numbers come before letters in ASCII index
print(a>b)


# class `str`

#|-------------|---------------------------|
#| **Section** |       **Members**         |
#|-------------|---------------------------|
#|    Data     |  string,      length      |
#|-------------|---------------------------|
#|             |  find(),       index(),   |
#|   Methods   |  endswith(),   isalpha(), |
#|             |  lower(),      upper()    |
#|-------------|---------------------------|

# Note:- String class objects are immutable, which means that once a string is created, it cannot be modified.
# Any operation that seems to modify a string actually creates a new string object.

print(dir(str)) # This will show the list of all the methods of the string class

# -----------------------------------------------------------------------------------------------------------
# Find and Index:
# -----------------------------------------------------------------------------------------------------------

str1 = "Welcome to python programming"
print(str1)
# 1.find() method: It returns the index of the first occurrence of  the specified value. If the value is not found, it returns -1.

# a)find:
#   Prototype: str.find(sub, start, end)  ---> wherever character is first found, return the index of that character in the string. If not found, return -1
#   Parameters:
#   sub: This is the substring to be searched in the given string.
#   start: This is the starting index from where the search begins. It is optional and defaults to 0.
#   end: This is the ending index where the search ends. It is optional and defaults to the length of the string.
print(str1.find("python"))  #--> 11
print(str1.find("Python"))  #--> -1, since 'P' is capital here and 'p' is small in the string
print(str1.find("o", 5)) #--> 9, since 'o' is found at index 9 and we have given the starting index as 5, so it starts searching from index 5 and finds 'o' at index 9
print(str1.find("t", 5, 10)) #--> 8, since 't' is found at index 8 and we have given the starting index as 5 and ending index as 10, so it starts searching from index 5 and finds 't' at index 8

str1 = "Welcome to python programming"
#b) rfind:
#   Prototype: str1.rfind(sub, start, end)  ---> wherever character is (last found or) found first but searching in reverse order, return the index of that character in the string. If not found, return -1
print(str1.rfind("o")) #--> 20, since 'o' is found at index 20 and it is the last occurrence of 'o' in the string
print(str1.rfind("to"))

str1 = "Welcome to python programming"
## 2.index() method: It returns the index of the first occurrence of the specified value. If the value is not found, it raises a "ValueError".
# a) index:
print(str1.index("python")) #--> 11
print(str1.index("Python")) #--> ValueError: substring not found, since 'P' is capital here and 'p' is small in the string  

# b) rindex(): It returns the index of the first occurrence of the specified value. If the value is not found, it raises a "ValueError". It searches in reverse order.
print(str1.rindex("o")) #--> 20, since 'o' is found at index 20 and it is the last occurrence of 'o' in the string
print(str1.rindex("to")) #--> 8, since 'to' is found at index 8 and it is the last occurrence of 'to' in the string

# 3.count() method: It returns the number of occurrences of a substring in the given string.
str1 = "Welcome to python programming"
print(str1.count("o")) #--> 3, since 'o' is found 3 times in the string
print(str1.count("to")) #--> 1, since 'to' is found 1 time in the string
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# Alignment and Padding:
# -----------------------------------------------------------------------------------------------------------
string1 = "   Hello" # string with leading spaces
string2 = "World   " # string with trailing spaces
string3 = "   Hello World   " # string with leading and trailing spaces
string4 = "Hello World" # string without leading and trailing spaces

# 1.ljust(width,fillchar) method: It left-aligns the string and pads it with the specified character (default is space) to a specified width.
# Parameters:
# width: This is the total width of the resulting string after padding.
# fillchar: This is the character used to pad the string. It is optional and defaults to a space.
print(string1.ljust(20, '*')) #--> '   Hello**********', since the total width is 20 and the original string is 8 characters long, so it adds 12 '*' characters to the right of the string to make the total width 20

# 2.rjust(width,fillchar) method: It right-aligns the string and pads it with the specified character (default is space) to a specified width.
print(string2.rjust(20, '*')) #--> '**********World   ', since the total width is 20 and the original string is 8 characters long, so it adds 12 '*' characters to the left of the string to make the total width 20

# 3.center(width,fillchar) method: It centers the string and pads it with the specified character (default is space) to a specified width.
print(string4.center(20, '*')) #--> '*****Hello World*****', since the total width is 20 and the original string is 11 characters long, so it adds 4 '*' characters to the left and 5 '*' characters to the right of the string to make the total width 20

# 4.zfill(width) method: It pads the string with zeros on the left to fill the specified width.
number = "123"
print(number.zfill(10)) #--> '0000000123', since the total width is 10 and the original string is 3 characters long, so it adds 7 '0' characters to the left of the string to make the total width 10

# strip fucntions
string1 = "   Hello" # string with leading spaces
string2 = "World   " # string with trailing spaces
string3 = "   Hello World   " # string with leading and trailing spaces
string4 = "Hello World" # string without leading and trailing spaces


# 5.lstrip() method: It removes the whitespace characters from the left side of the string.
print(string1.lstrip()) #--> 'Hello'

# 6.rstrip() method: It removes the whitespace characters from the right side of the string.
print(string2.rstrip()) #--> 'World'

# 7.strip() method: It removes the whitespace characters from both sides of the string.
print(string3.strip()) #--> 'Hello World'

# Parameters of strip functions:
# 1) chars: This is an optional parameter that specifies the set of characters to be removed from the string. If not provided, it defaults to removing whitespace characters.
string5 = "###Hello###" 
print(string5.strip('#')) #--> 'Hello', since it removes the '#' characters from both sides of the string
print(string5.lstrip('#')) #--> 'Hello###', since it removes the '#' characters from the left side of the string
print(string5.rstrip('#')) #--> '###Hello', since it removes the '#' characters from the right side of the string       

string6 = "$%Hello $@%"
print(string6.strip('$%@ '))# --> 'Hello', since it removes the '$', '%', '@' and ' ' characters from both sides of the string
# -----------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------
# Join and Split Methods:
# -----------------------------------------------------------------------------------------------------------
# 1.replace(old, new, count) method: It replaces all occurrences of a specified substring with another substring in the given string.
# Parameters:
# old: This is the substring to be replaced.
# new: This is the substring that will replace the old substring.
# count: This is an optional parameter that specifies the maximum number of occurrences to be replaced. If not provided, it replaces all occurrences.
string1 = "a-b-c-d-e-f-g-h"
print(string1.replace('-', '*')) #--> 'a*b*c*d*e*f*g*h', since it replaces all occurrences of '-' with '*'
print(string1.replace('-', '*', 3)) #--> 'a*b*c*d-e-f-g-h', since it replaces the first 3 occurrences of '-' with '*'


# 2. join(iterable) method: In simpler terms, it inserts the specified string between the elements of an iterable (like a list or tuple or a string) and returns a new string.
# Parameters:
# iterable: This is the collection of elements (like a list, tuple, or string) that you want to join together.
# With string:
s1 = "abc"
s2 = "xyz"
print(s1.join(s2)) #--> 'xabcyabcz', since it inserts the string 'abc' between each character of the string 'xyz'
# With list:
list1 = ['Hello', 'World', 'Python']
s3 = "-"
print(s3.join(list1)) #--> 'Hello-World-Python', since it inserts the string '-' between each element of the list
# With tuple:   
tuple1 = ('Hello', 'World', 'Python')
print(s3.join(tuple1)) #--> 'Hello-World-Python', since it inserts the string '-' between each element of the tuple


# 3. split(sep, maxsplit) method: It splits a string into a list of substrings based on a specified delimiter.
# Parameters:
# sep: This is the delimiter that specifies where to split the string. It is optional and defaults to any whitespace character (like space, tab, etc.).
# maxsplit: This is an optional parameter that specifies the maximum number of splits to be performed. If not provided, it splits the string at all occurrences of the delimiter.
string1 = "Messi Ronaldo Neymar"
string2 = "Messi-Ronaldo-Neymar"

print(string1.split()) #--> ['Messi', 'Ronaldo', 'Neymar'], since it splits the string at whitespace characters as the default delimiter
print(string2.split('-')) #--> ['Messi', 'Ronaldo', 'Neymar'], since it splits the string at '-' characters as the specified delimiter
print(string1.split(' ', 1)) #--> ['Messi', 'Ronaldo Neymar'], since it splits the string at the first occurrence of the space character as the specified delimiter and maxsplit is 1, so it only splits once
print(string2.split("$")) #--> ['Messi-Ronaldo-Neymar'], since it splits the string at '$' characters as the specified delimiter and since there is no '$' in the string, it returns the whole string as a single element in the list
# Note: If the specified delimiter is not found in the string, the split() method will return a list containing the original string as its only element.

#Similarly, there is a method called rsplit() which does the same thing but from reverse order

# splitlines() method: It splits a string into a list of lines based on the newline character ('\n').
string3 = "Hello\nWorld\nPython"
string4 = "Hello World Python\npranjal"
print(string3.splitlines()) #--> ['Hello', 'World', 'Python'], since it splits the string at newline characters as the delimiter
print(string3.splitlines(keepends=True)) #--> ['Hello\n', 'World\n', 'Python'], since it splits the string at newline characters as the delimiter and keeps the newline characters in the resulting list when keepends is True
# -----------------------------------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------------------------------
# Prefix and Suffix Methods:
# -----------------------------------------------------------------------------------------------------------

# 1. startswith(prefix, start, end) method: It checks if the string starts with the specified prefix. It returns True if the string starts with the prefix, otherwise it returns False.
# Parameters:       
# prefix: This is the substring that you want to check if the string starts with.
# start: This is the starting index from where the check begins. It is optional and defaults to 0.
# end: This is the ending index where the check ends. It is optional and defaults to the length of the string.
string1 = "Hello World"
print(string1.startswith("Hello")) #--> True, since the string starts with "Hello"
print(string1.startswith("H")) #--> True, since the string starts with "H"

# 2. endswith(suffix, start, end) method: It checks if the string ends with the specified suffix. It returns True if the string ends with the suffix, otherwise it returns False.
# Parameters:
# suffix: This is the substring that you want to check if the string ends with.
# start: This is the starting index from where the check begins. It is optional and defaults to 0.
# end: This is the ending index where the check ends. It is optional and defaults to the length of the string.
print(string1.endswith("World")) #--> True, since the string ends with "World"
print(string1.endswith("d")) #--> True, since the string ends with "d"

# 3. removeprefix(prefix) method: It removes the specified prefix from the string if it starts with that prefix. If the string does not start with the specified prefix, it returns the original string.
print(string1.removeprefix("Hello")) #--> ' World', since it removes the prefix "Hello" from the string
print(string1.removeprefix("H")) #--> 'ello World', since it removes the prefix "H" from the string

# 4. removesuffix(suffix) method: It removes the specified suffix from the string if it ends with that suffix. If the string does not end with the specified suffix, it returns the original string.
print(string1.removesuffix("World")) #--> 'Hello ', since it removes the suffix "World" from the string
print(string1.removesuffix("d")) #--> 'Hello Worl', since it removes the suffix "d" from the string

# 5. partition(sep) method: It splits the string into three parts based on the first occurrence of the specified separator. It returns a tuple containing the part before the separator, the separator itself, and the part after the separator.
string1 = "Hello World Python"
print(string1.partition(" ")) #--> ('Hello', ' ', 'World Python'), since it splits the string at the first occurrence of the space character as the separator and returns a tuple containing the part before the separator, the separator itself, and the part after the separator

# 6. rpartition(sep) method: It splits the string into three parts based on the last occurrence of the specified separator. It returns a tuple containing the part before the separator, the separator itself, and the part after the separator.
print(string1.rpartition(" ")) #--> ('Hello World', ' ', 'Python'), since it splits the string at the last occurrence of the space character as the separator and returns a tuple containing the part before the separator, the separator itself, and the part after the separator

# -----------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------
# Case Conversion Methods:
# -----------------------------------------------------------------------------------------------------------

# 1. capitalize() method: It converts the first character of the string to uppercase and the rest to lowercase.
string1 = "hello world"
print(string1.capitalize()) #--> 'Hello world'

# 2. lower() method: It converts all characters in the string to lowercase.
print(string1.lower()) #--> 'hello world'

# 3. upper() method: It converts all characters in the string to uppercase.
print(string1.upper()) #--> 'HELLO WORLD'

# 4. swapcase() method: It converts uppercase characters to lowercase and vice versa.
string2 = "Hello World"
print(string2.swapcase()) #--> 'hELLO wORLD'

# 5. title() method: It converts the first character of each word in the string to uppercase and the rest to lowercase.
string3 = "hello world python"
print(string3.title()) #--> 'Hello World Python'

# 6. casefold() method: It converts the string to lowercase and is more aggressive than lower() method in terms of case conversion, especially for certain Unicode characters.
# -----------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------
# Inquiry Methods:
# -----------------------------------------------------------------------------------------------------------
# 1. isalpha() method: It checks if all characters in the string are alphabetic (letters). It returns True if all characters are alphabetic and False otherwise. Note that it returns False if the string is empty or contains any non-alphabetic characters (like spaces, digits, punctuation, etc.). 
string1 = "HelloWorld"
print(string1.isalpha()) #--> True, since all characters in the string are alphabetic and there is at least one character
string2 = "Hello World" 
print(string2.isalpha()) #--> False, since there is a space character in the string which is not alphabetic, why? 

# 2. isalnum() method: It checks if all characters in the string are alphanumeric (letters and digits). It returns True if all characters are alphanumeric and False otherwise. Note that it returns False if the string is empty or contains any non-alphanumeric characters (like spaces, punctuation, etc.).
string6 = "Hello123"
print(string6.isalnum()) #--> True, since all characters in the string are alphanumeric and there is at least one character
string7 = "Hello 123" 
print(string7.isalnum()) #--> False, since there is a space character in the string which is not alphanumeric 

# 3. isspace() method: It checks if all characters in the string are whitespace characters (like space, tab, newline, etc.). It returns True if all characters are whitespace and False otherwise. Note that it returns False if the string is empty or contains any non-whitespace characters (like letters, digits, punctuation, etc.).
string8 = "   " 
print(string8.isspace()) #--> True, since all characters in the string are whitespace and there is at least one character
string9 = " Hello "
print(string9.isspace()) #--> False, since there are non-whitespace characters (like 'H', 'e', 'l', 'o') in the string which are not whitespace 

# 4. islower() method: It checks if all characters in the string are lowercase letters. It returns True if all characters are lowercase and False otherwise. Note that it returns False if the string is empty or contains any non-lowercase characters (like uppercase letters, digits, spaces, punctuation, etc.).
string10 = "hello world"
print(string10.islower()) #--> True, since all characters in the string are lowercase letters and there is at least one character
string11 = "Hello World"
print(string11.islower()) #--> False, since there are uppercase letters in the string which are not lowercase
string12 = "hello world"
print(string12.islower()) #--> True, since all characters in the string are lowercase letters and there is at least one character   

# 5. isupper() method: It checks if all characters in the string are uppercase letters. It returns True if all characters are uppercase and False otherwise. Note that it returns False if the string is empty or contains any non-uppercase characters (like lowercase letters, digits, spaces, punctuation, etc.).
string13 = "HELLO WORLD"
print(string13.isupper()) #--> True, since all characters in the string are uppercase letters and there is at least one character
string14 = "Hello World"
print(string14.isupper()) #--> False, since there are lowercase letters in the string which are not uppercase

# 6. istitle() method: It checks if the string is in title case, which means that the first character of each word is uppercase and the rest are lowercase. It returns True if the string is in title case and False otherwise. Note that it returns False if the string is empty or contains any non-title case characters (like all uppercase letters, all lowercase letters, digits, spaces, punctuation, etc.). 
string16 = "Hello World"
print(string16.istitle()) #--> True, since the first character of each word is uppercase and the rest are lowercase
string17 = "HELLO WORLD"
print(string17.istitle()) #--> False, since all characters are uppercase and not in title case

# 7. isprintable() method: It checks if all characters in the string are printable (i.e., they can be printed on the screen). It returns True if all characters are printable and False otherwise. Note that it returns False if the string is empty or contains any non-printable characters (like control characters, etc.).
string18 = "Hello World"    
print(string18.isprintable()) #--> True, since all characters in the string are printable and there is at least one character
string19 = "Hello\nWorld" 
print(string19.isprintable()) #--> False, since there is a newline character '\n' in the string which is not printable

# 8. isidentifier() method: It checks if the string is a valid identifier in Python. A valid identifier is a string that starts with a letter (a-z or A-Z) or an underscore (_) followed by letters, digits (0-9), or underscores. It returns True if the string is a valid identifier and False otherwise. Note that it returns False if the string is empty or contains any invalid characters for an identifier (like spaces, punctuation, etc.).
string20 = "variable_name"
print(string20.isidentifier()) #--> True, since the string is a valid identifier in Python
string21 = "1variable_name"
print(string21.isidentifier()) #--> False, since the string starts with a digit which is not allowed for a valid identifier in Python
# -----------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------
# Extra Inquiry Methods:
# -----------------------------------------------------------------------------------------------------------

# 1. isdigit() method: It checks if all characters in the string are digits (0-9). It returns True if all characters are digits and False otherwise. Note that it returns False if the string is empty or contains any non-digit characters (like letters, spaces, punctuation, etc.).
# It is ture for all characters in unicode that are classified as digits, which includes not only the ASCII digits (0-9) but also digits from other languages and scripts. For example, it will return True for characters like '٠' (Arabic-Indic digit zero) and '５' (Fullwidth digit five).
string22 = "12345"
print(string22.isdigit()) #--> True, since all characters in the string are digits
string23 = "12345a"
print(string23.isdigit()) #--> False, since there is a non-digit character 'a' in the string
string26 = " 23 34"
print(string26.isdigit()) #--> False, since there are space characters in the string which are not digits
string24 = "１２３４５" # Fullwidth digits
print(string24.isdigit()) #--> True, since all characters in the string are digits (Fullwidth digits) 
string25 = "٣" # Arabic-Indic digit three
print(string25.isdigit()) #--> True, since the character '٣' is classified as a digit in Unicode
subscriptstring26 = "₂" # Subscript digit two
print(subscriptstring26.isdigit()) #--> True, since the character '₂' is classified as a digit in Unicode
decimalstring27 = "3.45" # Decimal number as a string
print(decimalstring27.isdigit()) #--> False, since the character '.' is not a digit, even though '3' and '4' are digits

# 2. isdecimal() method: It checks if all characters in the string are decimal characters. It returns True if all characters are decimal and False otherwise. 
# Decimal characters are a subset of digits that include only the characters used to represent decimal numbers in various scripts. This includes the ASCII digits (0-9) and other decimal characters from different languages and scripts, but it does not include characters like superscript or subscript digits, or other digit-like characters that are not used for representing decimal numbers.
string28 = "12345"
print(string28.isdecimal()) #--> True, since all characters in the string are decimal characters
string29 = "12345a"
print(string29.isdecimal()) #--> False, since there is a non-decimal character 'a' in the string
string30 = " 23 34"
print(string30.isdecimal()) #--> False, since there are space characters in the string which are not decimal characters
devnagriDigits = "१२३४५" # Devanagari digits
print(devnagriDigits.isdecimal()) #--> True, since all characters in the string are decimal characters (Devanagari digits)
subscriptstring31 = "₂" # Subscript digit two
print(subscriptstring31.isdecimal()) #--> False, since the character '₂' is not classified as a decimal character in Unicode, it is classified as a digit but not a decimal character
decimalstring32 = "-3.45" # Negative decimal number as a string
print(decimalstring32.isdecimal()) #--> False, since the character '-' is not a decimal character, even though '3' and '4' are decimal characters

# "-", subscript digits, superscript digits, and other digit-like characters that are not used for representing decimal numbers will return False when using the isdecimal() method, even though they may return True when using the isdigit() method if they are classified as digits in Unicode.

# 3. isnumeric() method: It checks if all characters in the string are numeric characters. It returns True if all characters are numeric and False otherwise.
string33 = "12345"
print(string33.isnumeric()) #--> True, since all characters in the string are numeric characters
string34 = "12345a"
print(string34.isnumeric()) #--> False, since there is a non-numeric character 'a' in the string
string35 = " 23 34"
print(string35.isnumeric()) #--> False, since there are space characters in the string which are not numeric characters 
fractionstring = "½" # Fraction character
print(fractionstring.isnumeric()) #--> True, since the character '½' is classified as a numeric character in Unicode
romanNumeralString = "Ⅻ" # Roman numeral twelve
print(romanNumeralString.isnumeric()) #--> True, since the character 'Ⅻ' is classified as a numeric character in Unicode
superscriptstring = "³" # Superscript digit three   
print(superscriptstring.isnumeric()) #--> True, since the character '³' is classified as a numeric character in Unicode     

# Difference between isdigit(), isdecimal(), and isnumeric() methods:
# 1. isdigit() method returns True for characters that are classified as digits in Unicode, which includes a wide range of characters from various scripts, including ASCII digits, fullwidth digits, subscript and superscript digits, and other digit-like characters. It returns False for characters that are not classified as digits, such as letters, spaces, punctuation, etc.
# 2. isdecimal() method returns True only for characters that are classified as decimal characters in Unicode, which is a subset of digits that includes characters used to represent decimal numbers. It returns False for characters that are not classified as decimal characters, such as letters, spaces, punctuation, and even some digit-like characters that are not used for representing decimal numbers (like subscript digits).
# 3. isnumeric() method returns True for characters that are classified as numeric characters in Unicode, which includes digits, decimal characters, and other numeric characters like fractions and Roman numerals. It returns False for characters that are not classified as numeric characters, such as letters, spaces, punctuation, etc.

# 4. isascii() method: It checks if all characters in the string are ASCII characters (characters with Unicode code points in the range U+0000 to U+007F). It returns True if all characters are ASCII and False otherwise. Note that it returns False if the string is empty or contains any non-ASCII characters (like letters with accents, characters from non-Latin scripts, etc.).
string36 = "Hello World"
print(string36.isascii()) #--> True, since all characters in the string are ASCII characters and there is at least one character
string37 = "Hello Wörld"    
print(string37.isascii()) #--> False, since there is a non-ASCII character 'ö' in the string
string38 = "こんにちは" # Japanese characters   
print(string38.isascii()) #--> False, since all characters in the string are non-ASCII characters
# -----------------------------------------------------------------------------------------------------------


# With this we are done with almost all the methods of the string class:-
# 1. find() and index() methods for searching substrings - SEARCHING METHODS
# 2. Alignment and padding methods like ljust(), rjust(), center(), zfill() for aligning and padding strings - ALIGNMENT AND PADDING METHODS
# 3. strip functions like lstrip(), rstrip(), strip() for removing leading and trailing characters from strings - STRIP FUNCTIONS
# 4. join() and split() methods for joining and splitting strings - JOIN AND SPLIT METHODS
# 5. startswith(), endswith(), removeprefix(), removesuffix(), partition(), rpartition() methods for checking prefixes and suffixes and removing them - PREFIX AND SUFFIX METHODS
# 6. Case conversion methods like capitalize(), lower(), upper(), swapcase(), title(), casefold() for changing the case of characters in a string - CASE CONVERSION METHODS
# 7. Inquiry methods like isalpha(), isalnum(), isspace(), islower(), isupper(), istitle(), isprintable(), isidentifier() for checking the properties of characters in a string - INQUIRY METHODS
# 8. Extra inquiry methods like isdigit(), isdecimal(), isnumeric(), isascii() for checking specific types of characters in a string - EXTRA INQUIRY METHODS

 
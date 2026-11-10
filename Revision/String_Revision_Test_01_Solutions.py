# PART-A : 

# Q1. String slicing
# Given:
# s = "Programming"

# Without running the code, predict the output of:
# print(s[0:6]) -> Progra
# print(s[-4:]) -> ming
# print(s[::2]) -> Pormig
# print(s[::-1]) -> gnimmargorp
# print(s[5:2:-1]) -> arg

# Briefly explain the last expression.-> The last statment prints from 5 (inclusive) to 2 index in reverse order 

# Q2. Searching within strings
# Given:
# s = "banana bandana"
# Predict the output:

# print(s.find("ana")) -> 4
# print(s.rfind("ana")) -> 4
# print(s.count("ana")) -> 3
# print(s.find("xyz"))-> -1



# Also explain what happens if you replace the last .find() with .index(). -> if we replace .find() with .index() then all 3 statements would be giving the same result but the last statement might have thrown an error 


# Q3. String immutability
# Consider:
# s = "Python"
# s[0] = "J"


# Explain why this fails. Then write two different ways of producing "Jython" without directly assigning to a string index.

# This fails because string as a data type are immuatable in python and python doesn't simply allow the programmer to change a string at a particular index

# One way is using the replace function : 
s = "Python"
s = s.replace("P", "J")
print(s)

# Other is by string combination of string concatenation and slicing :
s = "Python"
s1 = "J"+s[1:] # This adds a "J" at the start of the string and then proceeds to add that "J" to the rest of the the string starting from index 1 so the first letter "P" is natuarlly ommited

# PS:- In both the cases, a new string object is returned and the no changes can or are done to the orignal string 


# Q4. Case conversion methods
# For:
# s = "hELLO pYTHON"


# Predict the output of:

# print(s.capitalize()) -> Hello python
# print(s.title()) -> Hello Python
# print(s.swapcase()) -> Hello Python
# print(s.lower()) -> hello python


# Explain one difference between .capitalize() and .title().

# -> .capitalize() only makes the first letter of the string capital and rest lowercase
# -> .title() makes the first letter of each word in the string capital( character seperated by a " " space character is called a word) and rest lowercase 

# Q5. Joining and splitting
# Given:
# s = "Messi-Ronaldo-Neymar"

# Write code that:
# 1. Splits the string into a list of three names. 
# 2. Joins those names using " | " as the separator.
# 3. Prints the final string.

s = "Messi-Ronaldo-Neymar"
s1 = s.split("-")
print(s1)
s2 = "|".join(s1)
print(s2)

# Q6. Tricky slicing
# Predict all outputs without executing:

s = "ABCDEFGHIJ"

print(s[8:2:-2]) # -> IGE
print(s[-2:-8:-2]) # -> IGE
print(s[2:8:-1]) # -> ERROR 
print(s[-20:20:3]) # -> ADGJ
print(s[::-3]) # -> JGDA

# Explain why the third expression behaves the way it does.

# ->  Because the direction of indexing is different from the start to end direction 

# Q7. strip() versus replace()
# Given:

s = "xyxPythonxyxy"
print(s.strip("xy")) # -> Python
print(s.lstrip("xy")) # -> Pythonxyxy
print(s.rstrip("xy")) # -> xyxPython
print(s.replace("xy", "")) # -> Python 

# What important distinction between .strip() and .replace() does this demonstrate?

# -> .strip() only removes the characters from the start and end of the string but not from the middle of the string whereas .replace() replaces all occurences of the substring in the string with another substring or an empty string if we want to remove it completely.

# 
# Q8. Inquiry methods
# For each expression, predict True or False and briefly explain why:

print("Python3".isalpha()) # -> False because the string contains a number 3 which is not an alphabet
print("Python3".isalnum()) # -> True because the string contains only alphanumeric characters
print("   \t\n".isspace()) # -> True because the string contains only whitespace characters
print("abc123!".islower()) # -> True because all alphabetic characters are lowercase
print("ABC123!".isupper()) # -> True because all alphabetic characters are uppercase
print("Hello World".istitle()) # -> True because the string is in title case
print("123abc".isidentifier()) # -> False because the string is not a valid identifier
print("Hello\nWorld".isprintable()) # -> False because the string contains a newline character which is not printable


# Q9. Alignment and padding
# Given:

s = "CAT"
print(s.ljust(8, "*")) #-> CAT*****
print(s.rjust(8, "-")) #-> -----CAT
print(s.center(8, ".")) #-> ..CAT... 
print(s.zfill(7)) #-> 00000CAT

#->? i have one question for you buddy :- in this "print(s.center(8, ".")) " this can be the correct answer "..CAT..." or "...CAT.." what will be the more correct one and why

# Explain what happens when the specified width is smaller than the original string length.
#-> Not really sure with this one buddy, let me run and check :
print(s.ljust(2, "8"))

# yeah it prints the orignal word, i know this might come of as cheating but i really couldn't help but running the code and checking the output asap


# Q10. split(), rsplit(), and partition()
# Given:

s = "apple,banana,cherry,mango"

# Predict:

print(s.split(",", 2)) #-> ["apple", "banana", "cherry,mango"]
print(s.rsplit(",", 2)) #-> ["apple,banana", "cherry", "mango"]
print(s.partition(",")) #-> ["apple", ",", "banana,cherry,mango"]
print(s.rpartition(",")) #-> ["apple,banana,cherry", ",", "mango"]


# Explain why partition() and split() return different data types.

# -> split() gives an array with elements that are made based on all the occurence of the substring ( if not givne the maxsplit explicitly)
# -> partition() divides the string and gives an array with 3 elements always [ "whatever is before the seperator", "the seperator itself", "whatever is after the seperator" ]

# Q11. Correct the broken code
# The following code is intended to count how many times "python" appears in a sentence, ignoring case.

s = "Python is fun. I love PYTHON and python."

s.lower()
count = s.count("python")

print(count)

# It gives an incorrect result.
# Identify the mistake, explain why it happens, and correct the code without using a loop.

# The correct version for this is something like this :- 

s = "Python is fun. I love PYTHON and python."
Count = s.count("python")

print(Count)


# why the above version didn't work, because before counting the occurence of the word "python" our code lowercased every word in string s, so 'Python', 'PYTHON' and 'python' all became 'python' hence the false count for the word 

# -> also you did say to not do it without loops and so it did , but even you know that functions like count(), len() etc internally use loop to do the job so there is that 


# Q12. Substring searching with boundaries
# Given:

s = "abracadabra"

# Predict:
print(s.find("bra", 2)) # -> 8
print(s.find("bra", 2, 9)) # -> -1
print(s.rfind("a", 0, 8)) # ->0
print(s.count("a", 3, 9)) # -> 3

# Explain whether the end parameter is inclusive or exclusive.

# -> guessing judging by how things are, i belive the end parameter is always exlusive in all the functions using start and stop , its just a GUESS i am not sure 

# Q13. Unicode character classification
# Predict the result of each expression:

print("123".isdecimal())# -> True
print("²".isdecimal()) # -> False
print("²".isdigit())# -> True
print("½".isdigit())# -> False
print("½".isnumeric())# -> True
print("Ⅻ".isnumeric())# -> True
print("१२३".isdecimal())# -> True

# Then explain the relationship between .isdecimal(), .isdigit(), and .isnumeric().

# don't know please can you esplain this to me buddy, i have no idea about this one.


# Q14. String formatting without f-strings
# Given:

names = ["Alice", "Bob", "Charlie"]

# Produce:

# ********Alice*********
# *********Bob**********
# ********Charlie*******

# Each line must have a total width of 22 characters.
# Use string methods from your notes, not manual calculations of how many * characters to append.

for i in range(len(names)):
    print(names[i].center(22, "*"))

# Q15. Removing prefixes and suffixes
# Given:

filename = "report_final_final.pdf"

# Write code using appropriate string methods to:
# 1. Remove the prefix "report_".
# 2. Remove the suffix ".pdf".
# 3. Remove only the final occurrence of "_final".

filename = ((filename.removeprefix("report_")).removesuffix(".pdf")).removesuffix("_final")
print(filename)

# Explain why .strip() is not a suitable substitute for .removeprefix() or .removesuffix().

# -> I don't know bud , maybe because strip removes from either side of the string wheras removeprefix and removesuffix target a spceific end of the string , Not sure can you explain me if i am not correct 


# Q16. String identity versus equality
# Study this code:

s1 = "hello"
s2 = s1
s3 = s1.replace("h", "j")

print(s1)#-> hello
print(s2)#-> hello
print(s3)#->jello

s1 = s1.upper()

print(s1) #-> HELLO
print(s2) #-> hello

# Predict all outputs, then explain:
# 1. Which variables initially refer to the same object? --> I belive s1 and s2 both refer to the same object whose values is "hello"
# 2. Does .replace() mutate the original string? --> No, none of the string class functions have the power to change or modify the orignal string object, string in general is a immutable object in python, hence '.replace()' function is no exception to this rule 
# 3. Why doesn't changing s1 affect s2? --> because initially when we do s1 = s2, here both s1 and s2 are pointing to the same object with value "hello" but when we do s1 = s1.upper() then at that moment a new object is created with value "HELLO" and then s1 starts pointing to that while s2 is still pointing to the orignal object with value "hello", s2 might have been modified too if s1 and s2 were lists (MAYBE) cuz of mutability of list data type
# Finally, explain whether s1 is s2 is a reliable way to compare string contents and why. --> No despite, s1 and s2 having the same value (and initially pointing to the same object) but on making some operations to s1 (or s2) they eventually point to a different object and while the 2 different object may (due to some operations ) have a similar value but that won't be the same object in memory and hence "s1 is s2" will eventually return false despite having the same value 


# Q17. Empty strings and special method behaviour
# Without running the code, predict the output of:

s = ""

print(s.isalpha()) #-> False
print(s.isdigit()) #-> False
print(s.isspace()) #-> False
print(s.isprintable()) #-> True
print(s.isascii()) #-> True
print(s.startswith("")) #-> True
print(s.endswith("")) #-> True
print("abc".count("")) #-> Not sure whats the output of this one, its really a tricky one 😅🤣
# Pay particular attention to the last three expressions. 
# Explain any results that surprise you.

# "print(s.isprintable()) #-> True" and "print(s.isascii()) #-> True" are surprising to me because I thought that an empty string would not be printable or ascii but it seems like it is considered as a printable and ascii character.

# PATTERN MATCHING:

# 1.'and|org': This pattern matches either 'and' or 'org'. The '|' symbol is used to specify an alternative, so the regex will ....
# ... match any string that contains either 'and' or 'org'.

# 2. '[abcd]' or '[a-d]': This pattern says that the string should have only one letter and one among these only i.e one of 'a', 'b', 'c' or 'd'. so it will match any string that contains exactly one of the characters.

# 3. '[abc]+': This pattern matches one or more occurrences of the characters 'a', 'b', or 'c'. The '+' symbol indicates that the preceding character class should appear at least once. So it will match strings like 'a', 'b', 'c', 'aa', 'abc', etc.
# ---------------------------------------------------------------------------------------------------------------------------------

## Now for using "Regular Expression" there is a module in the standard library called "re". We can use this module to work with regular expressions in Python.
import re
# A Quick recap on how to import a library in Python:
#  1. import re: This statement imports the entire 're' module, allowing you to access all of its functions and classes using the 're' prefix before a '.' and the function name. For example, you would use 're.search()' to call the 'search' function from the 're' module.
#  2. 'from re import *' or 'from re import {some specific function or class}': This statement imports specific functions or classes from the're' module directly into the current namespace. 
#  3. 'import re as regex' or 'import re as {some alias}': This statement imports the 're' module and gives it an alias (in this case, 'regex'). You can then use 'regex' instead of 're' to access the functions and classes in the module. For example, you would use 'regex.search()' to call the 'search' function from the 're' module.

# ---------------------------------------------------------------------------------------------------------------------------------

#  Functions of the 're' module:

# Validation functions:

# 1. re.match():
# -> This function checks for a match only at the begining of the string. 
# -> It returns a match object (object of 're' class) if the pattern is found at the beginning of the string, otherwise it returns None.
# -> Syntax: re.match(pattern, string, flags=0)
# ->Parameters:
#   - pattern: The regular expression pattern to search for.
#   - string: The string to search within.
#   - flag: Optional flags to modify the behavior of the regex (e.g., re.IGNORECASE for case-insensitive matching, re.MULTILINE for multiline matching, re.DOTALL for dotall matching).

print(re.match('abc', 'abcdef')) # This will return a match object because 'abc' is at the beginning of the string.
print(re.match("def", 'abcdef')) # This will return 'None' because 'def' is not at the beginning of the string.

# NOTE:- Now the above function prints "<re.Match object; span=(0, 3), match='abc'>" which is an object of the 're' class.
# we can make this only give the matched string by using the 'group()' method of the match object.
print(re.match('abc', 'abcdef').group()) # This will print 'abc' which is the matched string.
# we can also use the 'span()' method to get the start and end index of the matched string in the original string.
print(re.match('abc', 'abcdef').span()) # This will print '(0, 3)' which means that the matched string 'abc' starts at index 0 and ends at index 3 (exclusive) in the original string 'abcdef'.
# --> group() method: This method returns the part of the string where there was a match. Outputs a string from the match object.
# --> span() method: This method returns a tuple containing the start_index and end_index of the matched string in the original string. Outputs a tuple from the match object.


# 2. re.fullmatch():
# -> This function checks for the entire string to match the pattern (more like a stricter form of match())
# -> Also returns a 're' class object if the entire string matches the pattern and 'None" if it doesn't
# -> Syntax: re.fullmatch(pattern, string, flags=0) [Takes same parameters as match() function]

print(re.fullmatch('abc', 'ABc', re.IGNORECASE).group()) # -> Output: ABc. This will return a match object because the entire string 'ABc' matches the pattern 'abc' while igonring the case.
print(re.fullmatch("pran","PrAnjal", re.IGNORECASE)) # -> Output: None. This will return 'None' because the entire string 'PrAnjal' does not match the pattern 'pran' even while ignoring the case.


# Search and Extract functions:

# 1. re.search():
# -> This function searches for the first occurrence of the pattern in the string and returns a match object if found, otherwise it returns None.
# -> Syntax: re.search(pattern, string, flags=0) [Takes same parameters as match() function]
print(re.search('abc', 'abcdef')) # Output: <re.Match object; span=(0, 3), match='abc'>. This will return a match object because 'abc' is found in the string 'abcdef'
print(re.search('abc', 'abcdef').span()) # Output: (0, 3) becasuse we are using span() funtion here
print(re.search('pranjal', 'Nonu is a very good boy')) # Output: None. This will return 'None' because 'pranjal' is not found in the string 'Nonu is a very good boy'

# 2. re.findall():
# -> This function returns a list of all the matches of the pattern in the string. 
# -> Unlike search() which stops at the first match, findall() continues to search for all matches and returns them in a list. If no matches are found, it returns an empty list.
# -> Syntax: re.findall(pattern, string, flags=0) 

print(re.findall('can', 'can you can a can as a canner cans a can?')) # Output: ['can', 'can', 'can', 'can']. This will return a list of all the matches of the pattern 'can' in the string.
print(re.findall('pranjal', 'Nonu is a very good boy')) # Output: []. This will return an empty list because 'pranjal' is not found in the string 'Nonu is a very good boy'

# Compile and Split functions:

# 1. re.compile():
# -> This function compiles a regular expression pattern into a regex object, which can be used for matching using its methods
# -> This can be useful when you need to use the same pattern multiple times, as it allows you to compile the pattern once and reuse it, which can improve performance.
# -> Syntax: re.compile(pattern, flags=0) 

pattern = re.compile('can') # This compiles the pattern 'can' into a regex object and assigns it to the variable 'pattern'.
print(pattern.findall('can you can a can as a canner cans a can?')) # Output: ['can', 'can', 'can', 'can']. This will return a list of all the matches of the pattern 'can' in the string using the compiled regex object.  

# 2. re.split():
# -> This function splits the string on a pattern and return a list of substrings. 
# -> It is similar to the split() function for string. However, re.split() allows you to split the string based on a regular expression pattern, which can be more powerful and flexible than splitting on a fixed string.
# -> Syntax: re.split(pattern, string, maxsplit=0, flags=0)

string = "apple,banana;cherry orange"
print(re.split("[;, ]+", string)) #  Output: ['apple', 'banana', 'cherry', 'orange'].  

# IMPORTANT EDGE CASE:
string2 = "apple, banana; cherry,;,; lichi"
print(re.split("[;, ]+", string2)) # Output: ['apple', 'banana', 'cherry', 'lichi']. This will split the string based on the pattern which includes comma, semicolon and space. 
# The '+' symbol indicates that one or more occurrences of the delimiters should be treated as a single delimiter, so it will split the string correctly even if there are multiple delimiters in a row.

# on the other hand had we used this:
print(re.split("[;, ]", string2)) # Output: ['apple', '', 'banana', '', 'cherry', '', '', '', 'lichi']. This will split the string based on the pattern which includes comma, semicolon and space. 
# However, since we did not use the '+' symbol, it will treat each delimiter as a separate delimiter, which can lead to empty strings in the output when there are multiple delimiters in a row.
#---------------------------------------------------------------------------------------------------------------------------------


# QUANTIFIERS: 

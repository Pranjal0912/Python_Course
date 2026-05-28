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


# QUANTIFIERS: They tell how many times a pattern should occur in the string for a match to be found.
print("QUANTIFIERS:", end = "\n\n")


# 1. '*': [Zero or more occurrences]
#  - This quantifier matches zero or more occurrences of the preceding element. 
#  - It means that the pattern can occur any number of times, including not at all.
print(re.match('(ab)*', 'abababab')) 
print(re.match('(ab)*', '')) 
# Regex quantifiers (*, +, { }) are greedy by default, meaning they try to match as much text as possible.
# However, you can make them non-greedy (or lazy) by adding a '?' after the quantifier. This tells the regex engine to match as little text as possible while still satisfying the pattern.
print(re.match('(ab)*?', 'abababab'))  # Here it will match match "" (empty string) because the '*' quantifier is made non-greedy by adding '?', so it matches as little text as possible while still satisfying the pattern '(ab)*'.
print(re.findall('(ab)*?', 'abababab')) # Because *? is lazy, it first gives an empty match, but findall then continues and also finds the next valid "ab" matches. 

print(re.findall("(ab)*", "abababab")) # Output: ['ab', ''] . # re.findall() returns captured group contents if () capturing groups are present, otherwise it returns full matches.
print(re.findall('(?:ab)*', 'abababab')) # Output: ['abababab', ''] . Here by adding '?:' we are making the group non-capturing, so re.findall() returns the full matches instead of the captured group contents

print(re.fullmatch('(ab)*', 'ab').group()) 
print(re.fullmatch('(ab)*', ''))

# 2. '+': [One or more occurrences]
#  - This quantifier matches one or more occurrences of the preceding element.
#  - It means that the pattern must occur at least once, but can occur multiple times.
import re
print(re.match('(ab)+?', 'abababab').group()) # Output: abababab. This will return a match object because the entire string 'abababab' matches the pattern '(ab)+'. The '+' quantifier requires at least one occurrence of 'ab', and since 'abababab' consists of multiple occurrences of 'ab', it matches the entire string.
print(re.fullmatch('(ab)+', 'abababab').group()) # Output: abababab. This will return a match object because the entire string 'abababab' matches the pattern '(ab)+'. The '+' quantifier requires at least one occurrence of 'ab', and since 'abababab' consists of multiple occurrences of 'ab', it matches the entire string.
print(re.fullmatch('(ab)+', '')) # Output: None. This will return 'None' because the entire string '' does not match the pattern '(ab)+'. The '+' quantifier requires at least one occurrence of 'ab', and since the string is empty, it does not satisfy this requirement.


# 3. '?': [Zero or one occurrence]
#  - This quantifier matches zero or one occurrence of the preceding element.
#  - It means that the pattern can occur either not at all or exactly once.
print(re.match('(ab)?', 'abababab')) # Output: ab. This will return a match object because 'ab' is found at the beginning of the string 'ab abc abcd'. The '?' quantifier allows for zero or one occurrence of 'ab', so it matches 'ab' at the start of the string.
print(re.match('(ab)?', '')) # Output: <re.Match object; span=(0, 0), match=''>
print(re.fullmatch('(ab)?', 'ab').group()) # Output: ab. This will return a match object because the entire string 'ab' matches the pattern '(ab)?'. The '?' quantifier allows for zero or one occurrence of 'ab', so it matches 'ab' as the entire string.
print(re.fullmatch('(ab)?', '')) # Output: <re.Match object; span=(0, 0), match=''>

# 4. '{n}': [Exactly n occurrences]
#  - This quantifier matches exactly n occurrences of the preceding element.
import re 
print(re.fullmatch('(ab){3}', 'ababab').group()) # Output: ababab. This will return a match object because the entire string 'ababab' matches the pattern '(ab){3}'. The '{n}' quantifier requires exactly 3 occurrences of 'ab', and since 'ababab' consists of exactly 3 occurrences of 'ab', it matches the entire string.
print(re.fullmatch('(ab){3}', 'abab')) # Output: None. This will return 'None' because the entire string 'abab' does not match the pattern '(ab){3}'. The '{n}' quantifier requires exactly 3 occurrences of 'ab', and since 'abab' consists of only 2 occurrences of 'ab', it does not satisfy this requirement.

# 5. '{n,}': [At least n occurrences]
#  - This quantifier matches n or more occurrences of the preceding element.
import re
print(re.fullmatch('(ab){2,}', 'ababab').group()) # Output: ababab. This will return a match object because the entire string 'ababab' matches the pattern '(ab){2,}'. The '{n,}' quantifier requires at least 2 occurrences of 'ab', and since 'ababab' consists of 3 occurrences of 'ab', it matches the entire string.
print(re.fullmatch('(ab){2,}', 'ab')) # Output: None. This will return 'None' because the entire string 'ab' does not match the pattern '(ab){2,}'. The '{n,}' quantifier requires at least 2 occurrences of 'ab', and since 'ab' consists of only 1 occurrence of 'ab', it does not satisfy this requirement.
print(re.findall('(ab){2,}', 'abab ab ab')) # Output: ['ab']. This is because re.findall() returns captured group contents if () capturing groups are present, otherwise it returns full matches. The pattern '(ab){2,}' matches sequences of 'ab' that occur at least 2 times in a row. In the string 'abab ab ab', the sequence 'abab' contains 2 occurrences of 'ab', so it matches the pattern, while the other occurrences of 'ab' do not meet the requirement of at least 2 occurrences in a row.
print(re.findall('(?:ab){2,}', 'abab ab ab')) # Output: ['abab'] This is because by adding '?:' we are making the group non-capturing, so re.findall() returns the full matches instead of the captured group contents. The pattern '(?:ab){2,}' matches sequences of 'ab' that occur at least 2 times in a row. In the string 'abab ab ab', the sequence 'abab' contains 2 occurrences of 'ab', so it matches the pattern, while the other occurrences of 'ab' do not meet the requirement of at least 2 occurrences in a row.

# 6. '{n,m}': [Between n and m occurrences]
#  - This quantifier matches between n and m occurrences of the preceding element, inclusive.
import re
print(re.fullmatch('(ab){2,4}', 'abab').group()) # Output: abab. This will return a match object because the entire string 'abab' matches the pattern '(ab){2,4}'. The '{n,m}' quantifier requires between 2 and 4 occurrences of 'ab', and since 'abab' consists of exactly 2 occurrences of 'ab', it satisfies this requirement and matches the entire string.
print(re.fullmatch('(ab){2,4}', 'ababab').group()) # Output : ababab. This will return a match object because the entire string 'ababab' matches the pattern '(ab){2,4}'. The '{n,m}' quantifier requires between 2 and 4 occurrences of 'ab', and since 'ababab' consists of exactly 3 occurrences of 'ab', it satisfies this requirement and matches the entire string.
print(re.fullmatch('(ab){2,4}', 'ab')) # Output: None. This will return 'None' because the entire string 'ab' does not match the pattern '(ab){2,4}'. The '{n,m}' quantifier requires between 2 and 4 occurrences of 'ab', and since 'ab' consists of only 1 occurrence of 'ab', it does not satisfy this requirement.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# SPECIAL CHARACTERS: They have a special meaning in regular expressions and are used to define patterns for matching strings.

# 1. '.': This character matches any single character except a newline. For example, the pattern 'a.c' would match 'abc', 'a1c', 'a-c', etc., but not 'ac' or 'abcc'.

# Lets see some combinations of the above special character with quantifiers:

# '.+': This pattern matches one or more occurrences of any character except a newline.
# ACCPETS: uppercase, lowercase, digits, special characters, spaces, etc.
# REJECTS: only a newline character '\n' because '.' does not match a newline character.
import re
print(re.fullmatch('.+', 'Hello World! 123 @#$%^&*()_+').group()) # Output: Hello World!
# One important caveat here is that if we want a patter that has '.' in it then we need to use the escape character '\' before the '.' to indicate that we want to match a literal '.' character rather than using it as a special character. For example, the pattern 'a\.c' would match 'a.c' but not 'abc' or 'a1c'.
print(re.fullmatch('a\.c', 'a.c').group()) # Output: a.c. This will return a match object because the entire string 'a.c' matches the pattern 'a\.c'. The escape character '\' allows us to match the literal '.' character, so it matches 'a.c' as the entire string.

# 2. '^': This character matches the start of a string. For example, the pattern '^abc' would match 'abc' at the beginning of a string, but not 'xabc' or 'abcc'.

# Lets see some combinations of the above special character with quantifiers:
import re
print(re.match('^ab', 'ababc')) # Output: ab. This will return a match object because 'ab' is found at the beginning of the string 'ababc'. The '^' character asserts that the match must occur at the start of the string, so it matches 'ab' at the start of the string.

# 3. '$': This character matches the end of a string. For example, the pattern 'abc$' would match 'abc' at the end of a string, but not 'abcc' or 'xabc'.

# Lets see some combinations of the above special character with quantifiers:

import re
print(re.fullmatch('.+com$', 'example.com')) # Output: example.com. This will return a match object because the entire string 'example.com' matches the pattern '.+com$'. The '.+' part matches any characters before 'com', and the '$' asserts that 'com' must be at the end of the string, so it matches 'example.com' as the entire string.
print(re.fullmatch('.+com$', 'example.com.org')) # Output: None. This will return 'None' because the entire string 'example.com.org' does not match the pattern '.+com$'. The '.+' part matches any characters before 'com', but the '$' asserts that 'com' must be at the end of the string, and since 'example.com.org' has additional characters after 'com', it does not satisfy this requirement and does not match the entire string.

# 4. '[]': This character is used to define a character class, which matches any one of the characters inside the brackets. For example, the pattern '[abc]' would match 'a', 'b', or 'c', but not 'd' or 'ab'.
#   - You can also use a hyphen '-' to specify a range of characters. For example, the pattern '[a-z]' would match any lowercase letter from 'a' to 'z'.
#   - If you want to include a number that also can be done using the same way as above.

# Lets see some combinations of the above special character with quantifiers:

# - '[a-z]': This pattern matches any single lowercase letter from 'a' to 'z'. For example, it would match 'a', 'b', 'c', etc., but not '1' or 'A'.
# - '[a-z]+': This pattern matches one or more occurrences of any lowercase letter from 'a' to 'z'. For example, it would match 'hello', 'world', 'abc', etc., but not '123' or 'Hello'.
# - '[A-Z][a-z]+': This pattern matches a string that starts with an uppercase letter followed by one or more lowercase letters. For example, it would match 'Hello', 'World', 'Abc', etc., but not 'hello' or 'HELLO'.


# 5. '[^...]': This character is used to define a negated character class, which matches any character that is NOT inside the brackets. For example, the pattern '[^abc]' would match any character except 'a', 'b', or 'c'. For example, it would match 'd', 'e', '1', etc., but not 'a', 'b', or 'c'.

# Lets see some combinations of the above special character with quantifiers:

# - '[^a-z]': This pattern matches any single character that is NOT a lowercase letter from 'a' to 'z'. For example, it would match '1', 'A', '@', etc., but not 'a', 'b', 'c', etc.
# - '[^a-z]+': This pattern matches one or more occurrences of any character that is NOT a lowercase letter from 'a' to 'z'. For example, it would match '123', 'HELLO', '@@@', etc., but not 'hello', 'world', 'abc', etc.
# - '[^A-Z][^a-z]+': This pattern matches a string that starts with a character that is NOT an uppercase letter followed by one or more characters that are NOT lowercase letters. For example, it would match '1HELLO', '@@@WORLD', etc., but not 'Hello', 'World', 'Abc', etc.    


#  6. 'R|S': This character is used to specify an alternative, which matches either the pattern 'R' or the pattern 'S'. For example, the pattern 'cat|dog' would match either 'cat' or 'dog', but not 'catdog' or 'catt'.

# Lets see some combinations of the above special character with quantifiers:

import re 
print(re.fullmatch('.+com|.+org', 'example.com')) # Output: example.com. This will return a match object because the entire string 'example.com' matches the pattern '.+com|.+org'. The pattern '.+com' matches 'example.com', and since it is one of the alternatives specified by the '|', it satisfies the pattern and matches the entire string.
print(re.fullmatch('.+com|.+org', 'example.org')) # Output: example org. This will return a match object because the entire string 'example.org' matches the pattern '.+com|.+org'. The pattern '.+org' matches 'example.org', and since it is one of the alternatives specified by the '|', it satisfies the pattern and matches the entire string.

# Now, lets write some Regular Expressions for some real life use cases:
 
# 1. Name:
# Pranjal Verma
name_regex = re.compile('[A-Z][a-z]+ [A-Z][a-z]+') # This regex pattern matches a name that consists of two words, each starting with an uppercase letter followed by one or more lowercase letters, and separated by a space. For example, it would match 'Pranjal Verma', 'John Doe', etc., but not 'pranjal verma' or 'PRANJAL VERMA'.

# 2. Variable name:
# Rules to follow: 
    # -> It must start with a letter or an underscore.
    # -> It can only contain letters, digits, and underscores.

variable_name_regex = re.compile('[a-zA-Z_][a-zA-Z0-9_]*') # This regex pattern matches a valid variable name in Python. It starts with a letter (either uppercase or lowercase) or an underscore, followed by zero or more letters, digits, or underscores. For example, it would match 'variable_name', '_myVariable', 'var123', etc., but not '123variable' or 'my-variable'.

# 3. Time:
# Rules to follow:
    # -> It should be in the format of HH:MM
    # -> The hours (HH) should be between 00 and 23.
    # -> The minutes (MM) should be between 00 and 59

time_regex = re.compile('[012][0-9]:[0-5][0-9]') # This regex pattern matches a time in the format of HH:MM. The hours (HH) can be from 00 to 23, and the minutes (MM) can be from 00 to 59. For example, it would match '00:00', '12:30', '23:59', etc., but not '24:00' or '12:60'.

# 4. Domain Name:

domain_name_regex = re.compile('[a-zA-Z0-9]+\.(com|org|net|in|edu)$') # This regex pattern matches a domain name that consists of one or more letters or digits, followed by a dot, and then one of the specified top-level domains (com, org, net, in, edu). The '$' at the end asserts that the match must occur at the end of the string. For example, it would match 'example.com', 'mywebsite.org', 'test123.net', etc., but not 'example' or 'example.xyz'.


# ESCAPE SEQUENCES: They are used to match special characters in a string.
# -> Few escpace sequences are as follows:
# 1. '\d'(DIGITS): This escape sequence matches any digit character (0-9). For example, the pattern '\d' would match '1', '2', '3', etc in a string, but not 'a' or '@'.
# 2. '\D'(NON-DIGITS): This escape sequence matches any non-digit character. For example, the pattern '\D' would match 'a', '@', ' ', etc in a string, but not '1', '2', '3', etc.
# 3. '\w'(WORD CHARACTERS): This escape sequence matches any word character, which includes letters (both uppercase and lowercase), digits, and underscores. For example, the pattern '\w' would match 'a', 'Z', '0', '_', etc in a string, but not '@' or ' '.
# 4. '\W'(NON-WORD CHARACTERS): This escape sequence matches any non-word character. For example, the pattern '\W' would match '@', ' ', etc in a string, but not 'a', 'Z', '0', '_', etc.
# 5. '\s'(WHITESPACE): This escape sequence matches any whitespace character, which includes spaces, tabs, and newlines. For example, the pattern '\s' would match ' ', '\t'(tab), '\n'(newline), '\f'(line feed) etc in a string, but not 'a' or '@'.
# 6. '\S'(NON-WHITESPACE): This escape sequence matches any non-whitespace character. For example, the pattern '\S' would match 'a', '@', '0', etc in a string, but not ' ', '\t', '\n', etc.   
# 7. '\A'(START OF STRING): This escape sequence matches the start of a string. For example, the pattern '\A' would match the beginning of a string, but not anywhere else.
# 8. '\Z'(END OF STRING): This escape sequence matches the end of a string. For example, the pattern '\Z' would match the end of a string, but not anywhere else.

# Some examples of patterns :- 

# Date: DD/MM/YYYY

date_regex = re.compile('\d{2}/\d{2}/\d{4}')

# Password:
# Rules to follow:
    # -> It should be at least 8 characters long.

password_regex = re.compile('.{8,}') # This regex pattern matches a password that is at least 8 characters long. The '.' matches any character, and the '{8,}' quantifier specifies that there should be at least 8 occurrences of any character. For example, it would match 'password', '12345678', 'P@ssw0rd!', etc., but not 'pass' or '1234567'.

# Email:
# Example: my.id1@gmail.com
email_regex = re.compile('\w+\.?\w+@\w+\.(com|net|in|org|edu)$')
# Escape Sequences in Python:
# They are non-printable characters that are used to represent certain special characters in a string. They are typically used to include characters that are difficult to type directly, such as newlines, tabs, or quotes.

# Common Escape Sequences:
# \ - Backslash --> It is used to ignore new lines in a string. When a backslash is followed by a newline, it allows the string to continue on the next line without breaking.
print("hello\
world")  # Output: helloworld (the backslash allows the string to continue on the next line without breaking)
# \n - Newline
print("Hello\nWorld")  # Output: Hello (newline) World
# \t - Tab --> Leaves a tab space between Hello and World
print("Hello\tWorld")  # Output: Hello (tab) World
# \\ - Backslash -> if you want to include a backslash or a quote in a string, you can use the backslash as an escape character to indicate that the following character should be treated as a literal character rather than a special character.
print("Hello\\World")  # Output: Hello\World
# \' - Single Quote
print("Hello\'World")  # Output: Hello'World
# \" - Double Quote     
print("Valid\"So")  # Output: Valid"So
# \r - Carriage Return --> after printing "Valid", the cursor returns to the beginning of the line, and "So" overwrites "Valid". 
print("Valid\rSo")  # Output: Solid (So overwrites Va in Valid)
# \b - Backspace
print("Hello\bWorld")  # Output: HellWorld (removes 'o')
# \f - line Feed --> after printing "Hello", the cursor moves to the next line but in the same column as the last character of "Hello". Then "World" is printed starting from that position.
print("Hello\fWorld")  # Output: Hello (line feed) World
# \v - Vertical Tab 
print("Hello\vWorld")  # Output: Hello (vertical tab) World
# \o - Octal Value
print("Hello\101World")  # Output: HelloAWorld (A is the octal value 101)
# \x - Hexadecimal Value
print("Hello\x41World")  # Output: HelloAWorld (A is the hexadecimal value 41)
# \u - Unicode Character
print("Hello\u0041World")  # Output: HelloAWorld (A is the Unicode character with code point 0x41)
# \a - Bell/Alert
print("Hello\aWorld")  # Output: Hello (bell sound) World
# \0 - Null Character
print("Hello\0World")  # Output: Hello (null character) World
# \N{name} - Named Unicode Character
print("Hello\N{Smiling Face with Open Mouth}World")  # Output: Hello😊World 



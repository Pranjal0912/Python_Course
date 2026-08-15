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
print("Valid\rSo")  # Output: Solid ('So' overwrites 'Va' in 'Valid')
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

# ---------------------------------------------------------------- EXTRA --------------------------------------------------------------------------------

# ANSI Escape Sequences:
# ANSI escape sequences are special character sequences used to control terminal behavior such as colors, cursor movement, screen clearing, and text formatting.
# They usually start with ESC (\x1b) followed by '[' and one or more parameters.

# ANSI Cursor Movement Sequences:
# ANSI escape sequences can move the terminal cursor without printing spaces or new lines.
# Most cursor commands start with ESC (\x1b) followed by '['. We can also use '\033' or '\u001b' or simply 'char(27)' too.

# \x1b[nA - Cursor Up
# Moves the cursor up by n lines.
print("\x1b[3A")  # Moves cursor up 3 lines

# \x1b[nB - Cursor Down
# Moves the cursor down by n lines.
print("\x1b[2B")  # Moves cursor down 2 lines

# \x1b[nC - Cursor Forward (Right)
# Moves the cursor right by n columns.
print("\x1b[5C")  # Moves cursor right 5 columns

# \x1b[nD - Cursor Backward (Left)
# Moves the cursor left by n columns.
print("\x1b[4D")  # Moves cursor left 4 columns

# \x1b[nE - Cursor Next Line
# Moves cursor to the beginning of the nth line below.
print("\x1b[2E")  # Moves to start of line 2 lines down

# \x1b[nF - Cursor Previous Line
# Moves cursor to the beginning of the nth line above.
print("\x1b[2F")  # Moves to start of line 2 lines up

# \x1b[nG - Cursor Horizontal Absolute
# Moves cursor to column n on the current line.
print("\x1b[10G")  # Moves cursor to column 10

# \x1b[row;colH - Cursor Position
# Moves cursor to a specific row and column.
print("\x1b[5;10HHello")  # Row 5, Column 10

# \x1b[row;colf - Cursor Position (same as H)
print("\x1b[5;10fHello")  # Row 5, Column 10

# \x1b[H - Cursor Home
# Moves cursor to the top-left corner (row 1, column 1).
print("\x1b[H")

# \r - Carriage Return (Not ANSI but commonly used)
# Moves cursor to the beginning of the current line.
print("Loading...\rDone")
# Output: Doneing... (Done overwrites the beginning)

# \x1b[s - Save Cursor Position
# Saves the current cursor position.
print("\x1b[s")

# \x1b[u - Restore Cursor Position
# Returns cursor to the previously saved position.
print("\x1b[u")

# \x1b[?25l - Hide Cursor
print("\x1b[?25l")

# \x1b[?25h - Show Cursor
print("\x1b[?25h")

# Example: Updating text in place
import time

for i in range(5):
    print(f"\rProgress: {i}", end="") # what is it doing ? : The '\r' moves the cursor back to the beginning of the line, and 'end=""' prevents adding a new line after each print. This allows us to update the same line with new content, creating a dynamic effect in the terminal.
    time.sleep(1)

# Output updates on the same line:
# Progress: 0
# Progress: 1
# ...
# Progress: 4


# ANSI Text Formatting and Colors:
# ANSI escape sequences can change text color, background color, and text style in the terminal.
# Most formatting sequences start with ESC (\x1b) followed by '['.

# \x1b[0m - Reset Formatting
# Resets all colors and styles back to terminal defaults.
print("\x1b[0mNormal Text")

# Text Styles:

# \x1b[1m - Bold Text
print("\x1b[1mBold Text\x1b[0m")

# \x1b[2m - Dim/Faint Text
print("\x1b[2mDim Text\x1b[0m")

# \x1b[3m - Italic Text (may not be supported everywhere)
print("\x1b[3mItalic Text\x1b[0m")

# \x1b[4m - Underlined Text
print("\x1b[4mUnderlined Text\x1b[0m")

# \x1b[7m - Reverse Video
# Swaps foreground and background colors.
print("\x1b[7mReversed Text\x1b[0m")

# Standard Foreground (Text) Colors:

# 30 Black
# 31 Red
# 32 Green
# 33 Yellow
# 34 Blue
# 35 Magenta
# 36 Cyan
# 37 White

print("\x1b[31mRed Text\x1b[0m")
print("\x1b[32mGreen Text\x1b[0m")
print("\x1b[34mBlue Text\x1b[0m")

# Bright Foreground Colors:

# 90 Bright Black (Gray)
# 91 Bright Red
# 92 Bright Green
# 93 Bright Yellow
# 94 Bright Blue
# 95 Bright Magenta
# 96 Bright Cyan
# 97 Bright White

print("\x1b[91mBright Red\x1b[0m")
print("\x1b[96mBright Cyan\x1b[0m")

# Standard Background Colors:

# 40 Black
# 41 Red
# 42 Green
# 43 Yellow
# 44 Blue
# 45 Magenta
# 46 Cyan
# 47 White

print("\x1b[41mRed Background\x1b[0m")
print("\x1b[42mGreen Background\x1b[0m")

# Bright Background Colors:

# 100 Bright Black
# 101 Bright Red
# 102 Bright Green
# 103 Bright Yellow
# 104 Bright Blue
# 105 Bright Magenta
# 106 Bright Cyan
# 107 Bright White

print("\x1b[103mBright Yellow Background\x1b[0m")

# Combining Styles:

# Format:
# \x1b[style;color;backgroundm

print("\x1b[1;32mBold Green Text\x1b[0m")
print("\x1b[4;31mUnderlined Red Text\x1b[0m")

# 256 Color Mode:

# Format:
# \x1b[38;5;<n>m --> Text Color
# \x1b[48;5;<n>m --> Background Color

print("\x1b[38;5;208mOrange Text\x1b[0m")
print("\x1b[48;5;51mColored Background\x1b[0m")

# True Color (24-bit RGB):

# Text Color:
# \x1b[38;2;R;G;Bm

print("\x1b[38;2;255;165;0mOrange Text\x1b[0m")

# Background Color:
# \x1b[48;2;R;G;Bm

print("\x1b[48;2;0;255;0mGreen Background\x1b[0m")

# Example:

print("\x1b[1;97;41m ERROR \x1b[0m Something went wrong")
print("\x1b[1;30;42m SUCCESS \x1b[0m Operation completed")
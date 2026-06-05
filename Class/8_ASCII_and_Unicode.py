# Some Information about ASCII and Unicode:

# ASCII (American Standard Code for Information Interchange) is a character encoding standard that uses 7 bits to represent characters. It includes 128 characters, which consist of:
# A-Z: 65-90
# a-z: 97-122
# 0-9: 48-57
# control characters: 0-31 and 127
# Note:- There are 128 characters in the ASCII character set, which includes 95 printable characters and 33 non-printable control characters.
# 128 = 2^7, which means that each character in the ASCII character set can be represented using 7 bits. The 8th bit is often used for error checking or to represent extended ASCII characters.
# Hence a 'char' in python is of 1 byte (8 bits) and can represent 256 different characters (0-255), which includes the standard ASCII characters (0-127) and the extended ASCII characters (128-255).
print(ord('A'))  # Output: 65 --> This function returns the ASCII value of the character 'A'
print(chr(65))  # Output: 'A' --> This function returns the character corresponding to the ASCII value 65


# Unicode is a character encoding standard that uses a variable number of bytes to represent characters.
# It includes a much larger set of characters than ASCII, including characters from many different languages and scripts.
# Unicode can represent over 1 million characters, and it uses different encoding forms such as UTF-8, UTF-16, and UTF-32 to represent these characters in memory.
# In Python, a Unicode character can take up to 4 bytes of memonry, depending on the encoding used. The most common encoding for Unicode characters in Python is UTF-8, which uses 1 to 4 bytes to represent characters. 
# For example, ASCII characters (0-127) are represented using 1 byte in UTF-8, while characters outside the ASCII range may require 2, 3, or 4 bytes.

a = "\u03b1" # This is the Unicode character for the Greek letter alpha (α)
print(a)  # Output: α
b = "\U0001F600" # This is the Unicode character for the grinning face emoji (😀)
print(b)  # Output: 😀
c = "\u00A9" # This is the Unicode character for the copyright symbol (©)
print(c)  # Output: ©   
d = "\u03b1\u03b2\u03b3" # This is a string of three Unicode characters representing the Greek letters alpha (α), beta (β), and gamma (γ)
print(d)  # Output: αβγ
# a can also be represented like this in unicode:
a = "\x41" 
print(a)  # Output: A

# Unicode are divided into different planes, each plane can contain up to 65,536 characters. 
# The first plane (Plane 0) is called the Basic Multilingual Plane (BMP) and contains most of the commonly used characters.
# The other planes (Planes 1-16) are called Supplementary Planes and contain less commonly used characters, such as historical scripts, mathematical symbols, and emoji. 
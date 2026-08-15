# BASE CONVERSION IN PYTHON 

a=10 #integer literal
print(bin(a)) # Output: 0b1010 --> This is the binary representation of the integer 10. The '0b' prefix indicates that the number is in binary format.
print(type(bin(a))) # Output: <class 'str'> --> The 'bin()' function returns a string representation of the binary number.
print(oct(a)) # Output: 0o12 --> This is the octal representation of the integer 10. The '0o' prefix indicates that the number is in octal format.
print(type(oct(a))) # Output: <class 'str'> --> The 'oct()' function returns a string representation of the octal number.
print(hex(a)) # Output: 0xa --> This is the hexadecimal representation of the integer 10. The '0x' prefix indicates that the number is in hexadecimal format.
print(type(hex(a))) # Output: <class 'str'> --> The 'hex()' function returns a string representation of the hexadecimal number.
b = 0b1111 #binary literal
print(int(b)) # Output: 15 --> This converts the binary literal 0b1111 to its decimal equivalent. The 'int()' function is used to convert the binary literal to an integer. The binary number 1111 is equal to 15 in decimal.
print(type (int(b))) # Output: <class 'int'> --> The 'int()' function returns an integer representation of the binary literal.
c=True
print(bin(c)) # Output: 0b1 --> This is the binary representation of the boolean value True. In Python, True is equivalent to 1.
print(oct(a)) # Output: 0o12 --> This is the octal representation of the integer 10.
print(hex(a)) # Output: 0xa --> This is the hexadecimal representation of the integer 10.
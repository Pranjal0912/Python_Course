# BUILT IN NUMERIC FUNCTIONS IN PYTHON

# x + y --> sum of x and y
print(10 + 5) #--> 15, since the sum of 10 and 5 is 15
# x - y --> difference of x and y
print(10 - 5) #--> 5, since the difference of 10 and 5 is 5
# x * y --> product of x and y  
print(10 * 5) #--> 50, since the product of 10 and 5 is 50
# x / y --> quotient of x and y (floating-point division)
print(11 / 5) #--> 2.2, since the quotient of 11 and 5 is 2.2 (floating-point division)
# x // y --> quotient of x and y (floor division)
print(11 // 5) #--> 2, since the quotient of 11 and 5 is 2 (floor division)
# x % y --> remainder of x divided by y 
print(11 % 5) #--> 1, since the remainder of 11 divided by 5 is 1
# x ** y --> x raised to the power of y (exponentiation)
print(2 ** 3) #--> 8, since 2 raised to the power of 3 is 8
# -x --> negation of x (unary minus)
print(-5) #--> -5, since the negation of 5 is -5
# abs(x) --> absolute value of x
print(abs(-5)) #--> 5, since the absolute value of -5 is 5
# round(x) --> rounds x to the nearest integer
print(round(2.5)) #--> 2, since 2.5 rounds to the nearest integer which is 2
# round(x, n) --> rounds x to n decimal places
print(round(2.678, 2)) #--> 2.68, since 2.678 rounds to 2 decimal places which is 2.68
# pow(x, y) --> x raised to the power of y (exponentiation)
print(pow(2, 3)) #--> 8, since 2 raised to the power of 3 is 8
# divmod(x, y) --> returns a tuple containing the quotient and remainder of x divided by y
print(divmod(11, 5)) #--> (2, 1), since the quotient of 11 divided by 5 is 2 and the remainder is 1
# max(x1, x2, ..., xn) --> returns the largest of the given arguments
print(max(1, 5, 3)) #--> 5, since 5 is the largest of the given arguments (1, 5, 3)
# min(x1, x2, ..., xn) --> returns the smallest of the given arguments  
print(min(1, 5, 3)) #--> 1, since 1 is the smallest of the given arguments (1, 5, 3)
# sum(iterable) --> returns the sum of all items in the given iterable (like list, tuple, etc.)
print(sum([1, 2, 3, 4, 5])) #--> 15, since the sum of all items in the list [1, 2, 3, 4, 5] is 15

# Conversion functions in Python:
# int(x) --> converts x to an integer
print(int(2.5)) #--> 2, since converting 2.5 to an integer gives 2 (truncation)
# float(x) --> converts x to a floating-point number
print(float(2)) #--> 2.0, since converting 2 to a floating-point number gives 2.0
# complex(x) --> converts x to a complex number with real part x and imaginary part 0
print(complex(2)) #--> (2+0j), since converting 2 to a complex number gives (2+0j) where 2 is the real part and 0 is the imaginary part
# complex(x, y) --> converts x and y to a complex number with real part x and imaginary part y
print(complex(2, 3)) #--> (2+3j), since converting 2 and 3 to a complex number gives (2+3j) where 2 is the real part and 3 is the imaginary part
# conjugate(x) --> returns the complex conjugate of x (if x is a complex number)
print(complex(2, 3).conjugate()) #--> (2-3j), since the complex conjugate of (2+3j) is (2-3j)   

# Note: The above functions are built-in functions in Python and can be used directly without importing any module.

# Math module functions in Python:
# 'import math' is used to import the math module which contains various mathematical functions and constants.
import math
# math.sqrt(x) --> returns the square root of x in floating-point format
print(math.sqrt(16)) #--> 4.0, since the square root of 16 is 4.0
# math.pow(x, y) --> returns x raised to the power of y in floating-point format
print(math.pow(2, 3)) #--> 8.0, since 2 raised to the power of 3 is 8.0
# math.ceil(x) --> returns the smallest integer greater than or equal to x (ceiling function)
print(math.ceil(2.3)) #--> 3, since the smallest integer greater than or equal to 2.3 is 3
# math.floor(x) --> returns the largest integer less than or equal to x (floor function)
print(math.floor(2.7)) #--> 2, since the largest integer less than or equal to 2.7 is 2
# math.factorial(n) --> returns the factorial of n (n!) where n is a non-negative integer
print(math.factorial(5)) #--> 120, since the factorial of 5 (5!) is 120
# math.gcd(x, y) --> returns the greatest common divisor of x and y
print(math.gcd(12, 8)) #--> 4, since the greatest common divisor of 12 and 8 is 4   
# math.pi --> returns the value of pi (π) which is approximately 3.14159
print(math.pi) #--> 3.141592653589793, since the value of pi (π) is approximately 3.14159
# math.e --> returns the value of Euler's number (e) which is approximately 2.71828
print(math.e) #--> 2.718281828459045, since the value of Euler's number (e) is approximately 2.71828
# math.trunc(x) --> returns the integer part of x (truncation function)
print(math.trunc(2.9)) #--> 2, since the integer part of 2.9 is 2
# math.exp(x) --> returns e raised to the power of x (exponential function)
print(math.exp(1)) #--> 2.718281828459045, since e raised to the power of 1 is approximately 2.71828


# Bitwise operators in Python:
# For using bitwise operators, we can use the built-in functions or operators directly on integers.
# x & y --> bitwise AND of x and y
print(5 & 3) #--> 1, since the bitwise AND of 5 (0101 in binary) and 3 (0011 in binary) is 1 (0001 in binary)
# x | y --> bitwise OR of x and y
print(5 | 3) #--> 7, since the bitwise OR of 5 (0101 in binary) and 3 (0011 in binary) is 7 (0111 in binary)
# x ^ y --> bitwise XOR of x and y
print(5 ^ 3) #--> 6, since the bitwise XOR of 5 (0101 in binary) and 3 (0011 in binary) is 6 (0110 in binary)
# ~x --> bitwise NOT of x
print(~5) #--> -6, since the bitwise NOT of 5 (0101 in binary) is -6 (1010 in binary, two's complement)
# x << n --> left shift of x by n bits
print(5 << 1) #--> 10, since left shifting 5 (0101 in binary) by 1 bit gives 10 (1010 in binary)
# x >> n --> right shift of x by n bits    
print(5 >> 1) #--> 2, since right shifting 5 (0101 in binary) by 1 bit gives 2 (0010 in binary)
# Note: The above bitwise operators work on the binary representation of integers and can be used for various applications like bit manipulation, masking, etc.
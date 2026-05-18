# Python also alows C-style string formatting using the % operator. This is an older style of string formatting, but it is still widely used in Python 2 and is supported in Python 3.
# -> string: %s
# -> integer: %i
# -> float: %f
# -> decimal: %d
# -> ocatal: %o
# -> hexadecimal: %x
# -> exponential: %e
item = "Memory"
size = 32 
price = 11.75

# Now suppose i want to print a string that says "Cost of 32GB Memory is $11.75" 
print("Cost of", size, "GB", item, "is $", price) # This is the normal way of printing multiple variables in a string using the print function.
# But in this there is are spaces between the string part and variables.

# So this is where C-style string formatting comes in handy. We can use the % operator to format the string and insert the variables in the desired format.
print("Cost of %iGB %s is $%f" % (size, item, price)) # Cost of 32GB Memory is $11.75
# In the above example, %d is used for the integer variable 'size', %s is used for the string variable 'item', and %.2f is used for the float variable 'price' to format it to 2 decimal places. The variables are passed as a tuple after the % operator.

print(f'Cost of {size}GB {item} is ${price}') # -> Now this is the modern way of string formatting using f-strings (formatted string literals) which is more readable and easier to use than C-style string formatting. It was introduced in Python 3.6 and is now the recommended way to format strings in Python.


#----Example-2----------
data = 200
print('%x' % (data)) # c8 -> This will print the hexadecimal representation of the integer 200 which is 'c8'.
print('%o' % (data)) # 310 -> This will print the octal representation of the integer 200 which is '310'.


#----Example-3----------
data1 = 24
print('data is %10d' % (data1)) # data is         24 -> This will print the integer 24 right-aligned in a field of width 10. The number 10 specifies the minimum width of the field, and since 24 has only 2 digits, it will be padded with 8 spaces on the left to make it a total of 10 characters wide.
print('data is %-10d' % (data1)) # data is 24         -> This will print the integer 24 left-aligned in a field of width 10. The '-' sign before the width specifier indicates left alignment, so the number 24 will be printed first, followed by 8 spaces to fill the total width of 10 characters.
print('data is %010d' % (data1)) # data is 0000000024 -> This will print the integer 24 zero-padded in a field of width 10. The '0' before the width specifier indicates that the field should be padded with zeros instead of spaces, so the number 24 will be printed with 8 leading zeros to fill the total width of 10 characters.
print('data is %2.4f' % (data1)) # data is 24.0000 -> This will print the float representation of the integer 24 with a total width of 2 characters and 4 digits after the decimal point. The '2' before the decimal point specifies the minimum width of the field, and the '.4' after the decimal point specifies that 4 digits should be printed after the decimal point. Since 24 has only 2 digits, it will be printed as '24.0000' to meet the specified formatting requirements. 
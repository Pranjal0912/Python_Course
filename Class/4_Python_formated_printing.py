# Formated printing in python:

# Blueprint: print('{index:fw.p con}'format(variable))
# WHERE: 
#  - index: The position of the variable in the format method. It is optional and can be omitted if the variables are in the same order as they appear in the format string.
#  - f: It is a flag that can be used to specify the alignment of the variable in the output. It can be '<' for left-alignment, '>' for right-alignment, and '^' for center-alignment.
#  - w: It is the width of the field in which the variable will be printed. (Optional)
#  - p: It is the precision for floating-point numbers. (Optional)
#  - con: It is the type of conversion to be applied to the variable. It can be 's' for string, 'd' for decimal integer, 'f' for floating-point number, 
#   'o' for octal, 'x' for hexadecimal, ',' for thousand separato, '_' for underscore as thousand separator, and '%' for percentage. (Optional)

# Lets learn using examples:

item = "Memory"
size = 32 
price = 11.75

# Our Aim is to Print this :- 32Gb Memory costs $11.75
print("{}Gb {} costs ${}".format(size, item, price)) # 32Gb Memory costs $11.75 -> This is the basic way of using the format method to format a string. The curly braces {} are placeholders for the variables that we want to insert into the string. The variables are passed as arguments to the format method in the same order as they appear in the string.
print("{2}Gb {0} costs ${1}".format(item, price, size)) # 32Gb Memory costs $11.75 -> In this example, we have used the index to specify the position of the variables in the format method. The variable 'size' is at index 2, 'item' is at index 0, and 'price' is at index 1. So we can rearrange the order of the variables in the output by changing their index in the format string.

# Another usecase:
data = 100
print("start {0:15} end".format(data)) # start           100 end -> In this example, we have used the width specifier to specify the width of the field in which the variable 'data' will be printed. The number 15 specifies that the field should be at least 15 characters wide. Since '100' has only 3 characters, it will be padded with 12 spaces on the left to make it a total of 15 characters wide.
# Now the above result would be right-aligned by default but we can change the alignment using the flag. For example:
print("start {0:<15} end".format(data)) # start 100            end -> This will left-align the variable 'data' in the field of width 15. The '-' sign before the width specifier indicates left alignment, so the number '100' will be printed first, followed by 12 spaces to fill the total width of 15 characters.
print("start {0:>15} end".format(data)) # start           100 end -> This will right-align the variable 'data' in the field of width 15. The '>' sign before the width specifier indicates right alignment, so the number '100' will be printed with 12 spaces on the left to fill the total width of 15 characters.
print("start {0:^15} end".format(data)) # start      100       end -> This will center-align the variable 'data' in the field of width 15. The '^' sign before the width specifier indicates center alignment, so the number '100' will be printed with 6 spaces on the left and 6 spaces on the right to fill the total width of 15 characters.

# Conversion types:
# - Ocatal coversion:
print("start {0:10o} end".format(data)) # start    144 end -> This will print the octal representation of the integer 'data' which is '144' in a field of width 10. The 'o' conversion type is used to specify that the variable should be formatted as an octal number. 
# Lets try ',' separator now:
print("start {0:^15,} end".format(1234567)) # start    1,234,567    end -> This will print the integer '12345667' with a comma as a thousand separator in a field of width 15.
# Lets try, 'e' conversion type now:
print("start {0:15.4e} end".format(12.34565634)) # start     1.2346e+01 end -> This will print the floating-point number in scientific notation with 4 digits after the decimal point in a field of width 15.
# lets try, 'd' conversion type now: 
data2 = 1243.45689
print("start {:.2f} end".format(data2))


# There's another method of writing a fromated string in python:
item = "Memory"
size = 32 
price = 11.75
print(f'{size}Gb {item:^10} costs ${price:.2f}') # 32Gb   Memory   costs $11.75 -> This is the modern way of string formatting using f-strings (formatted string literals) which is more readable and easier to use than the format method.
# The syntax for f-strings is similar to the format method, but instead of using curly braces {} as placeholders, we can directly include the variables in the string by prefixing it with 'f' and enclosing the variables in curly braces {}.
# The same formatting options that we used in the format method can also be used in f-strings. In this example, we have used the width specifier to center-align the variable 'item' in a field of width 10 and the precision specifier to format the variable 'price' to 2 decimal places.

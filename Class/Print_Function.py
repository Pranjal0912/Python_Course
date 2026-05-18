# Print funtions -> Takes an object and returns a string representation of that object.


print("Hello World") # String
print(10) # Integer
print(3.14) # Float
print([1, 2, 3]) # List
# The print function can take multiple arguments and will print them separated by a space by default.
print("pranjal", 23, 3.14) # Multiple arguments: pranjal 23 3.14
# Now by default its taking space as a separator but can we change it to something else like a comma or a hyphen.?
# -> Yes we can change the separator using the 'sep' parameter of the print function.

# The real signature of the print function is:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# Parameters:
#  - *objects: Any number of objects to be printed. They will be converted to strings and printed. --> Positional argument
#  - sep: The separator between the objects. Default is a space. --> Keyword argument
#  - end: The string appended after the last object. Default is a newline. --> Keyword argument
#  - file: A file-like object (stream); defaults to the current sys.stdout. MEANING: The file to which the output is sent. By default, it is the standard output (console). -- Keyword argument
#  - flush: Whether to forcibly flush the stream. Default is False. --> Keyword argument

import sys # Importing the sys module to use sys.stdout for the file parameter in the print function.
print("pranjal", "verma", sep="*", end="!!!", file = sys.stdout, flush=False) # pranjal*verma!!!
print("This starts from the same line now ") # This starts from the same line now  because we have set the end parameter to "!!!" instead of the default "\n" which is a newline character.
                                            # So instead of moving to the next line after printing, it stays on the same line and prints "This starts from the same line now " right after "pranjal*verma!!!".
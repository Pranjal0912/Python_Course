# Python functions are generally used/called in 3 ways:

# 1. obj.method()
# -> Methods: functions that belong to a specific class/object.
# -> Example: string.upper(), list.append()

# 2. function(obj)
# -> General/global built-in functions.
# -> Work on many data types and are directly available in Python.
# -> Example: len(), type(), print(), input(), sorted()

# 3. module.function(obj)
# -> Functions stored inside modules/libraries.
# -> Modules help organize related functionality.
# -> Example: math.sqrt(), re.search(), random.randint()

# Key Difference:
# -> Methods belong to objects/classes.
# -> Built-in functions belong to Python's global built-in namespace.
# -> Module functions belong to imported modules/libraries.

# --------------------------------------------------------------------------------------------------------

# A Quick recap on how to import a library in Python:
#  1. import re: This statement imports the entire 're' module, allowing you to access all of its functions and classes using the 're' prefix before a '.' and the function name. For example, you would use 're.search()' to call the 'search' function from the 're' module.
#  2. 'from re import *' or 'from re import {some specific function or class}': This statement imports specific functions or classes from the're' module directly into the current namespace. 
#  3. 'import re as regex' or 'import re as {some alias}': This statement imports the 're' module and gives it an alias (in this case, 'regex'). You can then use 'regex' instead of 're' to access the functions and classes in the module. For example, you would use 'regex.search()' to call the 'search' function from the 're' module.

# ---------------------------------------------------------------------------------------------------------

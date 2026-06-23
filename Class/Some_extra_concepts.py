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

# PYTHON ECOSYSTEM 
#
# 1. Built-in Functions
# These are available immediately without import.
# Examples:
#   - print()
#   - len()
#   - range()
#   - sum()
#
# Built-in function = no import needed.
#
# --------------------------------------------------

# 2. Built-in Modules
# These come with Python interpreter but require import.
# Examples:
#   - math
#   - sys
#   - time
#   - itertools
#
# Example:
#   - import math
#   - math.sqrt(16)
#
# Built-in module = import needed, but already present in Python.
#
# --------------------------------------------------

# 3. Standard Library (stdlib)
# Standard Library = everything officially shipped with Python.
#
# Includes:
#   -> Pure Python modules:
#       - json, pathlib, re, collections
#
#   -> Built-in compiled modules:
#       - math, sys, time
#
# Important:
#   Built-in modules are a subset of stdlib.
#
# --------------------------------------------------

# 4. Module
# A module is simply one Python file.
#
# Example:
#   - calculator.py
#
# Rule:
#   One .py file = one module
#
# Example usage:
#   import calculator
#
# --------------------------------------------------

# 5. Package
# A package is a folder containing modules.
#
# Example:
#
#   utils/
#       __init__.py
#       math_utils.py
#       string_utils.py
#
# Here:
#   -  utils = package
#   -  math_utils = module
#
# Rule:
#   Package = collection of modules
#
# --------------------------------------------------

# 6. Library
# Library is an informal term for reusable code.
#
# A library can contain:
#   - one module
#   - one package
#   - many packages
#
# Examples:
#   - numpy
#   - pandas
#   - pytorch
#
# Library = umbrella term
#
# --------------------------------------------------

# 7. Third-party Packages
# These do NOT come with Python.
# They must be installed manually.
#
# Examples:
#   - numpy
#   - pandas
#   - requests
#   - django
#
# Installed using:
#   pip install pandas
# or
#   uv add pandas
#
# Third-party package = external package
#
# --------------------------------------------------

# 8. pip / uv
# These are package managers / installers.
#
# pip:
#   -> Traditional Python package installer
#
# uv:
#   -> Modern faster alternative
#   -> Also handles venvs, lockfiles, dependencies
#
# --------------------------------------------------

# FULL HIERARCHY
#
# Python Ecosystem
# |
# |-- Built-in Functions
# |     |-- print
# |     |-- len
# |     |-- range
# |
# |-- Standard Library
# |     |-- Built-in Modules
# |     |     |-- math
# |     |     |-- sys
# |     |
# |     |-- Pure Python Modules
# |           |-- json
# |           |-- os
# |           |-- pathlib
# |
# |-- Third-party Libraries / Packages
#       |-- numpy
#       |-- pandas
#       |-- pytorch
#
# --------------------------------------------------

# VOCAB SUMMARY
#
# module   = one Python file
# package  = folder of modules
# library  = reusable code collection
# built-in = comes with interpreter
# stdlib   = official Python shipped code
# third-party = installed via pip / uv

# ---------------------------------------------------------------------------------------------------------

# MUTABLE VS IMMUTABLE + `is` vs `==`

# 1. Assignment DOES NOT create a copy
# -----------------------------------
# In Python:
#
#   b = a
#
# does NOT create a new object.
# It only makes variable b point to the SAME object as a.
#
# Example:
#
#   list1 = [1, 2, 3]
#   list2 = list1
#
# Both list1 and list2 point to the same list object in memory.


# 2. `is` checks identity (same memory object)
# --------------------------------------------
# `is` checks whether two variables refer to the exact same object.
#
# Example:
#
#   list1 = [1,2,3]
#   list2 = list1
#   print(list1 is list2)
#
# Output:
#   True
#
# Because both variables point to the same object.


# 3. `==` checks value equality
# -----------------------------
# `==` checks whether values/content are equal.
#
# Example:
#
#   a = [1,2,3]
#   b = [1,2,3]
#
#   print(a == b)   # True (same content)
#   print(a is b)   # False (different objects)


# 4. Mutable objects
# ------------------
# Mutable objects can be modified in-place.
#
# Examples of mutable types:
#   list
#   dict
#   set
#
# Example:
#
#   list1 = [1,2,3]
#   list2 = list1
#   list2.append(4)
#
# Since both variables point to the same object,
# changing one affects the other.
#
# list1 becomes:
#   [1,2,3,4]


# 5. Immutable objects
# --------------------
# Immutable objects cannot be changed after creation.
#
# Examples:
#   int
#   float
#   str
#   tuple
#   bool
#
# If you "modify" an immutable object,
# Python creates a NEW object instead.
#
# Example:
#
#   s1 = "pranjal"
#   s2 = s1
#
#   s2 += "!"
#
# Python does NOT modify the old string.
# Instead it creates a new string:
#
#   "pranjal!"
#
# Now:
#   s1 -> "pranjal"
#   s2 -> "pranjal!"
#
# So:
#   s1 is s2
#
# becomes False.


# 6. Important rule
# -----------------
# Assignment NEVER copies.
#
#   b = a
#
# always means:
#   b now refers to the same object as a.
#
# Mutable vs Immutable only affects:
#   - Can object be changed in-place?
#   - Or must Python create a new object?


# 7. String special case (interning)
# ----------------------------------
# Python sometimes reuses identical strings for optimization.
#
# Example:
#
#   a = "hello"
#   b = "hello"
#
#   print(a is b)
#
# This may print True because Python may reuse the same string object.
#
# This optimization is called STRING INTERNING.
#
# Because of this, never use `is` to compare strings.


# 8. Best practice
# ----------------
# Use:
#   ==  -> compare values
#
# Use:
#   is  -> compare identity / memory object
#
# Common valid use of `is`:
#
#   if x is None:
#       ...
#
# Avoid:
#
#   if str1 is str2:
#       ...
#
# Instead use:
#
#   if str1 == str2:
#       ...



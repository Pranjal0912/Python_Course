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

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# A Quick recap on how to import a library in Python:
#  1. import re: This statement imports the entire 're' module, allowing you to access all of its functions and classes using the 're' prefix before a '.' and the function name. For example, you would use 're.search()' to call the 'search' function from the 're' module.
#  2. 'from re import *' or 'from re import {some specific function or class}': This statement imports specific functions or classes from the're' module directly into the current namespace. 
#  3. 'import re as regex' or 'import re as {some alias}': This statement imports the 're' module and gives it an alias (in this case, 'regex'). You can then use 'regex' instead of 're' to access the functions and classes in the module. For example, you would use 'regex.search()' to call the 'search' function from the 're' module.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# PYTHON ECOSYSTEM 
#
# 1. Built-in Functions
# These are available immediately without import.
# Examples:
#   - print()
#   - len()
#   - range()
#   - sum()

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

# Example:
#   - import math
#   - math.sqrt(16)

# Built-in module = import needed, but already present in Python.

# --------------------------------------------------

# 3. Standard Library (stdlib)
# Standard Library = everything officially shipped with Python.

# Includes:
#   -> Pure Python modules:
#       - json, pathlib, re, collections
#
#   -> Built-in compiled modules:
#       - math, sys, time

# Important:
#   Built-in modules are a subset of stdlib.
#
# --------------------------------------------------

# 4. Module
# A module is simply one Python file.

# Example:
#   - calculator.py

# Rule:
#   One .py file = one module

# Example usage:
#   import calculator

# --------------------------------------------------

# 5. Package
# A package is a folder containing modules.

# Example:

#   utils/
#       __init__.py
#       math_utils.py
#       string_utils.py

# Here:
#   -  utils = package
#   -  math_utils = module

# Rule:
#   Package = collection of modules

# --------------------------------------------------

# 6. Library
# Library is an informal term for reusable code.

# A library can contain:
#   - one module
#   - one package
#   - many packages

# Examples:
#   - numpy
#   - pandas
#   - pytorch

# Library = umbrella term

# --------------------------------------------------

# 7. Third-party Packages
# These do NOT come with Python.
# They must be installed manually.

# Examples:
#   - numpy
#   - pandas
#   - requests
#   - django

# Installed using:
#   pip install pandas
# or
#   uv add pandas

# Third-party package = external package
#
# --------------------------------------------------

# 8. pip / uv
# These are package managers / installers.

# pip:
#   -> Traditional Python package installer

# uv:
#   -> Modern faster alternative
#   -> Also handles venvs, lockfiles, dependencies

# --------------------------------------------------

# FULL HIERARCHY

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

# --------------------------------------------------

# VOCAB SUMMARY

# module   = one Python file
# package  = folder of modules
# library  = reusable code collection
# built-in = comes with interpreter
# stdlib   = official Python shipped code
# third-party = installed via pip / uv

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ============================================================
# NOTES: MUTABLE VS IMMUTABLE + `is` vs `==`
# ============================================================


# ============================================================
# 1. ASSIGNMENT DOES NOT CREATE A COPY
# ============================================================

# In Python:
#
#     b = a
#
# does NOT create a new object.
# It only makes variable b point to the SAME object as a.
#
# In simple words:
# Assignment creates another reference/name for the same object.

list1 = [1, 2, 3]
list2 = list1

print("list1:", list1)
print("list2:", list2)

print("list1 is list2:", list1 is list2)

# Both list1 and list2 point to the same list object in memory.


# ============================================================
# 2. `is` CHECKS IDENTITY
# ============================================================

# `is` checks whether two variables refer to the exact same object.
# It asks:
#
#     "Are these two names pointing to the same memory object?"
#
# It does NOT mainly care about whether the values look equal.

list1 = [1, 2, 3]
list2 = list1

print("list1 is list2:", list1 is list2)

# Output:
# True
#
# Why?
# Because list2 was assigned to list1.
# So both variables refer to the exact same list object.


# ============================================================
# 3. `==` CHECKS VALUE EQUALITY
# ============================================================

# `==` checks whether the values/content are equal.
# It asks:
#
#     "Do these two objects have the same value/content?"
#
# Two objects can be equal in value but still be different objects.

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)
print("a is b:", a is b)

# Output:
# a == b: True
# a is b: False
#
# Why?
# The two lists contain the same values,
# but they are two different list objects in memory.


# ============================================================
# 4. MUTABLE OBJECTS
# ============================================================

# Mutable objects can be modified in-place.
#
# Common mutable types:
#     list
#     dict
#     set
#
# "In-place" means the same object is changed,
# instead of creating a new object.

list1 = [1, 2, 3]
list2 = list1

list2.append(4)

print("list1 after list2.append(4):", list1)
print("list2 after list2.append(4):", list2)

print("list1 is list2:", list1 is list2)

# Output:
# list1 after list2.append(4): [1, 2, 3, 4]
# list2 after list2.append(4): [1, 2, 3, 4]
#
# Why?
# list1 and list2 point to the same list object.
# Since lists are mutable, append() modifies that same object in-place.


# ============================================================
# 5. MUTABLE EXAMPLE WITH DICTIONARY
# ============================================================

# Dictionaries are mutable.
# If two variables point to the same dictionary,
# changing one affects the other.

dict1 = {"name": "Pranjal", "age": 22}
dict2 = dict1

dict2["age"] = 23

print("dict1:", dict1)
print("dict2:", dict2)

print("dict1 is dict2:", dict1 is dict2)

# Both variables refer to the same dictionary object.


# ============================================================
# 6. MUTABLE EXAMPLE WITH SET
# ============================================================

# Sets are also mutable.
# Methods like add() change the set in-place.

set1 = {1, 2, 3}
set2 = set1

set2.add(4)

print("set1:", set1)
print("set2:", set2)

print("set1 is set2:", set1 is set2)


# ============================================================
# 7. IMMUTABLE OBJECTS
# ============================================================

# Immutable objects cannot be changed after creation.
#
# Common immutable types:
#     int
#     float
#     str
#     tuple
#     bool
#
# If you "modify" an immutable object,
# Python does NOT change the original object.
# Instead, Python creates a NEW object.

s1 = "pranjal"
s2 = s1

print("Before modification:")
print("s1:", s1)
print("s2:", s2)
print("s1 is s2:", s1 is s2)

s2 += "!"

print("After modification:")
print("s1:", s1)
print("s2:", s2)
print("s1 is s2:", s1 is s2)

# Explanation:
#
# Initially:
#     s1 -> "pranjal"
#     s2 -> "pranjal"
#
# After:
#     s2 += "!"
#
# Python creates a new string:
#     "pranjal!"
#
# Now:
#     s1 -> "pranjal"
#     s2 -> "pranjal!"
#
# The old string was not modified.


# ============================================================
# 8. IMMUTABLE EXAMPLE WITH INTEGER
# ============================================================

# Integers are immutable.
# Doing x += 1 creates a new integer object
# and makes x point to that new object.

x = 10
y = x

print("Before:")
print("x:", x)
print("y:", y)
print("x is y:", x is y)

y += 1

print("After:")
print("x:", x)
print("y:", y)
print("x is y:", x is y)

# x remains 10.
# y now points to a different integer object with value 11.


# ============================================================
# 9. IMMUTABLE EXAMPLE WITH TUPLE
# ============================================================

# Tuples are immutable.
# You cannot change an item inside a tuple.

t = (1, 2, 3)

try:
    t[0] = 100
except TypeError as error:
    print("Error:", error)

# Output:
# TypeError: 'tuple' object does not support item assignment


# ============================================================
# 10. IMPORTANT RULE
# ============================================================

# Assignment NEVER copies the object.
#
#     b = a
#
# always means:
#
#     b now refers to the same object as a.
#
# Mutable vs immutable only affects this:
#
#     Can the object itself be changed in-place?
#     Or must Python create a new object?


# ============================================================
# 11. COPYING A MUTABLE OBJECT
# ============================================================

# If you actually want a separate copy of a list,
# assignment is not enough.

original = [1, 2, 3]

same_reference = original
actual_copy = original.copy()

same_reference.append(4)
actual_copy.append(5)

print("original:", original)
print("same_reference:", same_reference)
print("actual_copy:", actual_copy)

print("original is same_reference:", original is same_reference)
print("original is actual_copy:", original is actual_copy)

# Explanation:
#
# same_reference = original
# means both names point to the same object.
#
# actual_copy = original.copy()
# creates a new list object with the same content.


# ============================================================
# 12. SHALLOW COPY WARNING
# ============================================================

# .copy() creates a shallow copy.
# This means the outer list is copied,
# but nested mutable objects inside it may still be shared.

nested1 = [[1, 2], [3, 4]]
nested2 = nested1.copy()

nested2[0].append(99)

print("nested1:", nested1)
print("nested2:", nested2)

print("nested1 is nested2:", nested1 is nested2)
print("nested1[0] is nested2[0]:", nested1[0] is nested2[0])

# The outer lists are different objects.
# But the inner lists are still shared.


# ============================================================
# 13. DEEP COPY
# ============================================================

# If you want to copy nested mutable objects too,
# use deepcopy from the copy module.

import copy

nested1 = [[1, 2], [3, 4]]
nested2 = copy.deepcopy(nested1)

nested2[0].append(99)

print("nested1:", nested1)
print("nested2:", nested2)

print("nested1 is nested2:", nested1 is nested2)
print("nested1[0] is nested2[0]:", nested1[0] is nested2[0])

# Now the outer list and inner lists are separate objects.


# ============================================================
# 14. STRING SPECIAL CASE: INTERNING
# ============================================================

# Python sometimes reuses identical strings for optimization.
# This is called string interning.
#
# Because of string interning, this may be True:

a = "hello"
b = "hello"

print("a == b:", a == b)
print("a is b:", a is b)

# a == b is True because both strings have the same value.
# a is b may also be True because Python may reuse the same string object.
#
# But do NOT rely on this behavior for normal string comparison.


# ============================================================
# 15. DO NOT USE `is` TO COMPARE STRINGS
# ============================================================

# Even if `is` sometimes appears to work with strings,
# it is not the correct way to compare string values.

str1 = "hello"
str2 = "".join(["he", "llo"])

print("str1:", str1)
print("str2:", str2)

print("str1 == str2:", str1 == str2)
print("str1 is str2:", str1 is str2)

# str1 == str2 checks value equality.
# str1 is str2 checks whether they are the exact same object.
#
# For strings, you almost always want ==.


# ============================================================
# 16. BEST PRACTICE
# ============================================================

# Use == when you want to compare values.
#
# Example:
#     if name == "Pranjal":
#         ...
#
# Use is when you want to compare identity.
#
# Most common valid use of is:
#     if x is None:
#         ...

x = None

if x is None:
    print("x is None")

# This is correct because None is a singleton object.
# There is only one None object in Python.


# ============================================================
# 17. AVOID THIS
# ============================================================

# Avoid using `is` for value comparison.

name1 = "Pranjal"
name2 = "Pran" + "jal"

# Bad style:
print("Bad style result:", name1 is name2)

# Good style:
print("Good style result:", name1 == name2)

# Even if the bad style prints True sometimes,
# it is conceptually wrong for value comparison.


# ============================================================
# 18. FINAL SUMMARY
# ============================================================

# Assignment:
#     b = a
#     Does not copy.
#     It makes b refer to the same object as a.

# `is`:
#     Checks identity.
#     Means: same object in memory?

# `==`:
#     Checks value equality.
#     Means: same content/value?

# Mutable objects:
#     Can be changed in-place.
#     Examples: list, dict, set.

# Immutable objects:
#     Cannot be changed in-place.
#     Examples: int, float, str, tuple, bool.

# Important:
#     Mutability is about whether the object can change.
#     Assignment is about names/references.
#     These are related concepts, but they are not the same thing.

# Golden line:
#     Use == for value comparison.
#     Use is for identity comparison.
#     Use is mainly when comparing with None.


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------
# ITERATOR VS ITERABLE
# ---------------------

# ============================================================
# NOTES: ITERATORS, ITERABLES, range(), zip(), AND CONSUMPTION
# ============================================================


# ============================================================
# 1. WHAT IS AN ITERATOR?
# ============================================================

# An iterator is an object that gives values one at a time.
# It remembers its current position.
# You get the next value from it using next().

nums = [10, 20, 30]

it = iter(nums)

print("First next:", next(it))
print("Second next:", next(it))
print("Third next:", next(it))

# After all values are consumed, calling next() again raises StopIteration.

try:
    print(next(it))
except StopIteration:
    print("Iterator is exhausted. No more values left.")


# ============================================================
# ITERABLE VS ITERATOR
# ============================================================

# An iterable is something that can produce an iterator.
# Examples: list, tuple, string, dict, set, range.
# You can use 'iter()' on an iterable to get an iterator.

nums = [1, 2, 3]

nums_iterator = iter(nums)

print("nums is:", nums)
print("nums_iterator is:", nums_iterator)

# A list is iterable, but it is not itself an iterator.

print("Is iter(nums) same object as nums?", iter(nums) is nums)

# But an iterator is usually its own iterator.

print("Is iter(nums_iterator) same object as nums_iterator?", iter(nums_iterator) is nums_iterator)


# ============================================================
# A 'for loop' internally uses iter() and next()
# ============================================================

# This:

for x in [100, 200, 300]:
    print("for loop value:", x)

# Is roughly similar to this:

my_list = [100, 200, 300]
my_iterator = iter(my_list)

while True:
    try:
        x = next(my_iterator)
        print("manual loop value:", x)
    except StopIteration:
        break


# ============================================================
# 2. HOW IS range DIFFERENT FROM zip?
# ============================================================

# range() returns a range object.
# A range object is iterable, but it is not itself an iterator.
# It can create a fresh iterator every time you loop over it.

r = range(5)

print("range object:", r)
print("Is range object its own iterator?", iter(r) is r)

print("First list(r):", list(r))
print("Second list(r):", list(r))

# Both list(r) calls work because range is reusable.
# Each time list(r) is called, Python creates a new iterator from the range.


# zip() returns a zip object.
# A zip object is already an iterator.
# It gives paired values one by one.

names = ["A", "B", "C"]
marks = [90, 80, 70]

z = zip(names, marks)

print("zip object:", z)
print("Is zip object its own iterator?", iter(z) is z)

print("First list(z):", list(z))
print("Second list(z):", list(z))

# The second list(z) is empty because zip got consumed the first time.
# zip is an iterator, so once it moves forward, it does not reset automatically.


# ============================================================
# range creates numbers lazily
# ============================================================

# range(5) does not store [0, 1, 2, 3, 4] as a full list in memory.
# It represents the pattern: start from 0, go up to 5, step by 1.

r = range(5)

print("range(5):", r)
print("list(range(5)):", list(r))


# ============================================================
# zip creates pairs lazily
# ============================================================

# zip does not create all pairs immediately.
# It stores references to the iterators of the given iterables.
# Then it gives one tuple at a time.

names = ["Pranjal", "Tiya", "Messi"]
scores = [95, 99, 100]

z = zip(names, scores)

print("First pair:", next(z))
print("Second pair:", next(z))
print("Third pair:", next(z))

try:
    print(next(z))
except StopIteration:
    print("zip object is exhausted.")


# ============================================================
# zip stops at the shortest iterable
# ============================================================

a = [1, 2, 3, 4]
b = ["x", "y"]

z = zip(a, b)

print("zip stops at shortest iterable:", list(z))


# ============================================================
# 3. SHOW HOW ITERATOR GETS CONSUMED WHILE ITERABLE DOESN'T
# ============================================================

# Example with iterable: list

nums = [10, 20, 30]

print("First list iteration:")
for x in nums:
    print(x)

print("Second list iteration:")
for x in nums:
    print(x)

# The list did not get consumed.
# Why?
# Because list is an iterable, not an iterator.
# Each for loop creates a fresh iterator from the list.


# Example with iterable: range

r = range(3)

print("First range iteration:")
for x in r:
    print(x)

print("Second range iteration:")
for x in r:
    print(x)

# The range did not get consumed.
# range is iterable and reusable.


# Example with iterator: zip

z = zip([1, 2, 3], ["a", "b", "c"])

print("First zip iteration:")
for pair in z:
    print(pair)

print("Second zip iteration:")
for pair in z:
    print(pair)

# The second zip loop prints nothing.
# Why?
# Because zip is an iterator and it was consumed in the first loop.


# Example with iterator made from a list

nums = [7, 8, 9]

it = iter(nums)

print("First iterator loop:")
for x in it:
    print(x)

print("Second iterator loop:")
for x in it:
    print(x)

# The second iterator loop prints nothing.
# The iterator object has already reached the end.


# ============================================================
# IMPORTANT SUMMARY
# ============================================================

# Iterable:
# Something that can give you an iterator.
# Examples: list, tuple, string, dict, set, range.

# Iterator:
# Something that gives values one by one using next().
# It remembers where it is.
# Once it is exhausted, it does not automatically restart.

# range:
# Iterable, reusable, not directly consumed.

# zip:
# Iterator, one-time-use, gets consumed.

# Golden line:
# Every iterator is iterable, but every iterable is not necessarily an iterator.
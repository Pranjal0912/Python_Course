# TUPLE :

# - A Tuple is a collection of ordered, immutable elements.
# - Tuples are similar to lists, but they cannot be modified after creation.
# - They are defined using parentheses () and can contain elements of different data types.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CREATING TUPLES:

t1 = (1, 2, 2, 4, 5) # A tuple of integers (can have duplicate values)
t2 = ('apple', 'banana', 'cherry') # A tuple of strings
t3 = (1, 'apple', 3.5, True) # A tuple with mixed data types
t4 = (1,2,[1,2,3],(1,2,3)) # A tuple with a list and another tuple as elements
t5 = () # An empty tuple

t5 = (1,) # A tuple with a single element (note the comma is necessary because otherwise it would be considered as an integer)
# Example to show the importance of comma in single element tuple:
a = (10)
print(type(a)) # This will print <class 'int'> because without the comma it is considered as an integer, not a tuple.
b = (10,)
print(type(b)) # This will print <class 'tuple'> because of the comma it is considered as a tuple. 

# Just like for creating a list from an iterable there is a function called list() similarly for creating a tuple from an iterable there is a function called tuple().
t1 = tuple([1, 2, 3, 4, 5]) # Creating a tuple from a list

# Another way to create a tuple is like this :
t2 = 1, 2, 3, 4, 5 # This is also a tuple of integers (without parentheses)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ACCESSING ELEMENTS IN A TUPLE:

# You can access elements in a tuple using indexing, just like lists.
# Indexing starts from 0 for the first element, 1 for the second element, and so on.
# Negative indexing is also allowed, where -1 refers to the last element, -2 to the second last, and so on.

t = (1, 2, 3, 4, 5)
print(t[0])  # Output: 1
print(t[1])  # Output: 2
print(t[-1]) # Output: 5
print(t[-2]) # Output: 4

# Since tuples are immutable, you cannot change the value of an element in a tuple. For example, t[0] = 10 will raise an error.
t[0] = 10 # This will raise a TypeError because tuples are immutable.
print(t) # Output: (1, 2, 3, 4, 5) - The tuple remains unchanged.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# TUPLE COMPREHENSIONS:
# Just like list comprehensions, there are also tuple comprehensions:

t = (x+1 for x in range(10)) # This will create a generator object, not a tuple. To create a tuple from this generator, we need to unpack it using "*":
t1 = (*(x+1 for x in range(10)), )# This will create a tuple with values from 1 to 10. Now it will also have a comma as well 

# Instead of using unpacking, we can also use the tuple() function to create a tuple from the generator:
t2 = tuple(x+1 for x in range(10)) # This will also create a tuple with values from 1 to 10.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# INDEXING AND SLICING:
# Just like lists, you can also use indexing and slicing on tuples to access specific elements or sub-tuples. The syntax is the same as for lists.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# TUPLE OPERATIONS:
# You can perform various operations on tuples, such as concatenation, repetition, and membership testing. Essentially, you can use the same operators that you use for lists.
# Along with this we have 2 operations that are exclusive to tuples only like unpacking and packing of tuples.

# 1. Concatenation: You can concatenate two or more tuples using the + operator.
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2) # Output: (1, 2, 3, 4, 5, 6)
# 2. Repetition: You can repeat a tuple a certain number of times using the * operator.
t = (1, 2, 3)
print(t * 3) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
# 3. Membership Testing: You can check if an element is present in a tuple using the in operator.
t = (1, 2, 3)
print(2 in t) # Output: True
print(4 in t) # Output: False

# 4. Packing: If you asssing mulitple values ( in one line seperated by commas) to a single variable, then all the values will be packed into a tuple and the variable will become a tuple.
t = 1, 2, 3, 4, 5 # This will create a tuple with values (1, 2, 3, 4, 5)
# 5. Unpacking: You can unpack the values of a tuple into separate variables using the * operator
t = (1, 2, 3, 4, 5)
x, y, z, e, f = t # Here x will be 1, y will be 2, z will be 3, e will be 4, and f will be 5.
print(x, y, z, e, f) # Output: 1 2 3 4 5
a, b, *c = t # Here a will be 1, b will be 2 and c will be [3, 4, 5] (a list)
print(a, b, c) # Output: 1 2 [3, 4, 5]

# Suppose we did like this:
t = (1, 2, 3, 4, 5)
a, b = t # This will raise a ValueError because there are more values in the tuple than variables to unpack into.
# So unpacking will only work if the number of variables on the left side of the assignment matches the number of elements in the tuple, or if you use the * operator to capture multiple values into a list.


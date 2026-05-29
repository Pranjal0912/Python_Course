# List in Python
#1. A list is a collection which is ordered and changeable. In Python, lists are written with square brackets '[]'.
List1 = [1,2,3,4,5]
print(List1)
#2. List can contain different data types
List2 = [1, "Hello", 3.14, True]
print(List2)
#3. List can also contain other lists (nested list)
List3 = [1, [2, 3], 4]
print(List3)

#--------------------------------------------------------------------------------------------------------------------------------

# Creation of a list
#1. Using square brackets
my_list = [1, 2, 3, 4, 5]
# 2. Using the list() constructor: list(iterable)
my_list2 = list((1, 2, 3, 4, 5))
# OR
my_list3 = list("abcde")
# OR
my_list4 = list(range(1, 6))
# OR
My_list5 = list([1, 2, 3, 4, 5])

# The list() constructor can take any iterable (like tuples, string, list itself etc) and convert it into a list.
# ->Now why does range work? 
# Because range() returns an iterable sequence of numbers, and list() can convert that sequence into a list.

print(my_list2)
print(my_list3)
print(my_list4)
print(My_list5)

#--------------------------------------------------------------------------------------------------------------------------------
# How list is created inside the memory?

# When a list is created in Python:-
# 1. Memory Allocation: Python allocates a block of memory to store the list. The size of this block is determined by the number of elements in the list and the type of elements it contains.
# 2. Reference Counting: Python uses reference counting to manage memory. When a list is created, a reference to that list is stored in a variable. If multiple variables reference the same list, they all point to the same memory location.
# 3. Garbage Collection: When a list is no longer referenced by any variable, Python's garbage collector will automatically free the memory allocated for that list, making it available for other objects.

#--------------------------------------------------------------------------------------------------------------------------------
# How to traverse a list?

# 1. Using a for loop
items = [1, 2, 3, 4, 5]
for item in items:
    print(item)# This means that for each item in the list 'items', the loop will execute the print statement, printing the current item to the console.

# 2. Using a while loop
items = [1, 2, 3, 4, 5]
i = 0
while i < len(items):
    print(items[i]) # This means that while the index 'i' is less than the length of the list 'items', the loop will execute the print statement, printing the item at index 'i' to the console. After each iteration, 'i' is incremented by 1, allowing the loop to traverse through all items in the list.
    i += 1

#--------------------------------------------------------------------------------------------------------------------------------
# What is heterogeneous list?
# A heterogeneous list is a list that contains elements of different data types. In Python, lists can hold a mix of data types, including integers, strings, floats, booleans, and even other lists. This allows for greater flexibility when working with data.
heterogeneous_list = [1, "Hello", 3.14, True, [1, 2, 3]]
print(heterogeneous_list)
# Thats how its different from 'Array' data type in other programming languages like C, C++, Java etc where all elements in an array must be of the same data type. 
# How this works:

            # L1
        # ┌─────┬─────┬────────┬──────┬────────┐
# Index → |  0  │  1  │   2    │  3   │   4    │
        # ├─────┼─────┼────────┼──────┼────────┤
# Value → │  7  │ 3.2 │ "John" │ True │ 5+6j   │
        # └─────┴─────┴────────┴──────┴────────┘

#--------------------------------------------------------------------------------------------------------------------------------
# How list is mutable in Python?
# A list is mutable in Python, which means that you can change its content after it has been created. 
# You can modify, add, or remove elements from a list after it has been created.
my_list = [1, 2, 3]
# Modifying an element
my_list[0] = 10 
print(my_list) # Output: [10, 2, 3]
# Adding an element
my_list.append(4)   
print(my_list) # Output: [10, 2, 3, 4]
# Removing an element
my_list.remove(2)   
print(my_list) # Output: [10, 3, 4]

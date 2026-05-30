# LIST IN PYTHON
#1. A list is a collection which is ordered and changeable. In Python, lists are written with square brackets '[]'.
List1 = [1,2,3,4,5]
print(List1)
#2. List can contain different data types
List2 = [1, "Hello", 3.14, True]
print(List2)
#3. List can also contain other lists (nested list)
List3 = [1, [2, 3], 4]
print(List3)

print(len(List3)) # Output: 3 because [2,3] is one elemnet of the list
# NOTE:- len() function can also be used for list infact it can be used for any iterable in python 
#--------------------------------------------------------------------------------------------------------------------------------

# CREATION OF LIST IN PYTHON
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
# HOW LIST IS STORED INSIDE THE MEMORY?

# When a list is created in Python:-
# 1. Memory Allocation: Python allocates a block of memory to store the list. The size of this block is determined by the number of elements in the list and the type of elements it contains.
# 2. Reference Counting: Python uses reference counting to manage memory. When a list is created, a reference to that list is stored in a variable. If multiple variables reference the same list, they all point to the same memory location.
# 3. Garbage Collection: When a list is no longer referenced by any variable, Python's garbage collector will automatically free the memory allocated for that list, making it available for other objects.

#--------------------------------------------------------------------------------------------------------------------------------
# HOW TO TRAVERSE A LIST IN PYTHON?

# 1. Using a for each loop
items = [1, 2, 3, 4, 5]
for item in items:
    print(item)# This means that for each item in the list 'items', the loop will execute the print statement, printing the current item to the console.

# 2. Using a for loop 
items = [1, 2, 3, 4, 5]
for i in range(len(items)):
    print(items[i]) # This means 'i' will take values from 0 to len(items)-1 acting as index to the list 

# 3. Using a while loop
items = [1, 2, 3, 4, 5]
i = 0
while i < len(items):
    print(items[i]) # This means that while the index 'i' is less than the length of the list 'items', the loop will execute the print statement, printing the item at index 'i' to the console. After each iteration, 'i' is incremented by 1, allowing the loop to traverse through all items in the list.
    i += 1

#--------------------------------------------------------------------------------------------------------------------------------
# WHAT DOES HETEROGENEOUS NATURE OF LIST MEAN?

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
# HOW LIST IS MUTABLE IN PYTHON?

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


#--------------------------------------------------------------------------------------------------------------------------------
# INDEXING AND SLICING IN A LIST

# For reading the data:

l1 = [10, 20, 30, 40, 50]
# Indexing (Read)
print(l1[3]) # Output: 40
x = l1[0] # so we can also store the value of an index in a variable and use it later in the program

# Slicing (Read)
# Syntax: list[start:stop:step]
print(l1[1:4]) # Output: [20, 30, 40] # This is exclusive of the stop index and inlusive of the start index. Similar to how we used this on string objects.

# For writing the data:

l2= [1,2,3,4,5]

# Indexing (Write)
# Modifying an element (suppose i want to modify this value "4" to "10")
l2[3] = 10
print(l2)

# Now remember in python a list can have a list as its element, so lets try and modify the vale of an element to list.

l2[4] = [1,45,5]
print(l2) # Output: [1, 2, 3, 10, [1, 45, 5]]

# Slicing (Write)

# basic syntax: 

# 1. list[start:stop] = [new_values] ( when only 'start' and 'stop' are given, we can give as many new values as we want and they will be inserted in place of the old values )
list1 = [1, 2, 3, 4, 5]
list1[0:0]=[10,20] # This means that we are inserting the values '10' and '20' at the index '0' (at the very start of the list).
print(list1) # Output: [10, 20, 1, 2, 3, 4, 5]
list_x = [1, 2, 3, 4, 5]
list_x[2:2]=[30,40] # This means that we are inserting the values '30' and '40' at the index '2' (between the 2nd and 3rd element of the list).
print(list_x) # Output: [1, 2, 30, 40, 3, 4, 5]
list2= [1, 2, 3, 4, 5]
list2[5:5]= [30,40] # This means that we are inserting the values '30' and '40' at the index '5' (at the very end of the list)
# Now for the end of the list, any start, stop value should be > the last index of the list, so in this case the last index is 4 so we wrote 5:5
# list2[6:6] = [30,40] # This will also work because 6 is also > the last index of the list which is 4
print(list2) # Output: [1, 2, 3, 4, 5, 30, 40]

# Now lets see how to insert someting between the list with different start and stop values
list3 = [1, 2, 3, 4, 5]
list3[1:4]= [30,40,50,60] #  Now here [1:4] means, the values at index 1 to index 3 will be removed and in their place the new values will be inserted i.e [30,40,50,60]
print(list3) # Output: [1, 30, 40, 50, 60, 5] 

# 2. list[start:stop:step] = [New_values] ( when 'start', 'stop' and 'step' are given, the number of new values should be equal to the number of old values that will be removed. )
list4 = [1, 2, 3, 4, 5]
list4[::2] = [10, 11,12] # This means that the values at index 0,2 and 4 will be replaced by the new values at 10,11 and 12 respectively.
print(list4) # Output: [10, 2, 11, 4, 12]
list5 = [1, 2, 3, 4, 5]
list5[::-1] = [10, 11, 12, 13, 14] # This means that the values at index 4,3,2,1 and 0 will be replaced by the new values in the reverse order only like 10 will replace 5,11 will replace 4 and so on.
print(list5) # Output: [14, 13, 12, 11, 10]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list[1:9:2] = [10, 11, 12, 13] # This means that the values at index 1,3,5 and 7 will be replaced by the new values at 10,11,12 and 13 respectively.
print(list)
#--------------------------------------------------------------------------------------------------------------------------------

# OPERATIONS ON LIST

# 1. Concatenation: We can concatenate two lists using the '+' operator.

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l2, id(l2))
l3 = l1 + l2
print(l3) # Output: [1, 2, 3, 4, 5, 6]


# Key thing to note here is : '+' and '+=' work differently 
# when we do 12 += l1, it will modify the orignal list l2 and add the elements of l1 to it
# but when we do l2 = l2 + l1, it will create a new list object and and the variabel l2 will now point to the new list object and the old list object will be garbage collected by python.
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
# Lets first check the id of the object that variable l2 is pointing to before the concatenation is performed:
print(l2, "Address_id: ", id((l2)))
# Now lets perform concatenation using '+' operator:
l2 = l2 + l1
print(l2, "Address_id: ", id((l2))) # Now you can see that the address_id of l2 has changed after the concatenation is performed using '+' operator 
# which means that a new list object has been created and l2 is now pointing to the new list object. 

# Now lets perform the same procedure with the '+=' operator:
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
print(l2, "Address_id: ", id((l2))) 
# Lets concatenate using "+=" 

l2 += l1
print(l2, "Address_id: ", id((l2))) 

# Now you can see that the address_id of l2 has not changed after the concatenation is performed using '+=' operator
# which means that the original list object that l2 was pointing to has been modified and no new list object has been created.

# **NOTE**:- This only happened because list are mutable in python, had it been anyother data type which is immutable in python like a string, or an int or a tuple etc
# the it would have created a new object in the memory irrespective of whether we used '+' or '+=' operator for concatenation.
# This same idea applies with any operation on a mutable type coupeld with the assignment operator, for example if we do *= with a list, then also it will modify the orignal list and will not create a new list object as compared to a simple '*'.

# Also list ype + int/float/str type will lead to a TypeError
l1 = [1, 2, 3]
print(l1+"pranjal") # TypeError: can only concatenate list (not "str") to list
print(l1+5) # TypeError: can only concatenate list (not "int")
print(l1+5.5) # TypeError: can only concatenate list (not "float") to list


# 2. Repetition: We can repeat a list a certain number of times using the '*' operator.

l1 = [1, 2, 3]
l2 = l1 * 3
print(l2) # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Repetition operator on a list is not defined with a float or a string, so it will lead to a TypeError
print(l1*2.5) # TypeError: can't multiply sequence by non-int of type 'float'
print(l1*"pranjal") # TypeError: can't multiply sequence by non-int of type 'str'


# 3. Membership: We can check if an element is present in a list using the 'in' keyword.('in'and 'not in' )
l1 = [1, 2, 3, 4, 5]
print(3 in l1) # Output: True
print(6 in l1) # Output: False

# Lets try this with a nested list
l2 = [[1, 2], [3, 4], 5]

print([1, 2] in l2) # Output: True
print([3, 4] in l2) # Output: True
print(5 in l2) # Output: True
print(3 in l2) # Output: False, because 3 is not an element of the list l2, it is an element of the list [3,4] which is an element of l2. So we have to check for the presence of the list [3,4] in l2 and not for the presence of 3 in l2.
print([3] in l2) # Output: False, because [3] is not an element of the list l2, it is an element of the list [3,4] which is an element of l2. So we have to check for the presence of the list [3,4] in l2 and not for the presence of [3] in l2.


# 4. Comparison: 

#-> We can compare two lists using the '==' operator. Two lists are considered equal if they have the same elements in the same order and with the same frequency.

print([1, 2, 3] == [1, 2, 3]) # Output: True
# It internally compares element by element and if all the elements are same in both the list and in the same order and with the same frequency then it will return True otherwise it wil return False
print([1, 2, 3] == [3, 2, 1]) # Output: False, because the order of the elements is different in both the lists.

# -> We can also compare two list using the >, <, >= and <= operators. When we compare two lists using these operators, Python compares the elements of the lists in a lexicographical manner (similar to how strings are compared).

# How it works:
# - It start comparing element by element and if there is any mismatch in th element then it will consider the greater string as one with the greater element at the first point of mismatch
# - If there is no mismatch in the elements and all the elements are same in both the lists then it will consider the greater string as one with more number of elements.

print([1, 2, 3] > [1, 2, 2]) # Output: True, because the first element that is different in both the lists is 3 and 2 and since 3 > 2, it will return True.
print([1, 2, 3] < [1, 2, 4]) # Output: True, because the first element that is different in both the lists is 3 and 4 and since 3 < 4, it will return True.
print([1,2,3,4] < [2]) # Output: True, because the first element that is different in both the lists is 1 and 2 and since 1 < 2, it will return True.
print([1,2,3] < [1,2,3,4]) # Output: True, because there is no mismatch in the elements of both the lists and all the elements are same in both the lists but the second list has more number of elements than the first list so it will return True.

# -> We can also compare two lists using the 'is' operator. The 'is' operator checks for identity, meaning it checks if both operands refer to the same object in memory. Two lists can be equal (have the same elements) but not identical (not the same object in memory).
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2) # Output: True, because both lists have the same elements in the same order and with the same frequency.
print(list1 is list2) # Output: False, because list1 and list2 are two different objects in memory, even though they have the same content. They are not identical, they are just equal in terms of their content.  
l1 = [1, 2, 3]
l2 = l1
print(l1 == l2) # Output: True, because both l1 and l2 have the same elements in the same order and with the same frequency.
print(l1 is l2) # Output: True, because l1 and l2 are pointing to the same object in memory. They are identical as well as equal.

#--------------------------------------------------------------------------------------------------------------------------------


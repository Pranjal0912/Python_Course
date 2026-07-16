# DICTIONARY :  

# - A dictionary is a collection of key-value pairs. 
# - Each key is unique and maps to a specific value.
# - Dictionaries are mutable, meaning you can change their content (add, remove, or modify key-value pairs) after they are created.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CREATING DICTIONARIES:

d1 = {1:"One", 2:"Two", 3:"Three", 4:"Four"} # A dictionary with integer keys and string values (Keys will always be unique, values can be duplicate)

#                                               ┌───┬────────┐  
#                                   d1{}------->│ 1 │  "One" │ 
#                                               ├───┼────────┤
#                                               │ 2 │  "Two" │
#                                               ├───┼────────┤
#                                               │ 3 │ "Three │
#                                               ├───┼────────┤
#                                               │ 4 │ "Four" │
#                                               └───┴────────┘
print(d1) # Output: {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
d2 = {} # An empty dictionary (This will not create an empty set, it will create an empty dictionary)

d3 = {1:4.5, 23.4:True, 3+4j:"pranjal"}
print(d3) # Output: {1: 4.5, 23.4: True, (3+4j): 'pranjal'} -> A dictionary with mixed data types as keys and values is also completely valid. The keys can be of any immutable data type (int, float, string, tuple, etc.) and the values can be of any data type (int, float, string, list, tuple, set, dictionary, etc.).

# ---------------------------------------------------------------------------------
# Question-> But why should the keys be immutable? 
# ---------------------------------------------------------------------------------
# ==> for knowing the answer to that we must first know how the dictionary interanally works. 


# A Python dictionary is implemented using a HASH TABLE.
#
# The basic lookup algorithm is:
#
#       key
#        │
#        ▼                              - 1. Internally, a dictionary uses a hash table to store its key-value pairs. 
#    hash(key)                          - 2. When you add key-value pairs to a dictionary, each key is hashed using a hash function like so : hash(key)-> this will return a hash value for the key which is an integer. 
#        │                              - 3. The hash value is then used to determine the index of the bucket where the key-value pair will be stored in the hash table.    
#        ▼                                          
#   bucket/index
#        │
#        ▼
# Compare actual key (if needed)
#        │
#        ▼
#     Return value
#
# Since Python can jump directly to the required bucket using the hash,dictionary lookup is O(1) on average.

# -----------------------------------------------------------------------------
# Why must keys be immutable?
# -----------------------------------------------------------------------------

# -> The hash of a key MUST remain constant for its entire lifetime inside the dictionary.
# -> If mutable objects (like lists) were allowed as keys, then modifying the object after insertion could change its hash.

#   Example:
#       - key = [1,2,3]
#       - d[key] = "Hello"
# Dictionary stores it according to:
#      -> hash([1,2,3]) ---> Bucket X
# 
# Later on if we modify the key:
#       - key.append(4) --> list becomes [1,2,3,4]

# During lookup:
#       - d[key]-> Python computes the NEW hash, The new hash goes to Bucket Y, and fails to find the key even though it actually exists in Bucket X.
# => The dictionary would become inconsistent/corrupted. Therefore dictionary keys must be HASHABLE.

# A hashable object is one whose hash value never changes during its lifetime. Most immutable objects are hashable:
#       - int
#       - float
#       - str
#       - bool
#       - tuple (only if all its elements are hashable)
#       - frozenset

# Mutable objects like list, dict and set are NOT hashable because their
# contents (and hence their hash) can change.

d4 = {(1,2):"Tuple as key", "NAME": "Pranjal", "Flag": True} # So if we have to use a group of values as a key, we can use a tuple as a key in the dictionary because tuples are immutable and hashable. 
# NOTE: But only a certain kinds on tuples are hashable, if suppose a tuple contains a list, then that tuple will not be hashable because the list is mutable and not hashable. Therefore the tuple will also not be hashable.
#--> So only those tuples are hashable which contain only hashable data types as their elements. For example:
t1 = (1,2,3) # This is a hashable tuple because it contains only hashable data types as its elements (int, float, str, bool, tuple, frozenset).
t2 = (1,2,[1,2,3]) # This is not a hashable tuple.

# SOME MORE INFORMATION ABOUT DICTIONARIES:
# -----------------------------------------------------------------------------
# Hash Collisions
# -----------------------------------------------------------------------------
#
# - Different keys can sometimes produce the same bucket. This is called a HASH COLLISION. 
#
# Python resolves collisions internally (using open addressing and probing in CPython) and then compares the actual keys using equality (==) to identify the correct one. Therefore:

#     ->  Same hash ≠ Same key

# 1. Hashes help locate candidate positions quickly
# 2. Actual key comparison confirms the correct match.
#
# =============================================================================
# IS A DICTIONARY ORDERED OR UNORDERED?
# =============================================================================
#
# - Prior to Python 3.7:
#   ==> Dictionaries were considered UNORDERED.
# - From Python 3.7 onwards:
#   ==> Dictionaries PRESERVE INSERTION ORDER.
# Example:
d = {"apple": 1, "banana": 2, "cat": 3}
# Iterating over the dictionary will always produce:

#       apple-> 1st
#       banana-> 2nd
#       cat-> 3rd
print(d) # Output: {'apple': 1, 'banana': 2, 'cat': 3} -> The order of the key-value pairs is preserved as they were inserted into the dictionary.
# IMPORTANT:

# Dictionaries STILL use hashing internally for O(1) lookup. It's just that modern Python simply maintains insertion order in addition to the hash table.
#
# Therefore a modern dictionary is best described as: "A hash-based mapping that preserves insertion order."

# -----------------------------------------------------------------------------
# Difference between Dictionary and Set
# -----------------------------------------------------------------------------

# Dictionary:
#   • Uses hashing internally.
#   • Preserves insertion order (Python 3.7+).
#   • Stores key-value pairs.
#   • Keys must be unique and hashable.

# Set:
#   • Uses hashing internally.
#   • Does NOT guarantee insertion order.
#   • Stores only unique elements.
#   • Elements must be hashable.

# -----------------------------------------------------------------------------
# SOME METHODS OF DICTIONARY CREATING DICTIONARIES:
# -----------------------------------------------------------------------------
# A) Using the dict() constructor:
# 1. Iterable pair method:

# Using the dict() constructor we can convert a list of tuples ( or a list of lists, a tuple of tuples, a tuple of lists, etc.) into a dictionary. 
# - Each tuple (or list) should contain exactly two elements: the first element will be the KEY and the second element will be the VALUE in the dictionary.
l1 = [(1, "One"), (2, "Two"), (3, "Three"), (4, "Four")]
d1 = dict(l1) # This will convert the list of tuples into a dictionary.
print(d1) # Output: {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}

# 2. Using zip() function:

# The zip() function can be used to combine two lists (or other iterables) into a zip object. The first list will provide the keys and the second list will provide the values.
# Q-> Now what is a zip object? 
#   - A zip object is an ITERATOR that generates tuples containing elements from the input iterables.
#   - Each tuple contains one element from each of the input iterables, paired together based on their position in the original iterables.
#   - The zip object can be converted into a list or other iterable types, such as a dictionary, using the dict() constructor.

#NOTE: for knowing what an iterator is, check the file Class/Some_extra_concepts.py in this repo.

l1 = ["a", "b", "c", "d"]
l2 = [1, 2, 3, 4]
l3 = zip(l1, l2) # This will create a zip object that contains pairs of elements from the two lists.
# If there were more elements in one list than the other, the zip object would only contain pairs up to the length of the shorter list. The extra elements in the longer list would be ignored.

# let us see how that zip object looks like:
print(l3) # Output: <zip object at 0x7f8c8c8c8c8c> -> This is a zip object that contains pairs of elements from the two lists. It is an iterator that generates tuples containing elements from the input iterables.
print(list(l3)) # Output: [('a', 1), ('b', 2), ('c', 3), ('d', 4)] 
# Now we can convert this zip object into a dictionary using the dict() constructor:
l3 = zip(l1, l2) # Recreate the zip object because it was exhausted by list(l3)
d1 = dict(l3) # This will convert the zip object into a dictionary.
print(d1) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4} -> This is a dictionary that contains key-value pairs from the two lists.

# 3. Using enumerate() function:

#Enumerate() function takes an iterable and returns an enumerate object that yields pairs of (index, element) for each element in the iterable. The index starts from 0 by default, but you can specify a different starting index using the start parameter.
l1 = ["One", "Two", "Three", "Four"]
l2 = enumerate(l1) # This will create an enumerate object that contains pairs of (index, element) for each element in the list.
print(l2) # Output: <enumerate object at 0x7f8c8c8c8c8c> -> This is an enumerate object that contains pairs of (index, element) for each element in the list. It is an iterator that generates tuples containing the index and the element from the input iterable.
print(list(l2)) #-> and object of enumerate is also an iterator, so we can convert it into a list using the list() constructor. This will print a list of tuples containing the index and the element from the input iterable.
# But an enumerate object doesn't get exhausted like a zip object so we can directly convert it into a dictionary using the dict() constructor:
d1 = dict(enumerate(l1)) # This will create a dictionary where the keys are the indices of the elements in the list and the values are the elements themselves.
print(d1) # Output: {0: 'One', 1: 'Two', 2: 'Three', 3: 'Four'} -> This is a dictionary that contains key-value pairs where the keys are the indices of the elements in the list and the values are the elements themselves.

# Now if we were to have different starting index for the keys, we can use an additional argument in the enumerate() function to specify the starting index for the keys in the dictionary.
d2 = dict(enumerate(l1, start=1)) # This will create a dictionary where the keys are the indices of the elements in the list starting from 1 and the values are the elements themselves.
print(d2) # Output: {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'} -> This is a dictionary that contains key-value pairs where the keys are the indices of the elements in the list starting from 1 and the values are the elements themselves.
#--------------------------------------------------------------------------------------------------------------------
# Now lets see how to create a dictionary using dictionary comprehension:
# B) Using dictionary comprehension:

# 1.Iterable pairs:

l1 = [(1, "One"), (2, "Two"), (3, "Three"), (4, "Four")]
d1 = {k: v for k, v in l1} # This will create a dictionary using dictionary comprehension where the keys and values are taken from the list of tuples.
print(d1) # Output: {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'} -> This is a dictionary that contains key-value pairs from the list of tuples.

# 2. zip() function:
l1 = ["a", "b", "c", "d"]
l2 = [1, 2, 3, 4]
l3 = zip(l1, l2) # This will create a zip object that contains pairs of elements from the two lists.
d1 = {k: v for k, v in l3} # This will create a dictionary using dictionary comprehension where the keys and values are taken from the zip object.
print(d1) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4} -> This is a dictionary that contains key-value pairs from the zip object.

# 3. enumerate() function:
l1 = ["One", "Two", "Three", "Four"]
d1 = {i: v for i, v in enumerate(l1, start=1)} # This will create a dictionary using dictionary comprehension where the keys are the indices of the elements in the list starting from 1 and the values are the elements themselves.
print(d1) # Output: {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'} -> This is a dictionary that contains key-value pairs where the keys are the indices of the elements in the list starting from 1 and the values are the elements themselves.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ACESSING DICTIONARY ELEMENTS:

# 1. Reading:
# Syntax: dictionary_name[key]-> This gives the value of that particular key in the dictionary.

d1 = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
print(d1[1]) # Output: One
# Now what happens if we try to read the value of the key which is not present in the dictionary?
print(d1[5]) # This will raise a KeyError because the key 5 is not present in the dictionary
# There is another way to read the value of a key in a dictionary that is using the get() method. The get() method returns the value for the specified key if the key is in the dictionary. If not, it returns None (or a default value if specified).
print(d1.get(1)) # Output: One
print(d1.get(5)) # Output: None (because the key 5 is not present in the dictionary)

# 2. Updating:
# Syntax: dictionary_name[key] = new_value -> This will update the value of the specified key in the dictionary. 
# NOTE: If the key is not present, it will add a new key-value pair to the dictionary.

d1 = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
d1[1] = "Uno" # Updating the value of key 1
print(d1) # Output: {1: 'Uno', 2: 'Two', 3: 'Three', 4: 'Four'}


# 3. Writing:
# Syntax: dictionary_name[New_key] = value -> This will add a new key-value pair to the dictionary. 
# NOTE: If the key already exists, it will update the value of that key.

d1 = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
d1[5] = "Five" # Adding a new key-value pair to the dictionary
print(d1) # Output: {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

# 4. Traversing:
# For traversing a dictionary, we can use a for loop to iterate over the keys or values of the dictionary.
d1 = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
for key in d1: # This will iterate over the keys of the dictionary
    print(key, d1[key]) # Output: 1 One, 2 Two, 3 Three, 4 Four 

#-> A different example of traversing a dictionary is using the range() and len() functions to iterate over the keys of the dictionary.
d = {"Name":"John", "Age":30, "City":"New York"}
for i in range (len(d)): # This will iterate over the keys of the dictionary using range and len
    print(list(d.keys())[i], list(d.values())[i]) # Output: Name John, Age 30, City New York

# How this works?

# 1."list(d.keys())[i]": We are using the keys() method to get the keys of the dictionary in a view object.
d = {"Name":"John", "Age":30, "City":"New York"}
print(d.keys()) # Output: dict_keys(['Name', 'Age', 'City']) -> This is a view object that displays a list of all the keys in the dictionary. This is not a list, but it can be converted into a list using the list() function.
print(list(d.keys())) # Output: ['Name', 'Age', 'City'] -> This is a list of all the keys in the dictionary. We can access the keys using indexing, just like we do with lists.
# And this is what we did in the for loop above to access the keys of the dictionary using indexing. We used the list() function to convert the view object into a list and then used indexing to access the key at the ith position in the list.
print(list(d.keys())[0]) # Output: Name -> This is the first key in the dictionary.
print(list(d.keys())[1]) # Output: Age -> This is the second key in the dictionary.
print(list(d.keys())[2]) # Output: City -> This is the third key in the dictionary.

# 2."list(d.values())[i]": We are using the values() method to get the values of the dictionary in a view object. This is similar to the keys() method, but it returns the values of the dictionary instead of the keys.
print(d.values()) # Output: dict_values(['John', 30, 'New York']) -> This is a view object that displays a list of all the values in the dictionary. 
print(list(d.values())) # Output: ['John', 30, 'New York'] -> This is a list of all the values in the dictionary. We can access the values using indexing, just like we do with lists.
print(list(d.values())[0]) # Output: John -> This is the first value in the dictionary.
print(list(d.values())[1]) # Output: 30 -> This is the second value in the dictionary.
print(list(d.values())[2]) # Output: New York -> This is the third value in the dictionary.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# METHODS OF DICTIONARY:

# 1. Looping through a dictionary:

# We can loop through a dictionary :
#   - using the 'keys()' method to get the keys of the dictionary and then using indexing to access the values of the dictionary.
#   - using the 'values()' method to get the values of the dictionary.
#   - using the 'items()' method to get the key-value pairs of the dictionary.
#   - using the 'get()' method to get the value of a key in the dictionary.

# lets see how to use these methods to loop through a dictionary:
d = {"Name":"John", "Age":30, "City":"New York"}
# A) Looping through the keys of the dictionary using the 'keys()' method:
print(d.keys()) # Output: dict_keys(['Name', 'Age', 'City']) -> This is a view object that displays a list of all the keys in the dictionary. This is not a list, but it can be converted into a list using the list() function.
# Although its the view object is not a list but it is still an iterable object, so we can use a for loop to iterate over the keys of the dictionary.

for key in d.keys(): # This will iterate over the keys of the dictionary using the 'keys()' method.
    print(key, f' : {d[key]}') # Output: Name: John, Age: 30, City: New York -> This will print the key and its corresponding value in the dictionary.

# B) Looping through the values of the dictionary using the 'values()' method:
print(d.values()) # Output: dict_values(['John', 30, 'New York']) -> Again this is a view object that displays a list of all the values in the dictionary. 
for value in d.values(): # This will iterate over the values of the dictionary using the 'values()' method.
    print(value) # Output: John, 30, New York -> This will print all the values in the dictionary.

# C) Looping through the key-value pairs of the dictionary using the 'items()' method:
print(d.items()) # Output: dict_items([('Name', 'John'), ('Age', 30), ('City', 'New York')]) -> This is a view object that displays a list of all the key-value pairs in the dictionary such that each element in the list is a tuple of (key, value). 
for k,v in d.items(): # This will iterate over the key-value pairs of the dictionary using the 'items()' method.
    print(k, f' : {v}') # Output: Name: John, Age: 30, City: New York -> This will print the key and its corresponding value in the dictionary.

# D) Looping through the keys of the dictionary using the 'get()' method:
for key in d: # This will iterate over the keys of the dictionary using the 'get()' method.
    print(key , f' : {d.get(key)}') # Output: Name: John, Age: 30, City: New York -> This will print the key and its corresponding value in the dictionary.

# - get() function's signature is: get(key, default=None) -> This means that if the key is not present in the dictionary, it will return the default value (which is None by default). We can specify a different default value if we want.
print(d.get("Country", "Not Found")) # Output: Not Found -> This will return the default value "Not Found" because the key "Country" is not present in the dictionary.
# Thats another difference between using the 'get()' method and using indexing to access the value of a key in the dictionary.
#   - If we use indexing to access the value of a key that is not present in the dictionary, it will raise a KeyError. 
#   - If we use the 'get()' method to access the value of a key that is not present in the dictionary, it will return the default value (which is None by default).

# There is another function called 'setdefault()' which is similar to the 'get()' method but it also allows us to set a default value for a key if the key is not present in the dictionary, that is it actually adds a new key-value pair to the dictionary if the key is not present in the dictionary. 

# The signature of the 'setdefault()' method is: setdefault(key, default=None) -> This means that if the key is not present in the dictionary, it will add a new key-value pair to the dictionary with the specified key and default value (which is None by default). We can specify a different default value if we want.
print(d.setdefault("Country", "USA")) # Output: USA -> This will add a new key-value pair to the dictionary with the key "Country" and the default value "USA" because the key "Country" is not present in the dictionary.
print(d) # Output: {'Name': 'John', 'Age': 30, 'City': 'New York', 'Country': 'USA'} -> This is the updated dictionary that contains the new key-value pair.

# 2. Some other useful methods of dictionary are:

# A) update() method: 
# Syntax: dictionary_name.update(other_dictionary) 
# - This method updates the dictionary with the key-value pairs from another dictionary. 
# - If a key already exists in the dictionary, its value will be updated with the new value from the other dictionary.
# Example:
d = {"Name":"John", "Age":30, "City":"New York"}
d1 = {"Age":31, "Country":"USA"}
d.update(d1) # This will update the dictionary d with the key-value pairs from the dictionary d1. The value of the key "Age" will be updated to 31 and a new key-value pair "Country":"USA" will be added to the dictionary d.
print(d) # Output: {'Name': 'John', 'Age': 31, 'City': 'New York', 'Country': 'USA'} -> This is the updated dictionary that contains the new key-value pair and the updated value of the key "Age".

# B) fromkeys() method:
# Syntax: dictionary_name.fromkeys(iterable, value)
# - This method creates a new dictionary with keys from the specified iterable and values set to the specified value (which is None by default)
# Example:
d = dict.fromkeys(["Name", "Age", "City"], "Unknown")
print(d) # Output: {'Name': 'Unknown', 'Age': 'Unknown', 'City': 'Unknown'} -> This creates a new dictionary with the specified keys and the specified value.
# - We can observe one thing in this method, that is its called on the dict class itself and not on an instance of the dict class. This is because it is a class method / static method. We will learn about static methods in the later classes of this course. 
 
# C) copy() method:
# Syntax: dictionary_name.copy()
# - This method returns a shallow copy of the dictionary. A shallow copy means that it creates a new dictionary with the same key-value pairs as the original dictionary, but the new dictionary is a separate object in memory.
# Example:
d = {"Name":"John", "Age":30, "City":"New York"}
d_copy = d.copy() # This will create a shallow copy of the dictionary d.
print(d_copy) # Output: {'Name': 'John', 'Age': 30, 'City': 'New York'} -> This is the copied dictionary.
print(d, f'This is the original dict', sep = ' ->')
print(d is d_copy) # Output: False -> This means that the original dictionary and the copied dictionary are two different objects in memory.

# D) pop() method:
# Syntax: dictionary_name.pop(key, default)
# - This method removes the specified key from the dictionary and returns its value.
# Example
d1 = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
print(d1.pop(2)) # Output: Two -> This will remove the key 2 from the dictionary and return its value "Two".
print(d1) # Output: {1: 'One', 3: 'Three', 4: 'Four'} -> This is the updated dictionary that does not contain the key 2.
print(d1.pop(5, "Not Found")) # Output: Not Found -> This will return the default value "Not Found" because the key 5 is not present in the dictionary.

# E) popitem() method:
# Syntax: dictionary_name.popitem()
# - This method removes and returns the last inserted key-value pair from the dictionary as a tuple.
# Example:
d1 = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
print(d1.popitem()) # Output: (4, 'Four') -> This will remove the last inserted key-value pair (4, 'Four') from the dictionary and return it as a tuple.
print(d1) # Output: {1: 'One', 2: 'Two', 3: 'Three'} -> This is the updated dictionary that does not contain the last inserted key-value pair.

# F) clear() method:
# Syntax: dictionary_name.clear()
# - This method removes all key-value pairs from the dictionary, leaving it empty.
# Example:
d1 = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
d1.clear() # This will remove all key-value pairs from the dictionary d1.
print(d1, type(d1)) # Output: {} <class 'dict'> -> This is the updated dictionary that is now empty.







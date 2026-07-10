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
#       -int
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

# SOME METHODS OF DICTIONARY CREATING DICTIONARIES:
# -----------------------------------------------------------------------------

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
# Now we can convert this zip object into a dictionary using the dict() constructor:
d1 = dict(l3) # This will convert the zip object into a dictionary.
print(d1) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4} -> This is a dictionary that contains key-value pairs from the two lists.

# 3. Using enumerate() function:

# The enumerate() function can be used to create a dictionary where the keys are the indices of the elements in the iterable and the values are the elements themselves.
l1 = ["One", "Two", "Three", "Four"]
d1 = dict(enumerate(l1)) # This will create a dictionary where the keys are the indices of the elements in the list and the values are the elements themselves.
print(d1) # Output: {0: 'One', 1: 'Two', 2: 'Three', 3: 'Four'} -> This is a dictionary that contains key-value pairs where the keys are the indices of the elements in the list and the values are the elements themselves.

# Now if we were to have different starting index for the keys, we can use an additional argument in the enumerate() function to specify the starting index for the keys in the dictionary.
d2 = dict(enumerate(l1, start=1)) # This will create a dictionary where the keys are the indices of the elements in the list starting from 1 and the values are the elements themselves.
print(d2) # Output: {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'} -> This is a dictionary that contains key-value pairs where the keys are the indices of the elements in the list starting from 1 and the values are the elements themselves.


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

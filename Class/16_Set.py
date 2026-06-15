# SET : In mathematics, a Set is a collection of distinct objects.
# In Python, a Set is an unordered collection of unique items. It is defined using curly braces {} or the built-in set() function.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CREATING A SET:

s1 = {1, 2, 3, 4, 5}
print(s1) # Output: {1, 2, 3, 4, 5}
s2 = {1,2,3,2,3,4,5,6} # Now since by definination a set is a collection of disticnt objects, so the duplicate values will be removed automatically 
print(s2) # Output: {1, 2, 3, 4, 5, 6}
set1 = {1, "hello", 3.4, True} # A set can contain elements of different data types
print(set1) # Output: {1, 'hello', 3.4, True}
s3 = {} # This creates an empty dictionary, not a set
print(type(s3)) # Output: <class 'dict'>
# So unlike a tuple or a list, empty set can't be created using {}. Instead, we have to use the set() function to create an empty set.
s3 = set() # This creates an empty set
set2 = {1} # This creates a set with one element

# Another way of creating a set is by using the built-in set() function:
s3 = set([1, 2, 3, 4, 5])
print(s3) # Output: {1, 2, 3, 4, 5}
s4 = set("hello") # Now since a set is a collection of distinct objects, so the duplicate values will be removed automatically
print(s4) # Output: {'h', 'e', 'l', 'o'}
# So here we can infer that a set function is a very good way for removing duplicate values from a list or a string.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# NOTE:
# Now a very IMPORTANT point of difference between a set and a list is that a set is an unordered collection. So where the element is stored in a set is not fixed, it can be stored anywhere in the memory.
s1 = {10,20,30,40,50}
print(s1) # Output: {50, 20, 40, 10, 30}
s2 = set("pranjal") 
print(s2) # Output: {'a', 'p', 'n', 'j', 'r', 'l'}
# Hence INDEXING and SLICING is not possible in a set. So if we try to do that, we will get an error.
 
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MUTABILITY OF A SET:

s = {1, 2, 3, 4, 5}
s.add(6) # Adding an element to the set using the add() method
print(s) # Output: {1, 2, 3, 4, 5, 6} (order may vary)
s.remove(3) # Removing an element from the set using the remove() method
print(s) # Output: {1, 2, 4, 5, 6} (order may vary)
s.add((1,2,3)) # A set can also contain a tuple as an element
print(s) # Output: {1, 2, 4, 5, 6, (1, 2, 3)} (order may vary)
s.add([1,2,3]) # This will give an error because a list is mutable and hence cannot be added to a set

# So we now know one more thing that a mutable object cannot be stored in a set, because if we change the value of that mutable object, then it will create a problem for the set to maintain its uniqueness property. 

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# HOW SET INTERANLLY WORKS:

# A set is implemented using a hash table.
# The hashing is done based on a hash function.
# The hashing function takes an input (or 'key') and returns an integer, which is used as an index in the hash table. This allows for fast lookups, insertions, and deletions of elements in the set.

# suppose we have a set s = {5, 10, 21, 15, 3, 11} and the size of the hash table is N = 10. The hash function will compute the following indices for each element:
# let the Hash Function be (h(x) = x % 10) and the corresponding indices in the hash table will be:

#          ┌───┬───────┐
# keys --> │ 0 │       │ <-- Element      s = {5, 10, 21, 15, 3, 11}               
#          ├───┼───────┤                  -> STEP:-1: h(5) = 5 % 10 = 5 : value 5 will be stored at index 5 in the hash table       
#          │ 1 │       │                  -> STEP:-2: h(10) = 10 % 10 = 0 : value 10 will be stored at index 0 in the hash table
#          ├───┼───────┤                  -> STEP:-3: h(21) = 21 % 10 = 1 : value 21 will be stored at index 1 in the hash table
#          │ 2 │       │                  -> STEP:-4: h(15) = 15 % 10 = 5 : value 15 will be stored at index 5 in the hash table (collision)     
#          ├───┼───────┤                  -> STEP:-5: h(3) = 3 % 10 = 3 : value 3 will be stored at index 3 in the hash table
#          │ 3 │       │                  -> STEP:-6: h(11) = 11 % 10 = 1 : value 11 will be stored at index 1 in the hash table (collision)  
#          ├───┼───────┤                  
#          │ 4 │       │                  ==> Now when a collision occurs, the set will use a method called chaining to resolve the collision. 
#          ├───┼───────┤                      - In this method, each index in the hash table will store a list of elements that hash to the same index.
#          │ 5 │       │                      - So in this case, index 1 will store the list [21, 11] and index 5 will store the list [5, 15].
#          ├───┼───────┤
#          │ 6 │       │                  ==> Finally this will be the final structure of the hash table after all the elements are added:
#          ├───┼───────┤                            
#          │ 7 │       │                        ┌───┬──────────┐
#          ├───┼───────┤                        │ 0 │    10    │    -> Now when we print set s, it will print the elements in the order they were added, i.e {10, 21, 11, 3, 5, 15}
#          │ 8 │       │                        ├───┼──────────┤  
#          ├───┼───────┤                        │ 1 │ [21, 11] │ 
#          │ 9 │       │                        ├───┼──────────┤
#          └───┴───────┘                        │ 2 │     /    │
#                                               ├───┼──────────┤
#                                               │ 3 │    3     │
#                                               ├───┼──────────┤
#                                               │ 4 │     /    │
#                                               ├───┼──────────┤
#                                               │ 5 │ [5, 15]│ | 
#                                               ├───┼──────────┤
#                                               │ 6 │     /    │
#                                               ├───┼──────────┤
#                                               │ 7 │     /    │
#                                               ├───┼──────────┤
#                                               │ 8 │     /    │
#                                               ├───┼──────────┤
#                                               │ 9 │     /    │
#                                               └───┴──────────┘

# - When the hash table is filled with elements to a certain threshold, it will be resized to a larger size and the elements will be rehashed to the new hash table. This is done to avoid collisions and maintain the efficiency of the set operations.
# - This threshold is typically around 70-80% of the hash table's capacity. When the number of elements in the set exceeds this threshold, the hash table will be resized to a larger size (usually doubling the size) and all the elements will be rehashed to the new hash table.
# - This process is called rehashing.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SET THEORY AND OPERATIONS:

# Now Set are orignally a mathematical concept, so in order to understand set in Python, it is important to understand the basic set theory concepts.
# Lets have a set 'S':
S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Along with this we have more sets A, B and C:
A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 8}
C = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Now both A and B are subsets of S, because all the elements of A and B are present in S. So we can say that A ⊆ S and B ⊆ S. In other words S is the superset of A and B, so we can say that S ⊇ A and S ⊇ B.
# Now look at C, C is also a subset of S, but C is also equal to S, because all the elements of C are present in S and all the elements of S are present in C. So we can say that C ⊆ S and S ⊆ C, which means that C = S. 
# So we can say that A and B are proper subsets of S but C is not a proper subset of S, because C = S. Also S is a proper superset of A and B. This can be written as A ⊂ S and B ⊂ S and S ⊃ A and S ⊃ B. 

# Now lets have 2 more sets D and E:
D = {1, 2, 3, 4, 5}
E = {6, 7, 8, 9, 10}
# Now here D and E are sets which do not have any common element, so we can say that D and E are disjoint sets. This can be written as D ∩ E = ∅, where ∅ is the empty set.

# Now lets see some mathematical operations on sets:
A = {1,2,3,5,7}
B = {5,7,9,10,11}

# 1.Union (A ∪ B) : This stands for A Union B, which is the set of all elements that are in A or in B or in both. So A ∪ B = {1,2,3,5,7,9,10,11}. A ∪ B = B ∪ A, which means that the union of A and B is the same as the union of B and A. 
# 2.Intersection (A ∩ B): This stands for A Intersection B, which is the set of all elements that are in A and B both. So A ∩ B = {5,7}. A ∩ B = B ∩ A, which means that the intersection of A and B is the same as the intersection of B and A. 
# 3.Difference (A - B): This stands for A Difference B, which is the set of all elements that are in A but not in B. So A - B = {1,2,3} (i.e exclusively in A but not in B). A - B != B - A, B - A = {9,10,11} (i.e exclusively in B but not in A).
# 4.Symmetric Difference (A Δ B): This stands for A Symmetric Difference B, which is the set of all elements that are in A or in B but not in both. So A Δ B = {1,2,3,9,10,11}. A Δ B = B Δ A.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SET OPERATIONS USING METHODS:

# 1. Union:
# Syntax: set1.union(set2) 
s1 = {1, 2, 3, 5, 7}
s2 = {5, 7, 9, 10, 11}
print(s1.union(s2)) # Output: {1, 2, 3, 5, 7, 9, 10, 11} : s1.union(s2) is akin to writing s1 ∪ s2
print(s1) # Output: {1, 2, 3, 5, 7} (s1 is not modified) so we can say that union is a non-destructive operation i.e it does not modify the original sets. It returns a new set which is the union of the two sets.

# 2. Intersection:
# Syntax: set1.intersection(set2)
s1 = {1, 2, 3, 5, 7}
s2 = {5, 7, 9, 10, 11}
s3 = s1.intersection(s2) # This is same as writing s1 ∩ s2
print(s3) # Output: {5, 7}
# This is also a non-destructive operation, so s1 and s2 are not modified.

# 3. Intersection Update: This function is intersection only but instead of giving a new set as output, it modifies the original set itself. So it is a destructive operation.
# Syntax: set1.intersection_update(set2)
s1 = {1, 2, 3, 5, 7}
id_s1_before = id(s1) # This will give the memory address of s1 before the intersection update
s2 = {5, 7, 9, 10, 11}
s1.intersection_update(s2) # This is same as writing s1 = s1 ∩ s2
print(s1.intersection_update(s2)) # Output: None (intersection_update does not return anything, it modifies the original set itself)
print(s1) # Output: {5, 7} (s1 is modified to be the intersection of s1 and s2)
print(id(s1)==id_s1_before) # Output: True (memory address of s1 is same before and after the intersection update, which means that s1 is modified and not a new set is created)

# 4. Difference: 
# Syntax: set1.difference(set2)
s1 = {1, 2, 3, 5, 7}
s2 = {5, 7, 9, 10, 11}
s3 = s1.difference(s2)
print(s3) # Output: {1, 2, 3} (elements that are in s1 but not in s2)
s4 = s2.difference(s1)
print(s4) # Output: {9, 10, 11} (elements that are in s2 but not in s1)
# This function is non-destructive, so s1 and s2 are not modified.

# 5. Difference Update: This function is difference only but instead of giving a new set as output, it modifies the original set itself. So it is a destructive operation.
# Syntax: set1.difference_update(set2)
s1 = {1, 2, 3, 5, 7}
id_s1_before = id(s1) # This will give the memory address of s1 before the difference update
s2 = {5, 7, 9, 10, 11}
s1.difference_update(s2) # This is same as writing s1 = s1 - s2
print(s1.difference_update(s2)) # Output: None (difference_update does not return anything, it modifies the original set itself)
print(s1) # Output: {1, 2, 3} (s1 is modified to be the difference of s1 and s2)
print(id(s1)==id_s1_before) # Output: True (memory address of s1 is same before and after the difference update, which means that s1 is modified and not a new set is created)

# 6. Symmetric Difference:
# Syntax: set1.symmetric_difference(set2)
s1 = {1, 2, 3, 5, 7}
s2 = {5, 7, 9, 10, 11}
s3 = s1.symmetric_difference(s2)
print(s3) # Output: {1, 2, 3, 9, 10, 11} (elements that are in s1 or in s2 but not in both)
# This function is non-destructive, so s1 and s2 are not modified.

# 7. Symmetric Difference Update: This function is symmetric difference only but instead of giving a new set as output, it modifies the original set itself. So it is a destructive operation.
# Syntax: set1.symmetric_difference_update(set2)
s1 = {1, 2, 3, 5, 7}
id_s1_before = id(s1) # This will give the memory address of s1 
s2 = {5, 7, 9, 10, 11}
s1.symmetric_difference_update(s2) 
print(s1.symmetric_difference_update(s2)) # Output: None (symmetric_difference_update does not return anything, it modifies the original set itself)
print(s1) # Output: {1, 2, 3, 9, 10, 11} (s1 is modified to be the symmetric difference of s1 and s2)
print(id(s1)==id_s1_before) # Output: True (memory address of s1 is same before and after the symmetric difference update, which means that s1 is modified and not a new set is created)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SET OPERATIONS USING OPERATORS:

# 1. Union: We can also perform union operation using the | operator. So A | B is same as A ∪ B.
A = {1,2,3,5,7}
B = {5,7,9,10,11}
print(A | B) # Output: {1, 2, 3, 5, 7, 9, 10, 11}
# Now this is also a non-destructive operation, so A and B are not modified.

# 2. Intersection: We can also perform intersection operation using the & operator. So A & B is same as A ∩ B.
A = {1,2,3,5,7}
B = {5,7,9,10,11}
print(A & B) # Output: {5, 7}
# Now this is also a non-destructive operation, so A and B are not modified.

# 3.Intersection Update: We can also perform intersection update operation using the &= operator. So A &= B is same as A = A ∩ B.
A = {1,2,3,5,7}
id_A_before = id(A) # This will give the memory address of A before the intersection update
B = {5,7,9,10,11}
A &= B # This is same as writing A = A ∩ B
print(A) # Output: {5, 7} (A is modified to be the intersection of A and B)
print(id(A)==id_A_before) # Output: True (memory address of A is same before and after the intersection update, which means that A is modified and not a new set is created)

# 4. Difference: We can also perform difference operation using the - operator. So A - B.
A = {1,2,3,5,7}
B = {5,7,9,10,11}
print(A - B) # Output: {1, 2, 3} (elements that are in A but not in B)
print(B - A) # Output: {9, 10, 11} (elements that are in B but not in A)
# Now this is also a non-destructive operation, so A and B are not modified.

# 5. Difference Update: We can also perform difference update operation using the -= operator. 
A = {1,2,3,5,7}
id_A_before = id(A) # This will give the memory address of A before the difference update
B = {5,7,9,10,11}
A -= B 
print(A) # Output: {1, 2, 3} (A is modified to be the difference of A and B)
print(id(A)==id_A_before) # Output: True (memory address of A is same before and after the difference update, which means that A is modified and not a new set is created)

# 6. Symmetric Difference: We can also perform symmetric difference operation using the ^ operator. So A ^ B is same as A Δ B.
A = {1,2,3,5,7}
B = {5,7,9,10,11}
print(A ^ B) # Output: {1, 2, 3, 9, 10, 11} (elements that are in A or in B but not in both)
# Now this is also a non-destructive operation, so A and B are not modified.   

# 7. Symmetric Difference Update: We can also perform symmetric difference update operation using the ^= operator. So A ^= B is same as A = A Δ B.
A = {1,2,3,5,7}
id_A_before = id(A) # This will give the memory address of A before the symmetric difference update
B = {5,7,9,10,11}
A ^= B # This is same as writing A = A Δ B
print(A) # Output: {1, 2, 3, 9, 10, 11} (A is modified to be the symmetric difference of A and B)
print(id(A)==id_A_before) # Output: True (memory address of A is same before and after the symmetric difference update, which means that A is modified and not a new set is created)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ADDING, UPDATION AND REMOVING ELEMENTS FROM A SET:

# 1. add(element): This method is used to add an element to the set. If the element is already present in the set, it will not be added again (because a set does not allow duplicate elements).

s = {1, 2, 3, 4, 5}
s.add(6) # Adding an element to the set using the add() method
print(s) # Output: {1, 2, 3, 4, 5, 6} (order may vary)
s.add(3) # This will not add 3 again to the set because 3 is already present in the set
print(s) # Output: {1, 2, 3, 4, 5, 6} (order may vary)
# It takes only one argument, which is the element to be added to the set. It does not return anything, it modifies the original set itself.
s.add((1,2,3)) # A set can also contain a tuple as an element
print(s) # Output: {1, 2, 3, 4, 5, 6, (1, 2, 3)} (order may vary)
s.add([1,2,3]) # This will give an error because a list is mutable and hence cannot be added to a set
print(s) # Output: {1, 2, 3, 4, 5, 6, (1, 2, 3)} (order may vary)

# 2. update(iterable): This method is used to add multiple elements to the set at once. It takes an iterable (like a string, tuple, etc.) as an argument and adds each element of the iterable to the set but not a list.

s = {1, 2, 3, 4, 5}
s.updeate((60,70))  # This will add 60 and 70 to the set because a tuple is an iterable and it will add each element of the tuple to the set.
print(s) # Output: {1, 2, 3, 4, 5, 60, 70} (order may vary)
s.update("hello") # This will add 'h', 'e', 'l', 'o' to the set because a string is an iterable and it will add each character of the string to the set.
print(s) # Output: {1, 2, 3, 4, 5, 60, 70, 'h', 'e', 'l', 'o'} (order may vary)
# It takes only one argument, which is the iterable whose elements are to be added to the set. It does not return anything, it modifies the original set itself.

# 3. copy(): This method is used to create a copy of the set. It returns a new set which is a copy of the original set. The copy is a shallow copy.
s1 = {1, 2, 3, 4, 5}
s2 = s1.copy() # This will create a copy of s1 and store it in s2
print(s2) # Output: {1, 2, 3, 4, 5} (order may vary)
print(s1 == s2) # Output: True (s1 and s2 have the same elements)
print(s1 is s2) # Output: False (s1 and s2 are different objects in memory)

# 4. pop(): This method is used to remove and return an arbitrary element from the set. Since a set is an unordered collection, there is no way to know which element will be removed. If the set is empty, it will raise a KeyError.
s = {1, 2, 3, 4, 5}
popped_element = s.pop() # This will remove and return an arbitrary element from the set
print(popped_element) # Output: 1 (or any other element from the set, because it is arbitrary)
print(s)

# 5. doscard(element): This method is used to remove an element from the set if it is present. If the element is not present in the set, it does nothing (it does not raise an error).
s = {1, 2, 3, 4, 5}
s.discard(3) # This will remove 3 from the set because 3 is present in the set
print(s) # Output: {1, 2, 4, 5} (order may vary)
s.discard(6) # This will do nothing because 6 is not present in the set
print(s) # Output: {1, 2, 4, 5} (order may vary)

# 6. remove(element): This method is used to remove an element from the set if it is present. If the element is not present in the set, it raises a KeyError.
s = {1, 2, 3, 4, 5}
s.remove(3) # This will remove 3 from the set because 3 is present in the set
print(s) # Output: {1, 2, 4, 5} (order may vary)
s.remove(6) # This will raise a KeyError    
s.remove(20, 30) # This will also raaise an error because remove() method takes only one argument. 

# 7.clear(): This method is used to remove all the elements from the set. It does not take any argument and it modifies the original set itself.
s = {1, 2, 3, 4, 5}
s.clear() # This will remove all the elements from the set
print(s) # Output: set() (an empty set)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# LIST COMPREHENSIONS AND SET COMPREHENSIONS:

# List comprehension for set are similar to that of list, we don't need to unpack the generator expression to create a set like in the case of tuple comprehension:
s = {x for x in range(10)} # This will create a set with values from 0 to 9
print(s) # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} (order may vary)

# Now just like in list comprehension, we can also add a condition in set comprehension as well as we can also have nested loops in set comprehension as well.

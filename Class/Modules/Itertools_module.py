# Itertools is a module in Python that provides various functions that work on iterators to produce complex iterators.
# It is a part of the standard library and can be imported using the following statement:
import itertools as it

# Some commonly used functions in the itertools module include:

# 1. count(start=0, step=1): This function returns an infinite iterator that generates consecutive numbers starting from the specified 'start' value and incrementing by the specified 'step' value. If no arguments are provided, it starts from 0 and increments by 1.
# Parameters:
# - start: The value from which the count will start (default is 0).
# - step: The value by which the count will be incremented (default is 1).

# suppose we want to generate an infinite sequence of numbers starting from 1 and incrementing by 1:
# we can do this:

# i = 1
# while True:
#     print(i)
#     i += 1
# Now itertools.count() is just a cleaner and more efficient way to achieve the same result:

for num in it.count(1,1):
    print(num)

# 2. cycle(iterable): This function returns an infinite iterator that cycles through the elements of the given iterable (like a list, tuple, or string) indefinitely. Once it reaches the end of the iterable, it starts again from the beginning.
# Parameters:
# - iterable: A sequence (like a list, tuple, or string) that you want to cycle through.

# Suppose we have a list of letters :- 
letters = ['A', 'B', 'C']
# and we want to cycle through these letters indefinitely:
i = 0
for i in range(len(letters)):
    print(letters[i])
    i+=1
    if i == len(letters):
        i = 0

# Now we can achieve the same result using itertools.cycle() in a cleaner way:

for letter in it.cycle(letters):
    print(f'\rletter is: {letter}', end='')


# 3. repeat(object, times=None): This function returns an iterator that produces the specified object repeatedly for a given number of times. If the 'times' parameter is not provided, it will repeat the object indefinitely.
# Parameters:
# - object: The object that you want to repeat.
# - times: The number of times to repeat the object (default is None, which means repeat indefinitely).

# Suppose we want to repeat the string "Hello" 5 times:
for i in range(5):
    print("Hello")  

# Now we can achieve the same result using itertools.repeat() in a cleaner way:
for greeting in it.repeat("Hello", 5):
    print(greeting)

# 4. product(*iterables, repeat=1): This function returns the Cartesian product of the input iterables. It generates all possible combinations of elements from the provided iterables. The 'repeat' parameter allows you to specify how many times to repeat the input iterables.
# Parameters:
# - *iterables: One or more iterables (like lists, tuples, or strings) that you want to compute the Cartesian product of.
# - repeat: The number of times to repeat the input iterables (default is 1).

# Suppose we have two lists:
shirt = ['red', 'blue']
pants = ['black', 'white']  
# and we want to generate all possible combinations of shirts and pants:
# we can use a nested for loop to achieve this:
for s in shirt:
    for p in pants:
        print(f'{s} shirt with {p} pants')

# Now we can achieve the same result using itertools.product() in a cleaner way:
for combination in it.product(shirt, pants):
    print(f'{combination[0]} shirt with {combination[1]} pants')

# what if we want to repeat the same list of shirts and pants 2 times to get combinations of 4 items (2 shirts and 2 pants):
for combination in it.product(shirt, pants, repeat=2):
    print(f'{combination[0]} shirt with {combination[1]} pants and my friend wears {combination[2]} shirt with {combination[3]} pants')

# For doing the same thing with nested loops, we would have to write 4 nested loops which is not efficient and not clean at all.



# 5. Permutations(iterable, r=None): This function returns an iterator that generates all possible permutations of the elements in the given iterable. If the 'r' parameter is specified, it generates permutations for those many elements at a time instead of the full length of the iterable.
# Parameters:
# - iterable: A sequence (like a list, tuple, or string) for which you want to generate permutations.
# - r: The number of elements to include in each permutation (default is None, which means use the full length of the iterable).

# Suppose we have a list : ['A', 'B', 'C']
list = ['A', 'B', 'C']
# and we want to generate all possible permutations of these elements:
# ABC,ACB,BAC,BCA,CAB,CBA

# Now if we were to do this using nested loops, we would have to write 3 nested loops:
for i in range(len(list)):
    for j in range(len(list)):
        for k in range(len(list)):
            if i != j and j != k and i != k:
                print(f'{list[i]}{list[j]}{list[k]}')
# Now we can achieve the same result using itertools.permutations() in a cleaner way:

list2= list(it.permutations(list))
print(list2) # Output: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')], because itertools.permutations() returns an iterator object, not a list. To see the actual permutations, you can convert the iterator to a list using the list() function.   


# 6. Combinations(iterable, r): This function returns an iterator that generates all possible combinations of the elements in the given iterable taken 'r' at a time. The order of elements in the combinations does not matter.
# Parameters:
# - iterable: A sequence (like a list, tuple, or string) for which you want to generate combinations.
# - r: The number of elements to include in each combination (required parameter).
# NOTE:- Combination means Number of ways to select items from a collection, where as Permuation means Number of ways to select and then arrange those selected items from a collection. In combination order does not matter, but in permutation order matters.

# # Suppose we have a list : ['A', 'B', 'C']
list = ['A', 'B', 'C']

# and we want to generate all possible combinations of these elements taken all at a time:
list2 = list(it.combinations(list, 2))
print(list2) # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')], because itertools.combinations() returns an iterator object, not a list. To see the actual combinations, you can convert the iterator to a list using the list() function.   

# if we were to do this for combination of 3 items at a time using itertools.combinations(), we would get:
list3 = list(it.combinations(list, 3))
print(list3) # Output: [('A', 'B', 'C')], because there is only one combination of 3 items that can be made from the list ['A', 'B', 'C'], which is the combination of all three items together.

# Now if we were to do this using nested loops, we would have to write 2 nested loops:
for i in range(len(list)):
    for j in range(i+1, len(list)):
        print(f'{list[i]}{list[j]}')


# 7. combinations_with_replacement(iterable, r): This function returns an iterator that generates all possible combinations of the elements in the given iterable taken 'r' at a time, allowing for repeated elements. The order of elements in the combinations does not matter.
# Parameters:   
# - iterable: A sequence (like a list, tuple, or string) for which you want to generate combinations with replacement.
# - r: The number of elements to include in each combination (required parameter).

# Suppose we have a list : ['A', 'B', 'C']
list = ['A', 'B', 'C']
# Now if we were to generate all possible combinations of these elements taken 2 at a time with repetition allowed:
list4 = list(it.combinations_with_replacement(list, 2))
print(list4) # Output: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')], because itertools.combinations_with_replacement() returns an iterator object, not a list. To see the actual combinations, you can convert the iterator to a list using the list() function.   

# If we were to do this using nested loops, we would have to write 2 nested loops and also add a condition to allow for repetition:
for i in range(len(list)):  
    for j in range(i, len(list)):
        print(f'{list[i]}{list[j]}')

# What if we want to generate combinations of 3 items at a time with repetition allowed:
list5 = list(it.combinations_with_replacement(list, 3))
print(list5) # Output: [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'C', 'C'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'C', 'C'), ('C', 'C', 'C')], because itertools.combinations_with_replacement() returns an iterator object, not a list. To see the actual combinations, you can convert the iterator to a list using the list() function.

# Similarly, if we were to do this using nested loops, we would have to write 3 nested loops and also add a condition to allow for repetition:
for i in range(len(list)):
    for j in range(i, len(list)):
        for k in range(j, len(list)):
            print(f'{list[i]}{list[j]}{list[k]}')



# These are just a few of the many functions available in the itertools module. The itertools module provides a wide range of functions for working with iterators, making it easier to create complex iterators and perform various operations on them efficiently.
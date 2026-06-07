# Random Module in Python

# -> The random module in Python provides functions for generating random numbers and performing random operations. 
# -> It is part of the Python Standard Library, so you can use it without installing any additional packages.
# -> To use the random module, you need to import it first using the statement 'import random'.

import random as rd
# Some commonly used functions in the random module include:

# 1. random(): This function returns a random float number between 0.0 and 1.0 (inclusive of 0.0 but not 1.0).

print(rd.random())

# 2. randint(a, b): This function returns a random integer N such that a <= N <= b. Both a and b are inclusive.

print(rd.randint(1, 10)) # Output: A random integer between 1 and 10 (inclusive).

# 3. choice(iterable, k): This function returns a random element from the non-empty iterable sequence (like a list, tuple, or string) provided as an argument.
# where iterable can be a list, tuple, or string. and k is an optional parameter that specifies the number of random elements to return. If k is not provided, it returns a single random element.
list = [1, 2, 3, 4, 5]
string = "Hello"
print(rd.choice(list)) # Output: A random element from the list (e.g., 1, 2, 3, 4, or 5).
print(rd.choice(string)) # Output: A random character from the string (e.g., 'H', 'e', 'l', 'o').

# 4. randrange(start, stop[, step]): This function returns a randomly selected element from the range created by the start, stop, and step arguments. The start is inclusive, while the stop is exclusive.
print(rd.randrange(1, 10)) # Output: A random integer from the range 1 to 9 (inclusive of 1 but not 10).
print(rd.randrange(1, 10, 2)) # Output: A random integer from the range 1 to 9 with a step of 2 (e.g., 1, 3, 5, 7, or 9).   

# 5. seed(a=None): This function initializes the random number generator with a specific seed value. If a is not provided, it uses the current system time. Using the same seed value will produce the same sequence of random numbers.
rd.seed(42) # Setting the seed to 42
print(rd.random()) # Output: A random float number that will be the same every time you run this code with the same seed (e.g., 0.6394267984578837).

for i in range(5):
    print(rd.randint(1, 100)) # Output: A sequence of 5 random integers between 1 and 100 that will be the same every time you run this code with the same seed.

# 6. shuffle(x): This function shuffles the sequence x in place, meaning it modifies the original sequence. It does not return a new shuffled sequence and modifies the original sequence.
# Where x can be a list, tuple, or string.

my_list = [1, 2, 3, 4, 5]
rd.shuffle(my_list)
print(my_list) # Output: The original list 'my_list' is shuffled in place, and the order of elements is changed.

# 7. sample(population, k): This function returns a new list containing k unique elements randomly selected from the population sequence or set. The population can be a list, tuple, or string.

population = [1, 2, 3, 4, 5]
k = 3
sampled_list = rd.sample(population, k)
print(sampled_list) # Output: A new list containing 3 unique elements randomly selected from the population list (e.g., [2, 4, 5]).

# 8. uniform(a, b): This function returns a random floating-point number N such that a <= N <= b for a <= b and b <= N <= a for b < a. The endpoints a and b are inclusive.
print(rd.uniform(1.0, 10.0)) # Output: A random float number between 1.0 and 10.0 (inclusive of both endpoints).

# Uniform is like the floating version of the randrange() function. It returns a random floating-point number between the specified range, while randrange() returns a random integer from the specified range.

# These are just a few of the many functions available in the random module. 

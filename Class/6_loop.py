i=1
while(True):   # this is while loop
    print(i)
    if(i==10):
        break
    i+=1

for j in range(1,4):  # this is for loop that uses range function  
    print(j)


# 'break' statement is used to break the nearest 'loop'
# 'continue' statement is used for skiping that particular iteration in a 'loop'
# 'for/while-else':- an  'else' can be used outside of if in a for loop or a while loop, such that that the else statment runs only if the loop is completed properly whithout anything breaking it. 

# A basic structure of a counter controlled ( for loop ) in python is :- 
    #for counter in range(start, stop, step):
    # -----body of loop-------
    #   print(counter)

# Now if i do like this :
print(range(1,4) )# this will not give you the numbers from 1 to 3 but it will give you a range object which is a generator object that generates the numbers from 1 to 3.

# -- Why is it like that?
# -> See a range object is a lightweight sequence description, so the object represents a sequence of numbers, but it does not store them in memory. Instead, it generates the numbers on-the-fly as you iterate over it. This is why when you print a range object, you see something like 'range(1, 4)' instead of the actual numbers. 

# -- Now why it does that ?
# -> EFFICIENCY: The range object is designed to be memory efficient. 
# 
# Imagine this : range(1, 1000000) would create a list of 999,999 numbers if it stored all the numbers in memory. This would consume a lot of memory and could slow down your program or even cause it to crash.
# Instead, the range just keeps track of the start, stop, and step values, and generates each number in the sequence only when you need it (i.e., when you iterate over it). This way, it uses a constant amount of memory regardless of the size of the range. 

# -> Thing of it like this : range is like a recipe for making a dish but not the actual dish itself.

# -- Now how to get the numbers from a range object?
# -> We can use the 'list()' function to convert the range object into a list
print(list(range(1,4))) # this will give you the numbers from 1 to 3 in a list format.
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
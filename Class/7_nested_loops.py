a = int(input("write number for which you want to create the number of lines in the triangle"))

# Now our outter loop will run for the number that the user will input that is 'a' here 
for i in range (1, a+1):
    # Now our inner loop will run for the number of times = the value of i at that particular time
    for j in range (1,i+1):
        print("*", end=" ")
    print(" ")
        
# --> This is how we use nested loops

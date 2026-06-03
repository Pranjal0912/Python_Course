# ------------Problem Statement----------------
# Write a program to rrotate a list by n positions to the left. Take the input of list and n from the user.


#-------------Decorator for the project--------------
Project_title = "DUPLICATE REMOVER"
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
print("-"*len(Project_title),Project_title,"-"*len(Project_title),sep = "")
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
# --------------------Core Logic---------------------

# --------------- Input from the user----------------
list = []
i=1
while True:
    value = input(f'Enter Number_{i}: ')
    if value.strip() == "":
        print(f"\033[F\033[KThe length of list is {len(list)}")
        break
    i+=1
    list = list + [int(value)]

# --------------- Rotating the list----------------
n = int(input("Enter the number of times you want to rotate the list: "))

# Method1: Using for loop
rotated = [None]*len(list)
for i in range (len(list)):
    rotated[i-n] = list[i] # This will place the element at index i in the original list to the index (i-n) in the rotated list. The negative index will wrap around to the end of the list, effectively rotating it to the left by n positions.
    
print(rotated)

# Method2: Using slicing
rotated2 = list[n:] + list[:n] # This will create a new list by concatenating the sublist of the original list starting from index n to the end of the list with the sublist of the original list starting from index 0 to index n-1. This effectively rotates the list to the left by n positions.
print(rotated2) 


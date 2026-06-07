# ------------Problem Statement----------------
# Write a program to generate all permutations of a list

#-------------Decorator for the project--------------
Project_title = "GENERATING PERMUTATIONS"
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
print("-"*len(Project_title),Project_title,"-"*len(Project_title),sep = "")
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
# --------------------Core Logic---------------------

# --------------- Input from the user----------------
list1 = []
i=1
while True:
    value = input(f'Enter Element_{i}: ')
    if value.strip() == "":
        print(f"\033[F\033[KThe length of list is {len(list1)}")
        break
    i+=1
    list1 = list1 + [value]

# ---------------- Generating permutations----------------

import itertools as it
permutations = list(it.permutations(list1))
print(f"The permutations of the list are: {permutations}")

for perm in permutations:
    print(perm)

# ------------Problem Statement----------------
# Write a program to remove duplicates from a list.


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


# -------------------Removing Duplicates----------------
newlist = []
for item in list:
    if item not in newlist:
        newlist.append(item)

print(newlist)




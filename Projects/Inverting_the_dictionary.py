# ------------Problem Statement----------------
# Write a program that interchanges the keys and values of a dictionary.


#-------------Decorator for the project--------------
from operator import inv


Project_title = "DICTIONARY INVERTER"
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
print("-"*len(Project_title),Project_title,"-"*len(Project_title),sep = "")
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )

# --------------------Core Logic---------------------

input_dict = {}
while True:
    key = input("Enter Key: ")
    if key.strip() == "":
        print(f"\033[F\033[KThank You!")
        break
    elif key in input_dict:
        print(f"\033[F\033[K-----Please enter a unique key!-----")
        continue
    else:
        value = input("Enter Value: ")
        input_dict[key]=value
        
inv_dict={}
for key, value in input_dict.items():
    if value in inv_dict:
        inv_dict[value].add(key) 
    else:
        inv_dict[value] = {key}

for i in inv_dict:
    print(f'{i} : {inv_dict[i]}')

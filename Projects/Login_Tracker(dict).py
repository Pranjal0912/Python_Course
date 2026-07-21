# ------------Problem Statement----------------
# Write a program that counts the number of times a number of users log in to the system.


#-------------Decorator for the project--------------
Project_title = "LOGIN TRACKER"
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
print("-"*len(Project_title),Project_title,"-"*len(Project_title),sep = "")
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )

# --------------------Core Logic---------------------

# Take in put from the user in a list:
input_list = []
i = 1
while True:
    value = input("Enter your name: ")
    if value.strip() == "":
        print(f"\033[F\033[KThank You!")
        break
    a = 2 if i>1 else 1
    print(f"\033[F\033[K"*a + "Welcome!")
    input_list.append(value)
    i += 1

# Create a log dictionary:
log = {}
for key in input_list:
    if key.strip().lower() in log:
        log[key.strip().lower()]+=1
    else:
        log[key.strip().lower()]=1

# Print the output:
for user,count in log.items():
    print(f"{user}: {count}")














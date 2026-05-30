# Take 2 inputs :- 
    # 1. Password
    # 2. Confirm Password
# Check if both the passwords are same or not
# If they are same, print "Password set successfully"
# If they are not same, print "Passwords do not match. Please try again." and if there is a case mismatch, print "Mismatch in case. Please try again."

# Take input from the user:
string1 = input("New Password: ")
string2 = input("Confirm Password: ")

# Check on the absolute values of the password:
if string1.lower() != string2.lower():
    print("Passwords do not match. Please try again.")

else:
    i = 0
    for char in string1:
        if char == string2[i]:
            i+=1
            continue
        else:
            print("Mismatch in case. Please try again.")
            break
    else: # This else block will be executed if the for loop completes without a break statement, meaning all characters matched in case.
        print("Password set successfully!")
# The above code is not an optimal solution, as it checks each character of the password one by one, which can be inefficient for long passwords. A more efficient way to check for case mismatch is to directly compare the original strings and their lowercase versions:

# SOLUTION_2: Without any loops
if string1 != string2:
    if string1.lower()==string2.lower():
        print("Mismatch in case. Please try again.")
    else:
        print("Passwords do not match. Please try again.")
else:
    print("Password set successfully!")
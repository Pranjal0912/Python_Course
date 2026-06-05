# Write a program that takes the imput from the user for Number of hours each day of a week for which a worker is working for, wages per hour and rate of increment in wage for overtime.
# Then calculate the weekly wages of the worker based on these 3 parameters

#-------------Decorator for the project--------------
Project_title = "WEEKLY WAGES CALCUALTOR"
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
print("-"*len(Project_title),Project_title,"-"*len(Project_title),sep = "")
print('-'*len(Project_title)*2, "-"*len(Project_title), sep ='' )
# --------------------Core Logic---------------------
print("Enter the work hours for each day:")
Days = ["Mon", "Tue", "Wed", "Thru", "Fri", "Sat", "Sun"]
WeeklyHours = [None]*7

payment_rate = int(input("Enter the Payment Rate:- "))
overtime = float(input("Enter the Overtime Payment Rate:- "))

for i in range(7):
    print(f'Duration of work done on {Days[i]}: ', end ="")
    WeeklyHours[i]=int(input())

time=0
Total_wages = 0
overtime_flag = False
for hours in WeeklyHours:
    if time<=40:
        sum += hours*payment_rate
        time += hours
    else:
        overtime_flag = True
        sum += hours*payment_rate*overtime

if overtime_flag:
    print(f'Here is your salary with added BONUS for your Overtime:- ${int(sum)}')
else:
    print(f'Here is your salary :- ${int(sum)}', end="")

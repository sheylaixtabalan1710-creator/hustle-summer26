# Sheyla Ixtabalan | Lab 4 | Red
# Ticket for Loop 1
ages = [17, 11, 25, 13, 9]
for age in ages:
    if age >= 13:
        print("Access Granted.")
    else:
        print("Too young.")
        #PREDICT: it will print access granted for ages 13 or rolder and too young for other ages.
#EXPLAIN: what The variable age holds each time the loop runs is the value of the current item in the ages list.
#Ticket while Loop 2
keep_checking = "yes"
while keep_checking == "yes":
    age = int(input("Enter your age: "))
    if age >= 13:
        print("Access Granted.")
    else:
        print("Too young.")
    keep_checking = input("Do you want to check another age? (yes/no): ")
#PREDICT: It will keep asking for the age until the user says no.
#EXPLAIN: The while loop is the right choice here instead of a for loop because we don't know how many times the user will want to check an age.
#Ticket 3
while True:
    age = input("Enter your age or type stop to exit: ")
    if age == "stop":
        break
    age = int(age)
    if age >= 13:
        print("Access Granted.")
    else:
        print("Too young.")
#PREDICT: It will keep asking for the age until the user types stop.
#EXPLAIN: The differnec between ticket 2's while loop and this one is that this one uses a break to exit the loop.
#Ticket funtions 4
def can_access(age):
    if age >= 13:
        return True
    else:
        return False
#PREDICT: The output looks the same as ticket 1 but whats differnet about how it works is that it uses a function to check the age instead of a loop.
#EXPLAIN: Putting the check inside a function is better than writing the if/else because it makes the code more organized.
# Ticket 5 Capstone
print(" --- StreamPass Signup Report ---")
signup_report = [22, 10, 15, 8, 19, 13]
approved = 0
for age, item in enumerate(signup_report, start=1):
    if item>= 13:
        print(f"Signup #{age}: | Age: {item} - Access Granted")
        approved += 1
    else:
        print(f"Signup #{age}: | Age: {item} - Too young")
print(f"Approved: {approved} out of {len(signup_report)}")
#PREDICT: It will print the age of each signup and whter they are too young or have access granted. There will be 4/6 approved.
#EXPLAIN: A List of every function I used to buld this funtion are loops, if/else statements, and the enumerate function.
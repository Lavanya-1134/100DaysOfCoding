#Program 1: Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

#Program 2: Print all even numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 ==0:
        print(i)

for i in range(6):
    if i == 3:
        continue
    print(i)

'''Program 3
Print the multiplication table of any number entered by the user
5 × 1 = 5
5 × 2 = 10
...
'''
num = int(input("ENter a number to print its multiplication table:"))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

'''Program 4
Find the sum of numbers from 1 to N.
Example:Enter N: 5
Output:
15'''
N = int(input("Enter N:"))
sum = 0
for i in range(1, N+1):
    sum += i
print(f"The sum of numbers from 1 to {N} is: {sum}")

'''Program 5
Print a star pattern:
*
**
***
****
*****
'''
for i in range(1, 6):
    print('*' * i)

#Program 6: Print numbers from 10 to 1 using a while loop.
i = 10
while i >= 1:
    print(i)
    i -= 1

'''Program 7
Create a simple password checker.
Keep asking the user for the password until they enter:
ResQHub123
Then print:
Access Granted
'''
password = input("Enter the password: ")
while password != "ResQHub123":
    print("Incorrect password. Try again.")
    password = input("Enter the password: ")
print("Access Granted")

'''Mini Project
Rescue Report Counter:
Ask the user:
How many rescue reports do you want to enter?
Example:3
Then use a loop to ask:
Animal Name:
Display:
Report 1 Saved
Report 2 Saved
Report 3 Saved'''

num_reports = int(input("How many rescue reports do you want to enter? "))
for i in range(1, num_reports + 1):
    animal_name = input(f"Enter the name of the animal for report {i}: ")
    print(f"Report {i} Saved")
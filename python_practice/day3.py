#Program 1: Check voting eligibility.
age = int(input("Enter Your age : "))
if age >= 18 :
    print("Congrats you are 'Eligible' to vote")
else:
    print("'Sorry' you are Not Eligible to vote")

#Program 2: Find greater number.
a= int(input("Enter num1 : "))
b= int(input("Enter num2 : "))

if (a>b):
    print("The greater nubmer is : ", a)
else:
    print("The greatedr number is : ",b)

#Program 3: Even or Odd.
number = int(input("Enter the number:"))
if number % 2 == 0 :
    print(number," is an even number")
else:
    print(number," is an odd number")

#Program 4: Positive Negative Zero.
if number > 0:
    print("Positive")

elif number == 0:
    print("Zero")

else:
    print("Negative")

#Program 5: Largest among three numbers.
a= int(input("Enter num1 : "))
b= int(input("Enter num2 : "))
c= int(input("Enter num3 : "))

if (a>b) and (a>c):
    print("The Largest nubmer is", a)
elif (b>a) and (b>c):
    print("The Largest number is", b)
else:
    print("The Largest number is", c)

#Program 6: Grade Calculator.
student_mark= int(input("Enter Your Marks : "))

if student_mark >= 85:
    print("Distinction")

elif student_mark >= 45:
    print("Pass")

else:
    print("Fail")

# Program 7: Leap Year.
# teach me

#Program 8: Simple Login.
# teach me

#⭐ Mini Project: Animal Rescue Priority System
name = input("Enter the name of animal : ")
age = int(input("Enter Your age : "))
injured = input("Enter the status injured 'Yes/No' : ")
bleeding = input("Enter the status bleeding 'Yes/No' : ")

if injured.lower() == "Yes" and bleeding.lower() == "Yes":
    print("🚨 Emergency Rescue")

elif injured.lower() == "Yes":
    print("⚠ Rescue Required")

elif bleeding.lower() == "Yes":
    print("⚠ Immediate First Aid Required")
else:
    print("✅ Animal is Safe")

# changes we use and operater two times 

name = input("Enter the name of animal : ")
age = int(input("Enter Your age : "))
injured = input("Enter the status injured 'Yes/No' : ")
bleeding = input("Enter the status bleeding 'Yes/No' : ")
walk = input("Is the animal able to walk? (Yes/No) : ")

if injured.lower() == "yes" and bleeding.lower() == "yes":
    print("🚨 Emergency Rescue")

elif injured.lower() == "yes" and walk.lower() == "no":
    print("🚑 High Priority Rescue")

elif injured.lower() == "yes":
    print("⚠ Rescue Required")

else:
    print("✅ Animal is Safe")
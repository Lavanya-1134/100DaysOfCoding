#Mini project
print("ANIMAL HEALTH REPORT")
animal_name = input("Enter the name of the animal : ")

animal_weight = int(input("Enter Weight animal : "))

medicine = int(input("Medicine : "))

medicine_required = animal_weight * medicine

print("Animal Name  : ",animal_name)
print("Weight       :",animal_weight, "kg")
print("Medicine     : ",medicine ,"ml per kg")

print("Medicine Required : ",medicine_required)

#Challenges
#Program 1: Find area of rectangle.
length = float(input("Enter the lenght : "))
width = float(input("Enter the width : "))
print("Area of Rectangle is : ",length * width)

#Program 2: Find area of circle.
r = float(input("Enter the value : "))
pi = 3.14
print("Area of Circle is : ", pi*r*r)

#Program 3: Convert Celsius to Fahrenheit.
celsius = float(input("Enter the value : "))
num1 = 9/5
num2 = 32
print("F = ", (celsius * num1) + num2)

#Program 4: Calculate BMI.
weight = float(input("Enter the weight : "))
height = float(input("Enter the height : "))
print("BMI : ", weight / (height * height))

# Program 5 
print("Animal Health Calculator")
print("BMI : ", weight / (height * height))
print("Weight       :",animal_weight, "kg")
print("Medicine     : ",medicine ,"ml per kg")
print("Medicine Required : ",medicine_required)

'''What is a variable?
it is the name given to the value

Why do we use int()?
to store the whole numbers rather than string

Why does input() return a string?
python reads input() nd return it as string as it is buit in if with mentioned int we try to store string it give ValueError

When would you use float()?
when we get decimal values

What is the difference between % and //?
%= modulus which stores remainder and // is floor decimal which stores no decimal values
'''


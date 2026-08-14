#Exercise 1 — Tuple
'''Print:
first subject
last subject
number of subjects
'''

subjects = ("Python", "Math", "Machine Learning", "DBMS")       
print(subjects[0])
print(subjects[-1])
print(len(subjects))

#Exercise 2 — Set
skills = {"Python", "SQL", "Python", "Git", "SQL"}
print(skills)
skills.add("Machine Learning")
print(skills)
skills.remove("Git")
print(skills)

#Exercise 3 — Dictionary
student = {
    "name": "Lavanya",
    "age": 20,
    "branch": "AIML",
    "college": "Your College"
}

print(student["name"])
print(student["branch"])
student["age"] = 21
print(student["age"])
student["city"] = "Mumbai"
print(student["city"])
student.pop("college")
print(student)

#MINI CHALLENGE
print("====== Student Profile ======")
student_profile = {
    "Name": "Lavanya",
    "Age": 20,
    "Branch": "AIML",
    "Skills": ["Python", "Machine Learning", "Git"]
}

name = input("Enter your name: ")
branch = input("Enter your branch: ")
print(student_profile)

'''
Q1
What's the main difference between a list and a tuple?
the common differene bet them is lists are mutable and tuples are immutable. this means u can change the values of a list but not of a tuple.

Q2
Why does this:
numbers = {1, 2, 2, 3, 3}
not contain duplicates?
set do not contain the duplicates so it automatically removes the duplicates and stores only the unique values.

Q3
How do you access "AIML" here?
student = {
    "name": "Lavanya",
    "branch": "AIML"
}
by using student["branch"] and print(student["branch"]) we can retrieve the value of "Aiml"

Q4
What's the difference between:
student["age"] = 21
it is used to update the value of the key "age" in the dictionary student to 21, while
and
student["city"] = "Mumbai"
it is used to add a new key-value pair to the dictionary student, where the key is "city" and the value is "Mumbai".

Q5 ⭐
What will this print?
skills = {"Python", "Python", "SQL"}
skills.add("Git")
skills.remove("SQL")
print(skills)
it will print the updated set and also removes the duplicates{"Python", "Git"}

'''
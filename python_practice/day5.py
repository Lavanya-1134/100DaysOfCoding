#Exercise 1 — String
name = "Lavanya Poojari"
print(name[0:7])
print(name[8:17])
print(name.upper())
print(name.lower())
print(len(name))

#Exercise 2 — String cleaning
email = "   LAVANYA@GMAIL.COM   "
print(email.strip().lower())

#Exercise 3 — List
languages = ["Python", "Java", "HTML", "CSS", "JavaScript"]
print(languages[0:5])
print(languages[4])
languages.append("C++")
languages.remove("Java")
languages.insert(2, "C#")
print(languages)
print(len(languages))

#Exercise 4 — Important ⭐
marks = [78, 92, 65, 88, 95]
print(max(marks))
print(min(marks))
print(sum(marks))
print(len(marks))
print(sum(marks)/len(marks))

#Day 5 Mini Challenge
print("Student Report")
print(input("Enter your name: "))
print(int(input("Enter your age: ")))
print(input("Enter your college: "))
print(input("Enter your Branch: "))

Skills = ["Python", "Machine Learning", "Git"]
print("The Skills You will Learn: ", Skills[0:3])




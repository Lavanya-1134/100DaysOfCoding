# Day 6 - Tuples, Sets & Dictionaries

## Topics Learned

*Tuples*
A tuple looks very similar to a list:
languages = ("Python", "Java", "C++")
The big difference?
List → can be changed
languages = ["Python", "Java", "C++"]
languages[1] = "JavaScript"
print(languages)
Tuple → cannot be changed
languages = ("Python", "Java", "C++")
languages[1] = "JavaScript"  ❌
Python will give you an error.

*Mutable vs Immutable*
📝 List = mutable (changeable)
🔒 Tuple = immutable (not changeable)

Why would we use tuples?
When you have data that shouldn't accidentally change.

*Sets*
A set is used when you want unique values.
numbers = {1, 2, 3, 4, 5}
Now watch this:
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)
You'll get something like: {1, 2, 3}
Duplicates disappear. 👀
That's the superpower of a set.
Example: Imagine you collected skills from different students:
skills = {
    "Python",
    "Python",
    "Machine Learning",
    "Python",
    "SQL"
}
print(skills)
You'll only have one "Python".

*Unique values*
List  → ordered + indexed
Tuple → ordered + indexed
Set   → unordered + unique

- Dictionaries
This one is VERY important for your future AI/ML work.
A dictionary stores:
key → value
Example:
student = {
    "name": "Lavanya",
    "age": 20,
    "branch": "AIML"
}
Think of it like a real dictionary:
"name"   → "Lavanya"
"age"    → 20
"branch" → "AIML"

Adding a new vale
student["college"] = "ABC College"
updating a value
student["age"] = 21
removing a value
student.pop("age")

Why dictionaries matter for AI/ML
You're going to see dictionaries EVERYWHERE later.
For example, API data often looks like:
response = {
    "status": "success",
    "prediction": "spam",
    "confidence": 0.94
}
Later when you work with:
APIs
JSON
Flask/FastAPI
Machine Learning predictions
LLM applications
RAG
databases
you'll constantly encounter this structure.
So don't treat dictionaries as just another Python topic.
This one deserves extra attention. 👀

- Key-value pairs
- Adding and updating dictionary values
- Removing dictionary values

## Practice

- Tuple operations
- Set operations
- Dictionary operations
- Student Profile mini challenge

## Key Learning

Lists are mutable, tuples are immutable,
sets store unique values, and dictionaries
store data as key-value pairs.
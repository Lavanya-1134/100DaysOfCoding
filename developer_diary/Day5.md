# Day 5 — Python Strings and Lists

## Today's Progress

Today I started learning about Python strings and lists.

### Concepts Covered

** String indexing **
Each character has a position called an index.
 L  a  v  a  n  y  a
 0  1  2  3  4  5  6
 Python also allows counting from the end:
  L  a  v  a  n  y  a
-7 -6 -5 -4 -3 -2 -1

*String slicing*
Slicing means taking a portion of a string.
print(name[0:3])/[:3] = Lav
print(name[3:]) = anya
print(name[:]) = Lavanya
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) = [20, 30, 40]

*String methods such as `lower()`= L:l, `upper()`=LAVANYA, `strip()`= Removes unnecessary spaces from the beginning and end., and 
`replace()`: text = "I like Python" print(text.replace("Python", "AI"))

*`len()` function*
A list stores multiple values in one variable. data = ["Lavanya", 21, 8.5, True]

*List indexing*
Just like strings, lists use indexes.
languages = ["Python", "Java", "C++"]
print(languages[0])

*Adding elements*
append()
Adds an item to the end. 
languages = ["Python", "Java"]
languages.append("C++")
print(languages) = ['Python', 'Java', 'C++']

*insert()*
Adds an item at a particular position.
languages.insert(1, "JavaScript") = ['Python', 'JavaScript', 'Java', 'C++']

*Removing elements*
remove()

*pop()*
Removes an item using its index.
languages.pop(1)

*Changing list values*
Unlike strings, lists are mutable.: That means you can change their elements.
Useful list functions
numbers = [10, 20, 30, 40]
Lengt= len(numbers)
Maximum= max(numbers)
Minimum= min(numbers)
Sum= sum(numbers)

String → immutable
List → mutable

## Reflection
String
↓
Sequence of characters
Immutable
Supports indexing and slicing

List
↓
Ordered collection
Mutable
Supports indexing and slicing
Can store different data types

Important methods:
lower()
upper()
strip()
replace()
split()

List methods:
append()
insert()
remove()
pop()

## Important Interview Questions
1. What is a string?
A string is a sequence of characters represented using quotes.

2. What is a list?
A list is an ordered, mutable collection that can store multiple values.

3. What is indexing?
Indexing is accessing an individual element using its position.

4. What is slicing?
Slicing extracts a portion of a sequence using:
[start:end]

5. Are strings mutable?
No. Strings are immutable.

6. Are lists mutable?
Yes. List elements can be changed after creation.

7. Difference between append() and insert()?
append() adds an element at the end, while insert() adds an element at a specified position.

**100 Days of Coding — Day 5/100 ✅**

# Day 3

## Topics Learned

- Boolean
- Comparison Operators
- if
- if else
- if elif else
- Logical Operators

## Realization

Today I learned how computers make decisions.
This is the first step towards making ResQHub intelligent because now the system can decide whether an animal needs emergency rescue or not.

## Confidence

⭐⭐⭐⭐☆

### Theory:
## Decision Making
This is how a computer "thinks".

Until now, our program executed every line.

From today, the computer can make decisions.

Example:
    IF animal is injured
        Show Emergency
ELSE
        Show Safe

# 1. Boolean Values
A Boolean has only two values.
.True
.False

# 2. Comparison Operators
| Operator | Meaning            |
| -------- | ------------------ |
| ==       | Equal              |
| !=       | Not Equal          |
| >        | Greater Than       |
| <        | Less Than          |
| >=       | Greater than Equal |
| <=       | Less than Equal    |


# 3. if Statement
if condition:
    statement

# 4. if else
if condition:
    statement
else:
    statement

# 5. if elif else
age = 10

if age <= 2:
    print("Baby")

elif age <= 10:
    print("Adult")

else:
    print("Old")

# 6. Logical Operators
# and: Both must be True.
age = 5
injured = True

if age > 2 and injured:
    print("Priority Rescue")

# or : One condition must be True.
if injured or age < 1:
    print("Immediate Help")

# not: opposite
logged = False

if not logged:
    print("Login First")
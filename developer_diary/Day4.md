# Day 4

## Topics Learned

- for loop
- while loop
- range()
- break
- continue
- nested loop (introduction)

## What I Learned

Today I learned how loops help avoid writing repetitive code.

I also understood how loops will help ResQHub AI process multiple rescue reports efficiently.

## Confidence

⭐⭐⭐⭐☆


### Theory

## What is a Loop?
A loop repeats a block of code
 for i in range(5):
    print("Welcome")

# 1.for loop 
for variable in sequence:
    # code
range(): generates numbers.
range(1,6)
# 2.while Loop
while condition:
    # code
count = 1
while count <= 5:
    print(count)
    count += 1
# break
Stops the loop immediately.
for i in range(10):
    if i == 5:
        break
    print(i)
# continue
Skips one iteration.
for i in range(6):
    if i == 3:
        continue
    print(i)
# 3.Nested Loop (Introduction)
for i in range(3):
    for j in range(2):
        print(i, j)

### Answer these in your diary:
# Difference between for and while.
for loop: it prints variable in sequence
while loop: it uses condition

# What does range(1,11) return?
numbers 1 to 10

# Difference between break and continue.
if we enter break then the loop stops immediately
if we enter continue the the code skips one iteration 

# Why are loops useful?
sometime the prgrammar wants to execute a group of statements or numbers multiple time
so to avoid this we use loops 

# What is a nested loop?
a loop inside a loop 
the loop outside is called outer loop
and inside is called inner loop

## Mistake I Learned From

While practicing the while loop, I initially forgot to update the loop variable.
This caused an infinite loop because the condition never became False.

I learned that when using a while loop, I should always make sure that the condition can eventually become False.
# Day 03 - Loops

## Date:
______________

---

# What is a Loop?

A loop is used to execute a block of code repeatedly.

Instead of writing the same code multiple times, we use loops to automate repetition.

Example:

```python
for i in range(5):
    print("Hello")
```

Output:

```
Hello
Hello
Hello
Hello
Hello
```

---

# Types of Loops

Python has two main types of loops:

1. for loop
2. while loop

---

# for Loop

A `for` loop is used when we know how many times we want to repeat something.

### Syntax

```python
for variable in range(start, stop, step):
    statements
```

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

---

# range()

The `range()` function generates a sequence of numbers.

## 1. range(stop)

Example:

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

---

## 2. range(start, stop)

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

---

## 3. range(start, stop, step)

Example:

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```
2
4
6
8
10
```

The third value (`step`) tells Python how much to increase or decrease the value each time.

---

# Printing in Reverse

Example:

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```
10
9
8
7
6
5
4
3
2
1
```

A negative step is used for reverse counting.

---

# while Loop

A `while` loop repeats as long as the condition is True.

### Syntax

```python
while condition:
    statements
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

# Infinite Loop

If the loop variable is not updated, the loop never ends.

Example:

```python
count = 1

while count <= 5:
    print(count)
```

This program runs forever because `count` never changes.

Always remember to update the loop variable.

Example:

```python
count += 1
```

or

```python
count -= 1
```

---

# Difference Between for and while

## for Loop

- Used when the number of repetitions is known.
- Simpler to write.
- Uses `range()`.

Example:

```python
for i in range(5):
    print(i)
```

---

## while Loop

- Used when repetitions depend on a condition.
- More flexible.
- Requires updating the loop variable.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# Programs Practiced

1. Print numbers from 1 to 10
2. Print numbers from 10 to 1
3. Print even numbers using for loop
4. Print odd numbers using for loop
5. Print your name multiple times
6. Print "Done!" after a loop
7. Print numbers using while loop
8. Reverse counting using while loop
9. Even numbers using while loop
10. Student Countdown Mini Project

---

# Key Points

- A loop repeats code.
- Python has two loops: `for` and `while`.
- `range(stop)` starts from 0.
- `range(start, stop)` includes the start but excludes the stop.
- `range(start, stop, step)` changes the increment/decrement.
- Use a negative step for reverse counting.
- `while` loops continue until the condition becomes False.
- Always update the loop variable in a `while` loop.
- Forgetting to update the variable causes an infinite loop.

---

# Day 03 Summary

✔ Learned for loop

✔ Learned range()

✔ Learned while loop

✔ Learned reverse counting

✔ Learned even and odd number programs

✔ Learned infinite loops

✔ Completed 10 Python programs

✔ Completed one mini project

---

# Next Topic

Day 04 - Functions

Topics:
- Why Functions are Needed
- Defining Functions
- Calling Functions
- Parameters
- Return Values
- Scope of Variables
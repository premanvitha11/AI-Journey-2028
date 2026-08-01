# Day 04 - Functions

## Date:
01/08/2026

---

# What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, we write it once inside a function and call it whenever needed.

Example:

```python
def greet():
    print("Hello")

greet()
```

Output:

```
Hello
```

---

# Advantages of Functions

- Code Reusability
- Better Readability
- Reduces Repetition
- Easier Debugging
- Makes Programs Modular

---

# Syntax of a Function

```python
def function_name():
    # code
```

Example:

```python
def welcome():
    print("Welcome to Python!")

welcome()
```

---

# Function with Parameters

Parameters allow us to pass values into a function.

Example:

```python
def greet(name):
    print("Hello", name)

greet("Premanvitha")
```

Output:

```
Hello Premanvitha
```

---

# Multiple Parameters

Example:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```
30
```

---

# Return Statement

The `return` keyword sends a value back to the place where the function was called.

Example:

```python
def add(a, b):
    return a + b

result = add(5, 7)

print(result)
```

Output:

```
12
```

---

# Difference Between print() and return

| print() | return |
|----------|----------|
| Displays output | Sends value back |
| Cannot be reused | Can be stored in a variable |
| Used only for displaying | Used for further calculations |

Example:

```python
def square(x):
    return x * x

num = square(5)

print(num)
```

Output:

```
25
```

---

# Calculator Using Functions

We can divide a calculator into separate functions.

```python
add()
subtract()
multiply()
divide()
```

Each function performs only one task.

---

# Even or Odd Function

Example:

```python
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

---

# Factorial Function

Factorial means the product of all positive integers from 1 to a given number.

Example:

```
5! = 5 × 4 × 3 × 2 × 1
```

Output:

```
120
```

Program:

```python
def factorial(number):
    fact = 1

    for i in range(1, number + 1):
        fact = fact * i

    return fact
```

---

# Concepts Learned Today

- Functions
- Function Syntax
- Function Calling
- Parameters
- Arguments
- Multiple Parameters
- Return Statement
- Difference between print() and return()
- Calculator using Functions
- Even/Odd Function
- Factorial Function

---

# Real-Life Examples of Functions

- Calculator App
- ATM Machine
- Login System
- Food Delivery App
- Banking Software
- AI Applications
- Games

---

# Interview Questions

### 1. What is a function?

A function is a reusable block of code that performs a specific task.

---

### 2. Why do we use functions?

To avoid repetition, improve readability, and organize code.

---

### 3. What is the difference between a parameter and an argument?

Parameter:
Variable written in the function definition.

Argument:
Actual value passed while calling the function.

Example:

```python
def greet(name):      # name is a parameter
    print(name)

greet("Premanvitha")  # "Premanvitha" is an argument
```

---

### 4. What is the purpose of the return statement?

It sends a value back from a function so it can be stored or used later.

---

### 5. Which is better: print() or return()?

`return()` is generally preferred because the returned value can be reused in other calculations or functions.

---

# Summary

Today I learned how to create and use functions in Python. I learned about parameters, arguments, return statements, calculator functions, even/odd checking, and factorial. Functions help make programs reusable, modular, and easier to maintain.
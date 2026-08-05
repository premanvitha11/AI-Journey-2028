# 🐍 Python Day 08 - File Handling, Modules & OOP (Introduction)

**Date:** 05-08-2026

---

# 📚 Topics Covered

- File Handling
- File Modes
- Modules
- Creating Custom Modules
- Object-Oriented Programming (OOP)
- Classes
- Objects
- Constructors
- Methods

---

# 📖 File Handling

Used to store data permanently in files.

## Write to a File

```python
file = open("sample.txt", "w")

file.write("Hello Python!")

file.close()
```

---

## Read from a File

```python
file = open("sample.txt", "r")

print(file.read())

file.close()
```

---

## Append to a File

```python
file = open("sample.txt", "a")

file.write("\nNew Line")

file.close()
```

---

## Using with open()

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

Automatically closes the file.

---

## Read Line by Line

```python
with open("sample.txt", "r") as file:

    for line in file:
        print(line.strip())
```

---

# File Modes

| Mode | Purpose |
|------|---------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |

---

# 📖 Modules

A module is a Python file containing reusable code.

---

## math Module

```python
import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)
```

---

## random Module

```python
import random

print(random.randint(1,10))
```

---

## datetime Module

```python
import datetime

print(datetime.datetime.now())
```

---

## Custom Module

### my_module.py

```python
def greet(name):
    print("Hello", name)

def square(num):
    return num * num
```

### use_module.py

```python
import my_module

my_module.greet("Premanvitha")

print(my_module.square(5))
```

---

# 📖 Object-Oriented Programming

OOP helps organize code using classes and objects.

---

## Creating a Class

```python
class Student:
    pass
```

---

## Constructor

```python
class Student:

    def __init__(self, name):

        self.name = name
```

---

## Creating Objects

```python
student = Student("Premanvitha")
```

---

## Methods

```python
class Student:

    def greet(self):

        print("Hello")
```

---

## Multiple Objects

```python
student1 = Student("Premanvitha")
student2 = Student("Rahul")
```

Each object has its own data.

---

# Key Concepts

- Class → Blueprint
- Object → Instance of a class
- self → Current object
- __init__() → Constructor
- Method → Function inside a class

---

# Programs Completed

1. write_file.py
2. read_file.py
3. append_file.py
4. with_open.py
5. read_lines.py
6. math_module.py
7. random_module.py
8. datetime_module.py
9. my_module.py
10. use_module.py
11. intro_class.py
12. student_class.py
13. student_method.py
14. multiple_objects.py
15. calculator_class.py

Total Programs: 15

---

# Next Topic

Day 09

- List Comprehensions
- Lambda Functions
- map()
- filter()
- zip()
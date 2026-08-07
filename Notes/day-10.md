# 🐍 Python Day 10 - Iterators, Generators, Decorators, Virtual Environments & pip

**Date:** 07-08-2026

---

# 📚 Topics Covered

- Iterators
- Generators
- Decorators
- Virtual Environments (venv)
- pip
- requirements.txt

---

# 📖 Iterators

An iterator is an object that allows you to access elements one at a time.

## Creating an Iterator

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output

```
10
20
30
```

---

## StopIteration

When there are no more elements, `next()` raises a `StopIteration` exception.

```python
numbers = [1, 2]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

---

## Iterator with Loop

```python
fruits = ["Apple", "Banana", "Mango"]

iterator = iter(fruits)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
```

---

## String Iterator

```python
name = "Premanvitha"

iterator = iter(name)

print(next(iterator))
```

---

## Tuple Iterator

```python
numbers = (100, 200, 300)

iterator = iter(numbers)

for value in iterator:
    print(value)
```

---

# 📖 Generators

A generator is a function that returns values one at a time using `yield`.

## Basic Generator

```python
def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))
```

---

## Generator with Loop

```python
def fruits():
    yield "Apple"
    yield "Banana"
    yield "Mango"

for fruit in fruits():
    print(fruit)
```

---

## Range Generator

```python
def count():
    for i in range(1, 6):
        yield i
```

---

## Square Generator

```python
def squares():
    for i in range(1, 6):
        yield i * i
```

---

## Generator Expression

```python
generator = (i for i in range(1, 6))
```

---

# 📖 return vs yield

| return | yield |
|--------|--------|
| Returns all values at once | Returns one value at a time |
| Function ends | Function pauses and resumes |
| Uses more memory | Uses less memory |

---

# 📖 Decorators

A decorator adds extra functionality to a function without changing its original code.

---

## Simple Decorator

```python
def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper
```

---

## Using @ Syntax

```python
@decorator
def greet():
    print("Hello")
```

---

## Timer Decorator

```python
import time

def timer(func):

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print(end - start)

    return wrapper
```

---

## Login Decorator

```python
@login_required
def dashboard():
    print("Dashboard")
```

---

# 📖 Virtual Environment (venv)

A virtual environment creates an isolated Python environment for a project.

Create a virtual environment

```bash
python3 -m venv venv
```

Activate (macOS/Linux)

```bash
source venv/bin/activate
```

Deactivate

```bash
deactivate
```

---

# 📖 pip

Install a package

```bash
pip install requests
```

View installed packages

```bash
pip list
```

Save dependencies

```bash
pip freeze > requirements.txt
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📖 requirements.txt

Stores all project dependencies with their versions.

Example

```text
requests==2.32.5
```

---

# 📖 .gitignore

Used to ignore files and folders that should not be uploaded to GitHub.

Example

```text
venv/
__pycache__/
*.pyc
```

---

# Programs Completed

1. basic_iterator.py
2. stop_iteration.py
3. iterator_loop.py
4. string_iterator.py
5. tuple_iterator.py
6. basic_generator.py
7. generator_loop.py
8. range_generator.py
9. square_generator.py
10. generator_vs_list.py
11. basic_function.py
12. simple_decorator.py
13. at_decorator.py
14. timer_decorator.py
15. login_decorator.py

Total Programs: 15

---

# Key Points

- `iter()` creates an iterator.
- `next()` retrieves the next element.
- `yield` creates a generator.
- Generators are memory efficient.
- Decorators extend function behavior.
- `@decorator` is cleaner syntax.
- `venv` isolates project dependencies.
- `pip` installs and manages Python packages.
- `requirements.txt` stores project dependencies.
- `.gitignore` prevents unnecessary files from being tracked.

---

# Next Topic

Day 11

- Advanced Python Revision
- Practical Python Problems
- Interview-style Coding Questions
- More LeetCode Practice
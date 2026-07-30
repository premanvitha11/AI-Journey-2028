# AI Engineer Journey 🚀

# Day 1 - Python Fundamentals

**Date:** 29 July 2026

---

## Objectives

- Set up Python development environment
- Learn Python syntax
- Understand variables and data types
- Take user input
- Display output
- Convert data types
- Learn arithmetic and comparison operators
- Write first Python programs

---

# Topics Covered

## 1. Variables

Variables are containers used to store data.

Example:

```python
name = "Premanvitha"
age = 20
cgpa = 7.34
```

---

## 2. Data Types

| Type | Example |
|------|---------|
| str | "Hello" |
| int | 20 |
| float | 7.34 |
| bool | True |

---

## 3. Input

```python
name = input("Enter your name: ")
```

- `input()` always returns a string.

---

## 4. Output

```python
print("Hello World")
print(name)
```

---

## 5. Type Conversion

```python
age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))
```

Used to convert strings into numbers.

---

## 6. type()

```python
print(type(age))
```

Displays the datatype of a variable.

---

## 7. Arithmetic Operators

| Operator | Meaning |
|----------|---------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| // | Floor Division |
| % | Modulus |
| ** | Power |

---

## 8. Comparison Operators

| Operator | Meaning |
|----------|---------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

Returns either `True` or `False`.

---

## 9. if-else

Basic decision making.

Example:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

---

# Programs Completed

- day-01.py
- student_details.py
- operators.py
- eligibility.py

---

# Errors Faced

### Error

```
zsh: command not found: python
```

### Reason

macOS uses `python3` instead of `python`.

### Solution

Run programs using:

```bash
python3 filename.py
```

or use **Run Python File** in VS Code.

---

# New Functions Learned

- print()
- input()
- int()
- float()
- type()

---

# Key Learnings

- Variables store values.
- `input()` always returns a string.
- Use `int()` and `float()` for numeric input.
- Comparison operators return `True` or `False`.
- `if` statements execute code only when the condition is true.
- Reading error messages helps in debugging.

---

# Day 1 Status

✅ Completed
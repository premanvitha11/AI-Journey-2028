# 🐍 Python Day 07 - Tuples, Sets & Exception Handling

**Date:** 04-08-2026

---

# 📚 Topics Covered

- Tuples
- Tuple Methods
- Tuple Unpacking
- Sets
- Set Operations
- Exception Handling
- try, except, finally

---

# 📖 Tuples

A tuple is an ordered and immutable collection.

```python
numbers = (10, 20, 30, 40)

print(numbers)
```

---

## Accessing Elements

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])
print(fruits[2])
```

---

## Tuple Methods

```python
numbers = (10,20,30,20,40)

print(numbers.count(20))

print(numbers.index(30))
```

---

## Tuple Unpacking

```python
student = ("Premanvitha","EEE",3)

name, branch, year = student

print(name)
print(branch)
print(year)
```

---

# Tuple vs List

## List

- Mutable
- Uses []

## Tuple

- Immutable
- Uses ()

---

# 📖 Sets

A set stores only unique values.

```python
numbers = {10,20,20,30,40}

print(numbers)
```

Duplicates are removed automatically.

---

## Add Elements

```python
fruits = {"Apple","Banana"}

fruits.add("Orange")
```

---

## Remove Elements

```python
fruits.remove("Banana")
```

---

## Set Operations

```python
A = {1,2,3}

B = {3,4,5}

print(A.union(B))

print(A.intersection(B))

print(A.difference(B))
```

---

## Membership

```python
colors = {"Red","Green","Blue"}

print("Green" in colors)
```

---

# 📖 Exception Handling

Used to prevent programs from crashing.

---

## try and except

```python
try:
    num = int(input())

    print(100/num)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## Multiple Exceptions

```python
try:
    num = int(input())

    print(100/num)

except ZeroDivisionError:
    print("Division by zero")

except ValueError:
    print("Invalid input")
```

---

## finally

```python
try:
    print(10/0)

except:
    print("Error")

finally:
    print("Program Finished")
```

---

## Generic Exception

```python
try:
    value = int(input())

except Exception as e:
    print(e)
```

---

# Key Points

## Tuple

- Ordered
- Immutable

## Set

- Unordered
- Unique values
- Fast membership checking

## Exception Handling

- try
- except
- finally
- Exception

---

# Programs Completed

- intro_tuple.py
- access_tuple.py
- tuple_methods.py
- tuple_unpacking.py
- intro_set.py
- duplicate_values.py
- add_remove_set.py
- set_operations.py
- membership_set.py
- basic_exception.py
- try_except.py
- multiple_exceptions.py
- finally_block.py
- generic_exception.py

Total Programs: 14

---

# Next Topic

Day 08

- File Handling
- Modules
- OOP (Introduction)
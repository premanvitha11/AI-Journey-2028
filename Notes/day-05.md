# 🐍 Python Day 05 - Lists, Nested Lists & Strings (Part 1)

**Date:** 02-08-2026

---

# 📌 What I Learned Today

- Lists
- Accessing Elements
- Modifying Lists
- List Methods
- Loops with Lists
- Sum of List
- Largest Number in a List
- List Slicing
- Nested Lists
- Introduction to Strings
- String Indexing
- String Slicing

---

# 📖 1. Lists

A list is a collection of multiple values stored in a single variable.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]
```

Lists are:

- Ordered
- Mutable (can be changed)
- Allow duplicate values

---

# 📖 2. Accessing Elements

Lists use indexing.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Output

```
Apple
Banana
Mango
```

Negative Indexing

```python
print(fruits[-1])
```

Output

```
Mango
```

---

# 📖 3. Modifying Lists

Lists are mutable.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)
```

Output

```
['Apple', 'Orange', 'Mango']
```

---

# 📖 4. List Methods

## append()

Adds an element to the end.

```python
numbers.append(50)
```

---

## insert()

Adds an element at a specified index.

```python
numbers.insert(1,100)
```

---

## remove()

Removes an element by value.

```python
numbers.remove(20)
```

---

## pop()

Removes an element using its index.

```python
numbers.pop(2)
```

---

## sort()

Sorts the list.

```python
numbers.sort()
```

---

# 📖 5. Looping Through Lists

```python
fruits = ["Apple","Banana","Mango"]

for fruit in fruits:
    print(fruit)
```

Output

```
Apple
Banana
Mango
```

---

# 📖 6. Sum of List

```python
numbers = [10,20,30,40]

total = 0

for number in numbers:
    total += number

print(total)
```

Output

```
100
```

---

# 📖 7. Largest Number in a List

```python
numbers = [10,80,25,40]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
```

Output

```
80
```

---

# 📖 8. List Slicing

Syntax

```python
list[start:end]
```

Remember:

- Start Index → Included
- End Index → Excluded

Examples

```python
numbers[1:4]

numbers[:3]

numbers[2:]

numbers[-3:]

numbers[::2]
```

---

# 📖 9. Nested Lists

Lists can contain other lists.

Example

```python
students = [
    ["Rahul",20],
    ["Anjali",21],
    ["Premanvitha",19]
]
```

Accessing values

```python
print(students[0])
print(students[2][0])
print(students[2][1])
```

Output

```
['Rahul',20]

Premanvitha

19
```

---

# 📖 10. Introduction to Strings

A string is a sequence of characters enclosed in quotes.

```python
name = "Premanvitha"
```

Strings are

- Ordered
- Immutable

Example

```python
print(type(name))
```

Output

```
<class 'str'>
```

---

# 📖 11. String Indexing

```python
language = "Python"

print(language[0])
print(language[-1])
```

Output

```
P
n
```

---

# 📖 12. String Slicing

```python
language = "Python"

print(language[0:2])

print(language[2:])

print(language[:4])

print(language[-3:])
```

Output

```
Py

thon

Pyth

hon
```

---

# ⭐ Difference Between Lists and Strings

| Lists | Strings |
|--------|----------|
| Mutable | Immutable |
| [] | "" or '' |
| Can modify elements | Cannot modify characters |
| Stores any data type | Stores characters |

---

# 🎯 Important Concepts Learned

✅ Lists store multiple values.

✅ Indexing starts from 0.

✅ Negative indexing starts from the end.

✅ Lists are mutable.

✅ Strings are immutable.

✅ Slicing extracts a portion of a list or string.

✅ for loops help iterate through lists.

✅ Nested lists store lists inside another list.

---

# 📝 Programs Completed Today

- intro_lists.py
- access_elements.py
- modify_list.py
- list_methods.py
- for_loop_lists.py
- sum_of_list.py
- largest_number.py
- mini_challenge.py
- mini_challenge2.py
- list_slicing.py
- nested_lists.py
- intro_strings.py
- string_indexing.py
- string_slicing.py

**Total Programs:** 14

---

# 🚀 Key Takeaways

- Learned how to work with lists efficiently.
- Understood indexing and slicing.
- Learned common list methods.
- Practiced loops with lists.
- Found the sum and largest value in a list.
- Learned nested lists.
- Started learning strings and their similarities with lists.
- Understood that strings are immutable.

---

# 🎯 Next Topic

Day 06

- String Methods
- Reverse String
- Count Vowels
- Palindrome
- Dictionaries
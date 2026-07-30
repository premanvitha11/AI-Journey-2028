# Day 02 - Strings & Conditional Statements

## Date:
30 July 2026

---

# 1. Strings

A string is a sequence of characters enclosed in single or double quotes.

Example:

```python
name = "Premanvitha"
college = "Vignan"
```

Type of string:

```python
print(type(name))
```

Output:

```
<class 'str'>
```

---

# 2. String Indexing

Each character has an index.

Example:

```
P r e m a n v i t h a
0 1 2 3 4 5 6 7 8 9 10
```

Negative Index:

```
P r e m a n v i t h a
-11.................-1
```

Examples:

```python
name[0]
name[3]
name[-1]
```

---

# 3. String Slicing

Syntax:

```python
string[start:end]
```

Examples:

```python
name[0:6]
name[2:7]
name[-4:]
```

---

# 4. String Methods

Length

```python
len(name)
```

Uppercase

```python
name.upper()
```

Lowercase

```python
name.lower()
```

Capitalize

```python
name.capitalize()
```

Title Case

```python
college.title()
```

Remove Spaces

```python
college.strip()
```

Find Character

```python
name.find("v")
```

Count Character

```python
name.count("a")
```

---

# 5. Conditional Statements

## if

Syntax

```python
if condition:
    statement
```

Example

```python
age = 20

if age >= 18:
    print("Eligible")
```

---

## if-else

```python
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## if-elif-else

```python
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")
```

---

# 6. Logical Operators

## AND

Returns True only if all conditions are True.

Example:

```python
if cgpa >= 7.5 and attendance >= 75:
    print("Eligible")
```

---

## OR

Returns True if at least one condition is True.

Example:

```python
if age < 12 or student == "yes":
    print("Discount")
```

---

## NOT

Reverses the Boolean value.

Example:

```python
logged_in = False

if not logged_in:
    print("Please Login")
```

---

# Programs Practiced

1. Strings
2. String Indexing
3. String Slicing
4. String Methods
5. Grade System
6. Scholarship Program
7. Movie Discount
8. Login Program
9. Placement Eligibility Checker

---

# Key Points

• Strings are immutable.

• Indexing starts from 0.

• Negative indexing starts from -1.

• Slicing extracts a part of a string.

• if checks a condition.

• elif checks another condition if the previous one is False.

• else executes when all conditions are False.

• and requires all conditions to be True.

• or requires at least one condition to be True.

• not reverses a Boolean value.

---

# Day 02 Summary

✔ Learned Strings

✔ Learned String Methods

✔ Learned Indexing & Slicing

✔ Learned Conditional Statements

✔ Learned Logical Operators

✔ Completed 9 Python Programs

---

Next Topic:
Day 03 - Loops (for, while, range, nested loops, pattern printing)
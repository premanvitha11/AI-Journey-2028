# 🐍 Python Day 06 - Strings & Dictionaries

**Date:** 03-08-2026

---

# 📚 Topics Covered

- String Methods
- Reverse String
- Count Vowels
- Palindrome
- Dictionaries
- Dictionary Methods
- Looping Through Dictionaries
- get() Method
- Removing Dictionary Elements

---

# 📖 String Methods

## len()

Returns the length of a string.

```python
text = "Python"

print(len(text))
```

---

## upper()

Converts all characters to uppercase.

```python
print(text.upper())
```

---

## lower()

Converts all characters to lowercase.

```python
print(text.lower())
```

---

## strip()

Removes leading and trailing spaces.

```python
text = "  Python  "

print(text.strip())
```

---

## replace()

Replaces part of a string.

```python
text = "I like Java"

print(text.replace("Java","Python"))
```

---

## find()

Returns the index of the first occurrence.

```python
text = "Programming"

print(text.find("g"))
```

Returns -1 if not found.

---

## count()

Counts the occurrences of a character.

```python
text = "banana"

print(text.count("a"))
```

---

## split()

Splits a string into a list.

```python
sentence = "Python is easy"

print(sentence.split())
```

---

# 📖 Reverse String

Using slicing

```python
text = "Python"

print(text[::-1])
```

Using loop

```python
reverse = ""

for ch in text:
    reverse = ch + reverse

print(reverse)
```

---

# 📖 Count Vowels

```python
text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print(count)
```

---

# 📖 Palindrome

```python
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

# 📖 Dictionaries

Dictionary stores data in key-value pairs.

```python
student = {
    "name":"Premanvitha",
    "branch":"EEE",
    "cgpa":7.34
}
```

---

# Access Values

```python
print(student["name"])
```

---

# Modify Values

```python
student["cgpa"] = 7.5
```

---

# Add New Key

```python
student["year"] = 3
```

---

# Dictionary Methods

```python
student.keys()

student.values()

student.items()
```

---

# Loop Through Dictionary

```python
for key in student:
    print(key, student[key])
```

Using items()

```python
for key, value in student.items():
    print(key, value)
```

---

# get() Method

```python
print(student.get("name"))

print(student.get("age"))

print(student.get("age","Not Available"))
```

---

# Remove Elements

```python
student.pop("cgpa")
```

or

```python
del student["cgpa"]
```

---

# Important Differences

## List

- Ordered
- Mutable
- Uses Index

## Dictionary

- Key-Value Pairs
- Mutable
- Uses Keys instead of Index

---

# Programs Completed

- string_methods.py
- reverse_string.py
- reverse_string_loop.py
- count_vowels.py
- palindrome.py
- intro_dictionary.py
- access_dictionary.py
- modify_dictionary.py
- add_dictionary.py
- dictionary_methods.py
- loop_dictionary.py
- dictionary_items.py
- get_method.py
- remove_dictionary.py

Total Programs: 14

---

# Key Takeaways

- Strings support many built-in methods.
- Slicing can reverse a string.
- Dictionaries store information as key-value pairs.
- get() is safer than direct indexing.
- items() is useful when looping through dictionaries.

---

# Next Topic

Day 07

- Tuples
- Sets
- Exception Handling
- File Handling (Introduction)
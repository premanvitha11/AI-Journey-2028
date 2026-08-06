# 🐍 Python Day 09 - List Comprehensions, Lambda Functions, map(), filter(), zip()

**Date:** 06-08-2026

---

# 📚 Topics Covered

- List Comprehensions
- Lambda Functions
- map()
- filter()
- zip()

---

# 📖 List Comprehensions

A shorter way to create lists.

## Basic Example

```python
numbers = [i for i in range(1,6)]

print(numbers)
```

Output

```
[1,2,3,4,5]
```

---

## Squares

```python
squares = [i*i for i in range(1,6)]

print(squares)
```

---

## Even Numbers

```python
even = [i for i in range(1,21) if i%2==0]

print(even)
```

---

## Convert to Uppercase

```python
names = ["rahul","priya","ravi"]

upper = [name.upper() for name in names]

print(upper)
```

---

## Filter Long Words

```python
words = ["cat","elephant","dog","python"]

long_words = [word for word in words if len(word)>3]

print(long_words)
```

---

# 📖 Lambda Functions

Anonymous one-line functions.

Syntax

```python
lambda arguments : expression
```

---

## Square

```python
square = lambda x: x*x

print(square(5))
```

---

## Addition

```python
add = lambda a,b:a+b

print(add(10,20))
```

---

## Maximum

```python
maximum = lambda a,b:a if a>b else b

print(maximum(20,15))
```

---

## Sorting

```python
students.sort(key=lambda x:x[1])
```

---

# 📖 map()

Applies a function to every element.

```python
numbers = [1,2,3,4]

result = list(map(lambda x:x*x,numbers))

print(result)
```

---

# 📖 filter()

Keeps elements satisfying a condition.

```python
numbers=[1,2,3,4,5,6]

even=list(filter(lambda x:x%2==0,numbers))

print(even)
```

---

# 📖 zip()

Combines multiple iterables.

```python
names=["Rahul","Priya"]

marks=[85,92]

students=list(zip(names,marks))

print(students)
```

---

## Unzip

```python
names,marks = zip(*students)
```

---

# Combined Example

```python
numbers=[1,2,3,4,5,6]

result=list(
map(lambda x:x*x,
filter(lambda x:x%2==0,numbers))
)

print(result)
```

---

# Key Points

## List Comprehension

- Shorter syntax
- Cleaner code

## Lambda

- Anonymous function
- One-line function

## map()

- Applies function to every element

## filter()

- Keeps matching elements

## zip()

- Combines multiple iterables

---

# Programs Completed

1. basic_list_comprehension.py
2. square_list.py
3. even_numbers.py
4. uppercase_names.py
5. long_words.py
6. basic_lambda.py
7. add_lambda.py
8. max_lambda.py
9. sort_lambda.py
10. lambda_string.py
11. map_function.py
12. filter_function.py
13. zip_function.py
14. unzip_function.py
15. combined_example.py

Total Programs: 15

---

# Next Topic

Day 10

- Iterators
- Generators
- Decorators (Introduction)
- Virtual Environments (venv)
- pip (Package Management)
# 🐍 Python Day 11 — Revision & Problem Solving

**Date:** 08-08-2026

---

## 🎯 Day 11 Goal

Day 11 was a **Python revision and problem-solving day**.

Instead of learning new Python concepts, I revised previously learned concepts by solving small programming exercises and beginner-level LeetCode problems.

---

# 💻 Python Practice

## 1. Count Vowels

Revised strings, loops, conditions, and the `in` operator.

```python
text = "hello world"

count = 0

for char in text:
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)
```

Output:

```text
Number of vowels: 3
```

---

## 2. Find Largest Number

Revised lists, loops, and conditions.

```python
numbers = [10, 20, 30, 40, 50]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
```

Output:

```text
50
```

---

## 3. Reverse a String

Revised strings and loops.

```python
text = "python"

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)
```

Output:

```text
nohtyp
```

---

## 4. Count Frequency

Revised dictionaries, loops, and conditions.

```python
numbers = [1, 2, 2, 3, 1, 2, 4]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)
```

Output:

```text
{1: 2, 2: 3, 3: 1, 4: 1}
```

---

## 5. Remove Duplicates

Revised lists, loops, conditions, and `append()`.

```python
numbers = [1, 2, 2, 3, 1, 4, 3]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
```

Output:

```text
[1, 2, 3, 4]
```

---

# 🧩 LeetCode Practice

## LeetCode #1672 — Richest Customer Wealth

Practiced nested lists, nested loops, and calculating totals.

```python
class Solution:
    def maximumWealth(self, accounts):
        richest = 0

        for customer in accounts:
            total = 0

            for money in customer:
                total += money

            if total > richest:
                richest = total

        return richest
```

**Status:** ✅ Completed

---

## LeetCode #1431 — Kids With the Greatest Number of Candies

Practiced lists, loops, conditions, `max()`, Boolean values, and `append()`.

```python
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        greatest = max(candies)

        result = []

        for candy in candies:
            if candy + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)

        return result
```

**Status:** ✅ Completed

---

# 🧠 What I Revised Today

Through the five practice programs and two LeetCode problems, I revised:

- Strings
- Lists
- Dictionaries
- Loops
- Conditions
- Nested lists
- `append()`
- `max()`
- Basic problem-solving

The focus was on **applying concepts already learned rather than learning new Python topics**.

---

# 📌 Day 11 Summary

- ✅ Python revision
- ✅ 5 practice programs completed
- ✅ LeetCode #1672 completed
- ✅ LeetCode #1431 completed
- ✅ Practiced basic problem-solving

---

# 🚀 Next Step

**Day 12 — Introduction to DSA**

Starting with:

- Arrays
- Array traversal
- Basic array operations
- Searching
- Time complexity
- Beginner-level array problems
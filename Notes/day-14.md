# Day 14 — Basic Maths for DSA

## 📚 Topic: Basic Maths

Started the **Basic Maths** section from Striver's DSA Sheet.

### 1. Extraction of Digits

Learned how to extract digits from an integer.

#### Get the last digit

```python
digit = x % 10
```

Example:

```text
1234 % 10 = 4
```

#### Remove the last digit

```python
x = x // 10
```

Example:

```text
1234 // 10 = 123
```

### 🔄 Digit Extraction Pattern

For a number like `1234`:

```text
1234 → 123 → 12 → 1 → 0
```

At each step:

```python
digit = x % 10
x = x // 10
```

---

## 2. Building a Number in Reverse

Learned how to construct a reversed number digit by digit:

```python
rev = rev * 10 + digit
```

Example for `123`:

```text
rev = 0

digit = 3 → rev = 3
digit = 2 → rev = 32
digit = 1 → rev = 321
```

---

## 💻 LeetCode Practice

### LeetCode #7 — Reverse Integer

**Problem:** Reverse the digits of a signed integer.

Examples:

```text
123   → 321
-123  → -321
120   → 21
```

### Concepts Used

* `% 10` → Extract last digit
* `// 10` → Remove last digit
* `rev * 10 + digit` → Build reversed number
* `abs()` → Handle negative numbers
* Sign handling
* 32-bit integer overflow

### Final Solution

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x != 0:
            digit = x % 10
            x = x // 10
            rev = rev * 10 + digit

        rev = sign * rev

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev
```

---

## 🧠 Key Takeaways

```text
x % 10        → Get last digit
x // 10       → Remove last digit
rev * 10      → Shift digits left
rev + digit   → Add new digit
```

### DSA Pattern Learned

**Digit Manipulation / Number Extraction**

This pattern will be useful in many Basic Maths problems involving integers and their digits.

## ✅ Day 14 Completed

* [x] Started Basic Maths
* [x] Learned digit extraction
* [x] Learned number reversal pattern
* [x] Solved LeetCode #7 — Reverse Integer
* [x] Understood overflow handling

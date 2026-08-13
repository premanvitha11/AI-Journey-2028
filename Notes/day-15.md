# Day 15 — DSA: Basic Maths

**Date: August 12, 2026**

Today I continued my DSA preparation by studying the Basic Maths section of Striver's DSA Sheet.

I completed the topics Palindrome Number, GCD of Two Numbers, and the Euclidean Algorithm. I practiced these concepts using Python and focused on understanding the logic behind each problem.

## 1. Palindrome Number

A palindrome number is a number that remains the same when its digits are reversed.

Examples:

- 121 → Palindrome
- 1221 → Palindrome
- 123 → Not a palindrome
- 10 → Not a palindrome

### Approach

To check whether a number is a palindrome:

1. Store the original number.
2. Reverse the number digit by digit.
3. Compare the reversed number with the original number.
4. If both are equal, the number is a palindrome.

### Important Logic

To extract the last digit:

    digit = n % 10

To remove the last digit:

    n = n // 10

To construct the reversed number:

    reverse = reverse * 10 + digit

### Example

For:

    121

The reversed number is:

    121

Since:

    121 == 121

the number is a palindrome.

## 2. GCD of Two Numbers

GCD stands for Greatest Common Divisor.

The GCD of two numbers is the largest positive number that divides both numbers exactly.

Example:

    12 and 18

Factors of 12:

    1, 2, 3, 4, 6, 12

Factors of 18:

    1, 2, 3, 6, 9, 18

Common factors:

    1, 2, 3, 6

Therefore:

    GCD = 6

### Basic Approach

I learned the basic approach of checking all possible numbers from 1 up to the smaller of the two numbers.

A number is a common divisor if:

    a % i == 0 and b % i == 0

The largest common divisor is the GCD.

### Example

For:

    a = 12
    b = 18

The answer is:

    GCD = 6

## 3. Euclidean Algorithm

The Euclidean Algorithm is an efficient method for finding the GCD of two numbers.

The main formula is:

    gcd(a, b) = gcd(b, a % b)

The process continues until the second number becomes 0.

At that point, the first number is the GCD.

### Example

Find the GCD of:

    48 and 18

Step 1:

    48 % 18 = 12

Therefore:

    gcd(48, 18) = gcd(18, 12)

Step 2:

    18 % 12 = 6

Therefore:

    gcd(18, 12) = gcd(12, 6)

Step 3:

    12 % 6 = 0

Therefore:

    GCD = 6

### Python Logic

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

When b becomes 0, a contains the GCD.

## Key Concepts Learned Today

- Palindrome numbers
- Reversing a number
- Extracting digits using %
- Removing digits using //
- GCD
- Common divisors
- Basic GCD approach
- Euclidean Algorithm
- Modulo operation
- Integer division
- While loops
- Efficient problem-solving

## Important Formulas

### Extract Last Digit

    digit = n % 10

### Remove Last Digit

    n = n // 10

### Reverse a Number

    reverse = reverse * 10 + digit

### Euclidean Algorithm

    gcd(a, b) = gcd(b, a % b)

## Practice Files

I practiced the following programs today:

1. 1_palindrome_number.py
2. 2_gcd_two_numbers.py
3. 3_gcd_euclidean_algorithm.py

All files are stored inside:

    DSA/DAY-15/

## What I Learned

Today I learned how to approach basic mathematical problems using loops, conditions, modulo, and integer division.

I understood how to reverse a number and use the reversed value to check whether a number is a palindrome.

I also learned the concept of GCD and first understood the basic approach of checking common divisors.

After understanding the basic approach, I learned the more efficient Euclidean Algorithm and understood how repeatedly taking the remainder helps find the GCD efficiently.

## Day 15 Summary

Today I completed the Basic Maths topics from Striver's DSA Sheet:

- Palindrome Number
- GCD of Two Numbers
- Euclidean Algorithm

I practiced the concepts in Python and focused on understanding the mathematical logic behind each problem instead of memorizing the code.

## Day 15 Completed

- ✅ Learned Palindrome Number
- ✅ Practiced reversing a number
- ✅ Learned GCD of two numbers
- ✅ Practiced the basic GCD approach
- ✅ Learned the Euclidean Algorithm
- ✅ Practiced modulo and integer division
- ✅ Implemented all concepts using Python

**Day 15 completed successfully.** 🚀
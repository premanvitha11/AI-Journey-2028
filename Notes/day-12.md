# Day 12 — DSA: Pattern Problems and LeetCode

Today I officially started my DSA preparation. I began with pattern problems to understand nested loops and improve my logical problem-solving skills. I practiced the patterns using Python and then solved a beginner-level array problem on LeetCode.

## DSA Pattern Practice

I learned the basic approach to solving pattern problems by identifying:

- Number of rows
- Number of elements in each row
- Number of spaces
- Number of stars or numbers
- Relationship between the row number and the number of elements

I learned that the outer loop generally controls the rows, while the inner loop controls the elements printed in each row.

Basic structure:

```python
for i in range(n):
    for j in range(...):
        print(...)
    print()

For increasing patterns, the number of elements generally increases using:

i + 1

For decreasing patterns, the number of elements can be controlled using:

n - i

For centered pyramid patterns, I learned to calculate spaces and stars separately.

Common formulas:

Spaces = n - i - 1
Stars = 2 * i + 1

For reversed centered patterns:

Spaces = i
Stars = 2 * (n - i) - 1

I practiced 10 pattern problems:

Square pattern
Right triangle
Number triangle
Same number repeated in each row
Inverted triangle
Inverted number triangle
Centered pyramid
Reversed centered pyramid
Diamond pattern
Increasing and decreasing triangle

All the pattern programs were practiced in Python and saved under:

DSA/DAY-01/DAY-12/
What I Learned from Patterns
How nested loops work.
How the outer loop controls rows.
How the inner loop controls columns/elements.
How to increase the number of elements in each row.
How to decrease the number of elements in each row.
How to repeat the same number in a row.
How to use spaces to create centered patterns.
How to create pyramids and reversed pyramids.
How to combine two patterns to create a diamond or increasing-decreasing pattern.
How to derive pattern logic instead of simply memorizing code.
LeetCode Practice

After completing the pattern practice, I started solving beginner-level DSA problems on LeetCode.

LeetCode #1470 — Shuffle the Array

The problem gives an array nums and an integer n.

Example:

nums = [2, 5, 1, 3, 4, 7]
n = 3

Since n = 3, the array is divided into two halves:

First half  → [2, 5, 1]
Second half → [3, 4, 7]

The elements need to be arranged alternately:

2, 3, 5, 4, 1, 7

Therefore, the output is:

[2, 3, 5, 4, 1, 7]
Approach

For every index from 0 to n - 1:

Take the element from the first half.
Take the corresponding element from the second half.
Add both elements to the result alternately.

The important indexing idea is:

nums[i]       → element from the first half
nums[n + i]   → corresponding element from the second half
Solution
class Solution:
    def shuffle(self, nums, n):
        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])

        return result
Example

For:

nums = [2, 5, 1, 3, 4, 7]
n = 3

The loop works as:

i = 0 → 2, 3
i = 1 → 5, 4
i = 2 → 1, 7

Final result:

[2, 3, 5, 4, 1, 7]
Key Concepts Practiced Today
Nested loops
Array/list indexing
Array traversal
for loops
range()
append()
Working with two parts of an array
Basic problem-solving
Converting a problem statement into an algorithm
Reflection

Today was my first dedicated DSA practice session. I started with pattern problems to build my logical thinking and strengthen my understanding of nested loops.

I practiced 10 different patterns in Python and learned how to identify the relationship between rows, columns, spaces, and elements.

I then solved my first beginner DSA LeetCode problem, LeetCode #1470 — Shuffle the Array. This helped me apply array indexing and traversal concepts to an actual problem.

I focused on understanding the logic behind the problems rather than memorizing solutions. I will continue learning DSA through a structured course and practice the concepts using Python.

Day 12 Summary
✅ Started DSA preparation
✅ Learned basic pattern-solving concepts
✅ Practiced 10 pattern problems
✅ Practiced nested loops
✅ Learned increasing and decreasing patterns
✅ Learned centered pattern logic
✅ Practiced spaces and stars
✅ Learned basic array traversal and indexing
✅ Solved LeetCode #1470 — Shuffle the Array
✅ Practiced DSA using Python

Day 12 completed successfully.
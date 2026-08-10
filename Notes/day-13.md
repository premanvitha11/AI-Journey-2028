# Day 13 — DSA: Pattern Practice

**Date: August 10, 2026**

Today I continued my DSA preparation by practicing pattern problems using Python. I focused on understanding nested loops, row and column relationships, spaces, stars, numbers, alphabets, symmetry, and different pattern structures.

I practiced 12 different patterns today and focused on understanding the logic behind each pattern instead of memorizing the code.

## DSA Pattern Practice

The main approach I used for solving pattern problems was to identify:

- Number of rows
- Number of elements in each row
- Number of spaces
- Number of stars or numbers
- Starting and ending values
- Whether the pattern is increasing or decreasing
- Whether the pattern is centered, mirrored, hollow, or symmetrical

The basic structure of most pattern programs is:

for i in range(n):
    for j in range(...):
        print(...)
    print()

The outer loop generally controls the rows, while the inner loop controls the elements printed in each row.

## Pattern 1 — 0-1 Alternating Triangle

Pattern:

1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

I learned how to create an alternating 0-1 pattern using row and column indexes.

The expression:

(i + j + 1) % 2

can be used to alternate between 0 and 1.

### Concepts Learned

- Nested loops
- Alternating values
- Modulo operator
- Row and column relationships

## Pattern 2 — Mirrored Number Pattern

Pattern:

1            1
1 2          2 1
1 2 3        3 2 1
1 2 3 4    4 3 2 1

This pattern consists of three parts:

1. Increasing numbers
2. Middle spaces
3. Decreasing numbers

The number of spaces decreases as the row number increases.

### Concepts Learned

- Multiple inner loops
- Increasing sequences
- Decreasing sequences
- Spaces
- Symmetrical patterns

## Pattern 3 — Continuous Number Triangle

Pattern:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

I used a separate variable to maintain the current number.

The number is increased after every print using:

num += 1

### Concepts Learned

- Continuous numbering
- Maintaining a variable across loops
- Nested loops
- Incrementing values

## Pattern 4 — Alphabet Triangle

Pattern:

A
A B
A B C
A B C D
A B C D E

Each row starts from A and increases up to the required letter.

I learned how to generate alphabets using:

chr(65 + j)

### Concepts Learned

- Character generation
- ASCII values
- chr()
- Nested loops with alphabets

## Pattern 5 — Reverse Alphabet Triangle

Pattern:

A B C D E
A B C D
A B C
A B
A

The number of letters decreases in every row while the starting letter remains A.

### Concepts Learned

- Decreasing loop ranges
- Inverted patterns
- Alphabet sequences

## Pattern 6 — Repeated Letter Triangle

Pattern:

A
B B
C C C
D D D D
E E E E E

The letter changes after every row, while the same letter is repeated throughout that row.

### Concepts Learned

- Repeating values
- Row-based character selection
- Character manipulation
- Nested loops

## Pattern 7 — Alphabet Palindrome Triangle

Pattern:

A
A B A
A B C B A
A B C D C B A
A B C D E D C B A

Each row contains an increasing alphabet sequence followed by a decreasing sequence.

This creates a palindrome-like pattern.

### Concepts Learned

- Symmetrical patterns
- Increasing and decreasing sequences
- Multiple inner loops
- Alphabet manipulation

## Pattern 8 — Reverse Starting Alphabet Triangle

Pattern:

E
D E
C D E
B C D E
A B C D E

The starting letter changes for every row while the ending letter remains E.

### Concepts Learned

- Changing starting values
- Reverse starting positions
- Nested loop ranges
- Character indexing

## Pattern 9 — Hollow Hourglass

Pattern:

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

This pattern contains stars on both sides and spaces in the middle.

The number of stars decreases toward the center and increases again.

### Concepts Learned

- Hollow patterns
- Spaces
- Symmetry
- Upper and lower halves
- Combining patterns

## Pattern 10 — Butterfly Pattern

Pattern:

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

The butterfly pattern consists of two mirrored halves.

The number of stars increases toward the center and then decreases.

### Concepts Learned

- Symmetry
- Increasing and decreasing stars
- Spaces
- Upper and lower halves

## Pattern 11 — Hollow Rectangle

Pattern:

****
*  *
*  *
*  *
****

Stars are printed only on the boundary of the rectangle.

A condition is used to check whether the current position is on:

- First row
- Last row
- First column
- Last column

Otherwise, a space is printed.

### Concepts Learned

- Boundary conditions
- Hollow patterns
- Row and column conditions
- if conditions inside nested loops

## Pattern 12 — Number Square Pattern

Pattern:

4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4

The outer layer contains the largest number and the values decrease toward the center.

For n = 4, the values are:

4 → 3 → 2 → 1

The value at each position depends on its distance from the nearest boundary.

### Concepts Learned

- Nested loops
- Matrix-like patterns
- Layer-based patterns
- Minimum distance from boundaries
- Symmetry

## What I Learned Today

Today I improved my understanding of:

- Nested loops
- Row and column relationships
- Increasing patterns
- Decreasing patterns
- Inverted patterns
- Number patterns
- Alphabet patterns
- Repeated values
- Alternating values
- Palindrome patterns
- Symmetrical patterns
- Hollow patterns
- Spaces and alignment
- Boundary conditions
- Upper and lower halves of patterns
- Using ASCII values for alphabets
- Using conditions inside nested loops

## Pattern-Solving Approach

Instead of memorizing pattern programs, I learned to break each pattern into smaller parts.

For every pattern, I ask:

1. How many rows are there?
2. How many elements are printed in each row?
3. How many spaces are needed?
4. Are the elements increasing or decreasing?
5. Does the pattern have symmetry?
6. Does the pattern have an upper and lower half?
7. Are there any special boundary conditions?
8. Does the value depend on the row or column number?

This approach helps me understand and derive the logic myself.

## Practice Files

I practiced 12 pattern problems today:

1. 1_alternating_triangle_pattern.py
2. 2_mirrored_number_pattern.py
3. 3_continuousnumber_triangle.py
4. 4_alphabet_triangle.py
5. 5_reversealphabet_triangle.py
6. 6_repeatedletter_triangle.py
7. 7_alphabet_palincrometriangle.py
8. 8_reversestarting_alphabet_triangle.py
9. 9_hollow_hourglass.py
10. 10_butterfly_pattern.py
11. 11_hollow_rectangle.py
12. 12_numbers_square_pattern.py

All files are stored inside:

DSA/DAY-13/

## Day 13 Summary

Today I continued my DSA preparation by practicing 12 different pattern problems.

I strengthened my understanding of nested loops and learned how to identify the relationship between rows, columns, spaces, stars, numbers, and alphabets.

I also practiced different types of patterns including increasing, decreasing, mirrored, palindrome, hollow, symmetrical, and layer-based patterns.

The main focus was understanding the logic behind each pattern instead of simply memorizing the code.

## Day 13 Completed

- ✅ Practiced 12 DSA patterns
- ✅ Improved nested loop understanding
- ✅ Practiced number patterns
- ✅ Practiced alphabet patterns
- ✅ Practiced alternating patterns
- ✅ Practiced palindrome patterns
- ✅ Practiced symmetrical patterns
- ✅ Practiced hollow patterns
- ✅ Practiced spaces and alignment
- ✅ Practiced conditions inside nested loops
- ✅ Strengthened pattern-solving logic

Day 13 completed successfully. 🚀
numbers = [12, 7, 18, 5, 20, 9]

count = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1

print("Even numbers =", count)
numbers = [25, 40, 10, 75, 60]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest =", largest)
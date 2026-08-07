fruits = ["Apple", "Banana", "Mango"]

iterator = iter(fruits)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
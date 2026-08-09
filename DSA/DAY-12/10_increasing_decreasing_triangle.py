n = 5
#increasing part
for i in range(n):
    for j in range(i + 1):
        print("*", end = " ")
    print()
#decreasing part
for i in range(n - 1):
    for j in range(n - i - 1):
        print("*", end = " ")
    print()
n = 5

# Upper half
for i in range(n):
    stars = n - i
    spaces = 2 * i

    print("*" * stars, end="")
    print(" " * spaces, end="")
    print("*" * stars)

# Lower half
for i in range(n - 1, -1, -1):
    stars = n - i
    spaces = 2 * i

    print("*" * stars, end="")
    print(" " * spaces, end="")
    print("*" * stars)
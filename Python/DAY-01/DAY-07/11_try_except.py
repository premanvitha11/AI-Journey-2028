try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Result:", num1 / num2)

except ZeroDivisionError:
    print("You cannot divide by zero.")
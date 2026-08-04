try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program finished.")
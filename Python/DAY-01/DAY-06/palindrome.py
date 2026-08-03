text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
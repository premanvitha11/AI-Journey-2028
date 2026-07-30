age = int(input("Enter your age:"))
student = input("Are you a student? (yes/no): ")

if age < 12 or student.lower() == "yes":
    print("Discount available")
else:
    print("Discount not available")
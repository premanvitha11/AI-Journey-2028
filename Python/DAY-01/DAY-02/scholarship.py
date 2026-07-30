marks = int(input("Enter your marks:"))
income = int(input("Enter your family income:"))

if marks >= 85 and income <= 500000:
    print("Scholarship Approved")
else:
    print("Scholarship not approved")
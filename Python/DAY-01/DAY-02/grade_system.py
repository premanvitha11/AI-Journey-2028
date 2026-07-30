marks = int(input("Enter your marks:"))

if marks >= 90:
    print("Grade: A")
    print("Excellent Performance!")
elif marks >= 80:
    print("Grade: B")
    print("Good Performance!")
elif marks >= 70:
    print("Grade: C")
    print("Satisfactory Performance!")
elif marks >= 60:
    print("Grade: D")
    print("Needs Improvement!")
else:
    print("Grade: F")
    print("Poor Performance!")

if marks >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")
    
name = input("Enter your name: ")
CGPA = float(input("Enter your CGPA: "))
Attendance = float(input("Enter your attendance percentage: "))

if CGPA >= 7.5 and Attendance >= 75:
    print("Eligible for placement drive")
else:
    print("Not eligible")

class Student:

    def __init__(self, name, branch):

        self.name = name
        self.branch = branch

    def display(self):

        print(self.name, "-", self.branch)

student1 = Student("Premanvitha", "EEE")
student2 = Student("Rahul", "CSE")

student1.display()
student2.display()
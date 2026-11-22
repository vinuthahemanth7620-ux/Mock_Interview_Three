
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Marks:", self.marks)

    def calculate(self):
        if self.marks > 600:
            print("You got grade A")

        elif self.marks > 400 and self.marks <= 600:
            print("You got grade B")

        else:
            print("You are failed")

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = int(input("Enter student marks: "))

    s = Student(name, age, marks)
    print("--------------------------")  
    s.display()
    s.calculate()

    print("*"*25)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Programming Language:", self.language)

dev = Developer("Rony", 50000, "Python")

print("Employee Details:")
dev.display_info()

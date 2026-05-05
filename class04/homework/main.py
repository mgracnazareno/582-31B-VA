# Implement a Book Class
print("---- Exercise 1 : Book Class -----")
class Book:
    counter = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.counter += 1

    def display_info(self):
        print(f"Book Title: {self.title}, Book Author: {self.author}")

book1 = Book("The Girl on the Train", "Paula Hawkins")
book2 = Book("Verity", "Colleen Hover")
book1.display_info()
book2.display_info()
print(f"Total Books:", Book.counter)


print("\n---- Exercise 2 -----")
class Student:
    school_name = "Vanier College"
    student_count = 0

    def __init__(self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade

        # Increase the counter every time a new Student is created
        Student.student_count += 1 

    def display_info(self):
        print(f"{self.name} studies {self.program} at {self.school_name}. Grade: {self.grade}")


s1 = Student("Alice", "Web development", "88")
s2 = Student("James", "Web Design", 90)
s1.display_info()
s2.display_info()
print(f"Student Count: " , Student.student_count)

print("\n---- Exercise 3 -----")
class Product:
    category= "Electronics"
    tax_rate = 0.15

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price + (self.price + self.tax_rate)

prod1 = Product("Keyboard", 25.99)
prod2 = Product("Mouse", 59.99)
prod3 = Product("Laptop Stand", 39.99)

print(f"Product: {prod1.name} | Price: ${prod1.price} | Price with Tax: ${prod1.price_with_tax():.2f}")
print(f"Product: {prod2.name} | Price: ${prod2.price} | Price with Tax: ${prod2.price_with_tax():.2f}")
print(f"Product: {prod3.name} | Price: ${prod3.price} | Price with Tax: ${prod3.price_with_tax():.2f}")

print("\n---- Exercise 4 -----")
class Employee:
    company_name = "Technova"
    bonus_rate = 0.10
    employee_count = 0

    def __init__(self, _name, _salary):
        self.name = _name
        self.salary = _salary
        Employee.employee_count += 1

    def calculate_bonus(self):
        return self.salary * self.bonus_rate
    
    def display_employee(self):
        print(f"{self.name} at {self.company_name}. Salary: {self.salary}. Bonus: {self.calculate_bonus()}")

emp1 = Employee("John", 50000)
emp2 = Employee("Kenny", 45500)
emp3 = Employee("Brad", 70000)
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()

print("\n--- Bonus Rate at 0.20 ---")
Employee.bonus_rate = 0.20
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()

print("\n--- Bonus Rate For Emp1 at 0.50 ---")
emp1.bonus_rate = 0.50
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()

print("\n--- Bonus Rate at 0.05 ---")
Employee.bonus_rate = 0.05
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()

print(f"\nTotal employees:  {Employee.employee_count}")

"""
emp1 has a SHADOWED bonus_rate.
when bonus_rate = 0.50 was assigned to emp1, it was stored as an instance attribute of emp1,
and despite having a class variable - bonus_rate, it was ignored for emp1. Instance variables
have priority over class attributes.
"""
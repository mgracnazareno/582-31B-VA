# Class attributes vs instance attributes
# instance attribute --> per-object state

class Student:
    school_name = "Vanier College" # This is our shared class attribute

    def __init__(self, name, program):
        # these are instance attributes / per-object state
        self.name = name
        self.program = program

student1 = Student("Alice", "Web development")
student2 = Student("Karim", "Computer Science")

print(student1.name)
print(student2.name)

print(student1.school_name)
print(student2.school_name)

Student.school_name = "ABC College" # we can change the shared attribute directly for all instances of a class
print("-------")
print(student1.school_name)
print(student2.school_name)

# Visual comparison:
    #  Instance attributes
    #   created with self
    #   usually set in __init__
    #   different per object

    # Class attributes
    #   defined in class body
    #   shared across all instances
    #   used for common data or class-level configuration

class Product:
    category = "Electronics" # shared

    def __init__(self, name, price):
        self.name = name # per-object
        self.price = price  # per object

product1 = Product("Keyboard", 10)
product2 = Product("Mouse", 25)

product1.price = 8

print(product1.price)
print(product2.price)
print(product1.category)
print(product2.category)

# shadowing a class attribute

class Employee:
    bonus = 0.5 # this is a class attribute

    def __init__(self, name):
        self.name = name    # this is an instance attribnute

employee1 = Employee("John")
employee2 = Employee("Jane")

print(f"Employee 1 Bonus: ", employee1.name)
print(f"Employee 2 Bonus: " ,employee2.name)

Employee.bonus = 1 # change class attribute globally

print(f"Employee 1 Bonus: ", employee1.bonus)
print(f"Employee 2 Bonus: " ,employee2.bonus)

employee1.bonus = 2 # changing the shadow attribute
                    # this doesn't change the class attribute itself
                    # we create a new instance attribute on employee1!

employee3 = Employee("test")

print(f"Employee 1 Bonus: ", employee1.bonus)  
print(f"Employee 2 Bonus: " ,employee2.bonus)
print(f"Employee 3 Bonus: ", employee3.bonus)

Employee.bonus = 0.5

print(f"Employee 1 Bonus: ", employee1.bonus)
print(f"Employee 2 Bonus: " ,employee2.bonus)
print(f"Employee 3 Bonus: ", employee3.bonus)

# the process above is shadowing
# we are  creating a new instance attribute based on a class attribute

# case study

# Good use case for class attributes are:
    # shared across all instances
    # conceptually the same for the whole class
    # they're usually configuration-like or constant-like
    # they're counters or class-wire metadata

# Bas use cases for class attrubtes are:
    # values that should usually be differented per object.
    # any values that changes often, or is individually different

# Examples
    # school name --> class attribute
    # max capacity --> class attribute (doesnt change)
    # account password --> instance attribute (changes, different per account)
    # tax rate --> class attribute (constant for everyone)
    # course grade --> instance attribute 

# enumerator
    # a class can have an enumerator


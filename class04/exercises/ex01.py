# Write a class of employee

# class attribute is :
    # base salary
    # bonus = 0.25
    # company name

# instance attributes are:
    # name
    # sales_count

# write a method that calculates their salary and returns it
#   conditon:  if sales over --> give bonus multiplier per sales
# base salary is : 500

class Employee:
    bonus = 0.25
    company_name = "ACME Electronics"
    base_salary = 500

    def __init__(self, name, sales_count):
        self.name = name
        self.sales_count = sales_count

    def calculate_salary(self):
        salary = self.base_salary
        if(self.sales_count > 10):
            salary += self.sales_count * self.bonus 
        # else:
        #     return "Sorry, You did not qualify for bonus"
        return salary
        
        

employee1 = Employee("Dede", 4)
print(employee1.name)
print(employee1.base_salary)
print("Employee 1: ", employee1.calculate_salary())
# print(emp1)
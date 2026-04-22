# Create a Friend class
# Requirements: 4-5 arguments, and initialize it
# Create 3 instances

class Friend():
    # initialize
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    #create a function that shows full information 
    def print_info(self):
        print(self.first_name, self.last_name, self.phone_number, self.email)

    # create a function that  greets them!
    def greet(self):
        # inside print use the name variable
        print("Hello " + self.first_name + "!")
        return 5

# create 3 instances
friend1 = Friend("Abhie", "Nartatez", "514-789-9000", "abhie@email.com")
friend2 = Friend("M-Ann", "Talaro", "514-1010-1010", "Mann@email.com")
friend3 = Friend("Yeye", "Bonel", "437-908-100", "yeye@email.com")

friend1.print_info()
friend2.print_info()
friend3.print_info()

friend1.greet()
friend2.greet()
friend3.greet()

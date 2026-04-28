# Create a User class
# give two attributes (username, password)
    # both in password setter function and __init__:
        # if password is less than 4 characters long, return an error!

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password(password)

    def set_name(self, name):
        self.name = name
    
    def set_password(self, pwd):
        if len(pwd) < 4:
           print("Invalid Password, it  must contain at least 4 characters.") 
        self.password = pwd

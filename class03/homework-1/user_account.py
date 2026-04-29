
class UserAccount:
    def __init__(self, username, active = False, login_count = 0):
        self.username = username
        self.active = active
        self.login_count = login_count

    def activate(self):
        if self.active:
            print(f"{self.username} is already active")
        else:
            self.active = True
            print(f"{self.username} has been activated")
    
    def deactivate(self):
        if not self.active:
            print(f"{self.username} is already inactive")
        else:
            self.active = False
            print(f"{self.username} is deactivated")
          
        
    def login(self):
        self.login_count += 1
        print(f"{self.username} logged in {self.login_count} times")

    def show_status(self):
        if (self.active):
            status = 'active'
        else:
            status = 'deactivated'
        print(f"{self.username} is currently {status} and logged in {self.login_count} times")


account = UserAccount('Abhie', True)
account.login()
account.login()
account.login()
account.activate()
account.deactivate()
account.show_status()

print("---------")
account1 = UserAccount("Liam")
account1.show_status()
account1.activate()
account1.login()
account1.deactivate()
account1.show_status()

print("-----")
account3 = UserAccount('usher',"", 3)
account3.show_status()
account3.activate()
account3.show_status()
account3.login()
account3.login()
account3.show_status()
account3.deactivate()
account3.show_status()
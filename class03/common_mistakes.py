# mistake 1 -- forgetting self

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    
    # Whatever function is create, ALWAYS PASS IN SELF
    def sell_one(): # WE NEED TO PASS SELF AS PARAMETER
        self.stock -= 1

# mistake 2 -- forgetting self. for attributes!
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    
    
    def sell_one(self): 
        self.stock -= 1 # If you don't put self. before attribute name, it won't recognize it !IMPORTANT!!

p = Product("test", 1)
print(p.stock)
p.sell_one()
print(p.stock)


# mistake 3
Product.sell_one() # THIS IS NOT CORRECT, DONT CALL CLASS NAME (Product vs product -- instance)
# p.sell_one()

# mistake 4
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    
    
    def sell_one(self): 
        # this doesn't change anything! MISTAKE!
        self.stock - 1

        # these are statements, changing state CORRECTLY
        self.stock = self.stock - 1
        self.stock -= 1

# Mistake 5

# don't mix printing and returning with each other

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    
    
    def get_name(self):
        # these two are not equal
        print(self.name) # used for quick demonstration
        return self.name # when the result needs to be stored/used elsewhere
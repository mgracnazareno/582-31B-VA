# Create a class of Fruit
    # give it 3 attributes (1 should be price)
    # define 3 methods that access the attributes and return them
    # define a method that changes the price to a new price (taken as a parameter)
        # and returns the new price

class Fruit:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    # define 3 methods that access the attributes and return them
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_price(self):
        return self.price
    

    # define a method that changes the price to a new price (taken as a parameter)
        # and returns the new price (USUALLY, WE DONT RETURN FOR SETTERS)
    def set_price(self, new_price):
       self.price = new_price
       print(f"New price is set to ${new_price}")
       
    
apple = Fruit("Apple", "Red", 10)
print(apple.get_name())
print(apple.set_price(25))
print(apple.get_price())

fruit1 = Fruit("Durian", "yellow", 10)
fruit2 = Fruit("Orange", "orange", 15)
fruit3 = Fruit("Strawberry", "red", 20)

fruits = [fruit1, fruit2, fruit3]

for fruit in fruits:
    print(f"{fruit.get_name()} is color {fruit.get_color()} with price of ${fruit.get_price()}")

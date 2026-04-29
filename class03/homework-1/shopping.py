'''
ShoppingCart Class
attributes: owner, item_count
methods: add_item(quantity), remove_item(quantity), show_cart()
'''

class ShoppingCart:
    def __init__(self, owner, item_count = 0):
        self.owner = owner
        self.item_count = item_count
    
    def add_item(self, quantity):
        self.item_count += quantity

    def remove_item(self, quantity):
        if (self.item_count >= quantity):
            self.item_count -= quantity
            print(f" {self.item_count} items has been removed in the cart.")
        else:
            print(f"Not enough items in cart. Only {self.item_count} available.")
    

    def show_cart(self):
        print(f"{self.owner} has {self.item_count} items in the cart.")


shopper1 = ShoppingCart("Meri")
shopper1.add_item(5)
shopper1.show_cart()
shopper1.remove_item(2)
shopper1.show_cart()
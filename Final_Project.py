class Inventory:
    def __init__(self, price):
        self.price = price
    
    def discount(self, discount):
        newprice = self.price - (self.price * (discount / 100))
        return newprice

     

class Mice(Inventory):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        return f"This is a {brand} mouse, and it is sold for {price}"
    

class MousePads(Inventory):
    def __init__(self, price, brand, material):
        self.brand = brand
        self.price = price
        self.material = material
        return f"This is a {brand} mousepad, of {material} and it is sold for {price}"

class Keyboards(Inventory):
    def __init__(self, price, brand, layout):
        self.price = price
        self.layout = layout
        self.brand = brand

    def __str__(self):
        return f"This is a {self.brand} Keyboard, with a {self.layout} Layout and it is sold for {self.price}"


keyboard1 = Keyboards(100, "Razer", "10 keyless") 

print(keyboard1.layout)

print(Keyboards.discount(keyboard1,20))

    
print(keyboard1)


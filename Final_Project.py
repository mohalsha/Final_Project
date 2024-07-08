class Inventory:
    totalitems=0
    item_list = []
    def __init__(self, price):
        self.price = price

        Inventory.totalitems += 1

    @classmethod
    def add_item(cls, item):
        cls.item_list.append(item)

    @classmethod
    def display_items(cls):
        for item in cls.item_list:
            print(item)

    def discount(self, discount):
        newprice = self.price - (self.price * (discount / 100))
        return newprice

     

class Mice(Inventory):
    mice_count=0
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        Mice.mice_count += 1
        Inventory.add_item(self)


    def __str__(self):
        return f"This is a {self.brand} mouse, and it is sold for {self.price}"
    

class MousePads(Inventory):
    mousepads_count=0
    def __init__(self, price, brand, material):
        self.brand = brand
        self.price = price
        self.material = material
        MousePads.mousepads_count += 1
        Inventory.add_item(self)
    
    def __str__(self):
        return f"This is a {self.brand} mousepad, made of {self.material} and it is sold for {self.price}"


class Keyboards(Inventory):
    keyboards_count=0
    def __init__(self, price, brand, layout):
        self.price = price
        self.layout = layout
        self.brand = brand
        Keyboards.keyboards_count += 1
        Inventory.add_item(self)

    def __str__(self):
        return f"This is a {self.brand} Keyboard, with a {self.layout} Layout and it is sold for {self.price}"


keyboard1 = Keyboards(100, "Lenovo", "10 keyless") 

mouse1 = Mice("Microsoft", 50)

mouse2 = Mice("HP",30)

print(keyboard1.layout)

print(Keyboards.discount(keyboard1,20))

    
print(keyboard1)

print(Keyboards.keyboards_count)

Inventory.display_items()
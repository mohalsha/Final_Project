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
    def remove_item(cls, item):
        if item in cls.item_list:
            cls.item_list.remove(item)

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
        return f"{self.brand} mouse, Price: {self.price}"
    

class MousePads(Inventory):
    mousepads_count=0
    def __init__(self, brand, price, material):
        self.brand = brand
        self.price = price
        self.material = material
        MousePads.mousepads_count += 1
        Inventory.add_item(self)
    
    def __str__(self):
        return f"{self.brand} mousepad, Material: {self.material}, Price: {self.price}"


class Keyboards(Inventory):
    keyboards_count=0
    def __init__(self, brand, price, layout):
        self.price = price
        self.layout = layout
        self.brand = brand
        Keyboards.keyboards_count += 1
        Inventory.add_item(self)

    def __str__(self):
        return f"{self.brand} Keyboard, Layout: {self.layout}  Price: {self.price}"


keyboard1 = Keyboards(100, "Lenovo", "10 keyless") 

mouse1 = Mice("Microsoft", 50)

mouse2 = Mice("HP",30)

t = 0
while t != "Exit":

    t = input("What is the item to be added? \n 1.Mouse \n 2.Mousepad \n 3.Keyboard:   \n Enter 'Exit' once done")

    if t == "1" or t == "Mouse":
        b = input("brand:   ")
        p = input("PRICE:   ")
        Mice(b,p)

    elif t == "2" or t == "Mousepad":
        b = input("brand:   ")
        p = input("PRICE:   ")
        m = input("Material:   ")
        MousePads(b,p,m)

    elif t == "3" or t == "Keyboard":
        b = input("brand:   ")
        p = input("PRICE:   ")
        l = input("Layout:   ")
        Keyboards(b,p,l)

    else: print("Please enter a valid item")


print(keyboard1.layout)

#print(Keyboards.discount(keyboard1,20))

    
print(keyboard1)

#print(Keyboards.keyboards_count)

Inventory.display_items()

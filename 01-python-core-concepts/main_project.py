class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock = self.stock - quantity
            return True
        else:
            return False

#Demo
p1 = Product("Laptop", 1200, 10)
p2 = Product("Phone", 800, 25)
p3 = Product("Tablet", 400, 15)

products = [p1, p2, p3]

print(p2.name)

with open("report.txt", 'w') as file:
    for p in products:
        file.write(f"{p.name},{p.price},{p.stock}\n") 
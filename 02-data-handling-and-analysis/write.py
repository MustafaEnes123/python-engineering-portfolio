class Product: 
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

#demo
p1 = Product("Laptop", 1200, 10)
p2 = Product("Phone", 800, 25)
p3 = Product("Tablet", 400, 15)
p4 = Product("Monitor", 300, 20)
p5 = Product("Keyboard", 100, 50)

products = [p1, p2, p3, p4, p5]


with open("products.txt", 'w') as file:
    for p in products:
        file.write(f"{p.name},{p.price},{p.stock}\n")
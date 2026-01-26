new_products = [
    {"name": "Mouse", "price": 50, "stock": 30},
    {"name": "Headphones", "price": 150, "stock": 40},
    {"name": "Webcam", "price": 80, "stock": 25},
    {"name": "Speaker", "price": 100, "stock": 35},
    {"name": "Charger", "price": 60, "stock": 45}
]

print(new_products[2]["name"])

# Modifying the price of the first product
new_products[0]["price"] = 60

print(new_products[0]["price"])

new_products[0]["color"] = "Black"
print(new_products[0]["color"])

for item in new_products:
    total_value = item["price"] * item["stock"]
    print(total_value)
import pandas as pd
data = [
    {'name': 'Laptop', 'price': 1200, 'stock': 30},
    {'name': 'Phone', 'price': 800, 'stock': 50},
    {'name': 'Tablet', 'price': 400, 'stock': 20},
    {'name': 'Monitor', 'price': 300, 'stock': 40},
    {'name': 'Keyboard', 'price': 100, 'stock': 70},
    {'name': 'Mouse', 'price': 50, 'stock': 100}
]
df = pd.DataFrame(data)
print(df)

#Asking questions about the DataFrame
print("Total number of products:", len(df))
print(df.name)

#Filtering products with price greater than 500
expensive_products = df[df.price > 500]
print(expensive_products)
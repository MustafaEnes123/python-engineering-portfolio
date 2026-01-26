with open("products.txt", 'r') as file:
    content = file.readlines()
    print(content)
    for line in content:
        name, price, stock = line.strip().split(',')
        print(f"Product Name: {name}, Price: {price}, Stock: {stock}")

# Converting price and stock to appropriate data types
price = float(price)
stock = int(stock)
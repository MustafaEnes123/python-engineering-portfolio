with (open("manual_data.txt", "r")) as file:
    manual_data = file.read()
print("Manual Data Loaded:")
print(manual_data)
lines = manual_data.strip().split("\n")
processed_data = []
for line in lines:
    name, price, stock = line.split(",")
    processed_data.append({
        "name": name.strip(),
        "price": float(price.strip()),
        "stock": int(stock.strip())
    })
print("Dictionary list is ready:")
print(processed_data)

#Libraries (NumPy)
import numpy as np
prices = np.array([item['price'] for item in processed_data])
stocks = np.array([item['stock'] for item in processed_data])
total_values = prices * stocks
print("Total values calculated using NumPy")

#Libraries (Pandas)
import pandas as pd
df = pd.DataFrame(processed_data)
df["total_value"] = total_values
print("Final DataFrame:")
print(df)
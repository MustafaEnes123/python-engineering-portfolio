import numpy as np
prices_list = [10, 20, 30, 40, 50]
prices_array = np.array(prices_list)
prices_newest = np.array([15, 25, 35, 45, 55])

print(prices_array + 5)
print(prices_array * 2)

def increase_prices():
    print(prices_array + 5)
    print(prices_array * 2)

#demo
print(increase_prices())

np.mean(prices_array)
np.max(prices_array)
np.min(prices_array)
print("Max price:", np.max(prices_array))
print("Min price:", np.min(prices_array))
print("Mean price:", np.mean(prices_array))

#numpy operations
total_prices = prices_array + prices_newest
print("Total Prices:", total_prices)
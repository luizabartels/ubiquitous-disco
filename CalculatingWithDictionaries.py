# Perform calculations on a dictionary of data.

prices = {
    'ACME': 45.23,
    'AAPL':612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# To perform the calculations, it's better to invert the keys and values.

min_price = min(zip(prices.values(), prices.keys()))

max_price = max(zip(prices.values(), prices.keys()))

prices_sorted = sorted(zip(prices.values(), prices.keys()))

# zip() creates an iterator that can only be consumed once

# If you want to know the key for min or max price

min(prices, key=lambda k: prices[k])
max(prices, key=lambda k: prices[k])

#If you want the min or max price instead

min_value = prices[min(prices, key=lambda k: prices[k])]

# If the values are duplicated, the smalest key will be returned first
# Make a list of the largest or smallest N items in a collection

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# As funções aceitam parâmetros, permitindo serem usadas com dados mais estruturados

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key = lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key = lambda s: s['price'])

print(cheap)
print(expensive)

# heapq.heapfy() coloca em ordem crescente a lista
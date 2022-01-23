prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
minimum = min(zip(prices.values(), prices.keys()))
maximum = max(zip(prices.values(), prices.keys()))
print(minimum)
print(maximum)
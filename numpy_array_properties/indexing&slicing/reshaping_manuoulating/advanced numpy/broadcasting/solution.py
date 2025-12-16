import numpy as np
prices = np.array([1000,2000,3000])
discount = 10 #scalar single value
final_prices = prices-(prices*discount/100)
print(final_prices)


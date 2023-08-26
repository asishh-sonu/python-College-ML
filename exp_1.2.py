# Create a tuple with five elements representing the price of products
product_prices = (25.99, 12.49, 9.99, 7.75, 15.00)

# A. Find the maximum and minimum price from the tuple
max_price = max(product_prices)
min_price = min(product_prices)

print("Maximum price:", max_price)
print("Minimum price:", min_price)

# B. Calculate the total cost of all products
total_cost = sum(product_prices)
print("Total cost of all products:", total_cost)

# C. Convert the tuple to a list and add a new product with its price
product_list = list(product_prices)
new_product_price = 18.50
product_list.append(new_product_price)

# D. Calculate the average price of the products
average_price = sum(product_list) / len(product_list)
print("Average price of the products:", average_price)

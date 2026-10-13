# Sales Data Calculator

# List of sales made
sales = [1500, 2500, 1800, 3200, 4000, 2200, 3500]

# Find the total sales amount
total_sales = sum(sales)

# Calculate the average sales amount
average_sales = total_sales / len(sales)

# Get the highest and lowest sales values
highest_sale = max(sales)
lowest_sale = min(sales)

# Print the sales details
print("All Sales:", sales)
print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)

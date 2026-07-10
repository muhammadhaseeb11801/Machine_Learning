## Import Required Library
import matplotlib.pyplot as plt

# Create X-axis Data
# Store the names of the products.

products = ["Laptop", "Mobile", "Tablet",
            "Headphones", "Smartwatch", "Camera"]

### Explanation
# This list contains product names.
# These values will appear on the X-axis.

# Create Y-axis Data
# Store the sales values.

sales = [45000, 62000, 28000, 15000, 21000, 17000]

### Explanation
# This list contains the sales amount of each product.
# These values will appear on the Y-axis.

# Create Colors
# Assign a different color to each bar.

colors = ["#4C72B0", "#DD8452", "#55A868",
          "#C44E52", "#8172B2", "#937860"]

### Explanation
# Each bar will have a different color.
# This makes the chart more attractive and easier to understand.

# Create Figure
# Set the size of the chart.

plt.figure(figsize=(10,6))

### Explanation
# **figure()** creates a new chart.
# **figsize=(10,6)** sets the chart width and height.

# Draw Bar Chart

bars = plt.bar(products, sales, color=colors)

### Explanation
# **bar()** creates a bar chart.
# products -> X-axis values.
# sales -> Y-axis values.
# color=colors applies different colors to each bar.

# Add Chart Title

plt.title("Sales by Product Line")

### Explanation
# Displays the chart title.

# Add X-axis Label

plt.xlabel("Product")

### Explanation
# Labels the X-axis.

# Add Y-axis Label

plt.ylabel("Sales (in Rs.)")

### Explanation
# Labels the Y-axis.

# Rotate X-axis Labels

plt.xticks(rotation=45)

### Explanation
# Rotates the product names by 45 degrees.
# This prevents labels from overlapping.

# Adjust Layout

plt.tight_layout()

### Explanation
# Automatically adjusts spacing.

# Save Chart

plt.savefig("sales_by_product_line.png")

### Explanation
# Saves the chart as a PNG image.

# Display Chart

plt.show()

### Explanation
# Displays the chart on the screen.

# Summary

# This program performs the following steps:
# - Import Matplotlib.
# - Create product data.
# - Create sales data.
# - Assign colors.
# - Create a figure.
# - Draw a bar chart.
# - Add title.
# - Add X-axis label.
# - Add Y-axis label.
# - Rotate X-axis labels.
# - Adjust layout.
# - Save the chart.
# - Display the chart.
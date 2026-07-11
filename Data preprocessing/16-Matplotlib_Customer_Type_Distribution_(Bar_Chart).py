## Import Required Library
import matplotlib.pyplot as plt

# Create X-axis Data
# Store different customer types.
customer_types = ["New", "Returning", "Loyal", "Wholesale"]

### Explanation
# This list contains different customer categories.
# These values will appear on the X-axis.

# Create Y-axis Data
# Store the number of customers.
counts = [120, 200, 150, 60]

### Explanation
# This list contains the total number of customers
# in each customer type.
# These values will appear on the Y-axis.

# Create Colors
# Assign different colors to each bar.
colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

### Explanation
# Each customer type bar will have a different color.
# This makes the chart easy to understand.

# Create Figure
# Set the size of the chart.
plt.figure(figsize=(8, 6))

### Explanation
# **figure()** creates a new chart.
# **figsize=(8,6)** sets the chart width and height.

# Draw Bar Chart
bars = plt.bar(customer_types, counts, color=colors)

### Explanation
# **plt.bar()** creates a bar chart.
# customer_types -> X-axis values.
# counts -> Y-axis values.
# color=colors assigns different colors to each bar.

# Add Chart Title
plt.title("Customer Type Distribution")

### Explanation
# Displays the chart title at the top.

# Add X-axis Label
plt.xlabel("Customer Type")

### Explanation
# Labels the horizontal (X) axis.

# Add Y-axis Label
plt.ylabel("Number of Customers")

### Explanation
# Labels the vertical (Y) axis.

# Adjust Layout
plt.tight_layout()

### Explanation
# Automatically adjusts spacing
# so labels are not cut off.

# Save Chart
plt.savefig("customer_type_distribution.png")

### Explanation
# Saves the chart as a PNG image.

# Display Chart

plt.show()

### Explanation
# Displays the chart on the screen.

# Summary

# This program performs the following steps:
# - Import Matplotlib.
# - Create customer type data.
# - Create customer count data.
# - Assign colors.
# - Create a figure.
# - Draw a bar chart.
# - Add chart title.
# - Add X-axis label.
# - Add Y-axis label.
# - Adjust layout.
# - Save the chart.
# - Display the chart.
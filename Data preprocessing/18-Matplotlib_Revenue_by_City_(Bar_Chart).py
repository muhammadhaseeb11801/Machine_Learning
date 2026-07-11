## Import Required Library
import matplotlib.pyplot as plt

# Create X-axis Data
# Store the names of the cities.
cities = ["Karachi", "Lahore", "Islamabad", "Faisalabad", "Multan", "Peshawar"]

### Explanation
# This list contains city names.
# These values will appear on the X-axis.

# Create Y-axis Data
# Store the revenue values.
revenue = [85000, 72000, 60000, 45000, 38000, 30000]

### Explanation
# This list contains the revenue earned from each city.
# These values will appear on the Y-axis.

# Create Colors
# Assign different colors to each bar.
colors = ["#4C72B0", "#DD8452", "#55A868",
          "#C44E52", "#8172B2", "#937860"]

### Explanation
# Each city bar will have a different color.
# This makes the chart more attractive.

# Create Figure
# Set the size of the chart.
plt.figure(figsize=(10,6))

### Explanation
# **figure()** creates a new chart.
# **figsize=(10,6)** sets the chart width and height.

# Draw Bar Chart
bar = plt.bar(cities, revenue, color=colors)

### Explanation
# **plt.bar()** creates a Bar Chart.
# cities -> X-axis values.
# revenue -> Y-axis values.
# color=colors applies different colors to each bar.

# Add Chart Title
plt.title("Revenue by City")

### Explanation
# Displays the chart title at the top.

# Add X-axis Label
plt.xlabel("City")

### Explanation
# Labels the horizontal (X) axis.

# Add Y-axis Label
plt.ylabel("Revenue (in Rs.)")

### Explanation
# Labels the vertical (Y) axis.

# Add Grid
plt.grid(axis="y", linestyle="-", alpha=0.7,color="black")

### Explanation
# Displays grid lines on the y-axis.
# linestyle="--" creates dashed grid lines.
# alpha=0.7 makes the grid slightly transparent.

# Rotate X-axis Labels
plt.xticks(rotation=45)

### Explanation
# Rotates city names by 45 degrees.
# This prevents labels from overlapping.

# Adjust Layout
plt.tight_layout()

### Explanation
# Automatically adjusts spacing
# so that labels are not cut off.

# Save Chart
plt.savefig("revenue_by_city.png")

### Explanation
# Saves the chart as a PNG image.

# Display Chart
plt.show()

### Explanation
# Displays the chart on the screen.

# Summary

# This program performs the following steps:
# - Import Matplotlib.
# - Create city data.
# - Create revenue data.
# - Assign colors.
# - Create a figure.
# - Draw a Bar Chart.
# - Add chart title.
# - Add X-axis label.
# - Add Y-axis label.
# - Rotate X-axis labels.
# - Adjust layout.
# - Save the chart.
# - Display the chart.
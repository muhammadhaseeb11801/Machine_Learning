## Import Required Library
import matplotlib.pyplot as plt

# Create X-axis Data
# Store the quantity values.

quantity = [1, 2, 2, 3, 4, 5, 3, 6, 7, 2, 8, 3, 4, 5, 6,
            1, 2, 3, 9, 4, 5, 2, 6, 7, 3, 4, 8, 2, 5, 6]

### Explanation
# This list contains quantity values.
# These values will appear on the X-axis.

# Create Y-axis Data
# Store the revenue values.

revenue = [150, 320, 300, 450, 600, 750, 470, 900, 1050, 310,
           1200, 460, 590, 740, 880, 160, 330, 440, 1350, 610,
           760, 300, 890, 1040, 450, 600, 1180, 320, 750, 870]

### Explanation
# This list contains revenue values.
# These values will appear on the Y-axis.

# Create Figure
# Set the size of the chart.

plt.figure(figsize=(10,6))

### Explanation
# **figure()** creates a new chart.
# **figsize=(10,6)** sets the chart width and height.

# Draw Scatter Plot

plt.scatter(
    quantity,
    revenue,
    color="#55A868",
    edgecolor="black"
)

### Explanation
# **scatter()** creates a Scatter Plot.
# quantity -> X-axis values.
# revenue -> Y-axis values.
# color sets the color of the points.
# edgecolor adds a black border around each point.

# Add Chart Title

plt.title("Quantity vs Revenue")

### Explanation
# Displays the chart title.

# Add X-axis Label

plt.xlabel("Quantity")

### Explanation
# Labels the horizontal (X) axis.

# Add Y-axis Label

plt.ylabel("Revenue (in Rs.)")

### Explanation
# Labels the vertical (Y) axis.

# Show Grid

plt.grid(True)

### Explanation
# Displays grid lines on the chart.
# Grid lines make the graph easier to read.

# Adjust Layout

plt.tight_layout()

### Explanation
# Automatically adjusts spacing
# so labels are not cut off.

# Save Chart

plt.savefig("quantity_vs_revenue_scatter.png")

### Explanation
# Saves the Scatter Plot as a PNG image.

# Display Chart

plt.show()

### Explanation
# Displays the Scatter Plot on the screen.

# Summary

# This program performs the following steps:
# - Import Matplotlib.
# - Create quantity data.
# - Create revenue data.
# - Create a figure.
# - Draw a Scatter Plot.
# - Add title.
# - Add X-axis label.
# - Add Y-axis label.
# - Display grid lines.
# - Adjust layout.
# - Save the chart.
# - Display the chart.
## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")

# Convert Date Column
# Convert the Date column into datetime format.
df["Date"] = pd.to_datetime(df["Date"])

### Explanation
# **pd.to_datetime()** converts the Date column
# from text (object) into datetime format.

# Feature Engineering

# Create Month Column
# Extract the month from the Date column.

df["Month"] = df["Date"].dt.month

### Explanation
# **dt.month** extracts the month number (1–12).

# Create Day Column
# Extract the day from the Date column.

df["Day"] = df["Date"].dt.day

### Explanation
# **dt.day** extracts the day of the month (1–31).

# Create Day Name Column
# Extract the name of the day.

df["Day Name"] = df["Date"].dt.day_name()

### Explanation
# **dt.day_name()** returns the day name
# such as Monday, Tuesday, Wednesday, etc.

# Create Total Price Column
# Calculate Total Price.

df["Total Price"] = df["Unit price"] * df["Quantity"]

### Explanation
# Multiply Unit Price by Quantity.
# Formula:
# Total Price = Unit Price × Quantity

# Create Revenue Column
# Copy Total into a new Revenue column.

df["Revenue"] = df["Total"]

### Explanation
# Revenue contains the same values as the Total column.
# This new column can be used for further analysis.

# Display First 10 Rows

print(df.head(10))

### Explanation
# Display the first 10 rows of the updated dataset.

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the dataset.
# - Convert the Date column into datetime.
# - Create Month, Day, and Day Name columns.
# - Create Total Price column.
# - Create Revenue column.
# - Display the first 10 rows.
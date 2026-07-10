## Import Required Library
import pandas as pd

# Load Dataset
# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")

# Display Dataset Shape
# Show the total number of rows and columns in the dataset.
print(df.shape)

### Explanation
# **shape** returns the dimensions of the dataset.
# The first value represents the total number of rows.
# The second value represents the total number of columns.
# The output is returned as a tuple.
# Example:
# (1000, 17)
# Here,
# 1000 = Number of Rows
# 17 = Number of Columns

# Summary

# This program performs the following steps:
# - Import the Pandas library.
# - Load the CSV dataset.
# - Store the dataset in a DataFrame named df.
# - Display the total number of rows and columns.
# - Verify the size of the dataset.
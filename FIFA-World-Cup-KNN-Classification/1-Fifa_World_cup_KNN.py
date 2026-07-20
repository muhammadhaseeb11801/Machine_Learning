## Import Required Libraries

import pandas as pd            # Import Pandas for data manipulation
import matplotlib.pyplot as plt   # Import Matplotlib for data visualization

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

### Explanation
# **Pandas** is a Python library used to read, manage,
# and analyze datasets.
# We use **pd** as the short name (alias) of Pandas.
#
# **Matplotlib** is a Python library used to create charts
# and graphs for visualizing data.
#
# **Scikit-learn (sklearn)** is a Machine Learning library.
# From it, we import tools for splitting data, scaling data,
# building a KNN model, and measuring accuracy.


## Load Dataset

# Read the CSV file and store it in a DataFrame named df.
df = pd.read_csv("data.csv")      # Change this to your file name

### Explanation
# **pd.read_csv()** reads the CSV file.
# The dataset is stored in a Pandas DataFrame called **df**.
# A DataFrame is a table consisting of rows and columns.


## Display First 10 Rows

# Show only the first 10 records of the dataset.
print("\n----- First 10 Rows -----")
print(df.head(10))

### Explanation
# **head(10)** displays the first 10 rows of the dataset.
# It helps us quickly inspect the data.
# This is useful for checking whether the dataset
# has been loaded correctly.
# By default, **head()** displays only the first 5 rows.
# Using **head(10)** displays the first 10 rows.


## Display Last 10 Rows

# Show only the last 10 records of the dataset.
print("\n----- Last 10 Rows -----")
print(df.tail(10))

### Explanation
# **tail(10)** displays the last 10 rows of the dataset.
# It helps us check whether the end of the dataset
# looks correct, with no broken or missing rows.


## Check Dataset Shape

# Display the number of rows and columns in the dataset.
print("\n----- Dataset Shape -----")
print(df.shape)

### Explanation
# **shape** returns a tuple in the form (rows, columns).
# It tells us how many total records (players) and how many
# features (columns) are present in the dataset.


## Check Column Names

# Display all column names present in the dataset.
print("\n----- Column Names -----")
print(df.columns)

### Explanation
# **columns** returns the list of all column names.
# This helps us know exactly which features are available
# to work with.


## Check Data Types

# Display the data type of each column.
print("\n----- Data Types -----")
print(df.dtypes)

### Explanation
# **dtypes** shows whether each column contains numbers
# (int, float) or text (object).
# This is important because Machine Learning models
# require numeric data.


## Statistical Summary

# Display statistical details of numeric columns.
print("\n----- Statistical Summary -----")
print(df.describe())

### Explanation
# **describe()** provides statistics such as mean, minimum,
# maximum, and standard deviation for numeric columns.
# It gives a quick overview of how the data is distributed.


## Check Missing Values

# Count the number of missing (null) values in each column.
print("\n----- Missing Values Before Handling -----")
print(df.isnull().sum())

### Explanation
# **isnull().sum()** counts how many empty/missing values
# exist in each column.
# Missing values must be handled before training a model.


## Fill Missing Values

# Fill missing values based on column type.
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].mean())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\n----- Missing Values After Handling -----")
print(df.isnull().sum())

### Explanation
# If a column contains **numbers**, missing values are filled
# with the **mean (average)** of that column.
# If a column contains **text**, missing values are filled
# with the **mode (most frequent value)** of that column.
# This ensures the dataset has no empty cells left.


## Remove Duplicate Records

# Remove any duplicate rows from the dataset.
df.drop_duplicates(inplace=True)

print("\nDuplicates Removed Successfully")
print("New Dataset Shape:", df.shape)

### Explanation
# **drop_duplicates()** removes rows that are exact copies
# of other rows.
# Duplicate records can bias the model, so removing them
# keeps the dataset clean and reliable.


## Define Features (Input)

# Select the columns that will be used as input for the model.
X = df[[
    "height_cm",
    "weight_kg",
    "age",
    "player_rating",
    "performance_score"
]]

### Explanation
# **X** represents the **features (inputs)** of the model.
# These are the columns the model will use to make predictions.


## Define Target (Output)

# Select the column that will be predicted by the model.
y = df["position"]       # We want to predict the player's position

### Explanation
# **y** represents the **target (output)** of the model.
# This is the value the model is trying to predict —
# in this case, the player's position.


## Encode Target Labels

# Convert text labels into numeric values.
encoder = LabelEncoder()
y = encoder.fit_transform(y)

### Explanation
# Machine Learning models only understand numbers, not text.
# **LabelEncoder** converts each unique position
# (e.g., Forward, Defender, Midfielder) into a number
# (e.g., 0, 1, 2).


## Split Data into Train and Test Sets

# Split the dataset into training data and testing data.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

### Explanation
# **train_test_split()** divides the dataset into two parts:
# - **80% Training data**: used to train the model.
# - **20% Testing data**: used to evaluate how well the model
#   performs on data it has never seen before.
# **random_state=42** ensures the split is the same every time
# the code is run.


## Feature Scaling

# Scale the feature values to a standard range.
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

### Explanation
# KNN is a **distance-based algorithm**, meaning it calculates
# the distance between data points.
# If one feature (e.g., height in cm: 150–200) has a much
# larger scale than another (e.g., rating: 0–10), it can
# unfairly dominate the distance calculation.
# **StandardScaler** rescales all features so they have
# a mean of 0 and a standard deviation of 1.


## Build and Train the KNN Model

# Create a KNN classifier and train it on the training data.
knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

### Explanation
# **KNN (K-Nearest Neighbors)** predicts a player's position
# by looking at the **3 nearest players** (n_neighbors=3)
# in the training data and assigning the most common
# position among them.
# **fit()** trains the model using the training data.


## Make Predictions

# Predict the position for the test data.
y_pred = knn.predict(X_test)

### Explanation
# **predict()** uses the trained model to make predictions
# on the test data, which the model has never seen before.


## Calculate Accuracy

# Measure how accurate the model's predictions are.
accuracy = accuracy_score(y_test, y_pred)

print("Prediction :", y_pred)
print("Accuracy   :", accuracy)

### Explanation
# **accuracy_score()** compares the predicted values
# with the actual values and calculates the percentage
# of correct predictions.


## Decode Predicted Labels

# Convert the predicted numeric labels back to text.
print("\nPredicted Positions:")
print(encoder.inverse_transform(y_pred))

### Explanation
# **inverse_transform()** converts the numeric predictions
# (0, 1, 2, ...) back into their original text labels
# (e.g., "Forward", "Defender").


## Line Chart - Player Rating

# Plot player ratings as a line chart.
plt.figure(figsize=(8,5))
plt.plot(df["player_rating"], label="Player Rating")
plt.title("Line Chart - Player Rating")
plt.xlabel("Players")
plt.ylabel("Rating")
plt.grid(True)
plt.legend()
plt.show()

### Explanation
# This line chart shows the rating trend across all players,
# making it easy to spot patterns, spikes, or drops.


## Scatter Plot - Height vs Weight

# Plot the relationship between height and weight.
plt.figure(figsize=(8,5))
plt.scatter(df["height_cm"], df["weight_kg"])
plt.title("Scatter Plot - Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.show()

### Explanation
# A scatter plot shows each player as a single point,
# helping us visually check if height and weight
# are related to each other.


## Bar Chart - Average Rating by Position

# Calculate and plot the average rating for each position.
avg_rating = df.groupby("position")["player_rating"].mean()

plt.figure(figsize=(8,5))
plt.bar(avg_rating.index, avg_rating.values)
plt.title("Average Player Rating by Position")
plt.xlabel("Position")
plt.ylabel("Average Rating")
plt.xticks(rotation=20)
plt.show()

### Explanation
# **groupby("position")** groups all players by their position,
# and **mean()** calculates the average rating for each group.
# The bar chart then compares these average ratings visually.


## Pie Chart - Player Position Distribution

# Count how many players belong to each position.
position_count = df["position"].value_counts()

plt.figure(figsize=(7,7))
plt.pie(
    position_count.values,
    labels=position_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Player Position Distribution")
plt.show()

### Explanation
# **value_counts()** counts how many players exist for
# each position.
# The pie chart shows the percentage share of each
# position in the entire dataset.


## Histogram - Age Distribution

# Plot the distribution of player ages.
plt.figure(figsize=(8,5))
plt.hist(df["age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

### Explanation
# A histogram groups ages into ranges (bins) and shows
# how many players fall into each range, helping us see
# the overall age distribution of the dataset.


## Subplots - Combined View

# Display all four charts together in a single 2x2 grid.
fig, ax = plt.subplots(2, 2, figsize=(12,8))

# Line
ax[0,0].plot(df["player_rating"])
ax[0,0].set_title("Player Rating")

# Scatter
ax[0,1].scatter(df["height_cm"], df["weight_kg"])
ax[0,1].set_title("Height vs Weight")

# Bar
ax[1,0].bar(avg_rating.index, avg_rating.values)
ax[1,0].set_title("Average Rating by Position")
ax[1,0].tick_params(axis='x', rotation=20)

# Histogram
ax[1,1].hist(df["age"], bins=10)
ax[1,1].set_title("Age Distribution")

plt.tight_layout()
plt.show()

### Explanation
# **subplots(2, 2)** creates a 2x2 grid of charts so that
# the line chart, scatter plot, bar chart, and histogram
# can all be viewed together in one window for easy comparison.


## Summary

# This program performs the following steps:
# - Import the required libraries (Pandas, Matplotlib, Scikit-learn).
# - Load the CSV dataset into a DataFrame.
# - Explore the dataset (rows, shape, columns, data types, statistics).
# - Handle missing values and remove duplicate records.
# - Define the features (X) and target (y).
# - Encode the target labels into numeric form.
# - Split the dataset into training and testing sets.
# - Scale the features using StandardScaler.
# - Build and train a KNN classifier.
# - Make predictions and evaluate the model's accuracy.
# - Decode the predictions back into readable labels.
# - Visualize the dataset using line, scatter, bar, pie,
#   and histogram charts, plus a combined subplot view.

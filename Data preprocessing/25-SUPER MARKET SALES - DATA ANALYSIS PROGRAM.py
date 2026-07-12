# =====================================================
# SUPER MARKET SALES - DATA ANALYSIS PROGRAM
# =====================================================

# ---------------------------
# 1. Import Required Library
# ---------------------------
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 2. Load the Dataset
# ---------------------------
df = pd.read_csv("data.csv")
print(df)

# ---------------------------
# 3. View the Dataset
# ---------------------------
print("\n----- First 10 Rows -----")
print(df.head(10))

print("\n----- Last 10 Rows -----")
print(df.tail(10))

# ---------------------------
# 4. Check Dataset Size
# ---------------------------
print("\n----- Dataset Shape -----")
print(df.shape)

print("\n----- Column Names -----")
print(df.columns)

# ---------------------------
# 5. Check Data Types
# ---------------------------
print("\n----- Data Types -----")
print(df.dtypes)

print("\n----- Statistical Summary -----")
print(df.describe())

# ---------------------------
# 6. Check Missing Values
# ---------------------------
print("\n----- Missing Values Before Handling -----")
print(df.isnull().sum())

# ---------------------------
# 7. Fill Missing Values
# ---------------------------
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].mean())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\n----- Missing Values After Handling -----")
print(df.isnull().sum())

# ---------------------------
# 8. Remove Duplicate Records
# ---------------------------
df.drop_duplicates(inplace=True)
print("\nDuplicates removed. New shape:", df.shape)

# ---------------------------
# 9. Convert Date Format
# ---------------------------
df["Date"] = pd.to_datetime(df["Date"])

# ---------------------------
# 10. Create Month Column
# ---------------------------
df["Month"] = df["Date"].dt.month_name()

# ---------------------------
# 11. Product Line Cleaning
# ---------------------------
df["Product_Line_Cleaning"] = df["Product line"].str.strip()

# ---------------------------
# 12. Create Revenue Column
# ---------------------------
df["Revenue"] = df["Total"]

# ---------------------------
# 13. Monthly Revenue Analysis
# ---------------------------
monthly_revenue = df.groupby("Month")["Revenue"].sum()
print("\n----- Monthly Revenue -----")
print(monthly_revenue)

# =====================================================
# CHARTS SECTION
# =====================================================

# ---------------------------
# 14. Line Chart - Monthly Revenue Trend
# ---------------------------
plt.figure(figsize=(8, 5))
plt.plot(monthly_revenue.index, monthly_revenue.values, marker="o", color="blue")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart_1_monthly_revenue_line.png")
plt.show()

# ---------------------------
# 15. Product Line Analysis + Bar Chart
# ---------------------------
product_sales = df.groupby("Product line")["Revenue"].sum().sort_values(ascending=False)
print("\n----- Revenue by Product Line -----")
print(product_sales)

plt.figure(figsize=(9, 5))
plt.bar(product_sales.index, product_sales.values, color="teal")
plt.title("Revenue by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Revenue")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("chart_2_product_line_bar.png")
plt.show()

# ---------------------------
# 16. Barh Chart - Product Line (Horizontal)
# ---------------------------
plt.figure(figsize=(8, 5))
plt.barh(product_sales.index, product_sales.values, color="orange")
plt.title("Revenue by Product Line (Horizontal)")
plt.xlabel("Revenue")
plt.ylabel("Product Line")
plt.tight_layout()
plt.savefig("chart_3_product_line_barh.png")
plt.show()

# ---------------------------
# 17. Payment Method Analysis + Pie Chart
# ---------------------------
payment_counts = df["Payment"].value_counts()
print("\n----- Payment Method Counts -----")
print(payment_counts)

plt.figure(figsize=(6, 6))
plt.pie(payment_counts.values, labels=payment_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Payment Method Distribution")
plt.tight_layout()
plt.savefig("chart_4_payment_pie.png")
plt.show()

# ---------------------------
# 18. Customer Type Distribution + Bar Chart
# ---------------------------
customer_counts = df["Customer type"].value_counts()
print("\n----- Customer Type Counts -----")
print(customer_counts)

plt.figure(figsize=(6, 5))
plt.bar(customer_counts.index, customer_counts.values, color=["purple", "green"])
plt.title("Customer Type Distribution")
plt.xlabel("Customer Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("chart_5_customer_type_bar.png")
plt.show()

# ---------------------------
# 19. Quantity Histogram
# ---------------------------
plt.figure(figsize=(7, 5))
plt.hist(df["Quantity"], bins=10, color="skyblue", edgecolor="black")
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("chart_6_quantity_hist.png")
plt.show()

# ---------------------------
# 20. Unit Price Histogram
# ---------------------------
plt.figure(figsize=(7, 5))
plt.hist(df["Unit price"], bins=10, color="salmon", edgecolor="black")
plt.title("Unit Price Distribution")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("chart_7_unitprice_hist.png")
plt.show()

# ---------------------------
# 21. Scatter Plot - Quantity vs Revenue
# ---------------------------
plt.figure(figsize=(7, 5))
plt.scatter(df["Quantity"], df["Revenue"], color="darkred", alpha=0.6)
plt.title("Quantity vs Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("chart_8_quantity_vs_revenue_scatter.png")
plt.show()


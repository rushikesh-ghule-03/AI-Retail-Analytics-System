import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\Rushikesh ghule\OneDrive\Desktop\AI-Retail-Analytics-System\data\superstore.csv", encoding='latin1'
)

# Show first 5 rows
print(df.head())

# Show columns
print(df.columns)

# Dataset shape
print(df.shape)

# Dataset information
print(df.info())

# Missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert order date into datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

print("\nDate Column Converted")

# Total Sales
total_sales = df['Sales'].sum()

print("\nTotal Sales:")
print(total_sales)

# Total Profit
total_profit = df['Profit'].sum()

print("\nTotal Profit:")
print(total_profit)

# Average Sales
average_sales = df['Sales'].mean()

print("\nAverage Sales:")
print(average_sales)

# Highest Sales
highest_sales = df['Sales'].max()

print("\nHighest Sales:")
print(highest_sales)

# Lowest Sales
lowest_sales = df['Sales'].min()

print("\nLowest Sales:")
print(lowest_sales)

# Category Wise Sales
category_sales = df.groupby('Category')['Sales'].sum()

print("\nCategory Wise Sales:")
print(category_sales)

# Category Wise Profit
category_profit = df.groupby('Category')['Profit'].sum()

print("\nCategory Wise Profit:")
print(category_profit)


#  Category Wise Sales Chart

plt.figure(figsize=(8, 5))

category_sales.plot(
    kind='bar',
    color=['skyblue', 'orange', 'green']
)

plt.title("Category Wise Sales Analysis", fontsize=16)

plt.xlabel("Category", fontsize=12)

plt.ylabel("Sales", fontsize=12)

plt.xticks(rotation=0)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

#  Category Wise Profit Chart

plt.figure(figsize=(8, 5))

category_profit.plot(
    kind='bar',
    color=['purple', 'red', 'teal']
)

plt.title("Category Wise Profit Analysis", fontsize=16)

plt.xlabel("Category", fontsize=12)

plt.ylabel("Profit", fontsize=12)

plt.xticks(rotation=0)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


# Create Month Column

df['Month'] = df['Order Date'].dt.month

print("\nMonth Column Created")

# Monthly Sales Analysis

monthly_sales = df.groupby('Month')['Sales'].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Professional Monthly Sales Trend Chart

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker='o',
    linewidth=3,
    linestyle='-'
)

plt.title("Monthly Sales Trend", fontsize=16)

plt.xlabel("Month", fontsize=12)

plt.ylabel("Sales", fontsize=12)

plt.xticks(monthly_sales.index)

plt.grid(linestyle='--', alpha=0.7)

plt.show()

# Region Wise Sales

region_sales = df.groupby('Region')['Sales'].sum()

print("\nRegion Wise Sales:")
print(region_sales)

# Region Wise Profit

region_profit = df.groupby('Region')['Profit'].sum()

print("\nRegion Wise Profit:")
print(region_profit)

# Region Wise Sales Chart

plt.figure(figsize=(8, 5))

region_sales.plot(
    kind='bar',
    color=['blue', 'green', 'orange', 'red']
)

plt.title("Region Wise Sales Analysis", fontsize=16)

plt.xlabel("Region", fontsize=12)

plt.ylabel("Sales", fontsize=12)

plt.xticks(rotation=0)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

# Region Wise Profit Chart

plt.figure(figsize=(8, 5))

region_profit.plot(
    kind='bar',
    color=['purple', 'teal', 'gold', 'crimson']
)

plt.title("Region Wise Profit Analysis", fontsize=16)

plt.xlabel("Region", fontsize=12)

plt.ylabel("Profit", fontsize=12)

plt.xticks(rotation=0)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

# Discount vs Profit Analysis

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x='Discount',
    y='Profit',
    data=df
)

plt.title("Discount vs Profit Analysis", fontsize=16)

plt.xlabel("Discount", fontsize=12)

plt.ylabel("Profit", fontsize=12)

plt.grid(linestyle='--', alpha=0.7)

plt.show()
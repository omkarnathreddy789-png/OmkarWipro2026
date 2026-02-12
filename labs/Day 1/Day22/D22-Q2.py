import pandas as pd
import numpy as np


df = pd.read_csv("sales.csv")

print("\nOriginal Data:")
print(df)


df["Total"] = df["Quantity"] * df["Price"]

print("\nData with Total column:")
print(df)

daily_sales = df["Total"].values

total_sales = np.sum(daily_sales)
average_daily_sales = np.mean(daily_sales)
std_dev_sales = np.std(daily_sales)

print("\nSales Statistics:")
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_daily_sales)
print("Standard Deviation of Daily Sales:", std_dev_sales)


best_product = df.groupby("Product")["Quantity"].sum().idxmax()
best_quantity = df.groupby("Product")["Quantity"].sum().max()

print("\nBest Selling Product:", best_product)
print("Total Quantity Sold:", best_quantity)

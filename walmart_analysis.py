import pandas as pd

# Load dataset
df = pd.read_csv("Walmart.csv")

# View first 5 rows
print(df.head())

# Basic info
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
df = df.dropna()
df = df.drop_duplicates()

print("After cleaning:", df.shape)
store_sales = df.groupby("Store")["Weekly_Sales"].sum()
print(store_sales)
print("Top 5 Stores:")
print(store_sales.sort_values(ascending=False).head())

print("Bottom 5 Stores:")
print(store_sales.sort_values().head())
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
# Remove rows where date conversion failed
df = df.dropna(subset=["Date"])

print(df.dtypes)
print(df["Date"].head())
import matplotlib.pyplot as plt

# Total sales over time
time_sales = df.groupby("Date")["Weekly_Sales"].sum()

plt.figure(figsize=(12,5))
plt.plot(time_sales)
plt.title("Total Walmart Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Weekly Sales")
plt.show()
# Create Month column
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Weekly_Sales"].mean()

plt.figure(figsize=(8,4))
monthly_sales.plot(kind="bar")
plt.title("Average Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Average Sales")
plt.show()
holiday_sales = df.groupby("Holiday_Flag")["Weekly_Sales"].mean()
print("Average Sales (0 = Non-Holiday, 1 = Holiday):")
print(holiday_sales)
correlation = df.corr(numeric_only=True)
print("Correlation with Weekly Sales:")
print(correlation["Weekly_Sales"].sort_values(ascending=False))
# Conclusion:
# The Walmart sales analysis revealed clear time-based trends and seasonal patterns.
# Sales were higher during holiday weeks.
# Seasonal patterns were observed across months.
# These insights help improve forecasting and inventory planning.

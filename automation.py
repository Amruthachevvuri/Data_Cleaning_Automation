import pandas as pd

# Load CSV Dataset
data = pd.read_csv("Sales_data.csv")

# Display Dataset
print("Dataset:")
print(data)

# Dataset Information
print("\nDataset Info:")
print(data.info())

# Check Missing Values
print("\nMissing Values:")
print(data.isnull().sum())

# Check Duplicate Rows
print("\nDuplicate Rows:", data.duplicated().sum())

# Fill Missing Values
data['Sales_Amount'] = data['Sales_Amount'].fillna(
    data['Sales_Amount'].mean()
)

data['Region'] = data['Region'].fillna('Unknown')

data['Customer_Type'] = data['Customer_Type'].fillna('Unknown')

# Verify Missing Values Removed
print("\nMissing Values After Cleaning:")
print(data.isnull().sum())

# Remove Duplicate Rows
data = data.drop_duplicates()

print("\nRows After Removing Duplicates:")
print(len(data))

# Standardize Region Names
data['Region'] = data['Region'].str.upper()

print("\nUnique Regions:")
print(data['Region'].unique())

# Summary Statistics
print("\nSummary Statistics:")
print(data.describe())

# Sales by Region
region_sales = data.groupby('Region')['Sales_Amount'].sum()

print("\nSales by Region:")
print(region_sales)

# Sales by Product Category
category_sales = data.groupby('Product_Category')['Sales_Amount'].sum()

print("\nSales by Product Category:")
print(category_sales)

# Sales by Customer Type
customer_sales = data.groupby('Customer_Type')['Sales_Amount'].sum()

print("\nSales by Customer Type:")
print(customer_sales)

# Export Cleaned Dataset
data.to_csv("cleaned_sales_data.csv", index=False)

# Export Reports
region_sales.to_csv("sales_by_region.csv")
category_sales.to_csv("sales_by_category.csv")
customer_sales.to_csv("sales_by_customer_type.csv")

print("\nReports Exported Successfully!")

import matplotlib.pyplot as plt
# Ssles by Region
plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.show()
# Sales by Product Category
plt.figure(figsize=(6,5))
category_sales.plot(kind='bar')
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales Amount")
plt.show()
# Sales by Customer Type
plt.figure(figsize=(6,5))
customer_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Customer Type")
plt.ylabel("")
plt.show()
# Saves Charts Automatically
plt.savefig("sales_by_region.png")
plt.savefig("sales_by_category.png")
plt.savefig("sales_by_customer_type.png")
plt.show()
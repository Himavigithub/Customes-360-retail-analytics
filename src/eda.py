import pandas as pd
import matplotlib.pyplot as plt
import os

# Get project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Load cleaned data
sales_path = os.path.join(project_root, "data", "sales_data.csv")
sales = pd.read_csv(sales_path)

# Total Sales by Category
category_sales = sales.groupby("category")["price"].sum()
category_sales.plot(kind="bar", title="Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# Region-wise Sales
region_sales = sales.groupby("region")["price"].sum()
region_sales.plot(kind="pie", autopct="%1.1f%%", title="Sales by Region")
plt.show()

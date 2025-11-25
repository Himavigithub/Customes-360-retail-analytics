import pandas as pd
import os

# Get the project root folder
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def load_data():
    sales_path = os.path.join(project_root, "data", "sales_data.csv")
    customers_path = os.path.join(project_root, "data", "customers.csv")
    
    sales = pd.read_csv(sales_path)
    customers = pd.read_csv(customers_path)
    return sales, customers

def clean_data(sales, customers):
    sales["date"] = pd.to_datetime(sales["date"])
    sales["total_sales"] = sales["price"] * sales["quantity"]
    customers.fillna({"loyalty_score": customers["loyalty_score"].mean()}, inplace=True)
    return sales, customers

if __name__ == "__main__":
    sales, customers = load_data()
    sales, customers = clean_data(sales, customers)
    print("Sales Data:\n", sales)
    print("\nCustomers Data:\n", customers)

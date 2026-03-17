# 🛒 Customer 360 Retail Sales Analysis

## 📌 Project Overview

This project performs a **Customer 360 Retail Analysis** to understand customer behavior, product performance, and sales patterns using Python and Power BI.

The objective is to transform raw retail transaction data into meaningful business insights that help organizations improve **customer retention, marketing strategies, and sales performance**.

The analysis includes:

• Customer Segmentation using RFM Analysis  
• Customer Retention using Cohort Analysis  
• Product Association using Market Basket Analysis  
• Sales Insights Visualization using Power BI  

---

# 📊 Dashboard Preview

## Retail Sales Overview
![Dashboard](images/dashboard_overview.png)

## Customer and Product Distribution
![Customers](images/customer_distribution.png)

## Pareto Sales Analysis
![Pareto](images/pareto_analysis.png)

---

# 📂 Dataset

The dataset contains retail transaction records including:

- Customer ID
- Invoice Date
- Product Details
- Sales Amount
- Order Information
- Delivery Type
- Region and Category

Total transactions analyzed: **~397,000**

---

# 🧠 Python Analysis

Python was used to perform advanced customer and sales analysis.

## 1️⃣ RFM Analysis (Customer Segmentation)

RFM stands for:

- **Recency** → How recently a customer purchased
- **Frequency** → How often a customer purchases
- **Monetary** → How much money the customer spends

Customers were scored from **1–5** for each metric and grouped into segments such as:

- Champions
- Loyal Customers
- At Risk
- Recent Customers
- Hibernating

This helps businesses identify **high-value customers and target them effectively.**

---

## 2️⃣ Cohort Analysis (Customer Retention)

Cohort analysis groups customers based on their **first purchase month** and tracks how many customers return in subsequent months.

This helps measure:

- Customer retention
- Customer lifetime engagement
- Loyalty patterns

---

## 3️⃣ Market Basket Analysis

Market Basket Analysis identifies products that are frequently purchased together.

The **Apriori algorithm** was used to generate association rules.

Example rule:

Product A → Product B

Meaning customers who buy Product A are also likely to buy Product B.

This helps businesses with:

- Product bundling
- Cross-selling strategies
- Recommendation systems

---

# 📈 Power BI Dashboard

Power BI was used to build an interactive dashboard with key insights such as:

• Total Sales and Profit  
• Sales by Category and Region  
• Profit vs Sales Trend  
• Customer Distribution  
• Delivery Performance  
• Pareto Sales Analysis (80/20 Rule)

These visualizations help stakeholders make **data-driven decisions**.

---

# 🧰 Technologies Used

Python  
Pandas  
NumPy  
MLxtend  
PostgreSQL  
Power BI  

---

# 📊 Key Insights

• A small number of product categories generate the majority of sales (Pareto principle).  
• High-value customers contribute significantly to revenue.  
• Customer retention drops after the first few months.  
• Certain products are frequently purchased together.

These insights help improve **marketing strategies and sales planning**.

---

# 🚀 How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/customer-360-retail-analysis.git
```

2 Install dependencies

```
pip install -r requirements.txt
```

3 Run the analysis script

```
python rfm_engine.py
```

4 Open the Power BI dashboard

```
customer_360.pbix
```



# 📌 Project Structure

```
customer-360-retail-analysis
│
├── postgres sql
├── vscode
├── data
├── src
├── dashboard
├── requirements.txt



Data Analytics | Python | Power BI | SQL

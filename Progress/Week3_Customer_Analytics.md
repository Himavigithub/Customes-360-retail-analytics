# Week 3 – Customer Analytics Using Python

## Objective
Analyze customer purchasing behavior using Python.

## Techniques Implemented

### RFM Analysis
Customer segmentation based on:

- **Recency** – How recently a customer purchased
- **Frequency** – Number of purchases
- **Monetary** – Total spending

Example calculation:


rfm = df.groupby("customer_id").agg({
"invoice_date": lambda x: (snapshot_date - x.max()).days,
"customer_id": "count",
"total_sales": "sum"
})


### Customer Segments
- Champions
- Loyal Customers
- Recent Customers
- At Risk
- Hibernating

### Cohort Analysis
Performed cohort analysis to analyze **customer retention patterns over time**.

### Market Basket Analysis
Used **Apriori Algorithm** to identify frequently purchased product combinations.

Example rule:


Product 20725 → Product 20726


## Outcome
Generated customer segmentation insights and product association rules.

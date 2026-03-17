import pandas as pd
import psycopg2

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="consumer360",
    user="postgres",
    password="postgres",
    port="5432"
)

query = """
SELECT customer_id,
       invoice_date,
       total_sales
FROM fact_sales;
"""

df = pd.read_sql(query, conn)

conn.close()

print(df.head())
print(df.info())
df['invoice_date'] = pd.to_datetime(df['invoice_date'])

print(df.dtypes)
import datetime as dt

# Set reference date (today)
today = df['invoice_date'].max() + dt.timedelta(days=1)

rfm = df.groupby('customer_id').agg({
    'invoice_date': lambda x: (today - x.max()).days,
    'customer_id': 'count',
    'total_sales': 'sum'
})

rfm.rename(columns={
    'invoice_date': 'Recency',
    'customer_id': 'Frequency',
    'total_sales': 'Monetary'
}, inplace=True)

print(rfm.head())

# Create R, F, M scores using quintiles

rfm['R_score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm['M_score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

# Convert to integer
rfm['R_score'] = rfm['R_score'].astype(int)
rfm['F_score'] = rfm['F_score'].astype(int)
rfm['M_score'] = rfm['M_score'].astype(int)

print(rfm.head())

rfm['RFM_Score'] = (
    rfm['R_score'].astype(str) +
    rfm['F_score'].astype(str) +
    rfm['M_score'].astype(str)
)

print(rfm.head())

def segment_customer(row):
    if row['R_score'] >= 4 and row['F_score'] >= 4 and row['M_score'] >= 4:
        return "Champions"
    elif row['R_score'] >= 3 and row['F_score'] >= 3:
        return "Loyal Customers"
    elif row['R_score'] >= 4:
        return "Recent Customers"
    elif row['R_score'] <= 2 and row['F_score'] >= 3:
        return "At Risk"
    else:
        return "Hibernating"

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

print(rfm['Segment'].value_counts())
rfm.groupby('Segment')['Monetary'].mean().sort_values(ascending=False)
rfm = rfm.reset_index()
print(rfm.head())
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/consumer360")
print(rfm.columns)

rfm.to_sql("customer_rfm", engine, if_exists="replace", index=False)

print("RFM table successfully written to PostgreSQL")
# Reconnect to database for cohort analysis
conn = psycopg2.connect(
    host="localhost",
    database="consumer360",
    user="postgres",
    password="postgres",
    port="5432"
)

query = """
SELECT customer_id,
       invoice_date
FROM fact_sales;
"""

df = pd.read_sql(query, conn)

conn.close()
df['invoice_date'] = pd.to_datetime(df['invoice_date'])
# Create purchase month column
df['InvoiceMonth'] = df['invoice_date'].dt.to_period('M')

# Get customer's first purchase month
df['CohortMonth'] = df.groupby('customer_id')['invoice_date'] \
                       .transform('min') \
                       .dt.to_period('M')

print(df.head())
df['CohortIndex'] = (
    (df['InvoiceMonth'].dt.year - df['CohortMonth'].dt.year) * 12 +
    (df['InvoiceMonth'].dt.month - df['CohortMonth'].dt.month) + 1
)

print(df.head())
cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])['customer_id'] \
                .nunique() \
                .reset_index()

cohort_counts = cohort_data.pivot(index='CohortMonth',
                                   columns='CohortIndex',
                                   values='customer_id')

print(cohort_counts.head())
retention = cohort_counts.divide(cohort_counts.iloc[:,0], axis=0)

print(retention.head())
conn = psycopg2.connect(
    host="localhost",
    database="consumer360",
    user="postgres",
    password="postgres",
    port="5432"
)

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# -----------------------------
# STEP 1: Load smaller dataset
# -----------------------------

query = """
SELECT invoice_no, stock_code
FROM clean_retail
LIMIT 200000
"""

basket_df = pd.read_sql(query, conn)

# -----------------------------
# STEP 2: Remove rare products
# -----------------------------

product_counts = basket_df['stock_code'].value_counts()
top_products = product_counts[product_counts > 50].index  # keep products sold > 50 times

basket_df = basket_df[basket_df['stock_code'].isin(top_products)]

# -----------------------------
# STEP 3: Create Basket Matrix
# -----------------------------

basket_matrix = (
    basket_df
    .groupby(['invoice_no', 'stock_code'])['stock_code']
    .count()
    .unstack()
    .fillna(0)
)

basket_matrix = (basket_matrix > 0)

print("Basket shape:", basket_matrix.shape)

# -----------------------------
# STEP 4: Run Apriori SAFELY
# -----------------------------

frequent_itemsets = apriori(
    basket_matrix,
    min_support=0.02,   # increased support
    use_colnames=True
)

print("Frequent Itemsets:")
print(frequent_itemsets.head())

# -----------------------------
# STEP 5: Association Rules
# -----------------------------

if not frequent_itemsets.empty:
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    print("Rules:")
    print(rules.head())
else:
    print("No frequent itemsets found. Increase support.")
rules.to_csv("association_rules.csv", index=False)
print("Association rules exported successfully.")
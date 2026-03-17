-- ==============================
-- CUSTOMER 360 RETAIL ANALYSIS
-- POSTGRESQL WORKFLOW
-- ==============================

-- 1. Create Database
CREATE DATABASE retail_customer360;

-- Connect to database
\c retail_customer360;

-- 2. Create Retail Transactions Table
CREATE TABLE retail_transactions (
    invoice_no VARCHAR(20),
    stock_code VARCHAR(20),
    description TEXT,
    quantity INT,
    invoice_date TIMESTAMP,
    price FLOAT,
    customer_id INT,
    country VARCHAR(50)
);

-- 3. Import Retail Dataset (CSV file)
COPY retail_transactions
FROM '/path/retail_dataset.csv'
DELIMITER ','
CSV HEADER;

-- 4. Preview Dataset
SELECT * FROM retail_transactions
LIMIT 10;

-- 5. Check Total Records
SELECT COUNT(*) FROM retail_transactions;

-- 6. Identify Missing Customer IDs
SELECT COUNT(*)
FROM retail_transactions
WHERE customer_id IS NULL;

-- 7. Remove Records with Missing Customer IDs
DELETE FROM retail_transactions
WHERE customer_id IS NULL;

-- 8. Check Duplicate Transactions
SELECT invoice_no, customer_id, COUNT(*)
FROM retail_transactions
GROUP BY invoice_no, customer_id
HAVING COUNT(*) > 1;

-- 9. Calculate Total Sales Per Customer
SELECT
    customer_id,
    SUM(quantity * price) AS total_sales
FROM retail_transactions
GROUP BY customer_id
ORDER BY total_sales DESC;

-- 10. Prepare Data for RFM Analysis
SELECT
    customer_id,
    MAX(invoice_date) AS last_purchase,
    COUNT(invoice_no) AS frequency,
    SUM(quantity * price) AS monetary
FROM retail_transactions
GROUP BY customer_id;

-- 11. Export Processed RFM Data
COPY (
SELECT
    customer_id,
    MAX(invoice_date) AS last_purchase,
    COUNT(invoice_no) AS frequency,
    SUM(quantity * price) AS monetary
FROM retail_transactions
GROUP BY customer_id
)
TO '/path/customer_rfm.csv'
CSV HEADER;

-- ==============================
-- End of PostgreSQL Data Pipeline
-- ==============================

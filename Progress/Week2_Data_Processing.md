# Week 2 – Data Engineering & PostgreSQL Integration

## Objective
Clean the retail dataset and store structured data in PostgreSQL.

## Tasks Completed
- Connected Python with PostgreSQL database
- Extracted retail transaction data using SQL
- Loaded dataset into Python for processing
- Cleaned and structured data

## SQL Query Example

SELECT customer_id, invoice_date, total_sales
FROM retail_transactions;


## Data Cleaning Steps
- Removed missing customer IDs
- Converted invoice_date to datetime format
- Verified numeric format for sales values
- Checked duplicate records

## Data Storage
Cleaned data stored in PostgreSQL tables.

Example table created:

customer_rfm


## Outcome
Cleaned dataset successfully stored and prepared for analytics.

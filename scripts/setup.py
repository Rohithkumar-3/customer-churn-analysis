# %% 
# ---- IMPORTS ----
import pandas as pd
import sqlite3

# %%
# ---- LOAD CSV ----
df = pd.read_csv('../data/telco_churn.csv')
print("Shape:", df.shape)
print(df.head())

# %%
# ---- CREATE SQLITE DATABASE ----
conn = sqlite3.connect('../data/churn.db')
df.to_sql('customers', conn, if_exists='replace', index=False)
print("Data loaded into churn.db successfully!")

# %%
# ---- QUERY 1: Overall churn rate ----
q1 = """
SELECT Churn, COUNT(*) AS total,
ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM customers
GROUP BY Churn
"""
print(pd.read_sql_query(q1, conn))

# %%
# ---- QUERY 2: Churn by contract type ----
q2 = """
SELECT Contract, COUNT(*) AS total_customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS churned,
ROUND(SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2) AS churn_rate
FROM customers
GROUP BY Contract
ORDER BY churn_rate DESC
"""
print(pd.read_sql_query(q2, conn))

# %%
# ---- QUERY 3: Churn by tenure bucket ----
q3 = """
SELECT 
    CASE 
        WHEN tenure <= 12 THEN '0-12 months'
        WHEN tenure <= 24 THEN '13-24 months'
        WHEN tenure <= 48 THEN '25-48 months'
        ELSE '49+ months'
    END AS tenure_group,
    COUNT(*) AS total,
    ROUND(SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2) AS churn_rate
FROM customers
GROUP BY tenure_group
ORDER BY churn_rate DESC
"""
print(pd.read_sql_query(q3, conn))

# %%
# ---- QUERY 4: Avg charges churned vs retained ----
q4 = """
SELECT Churn,
ROUND(AVG(CAST(MonthlyCharges AS FLOAT)),2) AS avg_monthly_charges,
ROUND(AVG(tenure),1) AS avg_tenure_months
FROM customers
GROUP BY Churn
"""
print(pd.read_sql_query(q4, conn))

# %%
# ---- QUERY 5: Churn by payment method ----
q5 = """
SELECT PaymentMethod, COUNT(*) AS total,
ROUND(SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2) AS churn_rate
FROM customers
GROUP BY PaymentMethod
ORDER BY churn_rate DESC
"""
print(pd.read_sql_query(q5, conn))

# %%
# ---- SAVE RESULTS ----
pd.read_sql_query(q2, conn).to_csv('../data/churn_by_contract.csv', index=False)
print("Results saved!")
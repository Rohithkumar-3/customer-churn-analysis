# 📊 Customer Churn Analysis & Prediction

An end-to-end data analyst project analyzing customer churn for a telecom company using Python, SQL, and Power BI.

---

## 🎯 Problem Statement
A telecom company is losing customers every month. The goal is to:
- Identify **why** customers are churning
- Predict **which** customers are likely to churn next
- Provide **actionable recommendations** to reduce churn

---

## 📁 Project Structure

```
churn_project/
│
├── data/                        # Raw and cleaned data
│   ├── telco_churn.csv          # Original Kaggle dataset
│   └── churn.db                 # SQLite database
│
├── scripts/                     # Python analysis scripts
│   ├── step1_setup.py           # Data loading & SQL queries
│   ├── step2_eda.py             # Data cleaning & EDA charts
│   ├── step3_model.py           # ML churn prediction model
│   └── step4_export.py          # Export CSVs for Power BI
│
├── outputs/                     # All generated outputs
│   ├── customers_clean.csv
│   ├── churn_by_contract.csv
│   ├── churn_by_payment.csv
│   ├── churn_by_tenure.csv
│   ├── churn_by_internet.csv
│   ├── at_risk_customers.csv    # High-risk customers flagged
│   └── *.png                    # EDA & model charts
│
├── churn_dashboard.pbix         # Power BI dashboard (3 pages)
├── requirements.txt             # Python dependencies
└── README.md
```

---

## 🛠️ Tools & Technologies

| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| Data manipulation | Pandas, NumPy |
| Database | SQLite, SQL |
| Visualization | Matplotlib, Seaborn |
| Machine learning | Scikit-learn |
| Dashboard | Microsoft Power BI |
| IDE | VS Code |

---

## 📊 Key Findings

| Finding | Insight |
|---------|---------|
| 📌 Contract type | Month-to-month customers churn at **43%** vs only **3%** for two-year contracts |
| 📌 Tenure | New customers (0–12 months) churn at **3x the rate** of long-term customers |
| 📌 Payment method | Electronic check users have the highest churn rate at **45%** |
| 📌 Monthly charges | Churned customers pay **$74/mo on average** vs $61 for retained customers |

---

## 🤖 Model Performance

| Model | AUC-ROC | Precision | Recall |
|-------|---------|-----------|--------|
| Logistic Regression | 0.83 | 0.76 | 0.58 |
| Random Forest | 0.85 | 0.79 | 0.62 |

✅ **Random Forest selected** as final model — better AUC and recall for churn detection.

---

## 💡 Business Recommendations

**1. Convert month-to-month customers to annual contracts**
Offer a 20% discount to high-risk month-to-month customers.
Estimated impact: Could reduce overall churn rate by 10–15%.

**2. Launch a 90-day onboarding program**
New customers in the first 12 months need proactive engagement —
check-in calls, tutorials, and service reviews.

**3. Incentivize auto-pay adoption**
Electronic check users churn at 45%. Offering a small billing
discount to switch to auto-pay could significantly reduce this.

---

## 🚀 How to Run

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/customer-churn-analysis.git
cd customer-churn-analysis
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run scripts in order**
```bash
cd scripts
python step1_setup.py
python step2_eda.py
python step3_model.py
python step4_export.py
```

**4. Open dashboard**
Open `churn_dashboard.pbix` in Power BI Desktop.

---

## 📸 Dashboard Preview

> Add screenshots of your 3 Power BI pages here after publishing.

---

## 📬 Contact

**Your Name**
📧 your.email@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/yourprofile)
💻 [GitHub](https://github.com/yourusername)

---

*Dataset: [Telco Customer Churn — Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)*

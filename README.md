# Customer Churn Analysis & Prediction

A data analytics project that explores customer churn in the telecom industry using Python, SQL, machine learning, and Power BI.

The idea behind this project is simple: understand why customers leave a telecom service, identify the factors associated with churn, and use historical customer data to predict which customers may be at risk of leaving.

## About the Project

Customer churn is a common problem for telecom companies. Losing customers affects revenue, and acquiring new customers can be more expensive than retaining existing ones.

In this project, I worked with telecom customer data to explore churn patterns, compare different customer groups, and build a machine learning model to identify customers who may be more likely to leave.

The analysis covers customer contracts, tenure, payment methods, internet services, and monthly charges. The results are also presented in a Power BI dashboard to make the findings easier to understand.

## Tools Used

- **Python:** Data cleaning, exploratory data analysis, and model development
- **Pandas & NumPy:** Data manipulation and preparation
- **SQL & SQLite:** Data storage, querying, and aggregation
- **Matplotlib & Seaborn:** Charts and data visualization
- **Scikit-learn:** Training and evaluating machine learning models
- **Power BI:** Interactive dashboard development

## Project Structure

```text
churn_project/
│
├── data/
│   └── churn_by_contract.csv
│
├── scripts/
│   ├── setup.py
│   ├── datacleaning_eda.py
│   ├── model.py
│   └── powerbi_export.py
│
├── outputs/
│   ├── customers_clean.csv
│   ├── churn_by_contract.csv
│   ├── churn_by_payment.csv
│   ├── churn_by_tenure.csv
│   ├── churn_by_internet.csv
│   ├── at_risk_customers.csv
│   └── *.png
│
├── Dashboard/
│   └── churn_dashboard.pbix
│
├── requirements.txt
└── README.md
```

The scripts handle different stages of the workflow, from preparing the data to generating analysis outputs and exporting data for Power BI.

## What I Found in the Data

A few patterns stood out during the analysis:

- **Contract type:** Month-to-month customers had a churn rate of around 43%, compared with approximately 3% for customers on two-year contracts.
- **Customer tenure:** Customers in their first year showed a higher tendency to churn than customers who had stayed for longer.
- **Payment method:** Customers paying through electronic checks had the highest churn rate, at around 45%.
- **Monthly charges:** Customers who left were paying approximately $74 per month on average, compared with $61 among customers who stayed.

These patterns suggest that contract flexibility, the early customer experience, payment preferences, and monthly costs may all be useful areas to investigate when trying to understand churn.

*Note: These figures should be verified against the dataset and the final analysis outputs before being treated as confirmed results.*

## Churn Prediction Model

I compared two classification models to see how well they could identify customers likely to churn.

| Model | ROC-AUC | Precision | Recall |
|---|---:|---:|---:|
| Logistic Regression | 0.83 | 0.76 | 0.58 |
| Random Forest | 0.85 | 0.79 | 0.62 |

Based on these reported evaluation results, Random Forest was selected as the final model. It achieved a higher ROC-AUC, precision, and recall than Logistic Regression.

The model can be used to generate churn-risk predictions for individual customers. These predictions can help prioritize customers for further analysis or retention efforts.

## Business Recommendations

Based on the patterns identified in the analysis, I would focus on three areas:

**1. Improve retention among month-to-month customers**

Test targeted offers or annual-plan discounts for customers showing signs of churn risk. The aim would be to encourage longer-term contracts without giving unnecessary discounts to customers who are likely to stay anyway.

**2. Focus on the first year of the customer journey**

Introduce follow-up calls, service reviews, and onboarding support during the first few months. This could help identify issues before customers decide to leave.

**3. Review the electronic-check payment experience**

Investigate whether billing problems, payment friction, or customer preferences contribute to the higher churn rate among electronic-check users. Where appropriate, encourage convenient alternatives such as automatic payments.

These are proposed actions based on the observed patterns. Their actual impact would need to be tested using a controlled experiment or a suitable retention campaign.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Rohithkumar-3/customer-churn-analysis.git
cd customer-churn-analysis
```

Replace the repository URL with the actual GitHub repository URL if the project has a different name.

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analysis scripts

Run the scripts from the project root directory:

```bash
python scripts/setup.py
python scripts/datacleaning_eda.py
python scripts/model.py
python scripts/powerbi_export.py
```

Run them in order so that the required data and output files are available to the later steps.

### 4. Open the Power BI dashboard

Open `Dashboard/churn_dashboard.pbix` using Power BI Desktop.

If the dashboard uses local CSV files, update the data source paths when prompted.

## Dataset

This project uses the [Telco Customer Churn dataset on Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).

The dataset contains customer information, service details, billing information, contract types, and churn status.

## Contact

**Rohith Kumar V**

- Email: mail.rohithkumar@gmail.com
- LinkedIn: https://www.linkedin.com/in/rohith-kumar-rk/
- GitHub: https://github.com/Rohithkumar-3

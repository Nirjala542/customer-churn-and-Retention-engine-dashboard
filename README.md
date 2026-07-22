# Customer Churn and Retention Engine Dashboard
https://customer-churn-engine.streamlit.app/

A Streamlit dashboard for exploring customer churn and retention insights using telecom customer data. The app visualizes churn distribution, revenue performance, customer risk, and retention recommendations with interactive charts and metrics.

## 🚀 Project Overview

This dashboard helps business users:
- Monitor customer churn and retention trends
- Identify high-risk customers and revenue at risk
- Analyze contract performance, revenue, and customer behavior
- Review individual customer profiles and retention recommendations
- Generate business insights and growth strategies

## 📂 Project Structure

```text
customer-churn-and-Retention-engine-dashboard/
├── app/
│   └── dashboards.py        # Main Streamlit dashboard application
├── dataset.ipynb           # Notebook for dataset exploration and preprocessing
├── requirements.txt        # Python package dependencies
├── telco.csv               # Original raw telecom dataset
└── telco_cleaned.csv       # Cleaned dataset used by the dashboard
```

## 🧰 Development Environment

- Python: `3.10+` (recommended)
- Platform: Windows, macOS, or Linux
- App framework: Streamlit
- Visualization: Plotly

## 📦 Dependencies

The project dependencies are listed in `requirements.txt`:

- `streamlit`
- `pandas`
- `plotly`
- `streamlit_option_menu`

## ✅ Features

- Dashboard overview with customer counts, churn, revenue, CLTV, and monthly charge
- Interactive charts: scatter, pie, bar, box, treemap, histogram, map
- Exploratory Data Analysis page with dataset preview, description, and missing value summary
- Customer Analytics page with churn/revenue visualizations and contract analysis
- Customer Profile page with detailed profile metrics and retention advice
- High Risk Customers page with downloadable list of risky accounts
- Revenue Analysis page with revenue breakdown and distribution analysis
- Retention Engine page with customer-specific risk-based recommendations
- Business Insights page with health meter and actionable suggestions

## ⚙️ Installation

1. Clone or download the repository.  
 git clone https://github.com/Nirjala542/customer-churn-and-Retention-engine-dashboard
2. Open a terminal in the project folder.
cd customer-churn-and-Retention-engine-dashboard
code .
3. Create a virtual environment (recommended):

```bash
python -m venv venv
```

4. Activate the environment:

Windows:
```powershell
venv\Scripts\Activate.ps1
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Dashboard

From the project root, run:

```bash
streamlit run app/dashboards.py
```

Then open the local URL shown in the terminal.

## 📈 Dataset Details

The dashboard uses `telco_cleaned.csv` and includes customer-level fields such as:
- `Customer ID`
- `Churn Label`
- `Churn Score`
- `Total Revenue`
- `Monthly Charge`
- `Contract`
- `Customer Status`
- `Internet Service`
- `Payment Method`
- `CLTV`
- `Tenure in Months`
- `Latitude` and `Longitude`

## 📝 Notes

- Ensure `telco_cleaned.csv` is present in the project root before running the app.
- The dashboard is built for Streamlit and requires a modern browser.

## 💡 Suggestions

For future improvement, consider adding:
- real-time churn prediction models
- CRM integration
- automated alerting for high-risk customers
- sentiment-based customer feedback analytics

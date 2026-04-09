# 📦 Vendor Invoice Intelligence System  
**Freight Cost Prediction & Invoice Risk Flagging**

---

## 📌 Table of Contents
- <a href="#project-overview">Project Overview</a>  
- <a href="#business-objectives">Business Objectives</a>  
- <a href="#data-sources">Data Sources</a>  
- <a href="#eda">Exploratory Data Analysis</a>  
- <a href="#models-used">Models Used</a>  
- <a href="#metrics">Evaluation Metrics</a>  
- <a href="#application">Application</a>  
- <a href="#project-structure">Project Structure</a>  
- <a href="#how-to-run-this-project">How to Run This Project</a>  
- <a href="#author--contact">Author & Contact</a>  

---

<h2 id="project-overview">🚀 Project Overview</h2>

This project implements an **end-to-end machine learning system** designed to support finance teams by:

1. **Predicting expected freight cost** for vendor invoices.  
2. **Flagging high-risk invoices** that require manual review due to abnormal cost, freight, or operational patterns.  

---

<h2 id="business-objectives">🎯 Business Objectives</h2>

### 1. Freight Cost Prediction (Regression)

**Objective:**  
Predict the expected freight cost for a vendor invoice using quantity, invoice value, and historical behavior.

**Why it matters:**
- Freight is a non-trivial component of landed cost  
- Poor freight estimation impacts margin analysis and budgeting  
- Early prediction improves procurement planning and vendor negotiation  

---

### 2. Invoice Risk Flagging (Classification)

**Objective:**  
Predict whether a vendor invoice should be flagged for manual approval due to abnormal cost, freight, or delivery patterns.

**Why it matters:**
- Manual invoice review does not scale  
- Financial leakage often occurs in large or complex invoices  
- Early risk detection improves audit efficiency and operational control  

---

<h2 id="data-sources">📂 Data Sources</h2>

Data is stored in a relational **SQLite database (`inventory.db`)** with the following tables:

- `vendor_invoice` → Invoice-level financial and timing data  
- `purchases` → Item-level purchase details  
- `purchase_prices` → Reference purchase prices  
- `begin_inventory`, `end_inventory` → Inventory snapshots  

SQL aggregation is used to generate invoice-level features.

---

<h2 id="eda">📊 Exploratory Data Analysis (EDA)</h2>

EDA focuses on business-driven questions, such as:

- Do flagged invoices have higher financial exposure?  
- Does freight scale linearly with quantity?  
- Does freight cost depend on quantity?  

Statistical tests (t-tests) are used to confirm that flagged invoices differ meaningfully from normal invoices.

---

<h2 id="models-used">🤖 Models Used</h2>

### Regression (Freight Prediction)
- Linear Regression (baseline)  
- Decision Tree Regressor  
- Random Forest Regressor (**final model**)  

### Classification (Invoice Flagging)
- Logistic Regression (baseline)  
- Decision Tree Classifier  
- Random Forest Classifier (**final model with GridSearchCV**)  

Hyperparameter tuning is performed using **GridSearchCV with F1-score** to handle class imbalance.

---

<h2 id="metrics">📈 Evaluation Metrics</h2>

### Freight Prediction
- MAE (Mean Absolute Error)  
- RMSE (Root Mean Squared Error)  
- R² Score  

### Invoice Flagging
- Accuracy  
- Precision, Recall, F1-score  
- Classification Report  
- Feature Importance Analysis  

---

<h2 id="application">🖥️ End-to-End Application</h2>

A Streamlit application demonstrates the complete pipeline:

- Input invoice details  
- Predict expected freight  
- Flag invoices in real time  
- Provide human-readable explanations  

---


---

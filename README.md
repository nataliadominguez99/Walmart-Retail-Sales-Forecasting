# 🛒 Walmart Retail Sales Forecasting – A Machine Learning Project

Forecasting Walmart’s weekly sales using historical data from multiple stores, departments, and external factors. The project combines **data cleaning, exploratory analysis, feature engineering, and machine learning models** to predict future sales and evaluate the effect of holidays, store type, and promotions.  

Additionally, the project integrates **Streamlit** for building an interactive dashboard where users can visualize sales trends and test model forecasts.  

---

## 📂 Dataset Description

- **Dataset Source:** [Kaggle – Walmart Sales Forecasting](https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast)  
- **Files Used:**
  - `features.csv` → External factors such as temperature, fuel price, CPI, unemployment, and promotional discounts (`MarkDown1–5`).
  - `stores.csv` → Metadata on stores, including store type (`A`, `B`, `C`) and size.
  - `train.csv` → Historical weekly sales by store and department.
  - `test.csv` → Data for evaluation (without sales labels).  

**Notable Quirks:**
- **Granularity:** Weekly sales per department per store.  
- **Holidays:** Flagged dates for **Super Bowl, Labor Day, Thanksgiving, Christmas**.  
- **Missing Values:** Many `MarkDown` columns contain NaNs.  
- **Store Diversity:** Different store types and sizes lead to varied sales behavior.  
- **Multiple Tables:** Required merging/joining for a complete dataset.  

---

## 🎯 Research Goal

- Predict **weekly sales** across Walmart stores and departments.  
- Analyze the influence of **holidays, promotions, store type/size, and economic conditions**.  
- Build a **Streamlit app** for interactive sales forecasting and visualization.  

---

## 🛠 Steps Taken

1. **Data Cleaning**
   - Converted date fields to datetime format  
   - Handled missing values in `MarkDown` features  
   - Checked for duplicates and outliers  
   - Merged tables (`features`, `stores`, `train`)  

2. **Exploratory Data Analysis (EDA)**
   - Distribution of weekly sales  
   - Impact of holidays on sales peaks  
   - Correlation analysis with external variables (fuel price, temperature, CPI)  
   - Store-level and department-level comparisons  

3. **Feature Engineering**
   - Created lag features and rolling means for time dependency  
   - Encoded categorical variables (`Store`, `Dept`, `Type`)  
   - Added holiday indicators and seasonality patterns  

4. **Modeling**
   - Baseline regression models (Linear Regression, Random Forest)  
   - Advanced models (XGBoost, LightGBM) for improved forecasting  
   - Performance evaluated with **RMSE** and **R2**  

5. **Streamlit App**
   - Built an interactive app to visualize sales distributions, trends, and forecasts  
   - Allows selection of store, department, and date ranges  
   - Displays model predictions alongside historical sales  

---

## 📌 Main Findings

- **Holiday Impact:** Strong sales spikes during Thanksgiving and Christmas, moderate during Super Bowl, mixed during Labor Day.  
- **Store Characteristics:** Type `A` stores (largest size) consistently show higher sales.  
- **Promotions:** `MarkDown` discounts significantly influence demand, though sparsely applied.  
- **Seasonality:** Sales increase toward year-end, showing clear quarterly patterns.  

---

## 💻 How to Reproduce

**Prerequisites:**
- Python **3.10+**
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `lightgbm`, `scipy`, `streamlit`

**Run Instructions:**
1. **Clone this repository**
   ```bash
   git clone https://github.com/nataliadominguez99/Walmart-Sales-Forecasting.git
2. **Navigate to the project folder**
   ```bash
    cd Walmart-Sales-Forecasting

3. **Install requirements**
   ```bash
    pip install -r requirements.txt

4. **Open the Jupyter Notebook**
- If you use Jupyter Notebook:
   ```bash
   jupyter notebook "Walmart Retail Sales Forecasting.ipynb"
- Or, open it in VSCode by double-clicking the file or using:
   ```bash
    code "Walmart Retail Sales Forecasting.ipynb"
  
5. **Ensure the dataset is in the correct location**
- The nextfiles must be in the same directory as the notebook:
  - features.csv
  - stores.csv
  - test.csv
  - train.csv

6. Run the Streamlit app
- streamlit run app.py

## 🚀 Next Steps

- Expand Streamlit app with forecasting simulations and dashboards
- Add external datasets (macroeconomic data, local events, weather)
- Implement deep learning models (LSTMs, Transformers) for time series
- Build Tableau dashboards for business stakeholders  

---

## 📁 Repo Structure
```bash
├── Walmart Retail Sales Forecasting.ipynb         # Notebook with cleaning, EDA, feature engineering, modeling
├── Walmart Retail Sales Forecasting - A Machine Learning Project.ppt   # Final project presentation
├── features.csv                                   # External factors dataset
├── stores.csv                                     # Store metadata
├── train.csv                                      # Training dataset with weekly sales
├── test.csv                                       # Test dataset without labels
├── app.py                                         # Streamlit app for visualization and forecasting
├── requirements.txt                               # Project dependencies

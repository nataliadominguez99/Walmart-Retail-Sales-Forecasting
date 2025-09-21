import streamlit as st
import pandas as pd
import pickle
import datetime

# ========================
# Load the model
# ========================
@st.cache_resource
def load_model():
    with open("best_xgb_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# ========================
# App configuration
# ========================
st.set_page_config(page_title="Weekly Sales", page_icon="🛒", layout="wide")
st.title("🛒 Walmart Weekly Sales Prediction")
st.markdown("This app uses the optimized **XGBoost model** to predict **Weekly Sales**.")

st.divider()

# ========================
# User input layout
# ========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏪 Store Information")
    store = st.selectbox("Select Store (1–45)", list(range(1, 46)))
    dept = st.selectbox("Select Department (1–81)", list(range(1, 82)))
    is_holiday_str = st.radio("Is it a holiday?", ["No", "Yes"], horizontal=True)
    is_holiday = 1 if is_holiday_str == "Yes" else 0

with col2:
    st.subheader("📅 Date Information")
    year = st.number_input("Year", min_value=2000, max_value=2030, value=2012, step=1)
    month = st.number_input("Month", min_value=1, max_value=12, value=5, step=1)
    day = st.number_input("Day", min_value=1, max_value=31, value=15, step=1)

    # Automatically compute day of week (0=Monday, ..., 6=Sunday)
    try:
        day_of_week = datetime.date(int(year), int(month), int(day)).weekday()
    except ValueError:
        st.warning("⚠️ Invalid date. Please check the year, month, and day values.")
        day_of_week = 0

# ========================
# Preprocessing
# ========================
input_data = pd.DataFrame({
    "Store": [store],
    "Dept": [dept],
    "IsHoliday": [is_holiday],
    "year": [year],
    "month": [month],
    "day": [day],
    "DayOfWeek": [day_of_week]
})

# One-hot encoding for Store and Dept
input_prep = pd.get_dummies(input_data, columns=["Store", "Dept"], drop_first=True)

# ========================
# Ensure same columns as training
# ========================
@st.cache_data
def get_train_columns():
    with open("train_columns.pkl", "rb") as f:
        train_columns = pickle.load(f)
    return train_columns

try:
    train_columns = get_train_columns()
    input_prep = input_prep.reindex(columns=train_columns, fill_value=0)
except FileNotFoundError:
    st.error("⚠️ Missing file 'train_columns.pkl'. Please save it from your notebook with the training columns.")

# ========================
# Prediction
# ========================
st.divider()
if st.button("🔮 Predict Weekly Sales", use_container_width=True):
    try:
        prediction = model.predict(input_prep)[0]
        st.metric("Predicted Weekly Sales", f"${prediction:,.2f}")
    except Exception as e:
        st.error(f"Prediction error: {e}")

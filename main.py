
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    file_path = "data/ecom_data.csv"  # Update with your correct path
    df = pd.read_csv(file_path)
    df['Signup_Date'] = pd.to_datetime(df['Signup_Date'])
    df['Last_Purchase_Date'] = pd.to_datetime(df['Last_Purchase_Date'])
    return df

df = load_data()

# Title
st.title("📊 E-Commerce CRM Analysis Dashboard")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df)

# Display Summary
st.subheader("Customer Summary Statistics")
st.write(df.describe())

# Churn Risk Visualization
st.subheader("Churn Risk Distribution")
fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(x="Churn_Risk", data=df, palette="coolwarm", ax=ax)
st.pyplot(fig)

# Loyalty Points vs Total Spend
st.subheader("Loyalty Points vs Total Spend")
fig, ax = plt.subplots()
sns.scatterplot(x=df["Total_Spend"], y=df["Loyalty_Points"], hue=df["Churn_Risk"], palette="coolwarm", ax=ax)
st.pyplot(fig)

st.write("📌 **Tip:** Identify high-spending, low-loyalty customers for targeted retention strategies.")

# Run: `streamlit run app.py`

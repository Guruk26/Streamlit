# Task 4 – Mini Dashboard

import streamlit as st

# Step 1: Title + Description
st.write("Simple Sales Dashboard")
st.write("This dashboard shows monthly sales data and a simple bar chart.")

# Step 2: Selectbox for months
months = ["January", "February", "March", "April"]
selected_month = st.selectbox("Select a month:", months)

# Step 3: Static dictionary of monthly sales
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

# Step 4: Display selected month’s sales
st.metric(label=f"Sales in {selected_month}", value=sales[selected_month])

# Step 5: Display bar chart of all sales
st.bar_chart(list(sales.values()))
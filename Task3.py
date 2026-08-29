# Task 3 – Product Form

import streamlit as st

st.title("Product Form")

# Step 1: Sidebar inputs
product_name = st.sidebar.text_input("Product Name")
category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Books", "Accessories"])
price = st.sidebar.number_input("Price", min_value=0.0)

# Step 2: Button to add product
if st.sidebar.button("Add Product"):
    st.success("Prooduct added succeddfully!")
    st.write(f"Product: {product_name}")
    st.write(f"Category: {category}")
    st.write(f"Price:", {price})
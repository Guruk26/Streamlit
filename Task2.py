# Task 2 – Price Calculator

import streamlit as st

st.title("Price Calculator")

# Step 1: Input product price
price = st.number_input("Enter product price:", min_value=0.0)

# Step 2: Slider for discount percentage
discount = st.slider("Select discount percentage:", 0, 50, 10)

# Step 3: Button to calculate
if st.button("Calculate Final Price"):
    final_price = price - (price * discount / 100)
    st.success(f"Final Price after {discount}% discount: {final_price}")

    # Extra: Show comparison table
    comparison = [["Before Discount", price], ['After Discount', final_price]]
    st.table(comparison)
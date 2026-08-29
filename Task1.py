# 📝 Task 1 – Basic Streamlit App (app_basic.py)

import streamlit as st

# Step 1: Display a title
st.title("Welcome to streamlit!")

# Step 2: Text input for user name
name = st.text_input("Enter your name:")

# Step 3: Button to trigger greeting
if st.button("Greet Me"):
    st.write(f"Hello, {name}")
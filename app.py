#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# App title
st.set_page_config(page_title="Calculation App", page_icon="🧮", layout="centered")
st.title("🧮 Handy Calculation App")

st.write("Enter the values below to get the final calculated result:")

# Input fields
a = st.number_input("Enter A", value=0.0)
b = st.number_input("Enter B", value=0.0)
c = st.number_input("Enter C", value=0.0)
d = st.number_input("Enter D", value=0.0)

# Perform calculation when button is clicked
if st.button("🔢 Calculate"):
    result = (a + b) * (c - d)  # 👉 Replace this with your own formula
    st.success(f"✅ Final Result: **{result:.2f}**")


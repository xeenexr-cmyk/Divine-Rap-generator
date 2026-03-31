import streamlit as st

st.set_page_config(page_title="Test App", layout="centered")

st.title("✅ App Working Test")

name = st.text_input("Enter anything")

if st.button("Submit"):
    st.success(f"App is working 🎉 → {name}")

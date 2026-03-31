import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Lyrics", layout="centered")

# API KEY
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🎤 AI Lyrics Generator")

topic = st.text_input("Enter Topic")

if st.button("Generate"):
    if topic:
        try:
            model = genai.GenerativeModel("gemini-pro")

            response = model.generate_content(
                f"Write a powerful Hindi rap song on {topic}"
            )

            st.write(response.text)

        except Exception as e:
            st.error(e)
    else:
        st.warning("Enter topic")

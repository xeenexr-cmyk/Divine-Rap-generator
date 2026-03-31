import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Lyrics", layout="centered")

# API KEY
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🎤 AI Lyrics Generator (Working 🔥)")

topic = st.text_input("Enter Topic")

if st.button("Generate Lyrics"):

    if topic:
        try:
            model = genai.GenerativeModel("gemini-pro")

            prompt = f"""
            Write a Hindi rap song on topic: {topic}

            - Good rhyming
            - No repetition
            - Emotional + powerful
            """

            response = model.generate_content(prompt)

            st.success("✅ Lyrics Generated")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Enter topic first")

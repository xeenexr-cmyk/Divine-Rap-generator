import streamlit as st
import google.generativeai as genai

# CONFIG
st.set_page_config(page_title="AI Lyrics Pro", layout="centered")

# API KEY
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ✅ SAFE MODEL
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🎤 Bollywood Level AI Lyrics Generator 🔥")

topic = st.text_input("Enter Topic")
style = st.selectbox("Style", ["Rap", "Bollywood", "Devotional"])
mood = st.selectbox("Mood", ["Aggressive", "Emotional", "Powerful"])
keywords = st.text_input("Keywords (optional)")

if st.button("Generate Lyrics"):

    if topic:
        prompt = f"""
        Write a HIGH QUALITY Hindi {style} song.

        Topic: {topic}
        Mood: {mood}
        Keywords: {keywords}

        Requirements:
        - Bollywood level quality
        - Strong rhyming
        - NO repetition
        - Emotional + powerful
        - Proper structure

        Structure:
        Title
        Verse 1
        Hook
        Verse 2
        Hook
        Outro
        """

        try:
            res = model.generate_content(prompt)
            st.success("✅ Lyrics Generated")
            st.write(res.text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Enter topic first")

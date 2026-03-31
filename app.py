import streamlit as st
import google.generativeai as genai

# CONFIG
st.set_page_config(page_title="AI Lyrics Pro", layout="centered")

# API KEY
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# TITLE
st.title("🎤 Bollywood Level AI Lyrics Generator 🔥")

# INPUTS
topic = st.text_input("Enter Topic (e.g. Shiv Tandav, Lanka Dahan)")
style = st.selectbox("Select Style", ["Rap", "Bollywood", "Devotional"])
mood = st.selectbox("Select Mood", ["Aggressive", "Emotional", "Powerful"])
keywords = st.text_input("Enter Keywords (optional)")

# BUTTON
if st.button("Generate Lyrics"):

    if topic:
        with st.spinner("🔥 Creating masterpiece lyrics..."):

            prompt = f"""
            Write a HIGH QUALITY Hindi {style} song.

            Topic: {topic}
            Mood: {mood}
            Keywords: {keywords}

            Strict Requirements:
            - Must feel like real Bollywood / professional rap
            - Strong rhyming (तुकबंदी)
            - NO repetition of lines
            - Deep storytelling
            - Natural Hinglish/Hindi mix
            - Each verse should be DIFFERENT

            Structure:
            🎤 Title

            🎶 Verse 1 (4-6 lines)
            🎧 Hook (2 lines catchy)

            🎶 Verse 2 (4-6 lines)
            🎧 Hook (2 lines)

            ✨ Outro (2-3 lines powerful ending)

            Make it emotional + cinematic + powerful.
            """

            try:
                # ✅ SAFE MODEL (no error)
                model = genai.GenerativeModel("gemini-1.5-flash-8b")
                response = model.generate_content(prompt)

                st.success("✅ Lyrics Generated!")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("⚠️ Please enter a topic")

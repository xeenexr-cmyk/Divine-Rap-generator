import streamlit as st
from groq import Groq

# Page setup
st.set_page_config(page_title="Bollywood AI Lyrics", layout="centered")

st.title("🔥 Bollywood Level AI Lyrics Generator 🎤")

# Inputs
topic = st.text_input("Enter Topic (e.g. Shiv Tandav, Lanka Dahan)")
style = st.selectbox("Select Style", ["Rap", "Bollywood", "Devotional Rap"])
mood = st.selectbox("Select Mood", ["Aggressive", "Emotional", "Powerful", "Peaceful"])

# Button
if st.button("Generate Lyrics"):

    if topic:
        try:
            # Groq client
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])

            # Strong Prompt
            prompt = f"""
            Write a HIGH QUALITY Hindi {style} song.

            Topic: {topic}
            Mood: {mood}

            Requirements:
            - Full Bollywood cinematic lyrics
            - Deep emotional storytelling
            - Strong rhyming like real songs
            - NO repetition
            - Proper structure:
              Intro
              Verse 1
              Hook
              Verse 2
              Hook
              Outro
            - Use poetic Hindi + modern rap fusion

            Make it sound like a viral song.
            """

            # API call (LATEST MODEL)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            output = response.choices[0].message.content

            st.success("✅ Lyrics Generated Successfully!")
            st.write(output)

        except Exception as e:
            st.error(f"❌ Error: {e}")

    else:
        st.warning("⚠️ Please enter a topic first")

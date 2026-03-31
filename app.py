import streamlit as st
from groq import Groq

st.set_page_config(page_title="Bollywood AI Lyrics", layout="centered")

st.title("🔥 Bollywood Level AI Lyrics Generator 🎤")

topic = st.text_input("Enter Topic (e.g. Shiv Tandav, Lanka Dahan)")
style = st.selectbox("Select Style", ["Rap", "Bollywood", "Devotional Rap"])
mood = st.selectbox("Select Mood", ["Aggressive", "Emotional", "Powerful", "Peaceful"])

if st.button("Generate Lyrics"):

    if topic:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])

            prompt = f"""
            Write a HIGH QUALITY Hindi {style} song.

            Topic: {topic}
            Mood: {mood}

            Requirements:
            - Full Bollywood level lyrics
            - Proper structure: Intro, Verse 1, Hook, Verse 2, Hook, Outro
            - Deep meaning, storytelling
            - Strong rhyming (like real songs)
            - NO repetition
            - Pure Hindi + Hinglish mix

            Make it emotional and impactful like a real viral song.
            """

            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}]
            )

            output = response.choices[0].message.content

            st.success("✅ Lyrics Generated")
            st.write(output)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Enter topic first")

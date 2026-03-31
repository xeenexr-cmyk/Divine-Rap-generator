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
            # API client
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])

            # 🔥 PRO LEVEL PROMPT
            prompt = f"""
            तुम एक professional Bollywood lyricist हो।

            Topic: {topic}
            Style: {style}
            Mood: {mood}

            Instructions:
            - Pure Hindi + Hinglish mix
            - Emotional, cinematic, powerful lyrics
            - Strong rhyming + smooth rap flow
            - No repetition
            - No music description (like Music: ...)

            Structure:
            🎤 Intro (2-3 lines, impactful)
            🎶 Verse 1 (deep storytelling, 4-6 lines)
            🔥 Hook (catchy, viral, repeatable)
            🎶 Verse 2 (more powerful than verse 1)
            🔥 Hook
            ✨ Outro (short emotional ending)

            Extra:
            - Use metaphors, divine imagery
            - Add punchlines and goosebumps feeling

            Make it feel like a viral YouTube devotional rap song.
            """

            # API call
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

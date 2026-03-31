import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Lyrics Pro", layout="centered")

st.title("🔥 Bollywood Level AI Lyrics Generator 🎤")

topic = st.text_input("Enter Topic (e.g. Shiv Tandav, Lanka Dahan)")
style = st.selectbox("Select Style", ["Rap", "Bollywood", "Devotional Rap"])
mood = st.selectbox("Select Mood", ["Aggressive", "Emotional", "Powerful", "Peaceful"])

if st.button("Generate Lyrics"):

    if topic:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])

            # 🔥 MASTER PROMPT (ChatGPT Level)
            prompt = f"""
You are a TOP Bollywood lyricist + Rap writer.

Write a HIGH QUALITY Hindi {style} song.

Topic: {topic}
Mood: {mood}

STRICT RULES:
- No explanation, ONLY lyrics
- No repetition
- No boring lines
- No music description
- Every line should feel powerful and meaningful

STYLE:
- Use Hindi + Hinglish mix
- Use internal rhymes (rap style)
- Add punchlines
- Add cinematic feel

STRUCTURE:

[Intro]
(2 impactful lines)

[Verse 1]
(4-6 lines, storytelling, deep imagery)

[Hook]
(2-3 lines, VERY catchy, viral level)

[Verse 2]
(4-6 lines, more powerful than verse 1)

[Hook]
(repeat but stronger)

[Outro]
(2 emotional lines)

IMPORTANT:
- Hook should feel like a viral reel
- Lines should feel like real song, not AI
- Add divine + powerful imagery

Make it goosebumps level 🔥
"""

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=1.2  # 🔥 creativity boost
            )

            output = response.choices[0].message.content

            st.success("✅ Lyrics Generated Successfully!")

            # Better formatting
            st.markdown(f"```\n{output}\n```")

        except Exception as e:
            st.error(f"❌ Error: {e}")

    else:
        st.warning("⚠️ Enter topic first")

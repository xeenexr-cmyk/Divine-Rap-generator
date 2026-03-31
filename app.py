import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="🔥 Bhakti Rap AI Studio", layout="centered")

st.title("🔥 Bhakti + Rap AI Studio 🎤")

# Inputs
topic = st.text_input("🎯 विषय", placeholder="Ram Bal Kand, Radha Krishna Prem, Meera Bhajan")
mode = st.selectbox("🎭 Mode Select", [
    "Hardcore Rap",
    "Devotional Rap",
    "Emotional Bhakti",
    "Story Rap (Ramayan Style)",
    "Bollywood Bhakti"
])
mood = st.selectbox("🔥 Mood", ["Aggressive", "Emotional", "Peaceful", "Spiritual", "Sad"])
keywords = st.text_input("🧠 Keywords", placeholder="राम, कृष्ण, प्रेम, विरह")

# Prompt Builder
def get_prompt():
    
    if mode == "Hardcore Rap":
        return f"""
Divine + Raftaar style hardcore rap.

Topic: {topic}
Mood: {mood}
Keywords: {keywords}

Aggressive rap with punchlines, rhymes, attitude.
"""

    elif mode == "Devotional Rap":
        return f"""
Bhakti rap likho (Hindi me).

Topic: {topic}
Mood: {mood}

Feel:
- Mahadev / Ram bhakti
- Devotion + power
- Rap flow + mantra feel

Structure:
Intro, Verse, Hook, Verse, Hook, Outro
"""

    elif mode == "Emotional Bhakti":
        return f"""
Radha Krishna / Meera style emotional bhakti rap.

Topic: {topic}

Feel:
- Prem, virah, dard
- Dil se likha hua lage
- Poetry + rap mix

Soft, deep, emotional Hindi lyrics.
"""

    elif mode == "Story Rap (Ramayan Style)":
        return f"""
Ramayan story rap likho (Bal Kand style).

Topic: {topic}

- Kahani format
- Doha/chaupai feel + rap flow
- Narrative storytelling

Scene-wise progression ho.
"""

    elif mode == "Bollywood Bhakti":
        return f"""
Modern Bollywood devotional rap likho.

Topic: {topic}

- Arijit Singh + Divine fusion
- Emotional + cinematic
- Easy words + catchy hook

Song viral hona chahiye.
"""

# Generate
if st.button("🚀 Generate Song"):

    with st.spinner("⚡ Creating masterpiece..."):

        prompt = get_prompt()

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=1.5,
                max_tokens=1200
            )

            lyrics = response.choices[0].message.content

            st.success("✅ Song Generated!")

            st.markdown("## 🎤 Lyrics:")
            st.code(lyrics)

        except Exception as e:
            st.error(f"❌ Error: {e}")

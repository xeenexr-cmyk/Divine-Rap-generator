import streamlit as st
from groq import Groq

# API
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI CONFIG
st.set_page_config(page_title="DivineRapTv Ultimate Engine", layout="wide", page_icon="🔱")

# STYLE
st.markdown("""
<style>
.stApp { background: #000; color: #fff; }
.stButton>button {
    background: linear-gradient(90deg,#ff0000,#ff7300);
    color: white; font-weight: bold;
    height: 3.5rem; border-radius: 10px;
}
.stTextArea textarea {
    background:#0a0a0a !important;
    color:#00ffcc !important;
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

st.title("🔱 DivineRapTv - FINAL RAP ENGINE 🔥")
st.write("Hardcore + Emotion + Bhakti + Suno Ready = Viral Song 🚀")

col1, col2 = st.columns([1,1.5])

# INPUT
with col1:
    topic = st.text_input("🎯 Topic", placeholder="जैसे: लंका दहन, राधा कृष्ण विरह, शिव तांडव")

    mode = st.selectbox("🎭 Style", [
        "Hardcore 🔥",
        "Bhakti Emotional 🙏",
        "Storytelling 📖",
        "Suno AI Song 🎧"
    ])

    generate = st.button("🚀 Generate PERFECT Song")

# MASTER PROMPT
def build_master_prompt(topic, mode):
    return f"""
तुम भारत के Top Divine Rap Hitmaker + Suno AI Expert हो।

🎯 TOPIC: {topic}
🎭 STYLE: {mode}

❗ FINAL RULES (STRICT):

1. **BALANCE**
   Hardcore + Emotion + Bhakti
   (सिर्फ aggression नहीं, feeling भी हो)

2. **LANGUAGE**
   - शुद्ध हिंदी
   - कोई गलती नहीं

3. **FLOW**
   - हर लाइन 4–7 शब्द
   - natural rap flow (robotic नहीं)

4. **RHYME**
   - हर 2 लाइन rhyme match (AA BB)
   - सुनने में musical लगे

5. **HOOK (MOST IMPORTANT 🔥)**
   - 3–4 लाइन
   - repeatable + catchy
   - reels में loop हो सके

6. **AD-LIBS (LIMITED)**
   - कभी-कभी: (हर हर!), (जय श्रीराम!)

7. **STRUCTURE**

[Intro]
(3 lines cinematic)

[Verse 1]
(10-12 lines)

[Hook] 🔥
(3-4 lines)

[Verse 2]
(10-12 lines, deeper emotion)

[Hook]

[Outro]
(2-3 lines)

8. **STYLE GUIDE**

Hardcore:
काल, अग्नि, विनाश, प्रलय

Bhakti:
समर्पण, भक्ति, आत्मा

Story:
दृश्य बदलते रहें

Suno:
smooth flow + melody friendly

---

🔥 OUTPUT: सिर्फ lyrics
"""

# GENERATE
def generate_song(topic, mode):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "तुम legendary divine rap writer हो। perfect lyrics लिखते हो।"},
                {"role": "user", "content": build_master_prompt(topic, mode)}
            ],
            temperature=0.9,
            max_tokens=1800
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# OUTPUT
if generate:
    if not topic:
        st.error("Topic डालो पहले")
    else:
        with st.spinner("🔥 Creating Divine Masterpiece..."):
            lyrics = generate_song(topic, mode)

            with col2:
                st.success("✅ PERFECT SONG READY 🚀")
                st.text_area("🎤 Lyrics", lyrics, height=600)

                st.download_button(
                    "📥 Download",
                    lyrics,
                    file_name=f"{topic}.txt"
                )

                st.info("💡 Suno AI / Udio में डालो → Full song ready!")

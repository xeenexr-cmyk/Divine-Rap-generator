import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
st.set_page_config(page_title="🔱 DivineRapTv Ultimate Studio", layout="wide")

# Custom UI
st.markdown("""
<style>
.stApp { background-color: #000; color: #fff; }
.stButton>button {
    background: linear-gradient(90deg, #ff0000, #ff7300);
    color: white;
    font-weight: bold;
    border: none;
    height: 3.5rem;
    width: 100%;
    border-radius: 10px;
    font-size: 1.2rem;
}
.stTextArea textarea {
    color: #00ffcc !important;
    background-color: #111 !important;
    font-family: monospace;
    font-size: 1.1rem !important;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🔱 DivineRapTv: Ultimate Bhakti Rap Studio")
st.write("🔥 Hardcore + Emotion + Devotion = Viral Rap Generator")

# Layout
col1, col2 = st.columns([1, 1.5])

# Inputs
with col1:
    topic = st.text_input("🎯 विषय (Topic)", placeholder="जैसे: लंका दहन, राधा कृष्ण विरह, मीरा का प्रेम")

    mode = st.selectbox("🎭 Style Select करें", [
        "Hardcore Rap 🔥",
        "Ramayan Story 📖",
        "Radha Krishna Prem 💙",
        "Meera Bhakti 🕊️",
        "Bollywood Bhakti 🎬"
    ])

    generate_btn = st.button("🚀 Generate Viral Song")

# Prompt Builder (FINAL GOD LEVEL)
def build_prompt(topic, mode):
    return f"""
तुम भारत के सबसे बड़े Bollywood lyricist + Divine Rap Hitmaker हो।

🎯 TOPIC: {topic}
🎭 STYLE: {mode}

तुम्हारा काम:
ऐसा गीत लिखो जो सुनते ही रोंगटे खड़े कर दे और repeat पर चल जाए।

❗ RULES:
- केवल शुद्ध हिन्दी
- हर लाइन 4-6 शब्द
- हर 2 लाइन rhyme match
- कोई भी लाइन boring नहीं
- हर 3 लाइन में punchline

🔥 STYLE CONTROL:

Hardcore Rap:
काल, अग्नि, प्रलय, विनाश

Ramayan Story:
सीन बदलते रहो (movie feel)

Radha Krishna:
विरह, आँसू, बांसुरी, रात

Meera Bhakti:
समर्पण, दर्द, प्रेम

Bollywood Bhakti:
cinematic + emotional flow

🔥 HOOK RULE:
- 3-4 लाइन max
- सबसे catchy
- reels friendly

📌 STRUCTURE:

[Intro]

[Verse 1] (16 bars)

[Hook] 🔥

[Verse 2] (16 bars)

[Hook]

[Outro]

अब शुरू करो:
"""

# Generate
if generate_btn:
    if not topic:
        st.error("⚠️ पहले topic डालो भाई!")
    else:
        with st.spinner("🔥 Divine lyrics बन रहे हैं..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक legendary divine rap lyricist हो।"},
                        {"role": "user", "content": build_prompt(topic, mode)}
                    ],
                    temperature=1.0,
                    max_tokens=2000
                )

                lyrics = response.choices[0].message.content

                with col2:
                    st.success("✅ Song Generated Successfully!")
                    st.markdown("### 🎤 DivineRapTv Official Lyrics")
                    st.text_area("", lyrics, height=750)

                    st.info("💡 Tip: इसे Suno AI / Udio में डालो और full song बनाओ!")

            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.caption("© DivineRapTv | Ultimate AI Bhakti Rap Studio 🚀")

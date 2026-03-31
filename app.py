import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="🔱 DivineRapTv Ultimate Studio", layout="wide")

# UI
st.markdown("""
<style>
.stApp { background-color: #000; color: #fff; }
.stButton>button {
    background: linear-gradient(90deg, #ff0000, #ff7300);
    color: white; font-weight: bold; border: none;
    height: 3.5rem; width: 100%;
    border-radius: 10px; font-size: 1.2rem;
}
.stTextArea textarea {
    color: #00ffcc !important;
    background-color: #111 !important;
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

st.title("🔱 DivineRapTv: Ultimate Bhakti Rap Studio")
st.write("🔥 Hardcore + Emotion + Devotion = VIRAL RAP 🔥")

col1, col2 = st.columns([1, 1.5])

with col1:
    topic = st.text_input("🎯 विषय (Topic)")
    
    mode = st.selectbox("🎭 Style", [
        "Hardcore Rap 🔥",
        "Ramayan Story 📖",
        "Radha Krishna Prem 💙",
        "Meera Bhakti 🕊️",
        "Bollywood Bhakti 🎬",
        "Shiv Tandav Style 🌙",
        "Hanuman Power 🚩"
    ])
    
    intensity = st.selectbox("💥 Intensity", [
        "Emotional 😢",
        "Balanced ⚖️",
        "Hardcore 🔥",
        "Viral Level 🚀"
    ])
    
    generate = st.button("🚀 Generate Viral Song")

# 🔥 FINAL GOD PROMPT
def build_prompt(topic, mode, intensity):

    return f"""
तुम भारत के सबसे बड़े Bollywood lyricist + Divine Rap Hitmaker हो।

🎯 TOPIC: {topic}
🎭 STYLE: {mode}
💥 INTENSITY: {intensity}

तुम्हारा काम:
ऐसा rap लिखो जो सुनते ही दिमाग में चिपक जाए (viral level)

❗ STRICT RULES:

1. ❌ “है / हूँ / था” शब्द लाइन के अंत में नहीं आएंगे  
2. ❌ कोई भी लाइन simple description नहीं होगी  
3. ❌ कोई repetition नहीं  
4. हर लाइन = punchline  
5. हर 2 लाइन rhyme match  

🔥 CINEMATIC WRITING:

❌ मत लिखो:
लंका जल रही है  

✅ ऐसे लिखो:
लंका में ज्वाला, मृत्यु का ताला  

---

🔥 EMOTION ENGINE:

Hardcore → काल, प्रलय, विनाश  
Ramayan → story flow (scene change)  
Radha → विरह, आँसू, रात  
Meera → समर्पण, दर्द  
Shiv → तांडव, भस्म, महाकाल  
Hanuman → शक्ति, गर्जना, लंका दहन  

---

🔥 VIRAL HOOK RULE:

- 3-4 लाइन  
- सबसे catchy  
- reels friendly  
- repeat value  

---

📌 STRUCTURE:

[Intro] (3-4 lines)

[Verse 1] (16 bars)

[Hook] 🔥

[Verse 2] (16 bars, different angle)

[Hook]

[Outro]

---

🔥 FINAL TARGET:

गीत ऐसा लगे:
👉 Bollywood + Divine + Hardcore fusion  
👉 हर 3 लाइन में goosebumps  

अब शुरू करो:
"""

# Generate
if generate:
    if not topic:
        st.error("Topic डालो भाई 🔥")
    else:
        with st.spinner("🔥 Viral lyrics बन रहे हैं..."):
            try:
                res = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम top divine rap hitmaker हो। तुम्हारे lyrics viral और cinematic होते हैं।"},
                        {"role": "user", "content": build_prompt(topic, mode, intensity)}
                    ],
                    temperature=0.95,
                    top_p=0.95,
                    max_tokens=2000
                )

                lyrics = res.choices[0].message.content

                with col2:
                    st.success("✅ Viral Song Ready!")
                    st.text_area("🎤 Lyrics", lyrics, height=750)

                    st.download_button(
                        "📥 Download",
                        lyrics,
                        file_name="divine_rap.txt"
                    )

                    st.info("💡 Suno AI / Udio में डालो → full song बनाओ")

            except Exception as e:
                st.error(e)

st.divider()
st.caption("🔥 DivineRapTv Ultimate System 🔥")

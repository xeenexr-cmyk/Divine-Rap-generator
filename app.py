import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="🔱 DivineRapTv Master Studio", layout="wide")

# UI
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
}
</style>
""", unsafe_allow_html=True)

st.title("🔱 DivineRapTv: MASTER RAP ENGINE 🔥")
st.write("🚀 VIRAL + BHAKTI + HARDCORE = HIT SONG")

col1, col2 = st.columns([1, 1.5])

with col1:
    topic = st.text_input("🎯 Topic")
    
    mode = st.selectbox("🎭 Style", [
        "Hardcore 🔥",
        "Ramayan Story 📖",
        "Radha Krishna 💙",
        "Meera Bhakti 🕊️",
        "Shiv Tandav 🌙",
        "Hanuman Power 🚩"
    ])
    
    intensity = st.selectbox("💥 Intensity", [
        "Emotional 😢",
        "Balanced ⚖️",
        "Hardcore 🔥",
        "Viral 🚀"
    ])
    
    generate = st.button("🚀 Generate MASTER SONG")

# 🔥 FINAL MASTER PROMPT
def build_master_prompt(topic, mode, intensity):

    return f"""
तुम भारत के सबसे बड़े Divine Rap Hitmaker हो।

🎯 TOPIC: {topic}
🎭 STYLE: {mode}
💥 INTENSITY: {intensity}

🎯 GOAL:
ऐसा rap लिखो जो सुनते ही viral हो जाए और repeat पर चले।

---

❗ STRICT RULES:

1. ❌ "है / हूँ / था" शब्द लाइन के अंत में नहीं आएंगे  
2. ❌ कोई भी लाइन description नहीं होगी  
3. ❌ कोई repetition नहीं  
4. हर line = punchline  
5. हर 2 line rhyme match  

---

🔥 WRITING STYLE:

- cinematic visuals
- attack mode writing
- powerful vocabulary

❌ मत लिखो:
"लंका जल रही है"

✅ ऐसे लिखो:
"लंका में ज्वाला, मृत्यु का ताला"

---

🔥 EMOTION + POWER:

- हर verse में energy बढ़ती जाए  
- भक्ति + क्रोध + भावना mix करो  
- listener को feel होना चाहिए  

---

🔥 MIC DROP RULE:

- हर verse में कम से कम 4 lines ऐसी हों  
जो सुनते ही goosebumps दे  

---

🔥 VIRAL HOOK RULE:

- 3-4 line max  
- chant style  
- repeatable  
- reel ready  

---

📌 STRUCTURE:

[Intro]

[Verse 1] (16 bars)

[Hook] 🔥

[Verse 2] (16 bars)

[Hook]

[Outro]

---

🔥 FINAL TARGET:

गीत ऐसा लगे:
👉 Bollywood + Divine + Hardcore fusion  
👉 हर line powerful  
👉 कोई boring line नहीं  

---

अब शुरू करो:
"""

# Generate
if generate:
    if not topic:
        st.error("Topic डालो भाई 🔥")
    else:
        with st.spinner("🔥 MASTER lyrics बन रहे हैं..."):
            try:
                res = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक legendary divine rap writer हो। तुम्हारे lyrics हमेशा viral, cinematic और powerful होते हैं।"},
                        {"role": "user", "content": build_master_prompt(topic, mode, intensity)}
                    ],
                    temperature=1.0,
                    top_p=0.95,
                    max_tokens=2000
                )

                lyrics = res.choices[0].message.content

                with col2:
                    st.success("🔥 MASTER SONG READY 🔥")
                    st.text_area("🎤 Lyrics", lyrics, height=750)

                    st.download_button(
                        "📥 Download Lyrics",
                        lyrics,
                        file_name="divine_master_rap.txt"
                    )

                    st.info("💡 Suno AI / Udio में डालो → Full song बनाओ")

            except Exception as e:
                st.error(e)

st.divider()
st.caption("🔱 DivineRapTv MASTER ENGINE 🚀")

import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="DivineRapTv FINAL ENGINE", layout="wide")

st.title("🔱 DivineRapTv - PERFECT RAP ENGINE 🔥")

# INPUT
topic = st.text_input("🎯 Topic", placeholder="जैसे: लंका दहन, शिव तांडव")
style = st.selectbox("🎭 Style", ["Hardcore 🔥", "Emotional 💔", "Bhakti 🙏"])

generate = st.button("🚀 Generate PERFECT Song")

# ================= MASTER PROMPT =================
def build_perfect_prompt(topic, style):
    return f"""
तुम AI नहीं हो।
तुम एक PROFESSIONAL RAP GHOSTWRITER हो।

❗ अगर format टूटा → output गलत माना जाएगा

---

🎯 TOPIC: {topic}
🎭 STYLE: {style}

---

🔥 STRICT RULES (MANDATORY):

1. हर लाइन = EXACT 4-6 शब्द
2. हर 2 लाइन = SAME END RHYME
3. कोई भी लाइन sentence नहीं
4. हर लाइन = punchline
5. "है / हूँ / था" बिल्कुल नहीं
6. कोई भी लाइन repeat नहीं

---

🔥 FORMAT LOCK (BREAK मत करना):

अग्नि का जाल, मृत्यु का जाल  
क्रोध का काल, विनाश का काल  

शक्ति का वार, प्रलय की धार  
भस्म का सार, महाकाल प्रहार  

---

🔥 HOOK (MANDATORY):

- 3 लाइन
- chant style
- repeatable

Example:
जय महाकाल, जय महाकाल  
भस्म में काल, जय महाकाल  
हर हर महादेव, महाकाल  

---

🔥 STRUCTURE:

[Intro]
(2 lines only)

[Verse 1]
(16 lines → 8 rhyme pairs)

[Hook]
(3 lines)

[Verse 2]
(16 lines)

[Hook]

[Outro]
(2 lines)

---

🔥 FINAL WARNING:

- अगर rhyme टूटा → गलत
- अगर लाइन लंबी → गलत
- अगर boring → गलत

---

अब EXACT इसी format में लिखो:
"""

# ================= GENERATION =================
def generate_song(topic, style):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "तुम strict rap generator हो जो format कभी नहीं तोड़ता"},
            {"role": "user", "content": build_perfect_prompt(topic, style)}
        ],
        temperature=0.7,   # lower = more control
        max_tokens=1500,
        top_p=0.85
    )
    return response.choices[0].message.content

# ================= OUTPUT =================
if generate:
    if not topic:
        st.error("⚠️ Topic डालो")
    else:
        with st.spinner("🔥 PERFECT lyrics बन रहे हैं..."):
            lyrics = generate_song(topic, style)

            st.success("✅ PERFECT SONG READY 🔥")
            st.text_area("🎤 Lyrics", lyrics, height=600)

            st.download_button(
                "📥 Download Lyrics",
                lyrics,
                file_name="perfect_rap.txt"
            )

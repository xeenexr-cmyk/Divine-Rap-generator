import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="DivineRapTv Ultimate Studio", layout="wide")

st.title("🔱 DivineRapTv - Ultimate Bhakti Rap Engine 🔥")

# INPUT
topic = st.text_input("🎯 Topic", placeholder="जैसे: लंका दहन, राधा कृष्ण विरह")
style = st.selectbox("🎭 Style", [
    "Hardcore 🔥",
    "Emotional 💔",
    "Bhakti 🙏",
    "Storytelling 📖"
])
generate = st.button("🚀 Generate MASTER Song")

# ================= PROMPT =================
def build_prompt(topic, style):
    return f"""
तुम भारत के सबसे खतरनाक Divine Rap Writer हो।

अगर output weak हुआ → reject

🎯 TOPIC: {topic}
🎭 STYLE: {style}

❗ RULES:

1. हर लाइन = 4-6 शब्द ONLY  
2. हर 2 लाइन = SAME RHYME  
3. कोई भी लाइन description नहीं  
4. हर लाइन punchline  
5. अंत में "है / हूँ / था" नहीं  

🔥 FORMAT:

अग्नि का जाल, मृत्यु का जाल  
क्रोध का काल, विनाश का काल  

🔥 HOOK:
- 3 लाइन
- chant style

🔥 STRUCTURE:

[Intro] (2 lines)
[Verse 1] (16 lines)
[Hook] (3 lines)
[Verse 2] (16 lines)
[Hook]
[Outro] (2 lines)

अब लिखो:
"""

# ================= REFINE =================
def refine_lyrics(raw):
    return f"""
इन lyrics को upgrade करो:

{raw}

RULE:
- rhyme perfect करो
- weak lines हटाओ
- punchlines बढ़ाओ
- hook viral बनाओ

Final lyrics दो:
"""

# ================= GENERATE =================
def generate_song(topic, style):
    # Step 1: Raw generation
    raw = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "तुम एक hardcore divine rap writer हो"},
            {"role": "user", "content": build_prompt(topic, style)}
        ],
        temperature=0.8,
        max_tokens=1500
    ).choices[0].message.content

    # Step 2: Refinement (IMPORTANT)
    final = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "तुम lyrics को perfect viral बनाते हो"},
            {"role": "user", "content": refine_lyrics(raw)}
        ],
        temperature=0.7,
        max_tokens=1500
    ).choices[0].message.content

    return final

# ================= OUTPUT =================
if generate:
    if not topic:
        st.error("⚠️ Topic डालो पहले")
    else:
        with st.spinner("🔥 MASTER lyrics बन रहे हैं..."):
            lyrics = generate_song(topic, style)

            st.success("✅ MASTER SONG READY 🔥")
            st.text_area("🎤 Lyrics", lyrics, height=600)

            st.download_button(
                "📥 Download Lyrics",
                lyrics,
                file_name="divine_rap.txt"
            )

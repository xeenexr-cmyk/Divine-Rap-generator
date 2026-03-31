import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="DivineRapTv 10/10 Engine", layout="wide")

st.title("🔱 DivineRapTv - ULTIMATE 10/10 RAP ENGINE 🔥")

# INPUT
topic = st.text_input("🎯 Topic", placeholder="जैसे: लंका दहन, शिव तांडव")
style = st.selectbox("🎭 Style", ["Hardcore 🔥", "Emotional 💔", "Bhakti 🙏"])

generate = st.button("🚀 Generate 10/10 Song")

# ================= STEP 1 =================
def build_prompt(topic, style):
    return f"""
तुम भारत के सबसे खतरनाक Divine Rap Ghostwriter हो।

🎯 TOPIC: {topic}
🎭 STYLE: {style}

❗ RULES:

- हर लाइन = 4-6 शब्द
- हर 2 लाइन = SAME RHYME
- कोई भी line boring नहीं
- कोई भी line repeat नहीं
- "है/हूँ/था" नहीं

FORMAT:

अग्नि का जाल, मृत्यु का जाल  
क्रोध का काल, विनाश का काल  

STRUCTURE:

[Intro] (2 lines)
[Verse 1] (16 lines)
[Hook] (3 lines)
[Verse 2] (16 lines)
[Hook]
[Outro] (2 lines)

अब लिखो:
"""

# ================= STEP 2 =================
def refine_prompt(raw):
    return f"""
इन lyrics को सुधारो:

{raw}

RULE:
- rhyme perfect करो
- lines short रखो
- punchlines बढ़ाओ
- weak lines हटाओ

Final improved lyrics:
"""

# ================= STEP 3 =================
def validate_prompt(refined):
    return f"""
इन lyrics को FINAL CHECK करो:

{refined}

❗ CHECK:

- कोई repetition नहीं
- हर line strong हो
- hook viral हो

HOOK FIX:
Hook को chant + powerful बनाओ

FINAL VERSION दो:
"""

# ================= GENERATION =================
def generate_song(topic, style):
    # Step 1
    raw = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "तुम raw rap writer हो"},
            {"role": "user", "content": build_prompt(topic, style)}
        ],
        temperature=0.8,
        max_tokens=1200
    ).choices[0].message.content

    # Step 2
    refined = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "तुम lyrics improver हो"},
            {"role": "user", "content": refine_prompt(raw)}
        ],
        temperature=0.7,
        max_tokens=1200
    ).choices[0].message.content

    # Step 3 (FINAL MAGIC)
    final = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "तुम viral rap doctor हो"},
            {"role": "user", "content": validate_prompt(refined)}
        ],
        temperature=0.6,
        max_tokens=1200
    ).choices[0].message.content

    return final

# ================= OUTPUT =================
if generate:
    if not topic:
        st.error("⚠️ Topic डालो पहले")
    else:
        with st.spinner("🔥 10/10 MASTERPIECE बन रहा है..."):
            lyrics = generate_song(topic, style)

            st.success("✅ 10/10 SONG READY 🔥")
            st.text_area("🎤 Final Lyrics", lyrics, height=600)

            st.download_button(
                "📥 Download",
                lyrics,
                file_name="ultimate_rap.txt"
            )

import streamlit as st
from groq import Groq
import time

# API
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="DivineRapTv - FINAL ENGINE", layout="wide")

# ================= UI =================
st.title("🔱 DivineRapTv - FINAL RAP ENGINE 🔥")
st.caption("🔥 Hardcore + Flow + Bhakti = VIRAL RAP")

col1, col2 = st.columns([1, 1.5])

# ================= INPUT =================
with col1:
    topic = st.text_input("🎯 Topic", placeholder="Mahakal Tandav, Hanuman Lanka Dahan")
    
    style = st.selectbox("🎭 Style", [
        "Hardcore 🔥",
        "Storytelling 📖",
        "Emotional 💙"
    ])
    
    mood = st.select_slider(
        "💥 Intensity",
        options=["Balanced", "Hardcore", "Viral"]
    )
    
    generate = st.button("🚀 Generate PERFECT Song")

# ================= PROMPT =================
def build_prompt(topic, style, mood):
    return f"""
तुम भारत के TOP Divine Rap Lyricist हो।

🎯 TOPIC: {topic}
🎭 STYLE: {style}
💥 MOOD: {mood}

🔥 CRITICAL RULES:

1. भाषा:
- शुद्ध हिंदी
- कोई typo नहीं
- आसान लेकिन powerful शब्द

2. FLOW:
- हर लाइन natural rap flow में हो
- जब बोलो तो smooth लगे

3. LINE LENGTH:
- 3-7 शब्द (flexible, forced नहीं)

4. RHYME:
- हर 2 लाइन rhyme match (AA BB)

5. REPETITION:
- same words बार-बार repeat मत करो

6. PUNCHLINE:
- हर 3 लाइन में strong punchline
- visual + powerful

Example:
"त्रिशूल उठा! समय भी थमा!"

7. HOOK RULE:
- 3-4 lines
- chant style
- easy to remember
- viral होना चाहिए

8. STYLE FEEL:
- Hardcore → aggressive + power
- Emotional → pain + depth
- Storytelling → scene based

9. NO FORCED VOCAB:
- words natural flow में आएं

📌 STRUCTURE:

[Intro] (2-3 lines)

[Verse 1] (12 lines)

[Hook] 🔥 (3-4 lines)

[Verse 2] (12 lines)

[Hook]

[Outro] (2 lines)

⚠️ OUTPUT ONLY LYRICS (NO EXTRA TEXT)
"""

# ================= CLEANER =================
def remove_repetition(text):
    lines = text.split("\n")
    seen = set()
    final = []
    
    for line in lines:
        if line.strip() and line not in seen:
            final.append(line)
            seen.add(line)
    
    return "\n".join(final)

# ================= GENERATE =================
def generate_lyrics(topic, style, mood):
    try:
        # Step 1 - Generate
        raw = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are India's best divine rap lyricist. Your songs are viral."},
                {"role": "user", "content": build_prompt(topic, style, mood)}
            ],
            temperature=0.9,
            max_tokens=2000
        ).choices[0].message.content
        
        # Step 2 - Clean repetition
        final = remove_repetition(raw)
        
        return final
    
    except Exception as e:
        return f"Error: {e}"

# ================= OUTPUT =================
with col2:
    if generate:
        if not topic:
            st.error("⚠️ Topic डालो")
        else:
            with st.spinner("🔥 Writing VIRAL lyrics..."):
                lyrics = generate_lyrics(topic, style, mood)
                
                st.success("✅ PERFECT SONG READY 🔥")
                st.text_area("", lyrics, height=600)
                
                st.download_button(
                    "📥 Download",
                    lyrics,
                    file_name=f"{topic}.txt"
                )
                
                st.info("💡 Use in Suno AI / Udio → Viral Song 🚀")

import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="DivineRapTv PRO Engine", layout="wide")

st.title("💀 DivineRapTv PRO RAP ENGINE 🔥")
st.caption("Multi-Step AI System | 10/10 Lyrics Guaranteed")

col1, col2 = st.columns([1, 1.5])

with col1:
    topic = st.text_input("🎯 Topic", placeholder="Shiv Sati, Mahakal Tandav")
    
    style = st.selectbox("🎭 Style", [
        "Hardcore 🔥",
        "Emotional 💙",
        "Storytelling 📖"
    ])
    
    generate = st.button("🚀 Generate PRO Song")

# ================= STEP SYSTEM =================

def ai_call(prompt, temp=0.9):
    return client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=temp,
        max_tokens=1800
    ).choices[0].message.content


# STEP 1 - RAW
def step1_raw(topic, style):
    return ai_call(f"""
Write Hindi Divine Rap.

Topic: {topic}
Style: {style}

Structure:
[Intro]
[Verse 1]
[Hook]
[Verse 2]
[Outro]

Natural flow, basic lyrics.
""")

# STEP 2 - FLOW FIX
def step2_flow(lyrics):
    return ai_call(f"""
Improve flow of these rap lyrics.

- Make lines smooth for rapping
- Keep Hindi natural
- Fix awkward lines

Lyrics:
{lyrics}
""", 0.7)

# STEP 3 - RHYME FIX
def step3_rhyme(lyrics):
    return ai_call(f"""
Make rhyme perfect.

Rules:
- Every 2 lines rhyme (AA BB)
- Keep meaning same
- Improve musicality

Lyrics:
{lyrics}
""", 0.7)

# STEP 4 - HOOK BOOST
def step4_hook(lyrics):
    return ai_call(f"""
Make HOOK viral.

Rules:
- 3-4 lines
- catchy + repeatable
- emotional or powerful

Lyrics:
{lyrics}
""", 0.8)

# STEP 5 - FINAL POLISH
def step5_final(lyrics):
    return ai_call(f"""
Final polish:

- Remove weak lines
- Add punchlines
- Remove repetition
- Make it sound like a hit song

Final Lyrics:
{lyrics}
""", 0.7)


# ================= GENERATE =================

def generate_pro(topic, style):
    s1 = step1_raw(topic, style)
    s2 = step2_flow(s1)
    s3 = step3_rhyme(s2)
    s4 = step4_hook(s3)
    final = step5_final(s4)
    
    return final


# ================= OUTPUT =================

with col2:
    if generate:
        if not topic:
            st.error("⚠️ Topic डालो")
        else:
            with st.spinner("💀 Generating PRO Lyrics..."):
                lyrics = generate_pro(topic, style)
                
                st.success("🔥 10/10 PRO LYRICS READY 🔥")
                st.text_area("", lyrics, height=600)
                
                st.download_button(
                    "📥 Download Lyrics",
                    lyrics,
                    file_name=f"{topic}_pro.txt"
                )
                
                st.info("💡 Use in Suno AI → Best Result 🚀")

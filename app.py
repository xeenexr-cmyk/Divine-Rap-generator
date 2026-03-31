import streamlit as st
from groq import Groq

# API Key setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page Configuration
st.set_page_config(page_title="DivineRapTv 10/10 Engine", layout="wide", page_icon="🔱")

# Custom CSS for DivineRapTv Branding
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; border-radius: 10px; height: 3em; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #262730; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 DivineRapTv - ULTIMATE 10/10 RAP ENGINE 🔥")
st.subheader("Bhakti + Rap + Emotion | No Poems, Pure Hip-Hop")

# --- INPUT SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("🎯 Enter Topic (जैसे: लंका दहन, कालभैरव अष्टक)", placeholder="Apna topic likho...")

with col2:
    style = st.selectbox("🎭 Select Writing Style", [
        "Hardcore Rap (Divine/Raftaar Style) 🔥", 
        "Ramayan Story Rap (Fast Flow) 📖", 
        "Radha-Krishna Prem (Melodic Rap) ❤️", 
        "Meera Bhakti Pain (Soulful Rap) 😭", 
        "Bollywood Bhakti Fusion (Commercial) 🎶"
    ])

generate = st.button("🚀 GENERATE 10/10 MASTERPIECE")

# --- STEP 1: THE RAW GHOSTWRITER (RAP FOCUS) ---
def build_prompt(topic, style):
    return f"""
तुम भारत के सबसे खतरनाक Hip-Hop Ghostwriter हो। 'DivineRapTv' के लिए Rap लिखो।

🎯 TOPIC: {topic}
🎭 STYLE: {style}

❗ STRICT RAP RULES:
- NO POETRY: कविता मत लिखो। कहानी मत सुनाओ। शब्दों से प्रहार करो।
- NO FILLERS: "है/हूँ/था/थी/रहा/रही" जैसे शब्दों को 90% हटा दो। 
- STACCATO FLOW: हर लाइन 4-6 शब्दों की हो। छोटी लाइन = तेज़ फ्लो।
- ATTITUDE: शब्दों में वज़न और 'Street Credibility' हो।
- RHYME: Internal Rhymes (लाइन के बीच में तुकबंदी) और End Rhymes (AA-BB) कड़क हों।

Example of Good Rap Flow: 
"लंका का द्वार, आँखों में आग। दशानन का काल, सब होगा राख!" (Short and Punchy)

STRUCTURE:
[Intro] (2 Cold Lines)
[Verse 1] (12 Fast Lines)
[Hook] (4 Viral/Chant Lines - Heavy Energy)
[Verse 2] (12 Fast Lines - Punchline Heavy)
[Outro] (1 Mic Drop Line)
"""

# --- STEP 2: THE REFINER (LYRICS IMPROVER) ---
def refine_prompt(raw):
    return f"""
इन lyrics को 'Poem' से 'Hardcore Rap' में बदलो:
{raw}

FIX THESE:
1. 'है/हैं' जैसे शब्दों को हटाकर 'Punchlines' बढ़ाओ।
2. हर 2 लाइन के बाद एक भारी Metaphor डालो।
3. Flow को 'Tight' करो ताकि 90-100 BPM की बीat पर फिट आए।
4. Rhyme Scheme को Complex और Professional बनाओ।

Improved Lyrics:
"""

# --- STEP 3: THE VIRAL DOCTOR (FINAL POLISH) ---
def validate_prompt(refined):
    return f"""
तुम Viral Rap Doctor हो। DivineRapTv के लिए Final Check करो:
{refined}

TASK:
1. Hook को 'Anthem' जैसा बनाओ (Chants + Power)।
2. 'Verse' में Aggression और Devotion का Perfect Mix हो।
3. सुनिश्चित करो कि यह पढ़ने में कविता नहीं, 'ASLI RAP' लगे।

Final 10/10 Rap Version:
"""

# --- GENERATION ENGINE ---
def generate_song(topic, style):
    try:
        # Step 1
        raw_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम Raw Rap Writer हो"},
                      {"role": "user", "content": build_prompt(topic, style)}],
            temperature=0.85
        )
        raw = raw_res.choices[0].message.content

        # Step 2
        refined_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम Expert Hip-Hop Refiner हो"},
                      {"role": "user", "content": refine_prompt(raw)}],
            temperature=0.75
        )
        refined = refined_res.choices[0].message.content

        # Step 3
        final_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम Viral Rap Specialist हो"},
                      {"role": "user", "content": validate_prompt(refined)}],
            temperature=0.65
        )
        return final_res.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# --- OUTPUT DISPLAY ---
if generate:
    if not topic:
        st.error("⚠️ अरे भाई! पहले Topic तो डालो।")
    else:
        with st.spinner(f"🔥 {style} के हिसाब से 10/10 Rap तैयार हो रहा है..."):
            final_lyrics = generate_song(topic, style)
            
            st.success("✅ ASLI RAP READY! 🎤")
            st.text_area("🎤 Final Rap for DivineRapTv", final_lyrics, height=600)

            st.download_button(
                label="📥 Download Master Rap",
                data=final_lyrics,
                file_name=f"{topic}_rap.txt",
                mime="text/plain"
            )

st.markdown("---")
st.caption("DivineRapTv 10/10 Engine | Dedicated to Bhakti Rap Excellence")

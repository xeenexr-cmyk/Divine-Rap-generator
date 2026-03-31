import streamlit as st
from groq import Groq
import time

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
st.set_page_config(page_title="DivineRapTv - SUNO AI BEAST 3.0", layout="wide", page_icon="🔱")

# --- DARK MODE STYLING ---
st.markdown("""
<style>
    .stApp { background: #000; color: #ff0000; }
    .stButton>button { 
        background: linear-gradient(45deg, #8b0000, #ff0000); 
        color: white; font-weight: bold; border: none; height: 3.5rem; border-radius: 5px;
    }
    .stTextInput>div>div>input { background-color: #111; color: #ff4b4b; border: 1px solid #ff0000; }
    .stTextArea textarea { background-color: #050505 !important; color: #00ff00 !important; border: 1px solid #333 !important; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

st.title("🔱 DivineRapTv - SUNO AI BEAST ENGINE 3.0 🔥")
st.subheader("Optimized for Suno AI v3.5/v4/v5.5 | Pure Hardcore Bhakti Trap")

# --- INPUT SECTION ---
col1, col2 = st.columns([2, 1])
with col1:
    topic = st.text_input("🎯 Enter War Topic", placeholder="Example: Mahakal Tandav, Ravan Vadh, Aghori Shakti")
with col2:
    mode = st.selectbox("⚔️ Select Style", ["Hardcore Vedic Trap 🔥", "Fast Flow Massacre ⚡", "Dark Tantric Rap 🌙"])

generate = st.button("🚀 GENERATE SUNO-READY LYRICS")

# --- PROMPT ENGINE ---
def build_suno_prompt(topic, mode):
    return f"""
तुम एक Pro Suno AI Prompt Engineer और Hardcore Rapper हो।

🎯 TARGET: {topic}
🎭 STYLE: {mode}

❗ RULES FOR SUNO AI OPTIMIZATION:
1. USE TAGS: [Intro], [Aggressive Rap Verse], [Power Hook], [Beat Drop], [Outro].
2. AD-LIBS: लाइनों के बीच में (Kya!), (Brrr!), (Kaal!), (Hah!) जैसे शब्द जोड़ो।
3. NO FILLERS: 'है/हूँ/था/रहा' बिलकुल मना है। सिर्फ 'Nouns' और 'Power Words'।
4. SYLLABLES: हर लाइन में 3-4 शब्द। छोटे शब्द = तेज़ रैप।
5. PUNCTUATION: हर लाइन के बाद "!" लगाओ ताaki AI Energy के साथ गाये।

STRUCTURE:
[Intro: Dark Ambient, Damru Sounds, Heavy Distortion]
[Aggressive Rap Verse 1: Fast Staccato Flow]
(16 short punchy lines with internal rhymes)
[Power Hook: Chanted, Anthemic, Heavy Bass]
(4 lines viral chant)
[Aggressive Rap Verse 2: Technical Flow]
[Outro: Fade out, Evil Laugh]
"""

def refine_for_suno(raw):
    return f"""
इन lyrics को Suno AI v5.5 के लिए 'Perfect' बनाओ:
{raw}

FIX PROTOCOL:
- "जैसे/जैसा" (Similes) हटाओ। सीधा 'Direct Punch' लिखो।
- हर 2 लाइन के बाद (TRRRRR!) या (AAG!) जैसे Ad-libs जोड़ो।
- सुनिश्चित करो कि हर लाइन 'Short' और 'Aggressive' है।
- [Structure Tags] को Bold और Clear रखो।

Final Suno-Ready Version:
"""

# --- GENERATION LOGIC ---
def generate_beast_lyrics(topic, mode):
    try:
        # Step 1: Raw Generation
        raw = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": build_suno_prompt(topic, mode)}],
            temperature=1.0
        ).choices[0].message.content

        # Step 2: Suno Optimization
        final = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम Suno AI के सबसे बड़े एक्सपर्ट हो।"},
                      {"role": "user", "content": refine_for_suno(raw)}],
            temperature=0.6
        ).choices[0].message.content

        return final
    except Exception as e:
        return f"Error: {str(e)}"

# --- OUTPUT ---
if generate:
    if not topic:
        st.error("⚠️ Topic likho pehle!")
    else:
        with st.spinner("💀 BEAST MODE: Writing Suno-Ready Masterpiece..."):
            lyrics = generate_beast_lyrics(topic, mode)
            st.success("✅ SUNO AI LYRICS READY!")
            st.text_area("🎤 Copy this into Suno AI Custom Mode:", lyrics, height=600)
            
            st.info("💡 **SUNO AI TIP:** Use 'Style' as: Hardcore Bhakti Trap, 100 BPM, Aggressive Male Vocals, Heavy Bass, Dark Atmosphere.")
            
            st.download_button("📥 Download Lyrics", lyrics, file_name=f"{topic}_suno_rap.txt")

st.markdown("---")
st.caption("DivineRapTv | Powered by Beast Engine 3.0 | Optimized for AI Music Generation")

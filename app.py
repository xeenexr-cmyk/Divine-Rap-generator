import streamlit as st
from groq import Groq

# API Key setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page Configuration
st.set_page_config(page_title="DivineRapTv Hyper-Engine", layout="wide", page_icon="🔱")

# UI Styling
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #ff0000; color: white; border-radius: 5px; height: 3.5em; font-weight: bold; border: none; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: white; border: 1px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 DivineRapTv - HYPER-ENGINE 10/10 🔥")
st.subheader("No Poetry. No Similes. Pure Hardcore Rap.")

# --- INPUT SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("🎯 Enter Topic (जैसे: अघोरी शिव, कालभैरव, तांडव)", placeholder="Topic likho aur aag lagao...")

with col2:
    style = st.selectbox("🎭 Select Rap Persona", [
        "Hardcore Kill Flow (Divine Style) 🔥", 
        "Fast Story Rap (Raftaar Style) 📖", 
        "Deep Soul Rap (Emotional Punch) 😭"
    ])

generate = st.button("🚀 GENERATE RAW HARDCORE RAP")

# --- THE "NO-POETRY" PROMPT LOGIC ---
def build_prompt(topic, style):
    return f"""
तुम एक 'Aggressive Hip-Hop Ghostwriter' हो। तुम कविता (Poem) से नफरat करते हो।

🎯 TOPIC: {topic}
🎭 STYLE: {style}

❗ STRICT RULES (FOLLOW OR BE FIRED):
1. NO SIMILES: "जैसे", "समान", "जैसा", "तैसे" का प्रयोग 100% मना है। (Example: Don't say 'Tiger jaisa', say 'Main Tiger').
2. NO FILLERS: "है", "हूँ", "था", "थी", "रहा", "रही" को 95% डिलीट करो। 
3. SYLLABLE CONTROL: हर लाइन में सिर्फ 4 से 5 शब्द होने चाहिए। 
4. STACCATO FLOW: लाइनें काटने वाली और छोटी हों। (Example: 'आँखों में आग। लंका राख।')
5. DIRECT IMPACT: सीधा वार करो। शब्दों में भारीपन (Heavy Vocabulary) लाओ।

STRUCTURE:
[Intro] - 2 Cold Lines (No music, just attitude)
[Verse 1] - 12 Lines (Rhyme scheme: AABB, Fast attack)
[Hook] - 4 Lines (Chant/Mantra Style - Extreme Energy)
[Verse 2] - 12 Lines (Aggressive Punchlines & Metaphors)
[Outro] - 1 Line (Mic Drop)
"""

def refine_prompt(raw):
    return f"""
ये lyrics अभी भी थोड़े 'Soft' हैं। इन्हें 'Hardcore Hip-Hop' में बदलो:
{raw}

FIX PROTOCOL:
1. "जैसे" (Like/As) वाली सारी लाइनें हटाओ। उन्हें 'Direct Statement' बनाओ।
2. हर line से "है/रहा" हटाकर उसे Short करो। 
3. Rhymes को 'Perfect' और 'Punchy' बनाओ।
4. Flow को इतना 'Tight' करो कि बीट (Beat) पर धमाका हो।

Final Raw Rap:
"""

# --- GENERATION ENGINE ---
def generate_song(topic, style):
    try:
        # Step 1: Raw Draft
        raw_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम Raw Rap Writer हो।"},
                      {"role": "user", "content": build_prompt(topic, style)}],
            temperature=0.9
        )
        raw = raw_res.choices[0].message.content

        # Step 2: Rap Filter
        final_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम एक Hip-Hop Surgeon हो जो कविता को काटकर रैप बनाता है।"},
                      {"role": "user", "content": refine_prompt(raw)}],
            temperature=0.6
        )
        return final_res.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# --- OUTPUT DISPLAY ---
if generate:
    if not topic:
        st.error("⚠️ Topic daalo pehle!")
    else:
        with st.spinner("🔥 Hyper-Engine Aag ugal raha hai..."):
            final_lyrics = generate_song(topic, style)
            
            st.success("✅ RAW HARDCORE RAP READY! 🎤")
            st.text_area("🎤 Final Rap for DivineRapTv", final_lyrics, height=600)

            st.download_button(
                label="📥 Download RAW Rap",
                data=final_lyrics,
                file_name=f"{topic}_raw_rap.txt",
                mime="text/plain"
            )

st.markdown("---")
st.caption("DivineRapTv Hyper-Engine | Powering the future of Bhakti Rap")

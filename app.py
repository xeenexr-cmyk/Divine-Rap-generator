import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI Setup
st.set_page_config(page_title="Divine Rap Studio v4.0", page_icon="🔱", layout="wide")

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 8px; background: linear-gradient(45deg, #ff4b2b, #ff416c); color: white; font-weight: bold; height: 3em; border: none; }
    .stTextInput>div>div>input { background-color: #161b22; color: #00ffcc; border: 1px solid #30363d; font-size: 18px; }
    .stTextArea>div>div>textarea { background-color: #0d1117; color: #c9d1d9; font-family: 'Courier New', Courier, monospace; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 Divine Rap Studio v4.0 (Pro Edition)")
st.write("### DivineRapTv के लिए असली 'Aggressive & Professional' लिरिक्स")

col1, col2 = st.columns([1, 1.2])

with col1:
    topic = st.text_input("🎯 विषय (जैसे: महाकाल का अट्टहास, रक्तबीज वध, कृष्ण की कुरुक्षेत्र वाणी)", placeholder="यहाँ अपना टॉपिक लिखें...")
    
    mode = st.selectbox("🎭 Flow और Energy चुनें", [
        "Aggressive/Hardcore (Fast Flow & Heavy Punchlines)",
        "Deep Storytelling (Cinematic Imagery)",
        "Emotional/Virah (Soulful & Melodic Rap)",
        "Trance/Psych (High Energy Psychedelic)"
    ])
    
    include_beat = st.checkbox("🎵 बीट गाइड और BPM शामिल करें?", value=True)
    st.divider()
    generate_btn = st.button("🚀 Generate Masterpiece")

def build_pro_prompt(topic, mode, include_beat):
    return f"""
तुम भारत के सबसे बड़े 'Divine Hip-Hop' Ghostwriter हो। तुम्हारा स्टाइल Professional Rappers जैसा है। 
DivineRapTv के लिए Lyrics लिखो जो 'Viral' होने के लायक हों।

🎯 TOPIC: {topic}
🎭 FLOW MODE: {mode}

❗ लिरिक्स लिखने के 'Strict' नियम:
1. **No Basic Rhymes:** 'गया हूँ', 'रहा हूँ' जैसे साधारण शब्द प्रतिबंधित हैं। इनकी जगह Multisyllabic Rhymes का उपयोग करो (जैसे: 'विनाश' के साथ 'आकाश' नहीं, बल्कि 'अट्टहास' या 'कारवास' लाओ)।
2. **Aggressive Vocabulary:** शुद्ध और भारी हिन्दी (जैसे: अघोर, भस्म, त्रिकाल, प्रचंड, मसान, हलाहल, गूँज, शून्य)।
3. **Strict Meter:** हर लाइन की लंबाई एक जैसी रखो ताकि Flow न टूटे। 
4. **Cinematic Punchlines:** ऐसी लाइनें जो 'Quotes' बन सकें।
5. **Format:** [Intro], [Verse 1], [Hook 🔥], [Verse 2], [Hook], [Outro]।

{ "साथ ही, अंत में Beat Type (Old School/Trap), BPM और प्रमुख Instruments (Damru, Sitar, Heavy Sub-Bass) की जानकारी दें।" if include_beat else "" }

लिखना शुरू करो:
"""

if generate_btn:
    if not topic:
        st.warning("महादेव! टॉपिक तो डालिए।")
    else:
        with st.spinner("🔥 शब्दों को आग में तपाया जा रहा है..."):
            try:
                # Temperature 0.8 रखा है ताकि AI भटके नहीं और तुकबंदी सटीक रखे
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक प्रोफेशनल हिन्दी रैप राइटर हो जो केवल 'Heavy' और 'Cinematic' कंटेंट लिखता है।"},
                        {"role": "user", "content": build_pro_prompt(topic, mode, include_beat)}
                    ],
                    temperature=0.8,
                    max_tokens=2000
                )

                lyrics_output = response.choices[0].message.content
                
                with col2:
                    st.success("✨ मास्टरपीस तैयार है!")
                    st.markdown("### 📜 Final Script & Music Guide")
                    st.text_area(label="Copy-Paste Ready Lyrics", value=lyrics_output, height=650)
                    
                    st.info("💡 Pro Tip: इन लिरिक्स को पढ़ते समय ज़ोर से बोलें (Recite) ताकि आपको Flow का अंदाजा हो सके।")
                
            except Exception as e:
                st.error(f"❌ Error: {e}")

st.divider()
st.caption("© 2026 DivineRapTv | Created for Professional Creators")

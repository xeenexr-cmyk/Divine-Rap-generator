import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI Setup for a Premium Experience
st.set_page_config(page_title="Divine Rap Studio: GOD MODE", page_icon="🔱", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 2px; background: linear-gradient(45deg, #4b0082, #ff0000); color: white; font-weight: 900; height: 3.5em; border: 1px solid #ff0000; font-size: 1.4rem; box-shadow: 0px 0px 20px #ff000055; }
    .stTextInput input { background-color: #0a0a0a; color: #ff3e3e; border: 1px solid #444; font-size: 1.2rem; }
    .stTextArea textarea { font-size: 1.2rem !important; color: #00ff00 !important; background-color: #050505 !important; font-family: 'Courier New', monospace; line-height: 1.5; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 Divine Rap Studio: THE GOD MODE")
st.write("### DivineRapTv: शब्दों की आग, महादेव का साथ।")

col1, col2 = st.columns([1, 1.4])

with col1:
    topic = st.text_input("🎯 विषय (Topic)", placeholder="जैसे: शिव तांडव, रावण वध, अघोरी की राख")
    mode = st.selectbox("🎭 फ्लो चुनें", ["Hardcore Boom Bap", "Aggressive Trap", "Vedic Drill"])
    st.divider()
    generate_btn = st.button("🔥 UNLEASH THE TANDAV")

def build_god_mode_prompt(topic, mode):
    return f"""
तुम भारत के सबसे बड़े Battle Rapper और संस्कृत के विद्वान हो। 'DivineRapTv' के लिए 'Vedic Rap' लिखो।

🎯 TOPIC: {topic}
🎭 STYLE: {mode}

❗ कड़े नियम (STRICT RULES):
1. **NO REPETITION:** Verse 1 और Verse 2 में एक भी लाइन या 'Rhyme' रिपीट नहीं होनी चाहिए। अगर Verse 1 में 'अकाल' यूज़ किया, तो Verse 2 में 'महाकाल' या 'विकराल' लाओ।
2. **MULTISYLLABIC RHYMES:** तुकबंदी गहरी होनी चाहिए (जैसे: 'विनाश' - 'अट्टहास', 'प्रचंड' - 'अखंड', 'त्रिनेत्र' - 'कुरुक्षेत्र')।
3. **PUNCHLINES:** हर 2 लाइन के बाद एक ऐसी लाइन लिखो जो सुनने वाले की रूह कँपा दे।
4. **FLOW METER:** हर लाइन 8-10 शब्दों की हो। छोटे शब्द, भारी इम्पैक्ट।

📌 FORMAT:
[Intro] (मंत्रों का उच्चारण + भारी डायलॉग)
[Verse 1] (8 अलग लाइन्स - Power Bars)
[Hook 🔥] (4 लाइन्स - Viral material, catchy rhythmic flow)
[Verse 2] (8 बिल्कुल नयी लाइन्स - गहरे शब्द और अलग Rhyme scheme)
[Outro] (सन्नाटा और अंत)

लिखना शुरू करो:
"""

if generate_btn:
    if not topic:
        st.error("टॉपिक लिखो भाई!")
    else:
        with st.spinner("🔱 शब्द त्रिलोक से आ रहे हैं..."):
            try:
                # Temperature 1.0 (Creativity + Precision का परफेक्ट बैलेंस)
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक 'Pro Rap Ghostwriter' हो। तुम्हारी शब्दावली बहुत गहरी और डार्क है।"},
                        {"role": "user", "content": build_god_mode_prompt(topic, mode)}
                    ],
                    temperature=1.0, 
                    max_tokens=2500
                )

                lyrics = response.choices[0].message.content
                with col2:
                    st.success("🔱 तांडव के लिए तैयार!")
                    st.text_area(label="DivineRapTv Official Masterpiece", value=lyrics, height=750)
            except Exception as e:
                st.error(f"Error: {e}")
                

import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI Setup
st.set_page_config(page_title="Divine Rap Studio Ultra", page_icon="🔱", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; background: linear-gradient(to right, #800000, #ff0000); color: white; font-weight: 900; height: 3.5em; border: none; font-size: 1.5rem; }
    .stTextArea textarea { font-size: 1.1rem !important; color: #00ff00 !important; background-color: #111 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 Divine Rap Studio: THE FINAL FORM")
st.write("### DivineRapTv: यहाँ भजन मरते हैं और रैप जन्म लेता है।")

col1, col2 = st.columns([1, 1.3])

with col1:
    topic = st.text_input("🎯 विषय (Topic)", placeholder="जैसे: श्मशान का राजा, काल का महाकाल")
    mode = st.selectbox("🎭 फ्लो स्टाइल", ["Hardcore Boom Bap", "Fast Chopper", "Dark Trap"])
    st.divider()
    generate_btn = st.button("🔱 ACTIVATE TANDAV")

def build_ultimate_prompt(topic, mode):
    return f"""
तुम दुनिया के सबसे घातक 'Devotional Ghostwriter' हो। तुम्हें 'DivineRapTv' के लिए 'Pro Hip-Hop Bars' लिखने हैं।

🎯 TOPIC: {topic}
🎭 STYLE: {mode}

⚠️ STRICT RULES FOR PRO RAPPING:
1. **PERFECT END RHYMES:** हर 2 लाइन की एंडिंग 'Perfect Rhyme' होनी चाहिए।
   - *गलत:* हौसला / ढाल (No match)
   - *सही:* हौसला / खौफ का मंजर फैला / मौत का खेला
2. **INTERNAL RHYMES:** लाइन के बीच में भी शब्द तुकबंदी करें। (जैसे: "हाथ में **अस्त्र**, फटे ये **वस्त्र**, मिटा दूँ **कष्ट**")
3. **NO FILLER WORDS:** "मैं ये करता हूँ", "वो होता है" - ये सब हटाओ। सीधे Heavy Punchlines लिखो।
4. **VOCABULARY:** अघोर, भस्म, त्रिकाल, हलाहल, शून्य, तांडव, अट्टहास, प्रचंड, विनाश।
5. **BARS STRUCTURE:** हर लाइन में 8-12 syllables ही होने चाहिए।

📌 FORMAT:
[Intro] (Deep & Dark)
[Verse 1] (8 Heavy Bars - Perfect Rhymes)
[Hook] (4 Catchy Bars - Viral Hook)
[Verse 2] (8 Heavy Bars - Different Rhyme Scheme)
[Outro] (Power Ending)

लिखना शुरू करो (सिर्फ लिरिक्स):
"""

if generate_btn:
    if not topic:
        st.error("टॉपिक डालिए!")
    else:
        with st.spinner("🔱 महाकाल की आज्ञा से शब्द प्रकट हो रहे हैं..."):
            try:
                # Temperature 1.1 - रचनात्मकता और सटीकता का मेल
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक Professional Battle Rapper हो। तुम्हारी तुकबंदी (Rhyming) एकदम परफेक्ट है।"},
                        {"role": "user", "content": build_ultimate_prompt(topic, mode)}
                    ],
                    temperature=1.1,
                    max_tokens=2000
                )

                lyrics = response.choices[0].message.content
                with col2:
                    st.success("🔥 ब्रह्मांड हिल गया! लिरिक्स तैयार हैं:")
                    st.text_area(label="DivineRapTv Official", value=lyrics, height=750)
            except Exception as e:
                st.error(f"Error: {e}")
                

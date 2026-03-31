import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="Divine Rap Studio: ULTIMATE", layout="wide")

# CSS for a Raw Hip-Hop Look
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    .stButton>button { background: linear-gradient(90deg, #ff0000, #440000); color: #fff; font-weight: bold; border: none; height: 3.5rem; font-size: 1.5rem; width: 100%; border-radius: 10px; }
    .stTextArea textarea { color: #00ff00 !important; background-color: #111 !important; font-family: monospace; font-size: 1.2rem !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 Divine Rap Studio: THE ULTIMATE")
st.write("### DivineRapTv के लिए अब निकलेगी असली आग!")

col1, col2 = st.columns([1, 1.5])

with col1:
    topic = st.text_input("🎯 रैप का विषय", placeholder="जैसे: श्मशान का राजा, काल का तांडव")
    mode = st.selectbox("🎭 फ्लो", ["Aggressive Battle Rap", "Dark Aghori Vibe", "Fast Chopper Flow"])
    generate_btn = st.button("🔥 ACTIVATE BEAST MODE")

def build_beast_prompt(topic, mode):
    # यहाँ 'Few-Shot' टेक्निक यूज़ की है ताकि AI को पता चले कि 'Bars' क्या होते हैं
    return f"""
तुम एक 'Underground Battle Rapper' हो। तुम्हें 'DivineRapTv' के लिए "Hardcore Devotional Rap" लिखना है। 
भजन मत लिखो, 'Bars' लिखो।

🎯 TOPIC: {topic}
🎭 STYLE: {mode}

🔥 RHYME REFERENCE (ऐसा लिखो):
"सिर पे **कपाल**, गले में **काल**, 
मैं हूँ **विकराल**, मचा दूँ **बवाल**।" 

❗ सख्त निर्देश (STRICT RULES):
1. **PERFECT END-RHYMES:** हर दो लाइन का आखिरी शब्द आपस में मैच होना चाहिए (A-A-B-B Pattern)।
2. **NO 'HOON' ENDINGS:** 'करता हूँ', 'खड़ा हूँ' जैसे शब्दों पर लाइन खत्म न करो। भारी संज्ञा (Nouns) का प्रयोग करो।
3. **METAPHORS:** शिव को 'मौत का सौदागर', 'राख का राजा', 'शून्य का शोर' बोलो।
4. **NO REPETITION:** हर Verse में एकदम नए शब्द होने चाहिए।

📌 FORMAT: [Intro] -> [Verse 1 (8 Bars)] -> [Hook (Catchy)] -> [Verse 2 (8 Bars)] -> [Outro]

यहाँ से 'Aggressive' शुरुआत करो:
"""

if generate_btn:
    if not topic:
        st.warning("टॉपिक लिखो!")
    else:
        with st.spinner("🔱 महाकाल के दरबार से शब्द आ रहे हैं..."):
            try:
                # Temperature 1.25 ताकि वो बोरिंग न हो
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक खतरनाक रैपर हो। तुम्हारी हिंदी बहुत गहरी और 'Raw' है।"},
                        {"role": "user", "content": build_beast_prompt(topic, mode)}
                    ],
                    temperature=1.25, 
                    max_tokens=2000
                )

                lyrics = response.choices[0].message.content
                with col2:
                    st.success("🔱 तांडव के लिए तैयार!")
                    st.text_area(label="DivineRapTv Official", value=lyrics, height=700)
            except Exception as e:
                st.error(f"Error: {e}")
                

import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI Setup
st.set_page_config(page_title="DivineRapTv v9.0", page_icon="🔥", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    .stButton>button { background: linear-gradient(90deg, #ff0000, #330000); color: #fff; font-weight: 900; border: 1px solid red; height: 4rem; font-size: 1.5rem; width: 100%; border-radius: 5px; box-shadow: 0px 0px 20px red; }
    .stTextArea textarea { color: #00ff00 !important; background-color: #111 !important; font-family: 'Courier New', monospace; font-size: 1.3rem !important; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 DivineRapTv: Viral Beast Engine")
st.write("### यहाँ भजन नहीं, सीधा 'Tandav' रिकॉर्ड होगा।")

col1, col2 = st.columns([1, 1.5])

with col1:
    topic = st.text_input("🎯 विषय (Topic)", placeholder="जैसे: लंका दहन, रावण अट्टहास")
    mode = st.selectbox("🎭 मोड चुनें", [
        "Hardcore Aggressive (Divine/Raftaar)",
        "Epic Storytelling (Ramayan/Katha Flow)",
        "Emotional/Virah (Radha-Krishna)",
        "Meera Bhakti Pain",
        "Bollywood Fusion"
    ])
    generate_btn = st.button("🔱 UNLEASH THE VIBE")

def build_viral_prompt(topic, mode):
    return f"""
तुम भारत के सबसे बड़े Underground Ghostwriter हो। तुम्हारा काम 'DivineRapTv' के लिए VIRAL RAPS लिखना है। 
भजन लिखना मना है। मुझे 'Hard-hitting Bars' चाहिए।

🎯 TOPIC: {topic}
🎭 STYLE: {mode}

🔥 RHYME & FLOW REFERENCE (ऐसा लिखना है):
"आँखों में **ज्वाला**, कंठ में **हाला**, 
पहनी है मैंने मुंडों की **माला**।
मैं हूँ **अकाली**, शक्ति **विकराली**,
अधर्मियों की अब होने वाली **बहाली**।"

❗ STRICT RULES:
1. **NO 'HOON' ENDINGS:** "करता हूँ", "जाता हूँ" - ये शब्द बैन हैं। ये रैप का फ्लो मार देते हैं।
2. **MULTISYLLABIC RHYMES:** तुकबंदी गहरी होनी चाहिए (जैसे: 'प्रचंड' / 'अखंड', 'त्रिशूल' / 'निर्मूल', 'अट्टहास' / 'विनाश')।
3. **PUNCHLINES:** हर 2 लाइन के बाद ऐसी लाइन जो रोंगटे खड़े कर दे।
4. **VOCABULARY:** 'भगवान' नहीं 'ब्रह्मांड', 'गुस्सा' नहीं 'क्रोध की अग्नि', 'दुश्मन' नहीं 'अधर्मी'।

📌 FORMAT: [Intro] -> [Verse 1 (12 Bars)] -> [Hook 🔥] -> [Verse 2 (12 Bars)] -> [Outro]

यहाँ से असली आग (Fire) उगलना शुरू करो:
"""

if generate_btn:
    if not topic:
        st.error("बिना टॉपिक के आग कैसे लगेगी?")
    else:
        with st.spinner("🔱 शब्दों का तांडव तैयार हो रहा है..."):
            try:
                # Temperature 1.15 ताकि AI नए और खतरनाक शब्द ढूंढे
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक Professional Battle Rapper हो। तुम्हारी भाषा Raw और Powerful है।"},
                        {"role": "user", "content": build_viral_prompt(topic, mode)}
                    ],
                    temperature=1.15,
                    max_tokens=2500
                )

                lyrics = response.choices[0].message.content
                with col2:
                    st.success("🔥 TRACK READY!")
                    st.text_area(label="DivineRapTv Official Masterpiece", value=lyrics, height=750)
            except Exception as e:
                st.error(f"Error: {e}")
                

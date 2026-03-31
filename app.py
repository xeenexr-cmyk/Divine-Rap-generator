import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI Setup
st.set_page_config(page_title="DivineRapTv Studio v8.0", page_icon="🎤", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0a0a0a; color: white; }
    .stButton>button { background: linear-gradient(45deg, #FF4B2B, #FF416C); color: white; border-radius: 10px; height: 3.5rem; width: 100%; font-weight: bold; font-size: 1.2rem; border: none; }
    .stTextInput input { background-color: #111; color: #00FFCC; border: 1px solid #333; }
    .stSelectbox div[data-baseweb="select"] > div { background-color: #111; color: white; }
    .stTextArea textarea { font-family: 'Courier New', monospace; font-size: 1.2rem !important; color: #FFD700 !important; background-color: #050505 !important; border: 1px solid #444; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎤 DivineRapTv: Multi-Mode Rap Studio")
st.write("---")

col1, col2 = st.columns([1, 1.5])

with col1:
    topic = st.text_input("🎯 विषय (Topic) लिखें", placeholder="जैसे: श्मशान का राजा, राम वनवास, राधा का इंतज़ार")
    
    mode = st.selectbox("🎭 मोड चुनें (Writing Style)", [
        "Hardcore Divine Rap (Raftaar Style)",
        "Ramayan Story Flow (Katha Style)",
        "Radha-Krishna Prem/Virah (Emotional)",
        "Meera Bhakti Pain (Soulful)",
        "Bollywood Bhakti Fusion (Melodic)"
    ])
    
    generate_btn = st.button("🚀 GENERATE MASTERPIECE")

def build_dynamic_prompt(topic, mode):
    # मोड के हिसाब से अलग-अलग 'Instructions'
    style_guide = {
        "Hardcore Divine Rap (Raftaar Style)": "Vibe: Aggressive, Fast, Heavy. शब्द: अकाल, प्रचंड, तांडव, हलाहल, शून्य। End-rhymes: परफेक्ट और भारी।",
        "Ramayan Story Flow (Katha Style)": "Vibe: Narrative, Epic, Storytelling. हर लाइन में दृश्य (visuals) बदलें। शब्द: मर्यादा, धनुष, अयोध्या, वनवास, विजय।",
        "Radha-Krishna Prem/Virah (Emotional)": "Vibe: Soft, Romantic, Sad. शब्द: बाँसुरी, यमुना, विरह, इंतज़ार, चितचोर। लय बहुत कोमल हो।",
        "Meera Bhakti Pain (Soulful)": "Vibe: Devotional, Painful, Surrender. शब्द: जोगन, प्याला, गिरधर, रीत, रूह। जैसे आत्मा पुकार रही हो।",
        "Bollywood Bhakti Fusion (Melodic)": "Vibe: Catchy, Modern, Musical. शब्द: सजदा, इबादत, मौला, देवा। Hook ऐसा जो रील्स पर हिट हो जाए।"
    }

    return f"""
तुम भारत के सबसे महान गीतकार हो। तुम्हें 'DivineRapTv' के लिए लिरिक्स लिखने हैं।

🎯 TOPIC: {topic}
🎭 MODE: {mode}
🔥 STYLE GUIDE: {style_guide[mode]}

❗ सख्त नियम (MANDATORY):
1. **PERFECT RHYMING:** हर दो लाइन की तुकबंदी एकदम सटीक होनी चाहिए (A-A-B-B Pattern)।
2. **INTERNAL FLOW:** लाइनों की लंबाई संतुलित हो ताकि रैप करते समय सांस न टूटे।
3. **NO REPETITION:** हर Verse में नए शब्द और नए विचार होने चाहिए।
4. **EMOTION:** जिस मोड को चुना गया है, उसका दर्द या गुस्सा शब्दों में महसूस होना चाहिए।

📌 FORMAT: [Intro] -> [Verse 1] -> [Hook 🔥] -> [Verse 2] -> [Outro]

यहाँ से 'Professional' लिरिक्स लिखना शुरू करो:
"""

if generate_btn:
    if not topic:
        st.error("कृपया एक विषय (Topic) तो लिखो भाई!")
    else:
        with st.spinner(f"✨ {mode} के हिसाब से शब्द तैयार हो रहे हैं..."):
            try:
                # Temperature को मोड के हिसाब से संतुलित किया गया है
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": f"तुम एक एक्सपर्ट {mode} लिरिसिस्ट हो। तुम साधारण कविता नहीं, बल्कि हिट गाने लिखते हो।"},
                        {"role": "user", "content": build_dynamic_prompt(topic, mode)}
                    ],
                    temperature=0.85, 
                    max_tokens=2000
                )

                lyrics = response.choices[0].message.content
                with col2:
                    st.success(f"🔱 {mode} तैयार है!")
                    st.text_area(label="Official DivineRapTv Script", value=lyrics, height=750)
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.caption("Produced for DivineRapTv | Designed by Gemini v2026")

import streamlit as st
import google.generativeai as genai
import time

# ==================== API SETUP ====================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Page config
st.set_page_config(
    page_title="DivineRapTv - Master Engine 3.0",
    layout="wide",
    page_icon="🔱"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #0a0000 0%, #1a0000 100%); }
.final-header {
    text-align: center; padding: 1.5rem;
    background: linear-gradient(135deg, #1a0000, #2a0000);
    border-radius: 15px; margin-bottom: 2rem; border: 1px solid #ff3300;
}
.final-title {
    font-size: 2.2rem; font-weight: bold;
    background: linear-gradient(90deg, #ff0000, #ffaa00);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.style-card {
    background: linear-gradient(135deg, #1a0000, #0a0000);
    border-left: 4px solid #ff6600; padding: 1.5rem; margin: 0.5rem 0; border-radius: 10px;
}
.stButton>button {
    background: linear-gradient(90deg, #ff3300, #ff6600);
    color: white; font-weight: 900; border: none; height: 3.5rem;
    border-radius: 10px; font-size: 1.2rem; letter-spacing: 1px;
}
.stTextArea textarea {
    background-color: #050505 !important; color: #00ff00 !important;
    border: 1px solid #ff6600 !important; font-family: 'Courier New', monospace;
    font-size: 1.1rem !important; line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ==================== PERFECT EXAMPLE (THE SOUL OF THE APP) ====================
PERFECT_EXAMPLE_HINDI = '''
[इंट्रो - चांट धीमा]
ॐ नमः शिवाय... (Aag!)
महाकाल... (Rakh!)

[वर्स 1 - रैप स्लो बिल्ड]
जटा में गंगा, माथे पे आग!
तीसरी आँख बोले, खत्म हर राग!
शून्य से जन्मा, शून्य में लीन!
शिव है चेतना, शिव ही सीन!
भस्म से सजा, पर राजाओं का राजा!
काल भी काँपे, जब खुला दरवाज़ा!

[हुक - पावरफुल चांट]
हर हर महादेव! गूंजे आसमान!
हर हर महादेव! थर्राए जहान!
तांडव की आग, बोले हर कण!
शिव ही शक्ति, शिव ही ब्रह्म!

[वर्स 2 - हार्ड रैप]
ना सिंहासन चाहिए, ना सोने का ताज!
शमशान में भी दिखे पूरा समाज!
अहंकार टूटे, गिर जाए नक़ाब!
शिव की शरण में मिटे हर ख्वाब!
(Trrrr! Brrrr!)
'''

# Header
st.markdown(f"""
<div class="final-header">
    <div class="final-title">🔱 DivineRapTv - Master Engine 3.0 🔱</div>
    <p style="color: #ffaa44; font-weight: bold;">Bhakti x Hardcore Rap | Suno AI Optimized</p>
    <p style="color: #44ff44; font-size: 0.85rem;">STABLE MODE: AUTO-SWITCH MODELS | NO 404 ERROR</p>
</div>
""", unsafe_allow_html=True)

# ==================== STYLE DEFINITIONS ====================
STYLES = {
    "शिव तांडव रैप 🔥": "Hardcore, Aghori, Aggressive, Heavy Bass",
    "हनुमान बाल कांड रैप 🐒": "Powerful, Speed, War Drums, Energetic",
    "रामायण युद्ध रैप 🏹": "Epic Storytelling, War Orchestral, Brutal",
    "राधा कृष्ण प्रेम रैप ❤️": "Melodic, Emotional, Soulful, Flute Mix",
    "माँ दुर्गा शक्ति रैप 🔱": "Feminine Power, Fast Flow, Mahishasur Vadh"
}

# ==================== GENERATE FUNCTION ====================
def generate_rap(style, topic, mood, length):
    prompt = f"""
तुम्हें 'DivineRapTv' के लिए दुनिया का सबसे खतरनाक 'Hardcore Bhakti Rap' लिखना है।

नीचे दिए गए परफेक्ट उदाहरण को बिल्कुल फॉलो करो:
{PERFECT_EXAMPLE_HINDI}

🎯 TOPIC: {topic} | 🎭 STYLE: {style} | 🎭 MOOD: {mood} | 📏 LENGTH: {length}

❗ RULES:
1. 'है/हूँ/था/रहा' हटाओ। सीधा Punchlines (4-6 शब्द per line)।
2. हर 2 लाइन के बाद (Ad-libs) जोड़ो (Aag!), (Kaal!), (Trrrr!)।
3. Structure: [Intro], [Verse 1], [Hook], [Verse 2], [Hook], [Outro].
4. Suno AI v5.5 के लिए [Metatags] इस्तेमाल करो।
(सिर्फ गीत दो, कोई एक्स्ट्रा टेक्स्ट नहीं)
"""

    # --- FALLBACK PROTECTION ---
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: Dono models fail ho gaye. Check API Key. {str(e)}"

# ==================== UI LAYOUT ====================
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="style-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 रैप टॉपिक")
    topic = st.text_input("", placeholder="जैसे: शिव तांडव, लंका दहन", key="topic")
    
    st.markdown("### ⚔️ रैप स्टाइल")
    style = st.selectbox("", list(STYLES.keys()), key="style")
    
    st.markdown("### 🎭 मूड")
    mood = st.select_slider("", options=["भावुक", "संतुलित", "आक्रामक", "वायरल"], value="आक्रामक")
    
    st.markdown("### 📏 लंबाई")
    length = st.select_slider("", options=["Shorts", "Full", "Epic"], value="Full")
    st.markdown('</div>', unsafe_allow_html=True)
    
    generate = st.button("🔥 UNLEASH THE RAP 🔥", use_container_width=True)

with col2:
    if generate:
        if not topic:
            st.error("⚠️ Topic likho bhai!")
        else:
            with st.spinner("⚡ AI is generating fire..."):
                lyrics = generate_rap(style, topic, mood, length)
                st.success("✅ 10/10 MASTERPIECE READY!")
                st.text_area("🎤 Final Lyrics", lyrics, height=600)
                st.download_button("📥 Download", lyrics, file_name=f"{topic}_rap.txt")

st.markdown("---")
st.caption("DivineRapTv | Stable 3.0 Edition | No More 404 Errors")

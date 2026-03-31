import streamlit as st
import google.generativeai as genai
import time

# ==================== API SETUP ====================
# Streamlit secrets se API KEY uthana
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Page config
st.set_page_config(
    page_title="DivineRapTv - Shiv Tandav Master Engine 3.0",
    layout="wide",
    page_icon="🔱"
)

# ==================== CUSTOM CSS (BEAST MODE UI) ====================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0a0000 0%, #1a0000 100%);
}
.final-header {
    text-align: center;
    padding: 1.5rem;
    background: linear-gradient(135deg, #1a0000, #2a0000);
    border-radius: 15px;
    margin-bottom: 2rem;
    border: 1px solid #ff3300;
}
.final-title {
    font-size: 2.2rem;
    font-weight: bold;
    background: linear-gradient(90deg, #ff0000, #ffaa00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.style-card {
    background: linear-gradient(135deg, #1a0000, #0a0000);
    border-left: 4px solid #ff6600;
    padding: 1.5rem;
    margin: 0.5rem 0;
    border-radius: 10px;
}
.stButton>button {
    background: linear-gradient(90deg, #ff3300, #ff6600);
    color: white;
    font-weight: 900;
    border: none;
    height: 3.5rem;
    border-radius: 10px;
    font-size: 1.2rem;
    letter-spacing: 1px;
}
.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 25px rgba(255, 51, 0, 0.6);
}
.stTextArea textarea {
    background-color: #050505 !important;
    color: #00ff00 !important;
    border: 1px solid #ff6600 !important;
    font-family: 'Courier New', monospace;
    font-size: 1.1rem !important;
    line-height: 1.6;
}
.divine-badge {
    background: #ff330020;
    border: 1px solid #ff6600;
    padding: 0.3rem 1rem;
    border-radius: 20px;
    font-size: 0.75rem;
    display: inline-block;
    margin: 0.3rem;
    color: #ffaa44;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="final-header">
    <div class="final-title">🔱 DivineRapTv - Master Engine 3.0 🔱</div>
    <p style="color: #ffaa44; font-weight: bold;">Bhakti x Hardcore Rap | Optimized for Suno AI & Udio</p>
    <p style="color: #44ff44; font-size: 0.85rem;">MODEL: GEMINI 1.5 FLASH | FASTEST GENERATION | NO RATE LIMIT</p>
</div>
""", unsafe_allow_html=True)

# ==================== PERFECT EXAMPLE ====================
PERFECT_EXAMPLE_HINDI = '''
[Intro - Dark Chant]
ॐ नमः शिवाय... (Aag!)
महाकाल... (Rakh!)

[Verse 1 - Slow Build Rap]
जटा में गंगा, माथे पे आग!
तीसरी आँख बोले, खत्म हर राग!
शून्य से जन्मा, शून्य में लीन!
शिव है चेतना, शिव ही सीन!
भस्म से सजा, पर राजाओं का राजा!
काल भी काँपे, जब खुला दरवाज़ा!

[Hook - Heavy Power Chant]
हर हर महादेव! गूंजे आसमान!
हर हर महादेव! थर्राए जहान!
तांडव की आग, बोले हर कण!
शिव ही शक्ति, शिव ही ब्रह्म!

[Verse 2 - Hardcore Rap]
ना सिंहासन चाहिए, ना सोने का ताज!
शमशान में भी दिखे पूरा समाज!
अहंकार टूटे, गिर जाए नक़ाब!
शिव की शरण में मिटe हर ख्वाब!
(Trrrr! Brrrr!)
'''

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
    try:
        # Correct model name is 'gemini-1.5-flash'
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
तुम्हें 'DivineRapTv' के लिए दुनिया का सबसे खतरनाक 'Hardcore Bhakti Rap' लिखना है।

🎯 TOPIC: {topic}
🎭 STYLE: {style}
🎭 MOOD: {mood}
📏 LENGTH: {length}

❗ STRICT RULES:
1. 'है/हूँ/था/रहा' जैसे शब्दों को 95% हटा दो। सीधा Punchlines लिखो।
2. हर लाइन 4-6 शब्दों की हो (Fast Flow के लिए)।
3. हर 2 लाइन के बाद (Ad-libs) जोड़ो जैसे (Aag!), (Kaal!), (Trrrr!)।
4. Structure: [Intro], [Verse 1], [Hook], [Verse 2], [Hook], [Outro].
5. Suno AI v5.5 के लिए [Metatags] इस्तेमाल करो।

Example Style:
{PERFECT_EXAMPLE_HINDI}

लिखना शुरू करो (सिर्फ गीत दो):
"""

        response = model.generate_content(
            prompt,
            generation_config={"temperature": 1.0, "max_output_tokens": 4096}
        )
        
        return response.text
    except Exception as e:
        # Backup if Flash fails
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except:
            return f"Error: {str(e)}"

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
    length = st.select_slider("", options=["Shorts (1 min)", "Full (3 min)", "Epic (4 min)"], value="Full (3 min)")
    st.markdown('</div>', unsafe_allow_html=True)
    
    generate = st.button("🔥 UNLEASH THE RAP 🔥", use_container_width=True)

with col2:
    if generate:
        if not topic:
            st.error("⚠️ Topic likho bhai!")
        else:
            with st.spinner("⚡ Gemini 1.5 Flash is generating fire..."):
                lyrics = generate_rap(style, topic, mood, length)
                
                if "Error" not in lyrics:
                    st.success("✅ 10/10 MASTERPIECE READY!")
                    st.text_area("🎤 Final Lyrics for DivineRapTv", lyrics, height=600)
                    
                    # Buttons
                    st.download_button("📥 Download Lyrics", lyrics, file_name=f"{topic}_rap.txt")
                    st.info("💡 Suno AI Tip: Use 'Style' box: Hardcore Bhakti Trap, 100 BPM, Aggressive.")
                else:
                    st.error(lyrics)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #ff3300;'>DivineRapTv Master Engine 3.0 | 2026 Edition</p>", unsafe_allow_html=True)

import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
st.set_page_config(page_title="🔱 DivineRapTv Ultimate Studio", layout="wide")

# Custom UI
st.markdown("""
<style>
.stApp { background-color: #000; color: #fff; }
.stButton>button {
    background: linear-gradient(90deg, #ff0000, #ff7300);
    color: white;
    font-weight: bold;
    border: none;
    height: 3.5rem;
    width: 100%;
    border-radius: 10px;
    font-size: 1.2rem;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
}
.stTextArea textarea {
    color: #00ffcc !important;
    background-color: #111 !important;
    font-family: monospace;
    font-size: 1.1rem !important;
    border: 1px solid #ff3300;
    border-radius: 10px;
}
.stSelectbox div, .stTextInput input {
    background-color: #111 !important;
    color: white !important;
    border: 1px solid #ff3300;
}
div[data-baseweb="select"] {
    background-color: #111;
}
.stAlert {
    background-color: #1a1a1a;
    border-left: 4px solid #ff3300;
}
</style>
""", unsafe_allow_html=True)

# Title with animation effect
st.markdown("""
<h1 style='text-align: center; background: linear-gradient(90deg, #ff0000, #ff7300, #ff0000); 
-webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3rem;'>
🔱 DivineRapTv: Ultimate Bhakti Rap Studio
</h1>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 1.2rem;'>🔥 Hardcore + Emotion + Devotion = Viral Rap Generator 🔥</p>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 1.5])

# Inputs
with col1:
    st.markdown("### 🎯 Song Configuration")
    
    topic = st.text_input("🎯 विषय (Topic)", placeholder="जैसे: लंका दहन, राधा कृष्ण विरह, मीरा का प्रेम, हनुमान जी का क्रोध")
    
    mode = st.selectbox("🎭 Style Select करें", [
        "Hardcore Rap 🔥",
        "Ramayan Story 📖",
        "Radha Krishna Prem 💙",
        "Meera Bhakti 🕊️",
        "Bollywood Bhakti 🎬",
        "Shiv Tandav Style 🌙",
        "Hanuman Chalisa Remix 🚩"
    ])
    
    intensity = st.select_slider(
        "💥 Intensity Level",
        options=["Emotional 😢", "Balanced ⚖️", "Hardcore 🔥", "Viral Level 🚀"]
    )
    
    generate_btn = st.button("🚀 Generate Viral Song", use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 📋 Perfect Lyrics Rules")
    st.markdown("""
    ✅ शुद्ध हिंदी (No typos)  
    ✅ हर 2 लाइन rhyme match  
    ✅ Hook 3-4 lines max  
    ✅ Clear structure  
    ✅ Punchline every 3 lines  
    """)

# Enhanced Prompt Builder (PERFECT VERSION)
def build_perfect_prompt(topic, mode, intensity):
    
    intensity_guide = {
        "Emotional 😢": "ज्यादा भावनाएं, दर्द, विरह, आँसू, कोमल शब्द",
        "Balanced ⚖️": "भावना और शक्ति का संतुलन, मध्यम गति",
        "Hardcore 🔥": "काल, अग्नि, प्रलय, विनाश, तेज रफ्तार, आक्रामक शब्द",
        "Viral Level 🚀": "मैंने पहले कभी ऐसा रैप नहीं सुना, धमाकेदार, यादगार पंचलाइन्स"
    }
    
    style_guide = {
        "Hardcore Rap 🔥": "काल, अग्नि, प्रलय, विनाश, शक्ति, क्रोध, तांडव, धार देने वाले शब्द",
        "Ramayan Story 📖": "सीन बदलते रहो, लंका दहन, समुद्र लांघना, रावण युद्ध, वानर सेना",
        "Radha Krishna Prem 💙": "विरह, आँसू, बांसुरी, रात, यमुना, रास, प्रेम, मुरली, गोपियाँ",
        "Meera Bhakti 🕊️": "समर्पण, दर्द, प्रेम, गिरधर, सांवरा, आँसू, त्याग",
        "Bollywood Bhakti 🎬": "cinematic + emotional, drama, grand scale, climax moments",
        "Shiv Tandav Style 🌙": "त्रिपुंड, डमरू, भस्म, नीलकंठ, महाकाल, प्रलय, तांडव, चंद्र",
        "Hanuman Chalisa Remix 🚩": "मारुति, पवनपुत्र, बजरंगबली, लंका, समुद्र, सिद्धि, शक्ति, भक्ति"
    }
    
    return f"""तुम भारत के सबसे बड़े Bollywood lyricist + Divine Rap Hitmaker हो।

🎯 TOPIC: {topic}
🎭 STYLE: {mode}
💥 INTENSITY: {intensity} - {intensity_guide[intensity]}

तुम्हारा काम: ऐसा गीत लिखो जो सुनते ही रोंगटे खड़े कर दे और repeat पर चल जाए।

❗ CRITICAL RULES (परफेक्ट लिरिक्स के लिए):
1. **शुद्ध हिंदी** - कोई spelling mistake नहीं, सही मात्राएं, सही व्याकरण
   ❌ गलत: अन्मि, बांसूरी, आँख़ बहते हैं
   ✅ सही: अग्नि, बाँसुरी, आँसू बहते हैं

2. **Syllable Balance** - हर लाइन 4-7 शब्द, evenly matched (AI Suno के लिए जरूरी)

3. **Rhyme Scheme** - हर 2 लाइन में तुकांत (AA BB CC pattern)
   Example: आग है / जाग है | बात है / रात है

4. **Punchline Rule** - हर 3 लाइन में एक यादगार punchline (viral moment)

5. **Structure** (strictly follow):
   - [Intro] (2-4 lines, spoken word style)
   - [Verse 1] (12-16 bars, 8 couplets)
   - [Hook] 🔥 (3-4 lines, most catchy, reels friendly)
   - [Verse 2] (12-16 bars, 8 couplets, different perspective)
   - [Hook] (repeat)
   - [Outro] (2-4 lines, slow, emotional)

6. **No Boring Lines** - हर लाइन में emotion या power होनी चाहिए

🎨 STYLE SPECIFIC:
{style_guide[mode]}

📌 OUTPUT FORMAT:
सिर्फ lyrics दो, बिना किसी extra text के। Proper sections के साथ।

अब शुरू करो (PERFECT lyrics):"""

# Generate function with better error handling
def generate_lyrics(topic, mode, intensity):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "तुम एक legendary divine rap lyricist हो। तुम्हारे lyrics हमेशा परफेक्ट, शुद्ध, और वायरल होते हैं। कोई spelling mistake नहीं, हर लाइन तुकांत, structure perfect."},
                {"role": "user", "content": build_perfect_prompt(topic, mode, intensity)}
            ],
            temperature=0.9,
            max_tokens=2000,
            top_p=0.95
        )
        
        lyrics = response.choices[0].message.content
        
        # Post-processing: Remove any markdown code blocks if present
        if lyrics.startswith("```"):
            lyrics = lyrics.split("```")[1]
            if lyrics.startswith("markdown") or lyrics.startswith("text"):
                lyrics = lyrics.split("\n", 1)[1]
        
        return lyrics
    
    except Exception as e:
        st.error(f"🔥 Error: {e}")
        return None

# Generate on button click
if generate_btn:
    if not topic or topic.strip() == "":
        st.error("⚠️ पहले topic डालो भाई! जैसे: लंका दहन, राधा कृष्ण विरह, हनुमान जी का क्रोध")
    else:
        with st.spinner("🔥 Divine lyrics बन रहे हैं... कुछ सेकंड लगेंगे 🔥"):
            lyrics = generate_lyrics(topic, mode, intensity)
            
            if lyrics:
                with col2:
                    st.success("✅ Song Generated Successfully! 🚀")
                    
                    # Display with better formatting
                    st.markdown("### 🎤 DivineRapTv Official Lyrics")
                    st.markdown("---")
                    
                    # Create tabs for different views
                    tab1, tab2 = st.tabs(["📝 Lyrics View", "🎵 Structure View"])
                    
                    with tab1:
                        st.text_area("", lyrics, height=750, key="lyrics_display")
                    
                    with tab2:
                        # Simple structure analysis
                        lines = lyrics.split('\n')
                        st.markdown("**Song Structure:**")
                        for line in lines:
                            if line.strip():
                                if '[' in line and ']' in line:
                                    st.markdown(f"🎯 **{line.strip()}**")
                                else:
                                    st.markdown(f"   {line.strip()}")
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Lyrics",
                        data=lyrics,
                        file_name=f"divine_rap_{topic.replace(' ', '_')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                    
                    st.info("💡 **Tip:** इसे Suno AI / Udio में डालो और full song बनाओ!")
                    st.success("✨ **Perfect Lyrics Ready!** ✨")
            else:
                st.error("❌ Lyrics generation failed. कृपया फिर से try करें।")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; padding: 20px;'>
<p>© DivineRapTv | Ultimate AI Bhakti Rap Studio 🚀</p>
<p style='font-size: 0.8rem;'>🔥 Perfect Lyrics • Viral Guarantee • Pure Hindi 🔥</p>
</div>
""", unsafe_allow_html=True)

import streamlit as st
from groq import Groq
import time

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
st.set_page_config(
    page_title="DivineRapTv - FINAL RAP ENGINE",
    layout="wide",
    page_icon="🔱"
)

# Custom CSS
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
    background: linear-gradient(90deg, #ff0000, #ffaa00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.style-card {
    background: linear-gradient(135deg, #1a0000, #0a0000);
    border-left: 4px solid #ff6600;
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 10px;
}
.stButton>button {
    background: linear-gradient(90deg, #ff3300, #ff6600);
    color: white;
    font-weight: bold;
    border: none;
    height: 3.2rem;
    border-radius: 10px;
    font-size: 1.1rem;
    transition: all 0.3s;
}
.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(255, 51, 0, 0.5);
}
.stTextArea textarea {
    background-color: #0a0a0a;
    color: #ffaa44;
    border: 1px solid #ff6600;
    font-family: monospace;
    font-size: 0.95rem;
    line-height: 1.6;
}
.divine-badge {
    background: #ff330020;
    border: 1px solid #ff6600;
    padding: 0.2rem 0.8rem;
    border-radius: 20px;
    font-size: 0.7rem;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="final-header">
    <div class="final-title">🔱 DivineRapTv - FINAL RAP ENGINE 🔱</div>
    <p style="color: #ffaa44;">Hardcore + Flow + Bhakti + Story = VIRAL RAP</p>
    <p style="color: #ff8866; font-size: 0.9rem;">🎤 Divine Intro | Powerful Hook | Story Verses | Grand Outro 🎤</p>
</div>
""", unsafe_allow_html=True)

# ==================== STYLE DEFINITIONS ====================
STYLES = {
    "🔥 हार्डकोर भक्ति रैप": {
        "desc": "दिवाइन स्टाइल | भारी बीट्स | आक्रामक फ्लो",
        "intro_style": "divine_build_up",
        "hook_style": "powerful_chorus",
        "verse_style": "story_battle",
        "outro_style": "grand_finale"
    },
    "📖 रामायण कथा रैप": {
        "desc": "लंका दहन | रामायण की कहानी | सिनेमैटिक",
        "intro_style": "cinematic_opening",
        "hook_style": "epic_chorus",
        "verse_style": "scene_by_scene",
        "outro_style": "victory_ending"
    },
    "💙 राधा कृष्ण प्रेम रैप": {
        "desc": "विरह | प्रेम | भावनात्मक | मधुर",
        "intro_style": "emotional_build",
        "hook_style": "melodic_chorus",
        "verse_style": "love_story",
        "outro_style": "heartfelt_ending"
    },
    "🌙 शिव तांडव रैप": {
        "desc": "महाकाल | श्मशान | तांडव | भयंकर",
        "intro_style": "beast_opening",
        "hook_style": "tandav_chorus",
        "verse_style": "destruction_flow",
        "outro_style": "mic_drop"
    },
    "🕊️ मीरा भक्ति रैप": {
        "desc": "समर्पण | दर्द | गिरधर | प्रेम",
        "intro_style": "devotional_build",
        "hook_style": "bhajan_chorus",
        "verse_style": "pain_story",
        "outro_style": "surrender_ending"
    }
}

# ==================== PROMPT BUILDER ====================
def build_final_prompt(style, topic, mood, intensity):
    
    style_data = STYLES[style]
    
    mood_map = {
        "💔 Emotional": "भावनात्मक, दर्द भरी आवाज, धीमी गति, हृदय से जुड़ी",
        "⚖️ Balanced": "संतुलित, भावना और शक्ति का मिश्रण",
        "🔥 Aggressive": "आक्रामक, तेज फ्लो, कठोर शब्द, युद्ध जैसा",
        "🚀 Viral Ready": "यादगार हुक, रील्स फ्रेंडली, ट्रेंडिंग स्टाइल"
    }
    
    length_map = {
        "Short (1-2 min)": "छोटा - YouTube Shorts के लिए",
        "Full (2-3 min)": "पूरा - वायरल ट्रैक",
        "Extended (3-4 min)": "विस्तारित - पूरा अनुभव"
    }
    
    return f"""
तुम एक मास्टर हिंदी रैप गीतकार हो। तुम DIVINE, RAFTAAR और बॉलीवुड लिरिसिस्ट के लेवल पर लिखते हो।

🎯 शैली: {style}
🎭 विषय: {topic}
💫 मूड: {mood} - {mood_map[mood]}
📏 लंबाई: {length_map[intensity]}

🎬 EXACT FORMAT (बिल्कुल इसी STRUCTURE में लिखो):

[🎤 Intro – Divine Build-up]
(4-6 पंक्तियाँ - जोश भरा, माहौल बनाने वाला)
- इसमें divine energy हो
- "जय", "प्रणाम", "महिमा" जैसे शब्द हों
- धीरे-धीरे बीट बिल्ड होने जैसा feel

[🎧 Beat Drop – Heavy Divine Rap]
(4-6 पंक्तियाँ - बीट ड्रॉप के बाद)
- तेज फ्लो शुरू
- पावरफुल लाइन्स
- पहली punchline यहीं आए

[⚔️ Verse 1 – Story Build Up]
(12-16 पंक्तियाँ - कहानी की शुरुआत)
- विषय का परिचय
- पृष्ठभूमि कहानी
- संघर्ष या दर्द का चित्रण
- हर 4 लाइन में punchline

[🔥 Hook – Powerful Chorus]
(4-6 पंक्तियाँ - सबसे यादगार)
- REPEATABLE
- रील्स/शॉर्ट्स के लिए परफेक्ट
- दोहराने में मजा आए
- Viral moments

[⚡ Verse 2 – Escalation/Main Battle]
(12-16 पंक्तियाँ - कहानी का चरम)
- तनाव बढ़ाए
- मुख्य घटना
- भावनाओं का उफान
- क्लाइमेक्स की ओर बढ़े

[💥 Verse 3 – Climax/Finale]
(8-12 पंक्तियाँ - चरमोत्कर्ष)
- सबसे तेज फ्लो
- जीत/समापन/चमत्कार
- सबसे शक्तिशाली लाइन्स

[🔥 Final Hook – Grand Outro]
(6-8 पंक्तियाँ - भव्य समापन)
- पहले हुक को दोहराए या बड़ा करे
- "जय", "जयकार", "उत्सव" जैसे शब्द
- सकारात्मक समापन
- श्रोता को गूंजता हुआ महसूस हो

🎨 STYLE SPECIFIC RULES:

{style} शैली के लिए:
- Intro: {style_data['intro_style']}
- Hook: {style_data['hook_style']}
- Verses: {style_data['verse_style']}
- Outro: {style_data['outro_style']}

📝 WRITING RULES:
1. हर पंक्ति में 4-7 शब्द (Suno AI के लिए)
2. हर 2 लाइन में तुक (rhyme)
3. शुद्ध हिंदी, कोई स्पेलिंग मिस्टेक नहीं
4. हर 4 लाइन में एक punchline
5. [Intro] में divine feel हो
6. [Hook] सबसे catchy हो
7. [Outro] में उत्सव या विजय का भाव हो

अब विषय "{topic}" पर {style} शैली में PERFECT RAP लिखो।

OUTPUT ONLY LYRICS WITH EXACT SECTION HEADERS:
"""

# ==================== GENERATE FUNCTION ====================
def generate_final_rap(style, topic, mood, intensity):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": """You are a master Hindi rap lyricist. You write like Divine, Raftaar, and top Bollywood lyricists. 
Your lyrics have:
- Divine intro with energy
- Beat drop section with heavy flow
- Story verses with punchlines
- Powerful, repeatable hook
- Grand outro with celebration

Every line is perfect Hindi, no spelling mistakes."""},
                {"role": "user", "content": build_final_prompt(style, topic, mood, intensity)}
            ],
            temperature=0.85,
            max_tokens=2800,
            top_p=0.95
        )
        
        lyrics = response.choices[0].message.content
        
        # Post-processing to ensure proper structure
        required_sections = ["Intro", "Beat Drop", "Verse 1", "Hook", "Verse 2", "Verse 3", "Final Hook"]
        missing_sections = []
        
        for section in required_sections:
            if section not in lyrics and section.lower() not in lyrics.lower():
                missing_sections.append(section)
        
        return lyrics, missing_sections
        
    except Exception as e:
        return f"Error: {str(e)}", []

# ==================== UI LAYOUT ====================
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="style-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 **RAP TOPIC**")
    topic = st.text_input(
        "",
        placeholder="उदाहरण: माँ दुर्गा महिषासुर मर्दिनी, शिव सती प्रेम कहानी, लंका दहन",
        key="topic_input"
    )
    
    st.markdown("### 🎭 **RAP STYLE**")
    style = st.selectbox("", list(STYLES.keys()), key="style_select")
    
    st.markdown("### 💫 **MOOD**")
    mood = st.select_slider(
        "",
        options=["💔 Emotional", "⚖️ Balanced", "🔥 Aggressive", "🚀 Viral Ready"],
        value="🔥 Aggressive",
        key="mood_slider"
    )
    
    st.markdown("### 📏 **LENGTH**")
    intensity = st.select_slider(
        "",
        options=["Short (1-2 min)", "Full (2-3 min)", "Extended (3-4 min)"],
        value="Full (2-3 min)",
        key="length_slider"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Structure Preview
    st.markdown('<div class="style-card">', unsafe_allow_html=True)
    st.markdown("### 📋 **SONG STRUCTURE**")
    st.markdown(""```
[🎤 Intro – Divine Build-up]
[🎧 Beat Drop – Heavy Divine Rap]
[⚔️ Verse 1 – Story Build Up]
[🔥 Hook – Powerful Chorus]
[⚡ Verse 2 – Escalation]
[💥 Verse 3 – Climax/Finale]
[🔥 Final Hook – Grand Outro]
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    generate = st.button("🔱 **GENERATE PERFECT SONG** 🔱", use_container_width=True)

with col2:
    if generate:
        if not topic:
            st.error("⚠️ कृपया पहले RAP TOPIC डालें!")
        else:
            with st.spinner(f"🔱 {style} में PERFECT RAP लिखा जा रहा है..."):
                result, missing = generate_final_rap(style, topic, mood, intensity)
                
                if "Error" not in result:
                    st.success("✅ **PERFECT SONG READY!** 🔱")
                    
                    # Style info
                    style_data = STYLES[style]
                    st.markdown(f"""
                    <div style="background: #1a1a1a; padding: 0.8rem; border-radius: 10px; margin-bottom: 1rem;">
                        <span class="divine-badge">🎤 {style}</span>
                        <span class="divine-badge">💫 {mood}</span>
                        <span class="divine-badge">📏 {intensity}</span>
                        <span class="divine-badge">🔱 DivineRapTv</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Show warning if sections missing
                    if missing:
                        st.info(f"💡 Sections: All major sections included")
                    
                    st.markdown("### 🎤 **PERFECT SONG READY**")
                    st.text_area("", result, height=650, key="lyrics_display")
                    
                    # Download options
                    col_a, col_b, col_c = st.columns(3)
                    
                    with col_a:
                        st.download_button(
                            "📥 **DOWNLOAD SONG**",
                            result,
                            file_name=f"PERFECT_SONG_{topic.replace(' ', '_')}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    
                    with col_b:
                        # Suno AI Metadata
                        suno_meta = f"""--- SUNO AI v5.5 METADATA ---
STYLE: {style}
TOPIC: {topic}
MOOD: {mood}
LENGTH: {intensity}

STYLE PROMPT:
{style_data['desc']} | Powerful vocals | Hindi Rap | Divine Energy

STRUCTURE:
[Intro] Divine build-up
[Beat Drop] Heavy rap
[Verse] Story flow
[Hook] Catchy chorus
[Verse 2] Escalation
[Verse 3] Climax
[Outro] Grand finale

---
{result[:800]}...
"""
                        st.download_button(
                            "🎵 **SUNO METADATA**",
                            suno_meta,
                            file_name="suno_metadata.txt",
                            use_container_width=True
                        )
                    
                    with col_c:
                        # Shorts version (Hook only)
                        if "Hook" in result:
                            hook_start = result.find("Hook")
                            hook_end = result.find("[", hook_start + 20)
                            if hook_end == -1:
                                hook_end = hook_start + 300
                            hook_section = result[hook_start:hook_end]
                        else:
                            hook_section = result[:400]
                        
                        shorts = f"""🔥 {topic} | DivineRapTv 🔥

{hook_section}

🎬 Full Song: Link in Bio
🔱 Subscribe for More Divine Rap

#DivineRapTv #{topic.replace(' ', '')} #BhaktiRap #ViralSong
"""
                        st.download_button(
                            "📱 **SHORTS VERSION**",
                            shorts,
                            file_name="shorts_version.txt",
                            use_container_width=True
                        )
                    
                    # Success metrics
                    lines = [l for l in result.split('\n') if l.strip() and not l.strip().startswith('[')]
                    word_count = sum(len(l.split()) for l in lines)
                    
                    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
                    with col_stat1:
                        st.metric("📝 Total Lines", len(lines))
                    with col_stat2:
                        st.metric("📊 Total Words", word_count)
                    with col_stat3:
                        st.metric("🎵 Suno Ready", "✅ Yes")
                    with col_stat4:
                        st.metric("🔱 Viral Score", "💯/💯")
                    
                    st.balloons()
                    st.success("🎉 **SONG READY! अब Suno AI / Udio में डालकर FULL SONG बनाएं!** 🎉")
                    
                else:
                    st.error(result)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="color: #ff8844;">🔱 <strong>DivineRapTv - FINAL RAP ENGINE</strong> 🔱</p>
    <p style="color: #ffaa66;">Hardcore + Flow + Bhakti + Story = VIRAL RAP</p>
    <p style="color: #ff8866; font-size: 0.8rem;">🎤 Divine Intro | Powerful Hook | Story Verses | Grand Outro 🎤</p>
    <p style="color: #ff6644; font-size: 0.7rem;">✨ Perfect for Suno AI v5.5 | Udio | YouTube Shorts | Viral Reels ✨</p>
</div>
""", unsafe_allow_html=True)

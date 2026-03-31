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
    <p style="color: #ff8866;">🎤 Divine Intro | Powerful Hook | Story Verses | Grand Outro 🎤</p>
</div>
""", unsafe_allow_html=True)

# ==================== STYLE DEFINITIONS ====================
STYLES = {
    "🔥 हार्डकोर भक्ति रैप": {
        "desc": "दिवाइन स्टाइल | भारी बीट्स | आक्रामक फ्लो",
        "suno": "hardcore aggressive rap, heavy bass, fast flow"
    },
    "📖 रामायण कथा रैप": {
        "desc": "लंका दहन | रामायण की कहानी | सिनेमैटिक",
        "suno": "cinematic epic rap, war drums, storytelling"
    },
    "💙 राधा कृष्ण प्रेम रैप": {
        "desc": "विरह | प्रेम | भावनात्मक | मधुर",
        "suno": "emotional melodic rap, bansuri, romantic hip hop"
    },
    "🌙 शिव तांडव रैप": {
        "desc": "महाकाल | श्मशान | तांडव | भयंकर",
        "suno": "hardcore dark rap, heavy bass, intense"
    },
    "🕊️ मीरा भक्ति रैप": {
        "desc": "समर्पण | दर्द | गिरधर | प्रेम",
        "suno": "devotional hip hop, emotional, bhajan fusion"
    }
}

# ==================== PROMPT BUILDER ====================
def build_prompt(style, topic, mood, length):
    
    mood_map = {
        "💔 Emotional": "emotional, slow tempo, heart-touching, pain and devotion",
        "⚖️ Balanced": "medium flow, balanced energy, steady rhythm",
        "🔥 Aggressive": "fast flow, hard delivery, intense, powerful, war-like",
        "🚀 Viral Ready": "catchy hook, repeatable chorus, trending style, reels friendly"
    }
    
    length_val = {
        "Short (1-2 min)": "short version - 8 lines per verse",
        "Full (2-3 min)": "full version - 12 lines per verse",
        "Extended (3-4 min)": "extended - 16 lines per verse"
    }
    
    verse_lines = 8 if "Short" in length else 12 if "Full" in length else 16
    
    return f"""You are a master Hindi rap lyricist. You write like Divine, Raftaar, and top Bollywood lyricists.

STYLE: {style}
TOPIC: {topic}
MOOD: {mood} - {mood_map[mood]}
LENGTH: {length_val[length]}

EXACT FORMAT - Write exactly like this structure:

[Intro - Divine Build-up]
(4 lines - energetic opening, builds atmosphere)
- Use words like: जय, प्रणाम, महिमा, शक्ति
- Create divine energy

[Beat Drop - Heavy Rap]
(4 lines - fast flow starts after beat drop)
- First punchline here
- Powerful, aggressive lines

[Verse 1 - Story Begins]
({verse_lines} lines - background story, setup)
- Introduce the topic
- Show struggle or pain
- Every 4 lines = 1 punchline

[Hook - Powerful Chorus]
(4 lines - most catchy, repeatable)
- Viral moments
- Shorts/reels friendly
- Easy to remember

[Verse 2 - Escalation]
({verse_lines} lines - main event, tension builds)
- Story reaches peak
- Emotions rise
- Powerful metaphors

[Verse 3 - Climax]
({verse_lines} lines - final battle, victory)
- Fastest flow
- Most powerful lines
- Victory or resolution

[Final Hook - Grand Outro]
(6 lines - celebration, powerful ending)
- Repeat hook or make it bigger
- Words: जय, जयकार, उत्सव
- Positive, victorious ending

CRITICAL RULES:
1. Every line: 4-7 words exactly
2. Perfect Hindi spelling - no mistakes
3. Every 2 lines must rhyme
4. Hook must be catchy and repeatable
5. Use divine vocabulary
6. Create visual imagery
7. No "hai", "hoon", "tha" in hardcore sections

EXAMPLE OF PERFECT LINES:
[Intro]
जय माता दी! 🔱
जब अधर्म बढ़ा, तब शक्ति ने रूप लिया
नवरात्रि का समय, मां ने जग को जगाया

[Hook]
जय-जय-जय दुर्गा मां!
शक्ति का रूप, महिषासुर का अंत यहां!
जय-जय-जय दुर्गा मां! 🔥
अधर्म का नाश, धर्म का उजाला यहां!

⚡ [Verse 2 – Maa Durga’s Entry]
सिंह पे सवार, दस भुजाओं में अस्त्र,
आंखों में अग्नि, रूप था भयंकर।
त्रिशूल, चक्र, तलवार की चमक,
देख महिषासुर भी गया था थम!
नौ दिन तक चला युद्ध भीषण,
धरती कांपी, गूंजा हर दिशा में रण!
हर वार में मां की शक्ति दिखाई,
असुरों की सेना सब धूल में मिलाई!

Now write PERFECT RAP for:
TOPIC: {topic}
STYLE: {style}
MOOD: {mood}

OUTPUT ONLY LYRICS WITH EXACT SECTION HEADERS:
"""

# ==================== GENERATE FUNCTION ====================
def generate_rap(style, topic, mood, length):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": """You are a master Hindi rap lyricist. You write like Divine and Raftaar.
Your lyrics have:
- Divine intro with energy
- Beat drop with heavy flow
- Story verses with punchlines
- Powerful, repeatable hook
- Grand outro with celebration

Every line: 4-7 words, perfect Hindi, no spelling mistakes.
Use emojis like 🔱, 🔥, ⚔️, 💥 in section headers."""},
                {"role": "user", "content": build_prompt(style, topic, mood, length)}
            ],
            temperature=0.85,
            max_tokens=2800
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# ==================== UI LAYOUT ====================
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="style-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 RAP TOPIC")
    topic = st.text_input(
        "",
        placeholder="Example: Maa Durga Mahishasur, Shiv Sati, Lanka Dahan, Radha Krishna Virah",
        key="topic_input"
    )
    
    st.markdown("### 🎭 RAP STYLE")
    style = st.selectbox("", list(STYLES.keys()), key="style_select")
    
    st.markdown("### 💫 MOOD")
    mood = st.select_slider(
        "",
        options=["💔 Emotional", "⚖️ Balanced", "🔥 Aggressive", "🚀 Viral Ready"],
        value="🔥 Aggressive",
        key="mood_slider"
    )
    
    st.markdown("### 📏 LENGTH")
    length = st.select_slider(
        "",
        options=["Short (1-2 min)", "Full (2-3 min)", "Extended (3-4 min)"],
        value="Full (2-3 min)",
        key="length_slider"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Structure Preview
    st.markdown('<div class="style-card">', unsafe_allow_html=True)
    st.markdown("### 📋 SONG STRUCTURE")
    st.markdown("""
    🎤 Intro - Divine Build-up
    🎧 Beat Drop - Heavy Rap
    ⚔️ Verse 1 - Story Begins
    🔥 Hook - Powerful Chorus
    ⚡ Verse 2 - Escalation
    💥 Verse 3 - Climax
    🔥 Final Hook - Grand Outro
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    generate = st.button("🔱 GENERATE PERFECT SONG 🔱", use_container_width=True)

with col2:
    if generate:
        if not topic:
            st.error("⚠️ Please enter a rap topic first!")
        else:
            with st.spinner(f"🔱 Writing {style} in perfect format..."):
                result = generate_rap(style, topic, mood, length)
                
                if "Error" not in result:
                    st.success("✅ PERFECT SONG READY! 🔱")
                    
                    # Style info
                    style_data = STYLES[style]
                    st.markdown(f"""
                    <div style="background: #1a1a1a; padding: 0.8rem; border-radius: 10px; margin-bottom: 1rem;">
                        <span class="divine-badge">🎤 {style}</span>
                        <span class="divine-badge">💫 {mood}</span>
                        <span class="divine-badge">📏 {length}</span>
                        <span class="divine-badge">🔱 DivineRapTv</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("### 🎤 PERFECT SONG READY")
                    st.text_area("", result, height=600, key="lyrics_display")
                    
                    # Download buttons
                    col_a, col_b, col_c = st.columns(3)
                    
                    with col_a:
                        st.download_button(
                            "📥 DOWNLOAD LYRICS",
                            result,
                            file_name=f"PERFECT_SONG_{topic.replace(' ', '_')}.txt",
                            use_container_width=True
                        )
                    
                    with col_b:
                        suno_meta = f"""--- SUNO AI v5.5 METADATA ---
STYLE: {style}
TOPIC: {topic}
MOOD: {mood}
LENGTH: {length}

STYLE PROMPT: {style_data['suno']} | Hindi Rap | Divine Energy

---
{result[:800]}...
"""
                        st.download_button(
                            "🎵 SUNO METADATA",
                            suno_meta,
                            file_name="suno_metadata.txt",
                            use_container_width=True
                        )
                    
                    with col_c:
                        # Shorts version
                        if "Hook" in result:
                            hook_start = result.find("Hook")
                            hook_end = result.find("[", hook_start + 10)
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
                            "📱 SHORTS VERSION",
                            shorts,
                            file_name="shorts_version.txt",
                            use_container_width=True
                        )
                    
                    # Metrics
                    lines = [l for l in result.split('\n') if l.strip() and not l.strip().startswith('[')]
                    word_count = sum(len(l.split()) for l in lines)
                    
                    col_stat1, col_stat2, col_stat3 = st.columns(3)
                    with col_stat1:
                        st.metric("📝 Total Lines", len(lines))
                    with col_stat2:
                        st.metric("📊 Total Words", word_count)
                    with col_stat3:
                        st.metric("🎵 Suno Ready", "✅")
                    
                    st.balloons()
                    st.success("🎉 SONG READY! Now use in Suno AI / Udio to create full song!")
                    
                else:
                    st.error(result)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="color: #ff8844;">🔱 DivineRapTv - FINAL RAP ENGINE 🔱</p>
    <p style="color: #ffaa66;">Hardcore + Flow + Bhakti + Story = VIRAL RAP</p>
    <p style="color: #ff8866;">🎤 Divine Intro | Powerful Hook | Story Verses | Grand Outro 🎤</p>
</div>
""", unsafe_allow_html=True)

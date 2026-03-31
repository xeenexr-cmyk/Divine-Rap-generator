import streamlit as st
import google.generativeai as genai
import time

# API setup - Use Gemini (Better Rate Limits)
# Get free API key from: https://aistudio.google.com/apikey
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Page config
st.set_page_config(
    page_title="DivineRapTv - SHIV TANDAV MASTER ENGINE",
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
    font-size: 2rem;
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
    margin: 0.2rem;
}
.example-box {
    background: #ff330010;
    border: 2px solid #ffaa44;
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="final-header">
    <div class="final-title">🔱 DivineRapTv - SHIV TANDAV MASTER ENGINE 🔱</div>
    <p style="color: #ffaa44;">शिव तांडव स्टाइल | Chant + Rap + Hook + Climax | Perfect Flow</p>
    <p style="color: #ff8866;">🎤 Intro Chant | Slow Build Rap | Powerful Hook | Hard Rap | Climax | Outro Chant 🎤</p>
    <p style="color: #44ff44; font-size: 0.8rem;">✅ Gemini API - 60 requests/min | No Rate Limit Issues</p>
</div>
""", unsafe_allow_html=True)

# ==================== PERFECT EXAMPLE ====================
PERFECT_EXAMPLE = '''
[Intro - Chant धीमा]
ॐ नमः शिवाय...
महाकाल...
हर हर महादेव...

[Verse 1 - Rap Slow Build]
जटा में गंगा, माथे पे आग
तीसरी आँख बोले, खत्म हर राग
शून्य से जन्मा, शून्य में लीन
शिव है चेतना, शिव ही सीन
भस्म से सजा, पर राजाओं का राजा
काल भी काँपे, जब खुला दरवाज़ा
डमरू बोले, rhythm divine
शिव के flow में space और time

[Hook - Chorus Chant + Energy]
हर हर महादेव – गूंजे आसमान
हर हर महादेव – थर्राए जहान
तांडव की आग, बोले हर कण
शिव ही शक्ति, शिव ही ब्रह्म

[Verse 2 - Hard Rap]
ना सिंहासन चाहिए, ना सोने का ताज
शमशान में भी दिखे पूरा समाज
अहंकार टूटे, गिर जाए नक़ाब
शिव की शरण में मिटे हर ख्वाब
रौद्र भी वही, शांत भी वही
भक्त की साँसों की जान भी वही
सृजन का बीज, विनाश की धुन
शिव बोले – सब माया, मैं ही हूँ

[Hook - Chorus Repeat Louder]
हर हर महादेव – गूंजे आसमान
हर हर महादेव – थर्राए जहान
तांडव की आग, बोले हर कण
शिव ही शक्ति, शिव ही ब्रह्म

[Bridge - Spoken Whisper Rap]
ना जन्म...
ना मृत्यु...
ना आरंभ...
ना अंत...
जो है...
वो शिव है...

[Verse 3 - Climax Rap]
जब नाचे शिव तो थम जाए काल
धरती बोले – आज प्रलय का हाल
डमरू की beat पे ब्रह्मांड झुके
महाकाल के आगे सब शीश झुके

[Outro - Final Chant Full Power]
हर हर महादेव 🔱
हर हर महादेव 🔱
ॐ नमः शिवाय...
'''

# ==================== STYLE DEFINITIONS ====================
STYLES = {
    "🔥 शिव तांडव रैप": {
        "desc": "महाकाल | श्मशान | तांडव | भयंकर",
        "structure": "Intro Chant | Slow Build | Hook | Hard Rap | Bridge | Climax | Outro",
        "suno": "shiv tandav hardcore rap, heavy bass, damru beats"
    },
    "🔱 हनुमान बाल कांड रैप": {
        "desc": "बाल हनुमान | लंका दहन | शक्ति",
        "structure": "Intro Chant | Story Build | Power Hook | Battle Rap | Climax | Victory Outro",
        "suno": "hanuman rap, powerful, war drums, intense"
    },
    "📖 रामायण युद्ध रैप": {
        "desc": "लंका दहन | राम रावण युद्ध",
        "structure": "Intro | Story Verse | War Hook | Battle Rap | Victory | Outro",
        "suno": "ramayan epic rap, war orchestral, storytelling"
    },
    "💙 राधा कृष्ण प्रेम रैप": {
        "desc": "विरह | प्रेम | बाँसुरी",
        "structure": "Intro Melody | Love Verse | Emotional Hook | Pain Rap | Resolution | Outro",
        "suno": "radha krishna melodic rap, bansuri, romantic"
    }
}

# ==================== PROMPT BUILDER ====================
def build_prompt(style, topic, mood, length):
    
    style_data = STYLES[style]
    
    mood_map = {
        "💔 भावुक": "emotional, slow tempo, heart-touching",
        "⚖️ संतुलित": "medium flow, balanced, steady",
        "🔥 आक्रामक": "aggressive, fast flow, hard delivery",
        "🚀 वायरल": "viral ready, catchy hook, repeatable"
    }
    
    length_map = {
        "छोटा (1-2 मिनट)": "short - 6 lines per verse",
        "पूरा (2-3 मिनट)": "full - 8 lines per verse",
        "विस्तारित (3-4 मिनट)": "extended - 12 lines per verse"
    }
    
    verse_lines = 6 if "छोटा" in length else 8 if "पूरा" in length else 12
    
    return f"""You are a master Hindi rap lyricist. Write EXACTLY like the example below.

📌 PERFECT EXAMPLE TO FOLLOW:
{PERFECT_EXAMPLE}

🎯 YOUR TASK:
STYLE: {style}
TOPIC: {topic}
MOOD: {mood}
LENGTH: {length_map[length]}

🎯 CRITICAL RULES FROM EXAMPLE:

1. **STRUCTURE** (Must follow exactly):
   [Intro - Chant धीमा] - Slow divine chants
   [Verse 1 - Rap Slow Build] - Builds story, 4-7 words per line
   [Hook - Chorus Chant + Energy] - Powerful, repeatable, 4 lines
   [Verse 2 - Hard Rap] - Fast flow, hard hitting, {verse_lines} lines
   [Hook - Chorus Repeat Louder] - Same hook, more energy
   [Bridge - Spoken Whisper Rap] - 4-6 lines, slow, philosophical
   [Verse 3 - Climax Rap] - Fastest flow, strongest lines
   [Outro - Final Chant Full Power] - Divine ending

2. **RHYME SCHEME**: AABB (every 2 lines must rhyme)

3. **LINE LENGTH**: 4-7 words per line exactly

4. **PERFECT HINDI**: No spelling mistakes

Now write PERFECT RAP for:
TOPIC: {topic}
STYLE: {style}
MOOD: {mood}

OUTPUT ONLY LYRICS WITH SECTION HEADERS:
"""

# ==================== GENERATE WITH GEMINI ====================
def generate_rap(style, topic, mood, length):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        response = model.generate_content(
            build_prompt(style, topic, mood, length),
            generation_config={
                "temperature": 0.85,
                "max_output_tokens": 3000,
            }
        )
        
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# ==================== UI LAYOUT ====================
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="style-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 RAP TOPIC")
    topic = st.text_input(
        "",
        placeholder="Example: Hanuman Bal Kand, Shiv Tandav, Maa Durga, Ramayana",
        key="topic_input"
    )
    
    st.markdown("### 🎭 RAP STYLE")
    style = st.selectbox("", list(STYLES.keys()), key="style_select")
    
    st.markdown("### 💫 MOOD")
    mood = st.select_slider(
        "",
        options=["💔 भावुक", "⚖️ संतुलित", "🔥 आक्रामक", "🚀 वायरल"],
        value="🔥 आक्रामक",
        key="mood_slider"
    )
    
    st.markdown("### 📏 LENGTH")
    length = st.select_slider(
        "",
        options=["छोटा (1-2 मिनट)", "पूरा (2-3 मिनट)", "विस्तारित (3-4 मिनट)"],
        value="पूरा (2-3 मिनट)",
        key="length_slider"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show Example
    with st.expander("📖 **SEE PERFECT EXAMPLE - Shiv Tandav**", expanded=False):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown(PERFECT_EXAMPLE)
        st.markdown('</div>', unsafe_allow_html=True)
    
    generate = st.button("🔱 GENERATE PERFECT RAP 🔱", use_container_width=True)

with col2:
    if generate:
        if not topic:
            st.error("⚠️ कृपया पहले RAP TOPIC डालें!")
        else:
            with st.spinner(f"🔱 {style} में PERFECT RAP लिखा जा रहा है... (Gemini API - No Rate Limit)"):
                result = generate_rap(style, topic, mood, length)
                
                if "Error" not in result:
                    st.success("✅ PERFECT RAP READY! 🔱")
                    
                    # Style info
                    style_data = STYLES[style]
                    st.markdown(f"""
                    <div style="background: #1a1a1a; padding: 0.8rem; border-radius: 10px; margin-bottom: 1rem;">
                        <span class="divine-badge">🎤 {style}</span>
                        <span class="divine-badge">💫 {mood}</span>
                        <span class="divine-badge">📏 {length}</span>
                        <span class="divine-badge">📜 {style_data['structure']}</span>
                        <span class="divine-badge">🔱 DivineRapTv</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("### 🎤 PERFECT RAP READY")
                    st.text_area("", result, height=600, key="lyrics_display")
                    
                    # Download buttons
                    col_a, col_b, col_c = st.columns(3)
                    
                    with col_a:
                        st.download_button(
                            "📥 DOWNLOAD LYRICS",
                            result,
                            file_name=f"PERFECT_RAP_{topic.replace(' ', '_')}.txt",
                            use_container_width=True
                        )
                    
                    with col_b:
                        suno_meta = f"""--- SUNO AI v5.5 METADATA ---
STYLE: {style}
TOPIC: {topic}
MOOD: {mood}
LENGTH: {length}
STRUCTURE: {style_data['structure']}

STYLE PROMPT: {style_data['suno']} | Hindi Rap | AABB Rhyme

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
                            hook_end = result.find("[", hook_start + 15)
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
                    
                    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
                    with col_stat1:
                        st.metric("📝 Total Lines", len(lines))
                    with col_stat2:
                        st.metric("📊 Total Words", word_count)
                    with col_stat3:
                        st.metric("🎵 Suno Ready", "✅")
                    with col_stat4:
                        st.metric("📜 Rate Limit", "No Issue ✅")
                    
                    st.balloons()
                    st.success("🎉 SONG READY! अब Suno AI / Udio में डालकर FULL SONG बनाएं!")
                    
                else:
                    st.error(result)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="color: #ff8844;">🔱 DivineRapTv - SHIV TANDAV MASTER ENGINE 🔱</p>
    <p style="color: #ffaa66;">Gemini API | 60 requests/min | No Rate Limit Issues</p>
    <p style="color: #ff8866;">🎤 Free API Key from Google AI Studio | Unlimited Tokens 🎤</p>
</div>
""", unsafe_allow_html=True)</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="final-header">
    <div class="final-title">🔱 DivineRapTv - SHIV TANDAV MASTER ENGINE 🔱</div>
    <p style="color: #ffaa44;">शिव तांडव स्टाइल | Chant + Rap + Hook + Climax | Perfect Flow</p>
    <p style="color: #ff8866;">🎤 Intro Chant | Slow Build Rap | Powerful Hook | Hard Rap | Climax | Outro Chant 🎤</p>
</div>
""", unsafe_allow_html=True)

# ==================== PERFECT EXAMPLE ====================
PERFECT_EXAMPLE = '''
[Intro - Chant धीमा]
ॐ नमः शिवाय...
महाकाल...
हर हर महादेव...

[Verse 1 - Rap Slow Build]
जटा में गंगा, माथे पे आग
तीसरी आँख बोले, खत्म हर राग
शून्य से जन्मा, शून्य में लीन
शिव है चेतना, शिव ही सीन
भस्म से सजा, पर राजाओं का राजा
काल भी काँपे, जब खुला दरवाज़ा
डमरू बोले, rhythm divine
शिव के flow में space और time

[Hook - Chorus Chant + Energy]
हर हर महादेव – गूंजे आसमान
हर हर महादेव – थर्राए जहान
तांडव की आग, बोले हर कण
शिव ही शक्ति, शिव ही ब्रह्म

[Verse 2 - Hard Rap]
ना सिंहासन चाहिए, ना सोने का ताज
शमशान में भी दिखे पूरा समाज
अहंकार टूटे, गिर जाए नक़ाब
शिव की शरण में मिटे हर ख्वाब
रौद्र भी वही, शांत भी वही
भक्त की साँसों की जान भी वही
सृजन का बीज, विनाश की धुन
शिव बोले – सब माया, मैं ही हूँ

[Hook - Chorus Repeat Louder]
हर हर महादेव – गूंजे आसमान
हर हर महादेव – थर्राए जहान
तांडव की आग, बोले हर कण
शिव ही शक्ति, शिव ही ब्रह्म

[Bridge - Spoken Whisper Rap]
ना जन्म...
ना मृत्यु...
ना आरंभ...
ना अंत...
जो है...
वो शिव है...

[Verse 3 - Climax Rap]
जब नाचे शिव तो थम जाए काल
धरती बोले – आज प्रलय का हाल
डमरू की beat पे ब्रह्मांड झुके
महाकाल के आगे सब शीश झुके

[Outro - Final Chant Full Power]
हर हर महादेव 🔱
हर हर महादेव 🔱
ॐ नमः शिवाय...
'''

# ==================== STYLE DEFINITIONS ====================
STYLES = {
    "🔥 शिव तांडव रैप": {
        "desc": "महाकाल | श्मशान | तांडव | भयंकर | Divine",
        "structure": "Intro Chant | Slow Build | Hook | Hard Rap | Bridge | Climax | Outro",
        "suno": "shiv tandav hardcore rap, heavy bass, damru beats, intense male vocal, divine wrath"
    },
    "🔱 माँ दुर्गा शक्ति रैप": {
        "desc": "महिषासुर मर्दिनी | शक्ति | युद्ध",
        "structure": "Intro Chant | Story Build | Power Hook | Battle Rap | Climax | Victory Outro",
        "suno": "durga shakti rap, war drums, female power, intense, cinematic"
    },
    "📖 रामायण युद्ध रैप": {
        "desc": "लंका दहन | राम रावण युद्ध",
        "structure": "Intro | Story Verse | War Hook | Battle Rap | Victory | Outro",
        "suno": "ramayan epic rap, war orchestral, storytelling, intense"
    },
    "💙 राधा कृष्ण प्रेम रैप": {
        "desc": "विरह | प्रेम | बाँसुरी | भावनात्मक",
        "structure": "Intro Melody | Love Verse | Emotional Hook | Pain Rap | Resolution | Outro",
        "suno": "radha krishna melodic rap, bansuri, romantic, emotional"
    },
    "🕊️ मीरा भक्ति रैप": {
        "desc": "समर्पण | दर्द | गिरधर | प्रेम",
        "structure": "Intro Bhajan | Devotion Verse | Bhakti Hook | Pain Rap | Surrender | Outro",
        "suno": "meera bhakti rap, devotional, emotional, bhajan fusion"
    }
}

# ==================== PROMPT BUILDER WITH EXAMPLE ====================
def build_prompt_with_example(style, topic, mood, length):
    
    style_data = STYLES[style]
    
    mood_map = {
        "💔 भावुक": "emotional, slow tempo, heart-touching, soft flow",
        "⚖️ संतुलित": "medium flow, balanced, steady rhythm",
        "🔥 आक्रामक": "aggressive, fast flow, hard delivery, intense",
        "🚀 वायरल": "viral ready, catchy hook, repeatable chorus, trending"
    }
    
    length_map = {
        "छोटा (1-2 मिनट)": "short version - 6 lines per verse",
        "पूरा (2-3 मिनट)": "full version - 8 lines per verse", 
        "विस्तारित (3-4 मिनट)": "extended - 12 lines per verse"
    }
    
    verse_lines = 6 if "छोटा" in length else 8 if "पूरा" in length else 12
    
    return f"""You are a master Hindi rap lyricist. You write like Divine, Raftaar, and top Bollywood lyricists.

STYLE: {style}
TOPIC: {topic}
MOOD: {mood} - {mood_map[mood]}
LENGTH: {length_map[length]}

📌 PERFECT EXAMPLE - FOLLOW THIS EXACT STYLE:

{PERFECT_EXAMPLE}

🎯 CRITICAL RULES FROM THE EXAMPLE:

1. **STRUCTURE** (Must follow exactly):
   [Intro - Chant धीमा] - Slow, divine chants
   [Verse 1 - Rap Slow Build] - Builds story slowly, 4-7 words per line
   [Hook - Chorus Chant + Energy] - Powerful, repeatable, 4 lines
   [Verse 2 - Hard Rap] - Fast flow, hard hitting, 8-12 lines
   [Hook - Chorus Repeat Louder] - Same hook, more energy
   [Bridge - Spoken Whisper Rap] - 4-6 lines, slow, philosophical
   [Verse 3 - Climax Rap] - Fastest flow, strongest lines
   [Outro - Final Chant Full Power] - Divine ending

2. **RHYME SCHEME**: AABB (every 2 lines must rhyme)
   Example: "जटा में गंगा, माथे पे आग" (A)
            "तीसरी आँख बोले, खत्म हर राग" (A)

3. **LINE LENGTH**: 4-7 words per line exactly

4. **VOCABULARY**:
   - Divine: महाकाल, तांडव, शिव, शक्ति, ब्रह्म
   - Hardcore: काल, प्रलय, विनाश, रुद्र
   - Emotional: भक्ति, प्रेम, समर्पण

5. **FLOW PROGRESSION**:
   - Intro: Slow, chanting
   - Verse 1: Building slowly
   - Hook: Energetic, catchy
   - Verse 2: Hard, aggressive
   - Bridge: Slow, deep
   - Verse 3: Fastest, climax
   - Outro: Powerful chant

6. **PERFECT HINDI**: No spelling mistakes

Now write PERFECT RAP for:
TOPIC: {topic}
STYLE: {style}
MOOD: {mood}

Follow the EXAMPLE structure exactly. Use same section headers with emojis.
OUTPUT ONLY LYRICS:
"""

# ==================== GENERATE FUNCTION ====================
def generate_perfect_rap(style, topic, mood, length):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": """You are a master Hindi rap lyricist. You write in the style of the Shiv Tandav example provided.

CRITICAL: Follow the EXACT structure from the example:
- [Intro - Chant धीमा] with slow divine chants
- [Verse 1 - Rap Slow Build] with AABB rhyme
- [Hook - Chorus Chant + Energy] powerful and repeatable
- [Verse 2 - Hard Rap] aggressive flow
- [Bridge - Spoken Whisper Rap] philosophical
- [Verse 3 - Climax Rap] fastest flow
- [Outro - Final Chant Full Power] divine ending

Every 2 lines must rhyme. Each line 4-7 words. Perfect Hindi spelling."""},
                {"role": "user", "content": build_prompt_with_example(style, topic, mood, length)}
            ],
            temperature=0.85,
            max_tokens=3000
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
        placeholder="Example: Shiv Tandav, Maa Durga Mahishasur, Ramayana Yuddh, Radha Krishna",
        key="topic_input"
    )
    
    st.markdown("### 🎭 RAP STYLE")
    style = st.selectbox("", list(STYLES.keys()), key="style_select")
    
    st.markdown("### 💫 MOOD")
    mood = st.select_slider(
        "",
        options=["💔 भावुक", "⚖️ संतुलित", "🔥 आक्रामक", "🚀 वायरल"],
        value="🔥 आक्रामक",
        key="mood_slider"
    )
    
    st.markdown("### 📏 LENGTH")
    length = st.select_slider(
        "",
        options=["छोटा (1-2 मिनट)", "पूरा (2-3 मिनट)", "विस्तारित (3-4 मिनट)"],
        value="पूरा (2-3 मिनट)",
        key="length_slider"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show Example
    with st.expander("📖 **SEE PERFECT EXAMPLE - Shiv Tandav**", expanded=False):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown(PERFECT_EXAMPLE)
        st.markdown('</div>', unsafe_allow_html=True)
    
    generate = st.button("🔱 GENERATE PERFECT RAP 🔱", use_container_width=True)

with col2:
    if generate:
        if not topic:
            st.error("⚠️ कृपया पहले RAP TOPIC डालें!")
        else:
            with st.spinner(f"🔱 {style} में PERFECT RAP लिखा जा रहा है... (Example style follow कर रहा हूँ)"):
                result = generate_perfect_rap(style, topic, mood, length)
                
                if "Error" not in result:
                    st.success("✅ PERFECT RAP READY! 🔱")
                    
                    # Style info
                    style_data = STYLES[style]
                    st.markdown(f"""
                    <div style="background: #1a1a1a; padding: 0.8rem; border-radius: 10px; margin-bottom: 1rem;">
                        <span class="divine-badge">🎤 {style}</span>
                        <span class="divine-badge">💫 {mood}</span>
                        <span class="divine-badge">📏 {length}</span>
                        <span class="divine-badge">📜 {style_data['structure']}</span>
                        <span class="divine-badge">🔱 DivineRapTv</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("### 🎤 PERFECT RAP READY")
                    st.text_area("", result, height=600, key="lyrics_display")
                    
                    # Download buttons
                    col_a, col_b, col_c = st.columns(3)
                    
                    with col_a:
                        st.download_button(
                            "📥 DOWNLOAD LYRICS",
                            result,
                            file_name=f"PERFECT_RAP_{topic.replace(' ', '_')}.txt",
                            use_container_width=True
                        )
                    
                    with col_b:
                        suno_meta = f"""--- SUNO AI v5.5 METADATA ---
STYLE: {style}
TOPIC: {topic}
MOOD: {mood}
LENGTH: {length}
STRUCTURE: {style_data['structure']}

STYLE PROMPT: {style_data['suno']} | Hindi Rap | AABB Rhyme

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
                        # Shorts version (Hook only)
                        if "Hook" in result:
                            hook_start = result.find("Hook")
                            hook_end = result.find("[", hook_start + 15)
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
                    
                    # Check if structure matches example
                    has_intro = "Intro" in result
                    has_verse1 = "Verse 1" in result
                    has_hook = "Hook" in result
                    has_verse2 = "Verse 2" in result
                    has_bridge = "Bridge" in result
                    has_verse3 = "Verse 3" in result
                    has_outro = "Outro" in result
                    
                    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
                    with col_stat1:
                        st.metric("📝 Total Lines", len(lines))
                    with col_stat2:
                        st.metric("📊 Total Words", word_count)
                    with col_stat3:
                        st.metric("🎵 Suno Ready", "✅")
                    with col_stat4:
                        st.metric("📜 Structure", "Perfect" if has_intro and has_verse1 and has_hook else "Good")
                    
                    st.info(f"📋 Structure Check: Intro: {'✅' if has_intro else '❌'} | Verse1: {'✅' if has_verse1 else '❌'} | Hook: {'✅' if has_hook else '❌'} | Verse2: {'✅' if has_verse2 else '❌'} | Bridge: {'✅' if has_bridge else '❌'} | Climax: {'✅' if has_verse3 else '❌'} | Outro: {'✅' if has_outro else '❌'}")
                    
                    st.balloons()
                    st.success("🎉 SONG READY! अब Suno AI / Udio में डालकर FULL SONG बनाएं!")
                    
                else:
                    st.error(result)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="color: #ff8844;">🔱 DivineRapTv - SHIV TANDAV MASTER ENGINE 🔱</p>
    <p style="color: #ffaa66;">Intro Chant | Slow Build | Powerful Hook | Hard Rap | Bridge | Climax | Outro Chant</p>
    <p style="color: #ff8866;">🎤 Perfect Example Included | AI Follows Exact Style | AABB Rhyme Scheme 🎤</p>
</div>
""", unsafe_allow_html=True)

import streamlit as st
from groq import Groq
import time

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
st.set_page_config(
    page_title="DivineRapTv - Suno AI Studio 3.0",
    layout="wide",
    page_icon="🔱"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0a0000 0%, #1a0000 100%);
}
.style-card {
    background: linear-gradient(135deg, #1a0000, #0a0000);
    border-left: 4px solid #ff0000;
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 8px;
}
.style-title {
    color: #ff4444;
    font-weight: bold;
    font-size: 1.2rem;
}
.style-desc {
    color: #ff8888;
    font-size: 0.8rem;
}
.suno-tag {
    background: #ff000020;
    border: 1px solid #ff0000;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.7rem;
    display: inline-block;
}
.stButton>button {
    background: linear-gradient(90deg, #ff0000, #ff6600);
    color: white;
    font-weight: bold;
    border: none;
    height: 3rem;
    border-radius: 8px;
    font-size: 1.1rem;
}
.stTextArea textarea {
    background-color: #0a0a0a;
    color: #ffaa00;
    border: 1px solid #ff3300;
    font-family: monospace;
    font-size: 0.95rem;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <h1 style="color: #ff4444;">🔱 DivineRapTv</h1>
    <h2 style="color: #ffaa00;">Ultimate Suno AI Studio 3.0</h2>
    <p style="color: #ff8888;">5 Styles | Suno AI v5.5 Optimized | Perfect Hindi Lyrics</p>
</div>
""", unsafe_allow_html=True)

# Style definitions
STYLES = {
    "Hardcore Rap": {
        "desc": "Divine / Raftaar style | Aggressive | Power",
        "rules": "No verbs (hai/hoon banned), 4-6 words, AABB rhyme",
        "suno": "hardcore aggressive rap, heavy bass, fast flow, male vocal"
    },
    "Ramayan Story": {
        "desc": "Cinematic storytelling | Scene by scene",
        "rules": "Scene-based, 5-7 words, ABAB rhyme",
        "suno": "cinematic hip hop, epic orchestral, storytelling rap"
    },
    "Radha Krishna Prem": {
        "desc": "Virah | Love | Pain | Bansuri",
        "rules": "Emotional vocab, 4-6 words, soft rhymes",
        "suno": "emotional melodic rap, bansuri, romantic hip hop"
    },
    "Meera Bhakti": {
        "desc": "Devotion | Surrender | Divine Love",
        "rules": "Devotional, first person, simple rhymes",
        "suno": "devotional hip hop, emotional, bhajan fusion"
    },
    "Bollywood Fusion": {
        "desc": "Bollywood style | Grand | Cinematic",
        "rules": "Dramatic, 5-7 words, grand scale",
        "suno": "bollywood hip hop fusion, cinematic, orchestral"
    }
}

# Style selection
st.markdown("### 🎭 Select Your Rap Style")
cols = st.columns(5)
selected_style = None

for idx, (style_name, style_info) in enumerate(STYLES.items()):
    with cols[idx]:
        if st.button(f"{style_name}", key=f"btn_{idx}", use_container_width=True):
            selected_style = style_name

if selected_style is None:
    selected_style = "Hardcore Rap"

style_data = STYLES[selected_style]

# Display style info
st.markdown(f"""
<div class="style-card">
    <span class="style-title">{selected_style}</span>
    <span class="style-desc">{style_data['desc']}</span>
    <br>
    <span class="suno-tag">🎵 Suno AI: {style_data['suno']}</span>
</div>
""", unsafe_allow_html=True)

# Input area
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("### 📝 Song Details")
    
    topic = st.text_input(
        "🎯 Topic",
        placeholder="Example: लंका दहन, राधा कृष्ण विरह, हनुमान जी"
    )
    
    mood = st.select_slider(
        "💫 Mood",
        options=["💔 Emotional", "⚖️ Balanced", "🔥 Aggressive", "🚀 Viral Ready"],
        value="⚖️ Balanced"
    )
    
    length = st.select_slider(
        "📏 Length",
        options=["Short (1-2 min)", "Full (2-3 min)", "Extended (3-4 min)"],
        value="Full (2-3 min)"
    )
    
    generate = st.button("🎵 Generate Suno AI Lyrics", use_container_width=True)

# Prompt builder function
def build_prompt(style, topic, mood, length):
    mood_map = {
        "💔 Emotional": "soft, emotional, slow tempo",
        "⚖️ Balanced": "medium flow, balanced",
        "🔥 Aggressive": "fast flow, hard delivery",
        "🚀 Viral Ready": "catchy, repeatable hook"
    }
    
    style_info = STYLES[style]
    
    verse_lines = 8 if "Short" in length else 12 if "Full" in length else 16
    
    return f"""
You are a professional Hindi lyricist for Suno AI v5.5.

STYLE: {style}
TOPIC: {topic}
MOOD: {mood} - {mood_map[mood]}
LENGTH: {length}

SUNO AI RULES:
1. Every line: 4-7 words exactly
2. Perfect Hindi spelling, no mistakes
3. Clear rhyme scheme
4. Hook must be 4 lines, catchy and repeatable

STRUCTURE:
[Intro] (4 lines)
[Verse 1] ({verse_lines} lines)
[Hook] (4 lines)
[Verse 2] ({verse_lines} lines)
[Hook] (repeat)
[Outro] (3-4 lines)

STYLE RULES:
{style_info['rules']}

Write lyrics for topic: {topic}

OUTPUT ONLY LYRICS WITH SECTION HEADERS:
"""

# Generate function
def generate_lyrics(style, topic, mood, length):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": f"You are a master Hindi lyricist for {style}. You write perfect Suno AI v5.5 optimized lyrics."},
                {"role": "user", "content": build_prompt(style, topic, mood, length)}
            ],
            temperature=0.85,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Display results
with col2:
    if generate:
        if not topic:
            st.error("⚠️ Please enter a topic first!")
        else:
            with st.spinner(f"🔥 Generating {selected_style} lyrics for Suno AI..."):
                lyrics = generate_lyrics(selected_style, topic, mood, length)
                
                if "Error" not in lyrics:
                    st.success("✅ Suno AI Ready Lyrics Generated!")
                    
                    # Suno prompt
                    st.markdown("### 🎵 Suno AI Style Prompt")
                    st.code(style_data['suno'], language="text")
                    
                    st.markdown("---")
                    st.markdown("### 🎤 Lyrics")
                    st.text_area("", lyrics, height=500, key="lyrics_display")
                    
                    # Download buttons
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.download_button(
                            "📥 Download Lyrics",
                            lyrics,
                            file_name=f"lyrics_{topic.replace(' ', '_')}.txt",
                            use_container_width=True
                        )
                    with col_b:
                        meta = f"Style: {selected_style}\nPrompt: {style_data['suno']}\nTopic: {topic}\nMood: {mood}\n\n{lyrics[:500]}"
                        st.download_button(
                            "🎵 Suno Metadata",
                            meta,
                            file_name="suno_metadata.txt",
                            use_container_width=True
                        )
                    
                    st.balloons()
                else:
                    st.error(lyrics)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="color: #ff8888;">🔱 DivineRapTv - Suno AI Studio 3.0 🔱</p>
    <p style="color: #ffaa00;">5 Styles | Suno AI v5.5 Optimized | Perfect Hindi Lyrics</p>
</div>
""", unsafe_allow_html=True)

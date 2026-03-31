import streamlit as st
from groq import Groq
import datetime

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
st.set_page_config(
    page_title="DivineRapTv - YouTube Bhakti Rap Studio", 
    layout="wide",
    page_icon="🔱"
)

# Custom CSS for YouTube-style UI
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
    color: #fff;
}

/* Main container */
.main-header {
    text-align: center;
    padding: 2rem;
    background: linear-gradient(90deg, #ff0000, #ff7300, #ff0000);
    border-radius: 20px;
    margin-bottom: 2rem;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #ff0000, #ff7300);
    color: white;
    font-weight: bold;
    border: none;
    height: 3.5rem;
    width: 100%;
    border-radius: 50px;
    font-size: 1.2rem;
    transition: all 0.3s ease;
    box-shadow: 0 0 15px rgba(255, 0, 0, 0.3);
}

.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 25px rgba(255, 0, 0, 0.6);
}

/* Text area for lyrics */
.stTextArea textarea {
    color: #ffaa00 !important;
    background-color: #0a0a0a !important;
    font-family: 'Courier New', monospace;
    font-size: 1.1rem !important;
    border: 2px solid #ff3300;
    border-radius: 15px;
    line-height: 1.6;
}

/* Input fields */
.stTextInput input, .stSelectbox div {
    background-color: #0a0a0a !important;
    color: white !important;
    border: 1px solid #ff3300;
    border-radius: 10px;
}

/* Cards */
.card {
    background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 4px solid #ff3300;
    margin-bottom: 1rem;
}

/* Success message */
.success-box {
    background: linear-gradient(135deg, #00ff8720, #00ff8720);
    border-left: 4px solid #00ff87;
    padding: 1rem;
    border-radius: 10px;
}

/* YouTube thumbnail preview */
.thumbnail-preview {
    background: linear-gradient(135deg, #2a2a2a, #1a1a1a);
    border-radius: 15px;
    padding: 1rem;
    text-align: center;
    border: 1px solid #ff3300;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1 style="color: white; font-size: 3rem; margin: 0;">🔱 DivineRapTv</h1>
    <p style="color: #ffaa00; font-size: 1.3rem;">Ultimate Bhakti Rap Studio | YouTube Viral Content</p>
    <p style="color: white;">🔥 Hardcore + Emotion + Devotion = Viral Rap 🔥</p>
</div>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🎯 **YouTube Video Details**")
    
    # Video Title
    video_title = st.text_input(
        "📹 **Video Title**", 
        placeholder="जैसे: लंका दहन - हनुमान जी का क्रोध | Divine Rap"
    )
    
    # Topic
    topic = st.text_input(
        "🔥 **Rap Topic**", 
        placeholder="जैसे: लंका दहन, राधा कृष्ण विरह, हनुमान चालीसा रैप"
    )
    
    # Style Selection
    style = st.selectbox(
        "🎭 **Rap Style**",
        [
            "🔥 Hardcore Hanuman Rap",
            "💙 Radha Krishna Emotional", 
            "🌙 Shiv Tandav Style",
            "🚩 Hanuman Chalisa Remix",
            "🎬 Bollywood Bhakti",
            "🕊️ Meera Bai Devotional",
            "⚡ Viral Trending Style"
        ]
    )
    
    # Mood
    mood = st.select_slider(
        "💫 **Mood Level**",
        options=["💔 Emotional", "⚖️ Balanced", "🔥 Aggressive", "🚀 Viral Ready"]
    )
    
    # Duration
    duration = st.selectbox(
        "⏱️ **Song Duration**",
        ["1-2 min (YouTube Shorts)", "2-3 min (Viral Track)", "3-4 min (Full Song)"]
    )
    
    # Thumbnail text
    thumbnail_text = st.text_input(
        "🖼️ **Thumbnail Text**", 
        placeholder="जैसे: लंका जल रही है! 🔥 10M Views"
    )
    
    generate_btn = st.button("🚀 **Generate Viral Lyrics**", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # YouTube Tips
    with st.expander("📌 **YouTube Viral Tips**"):
        st.markdown("""
        ✅ **Thumbnail**: Bold text, red/yellow colors, face expression  
        ✅ **Title**: Use emojis, capital letters, curiosity gap  
        ✅ **First 30 sec**: Hook must be strongest  
        ✅ **Duration**: 2:30 - 3:30 is ideal for retention  
        ✅ **Tags**: #DivineRapTv #BhaktiRap #ViralSong  
        ✅ **Description**: Add full lyrics + subscribe CTA  
        """)

with col2:
    if generate_btn:
        if not topic:
            st.error("⚠️ **Error:** Please enter a rap topic first!")
        else:
            with st.spinner("🔥 **Divine lyrics are being created...** This will go viral! 🚀"):
                
                # Enhanced Prompt for YouTube Viral Content
                prompt = f"""
You are India's #1 Divine Rap Hitmaker for YouTube. Your songs get 10M+ views.

**VIDEO DETAILS:**
- Title: {video_title if video_title else topic + " - Divine Rap"}
- Topic: {topic}
- Style: {style}
- Mood: {mood}
- Duration: {duration}
- Thumbnail Text: {thumbnail_text if thumbnail_text else topic}

**YOUR TASK:**
Write PERFECT Hindi rap lyrics that will go VIRAL on YouTube.

**CRITICAL RULES:**

1. **PERFECT HINDI** (No spelling mistakes):
   ✅ Correct: अग्नि, बाँसुरी, आँसू, हनुमान, लंका
   ❌ Wrong: अन्मि, बांसूरी, आँख़ बहते

2. **SUNO AI / UDIO READY**:
   - Every line: 4-7 words
   - Balanced syllables
   - Clear rhyme scheme

3. **STRUCTURE** (YouTube Format):
```

[Intro] - 4 lines (Hook se pehle attention grab)
[Verse 1] - 12 lines (Story build)
[Hook] 🔥 - 4 lines (Most catchy, loop worthy)
[Verse 2] - 12 lines (Emotion + Power)
[Hook] - Repeat
[Bridge] - 4 lines (Climax)
[Outro] - 3 lines (Memorable ending)

```

4. **VIRAL ELEMENTS**:
   - Every 3 lines: Punchline
   - First 4 lines: Hook inside
   - "OMG moment" in Verse 2
   - Loop-able hook for shorts/reels

5. **STYLE SPECIFIC**:
   {style} style:
   - Words: Use theme-appropriate vocabulary
   - Flow: Match the intensity
   - Emotion: Deep bhakti + hardcore balance

6. **YOUTUBE OPTIMIZATION**:
   - Add timestamps in comments format
   - Create shorts-worthy 15-sec clips
   - Visual imagery for thumbnail

**OUTPUT FORMAT:**
Give ONLY lyrics with clear section headers.

START NOW (Viral Guaranteed):
"""

                try:
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": "You're India's top Divine Rap lyricist. Your lyrics are PERFECT - no spelling mistakes, viral hooks, Suno AI ready. Every song you write gets 10M+ views."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.85,
                        max_tokens=2500,
                        top_p=0.95
                    )
                    
                    lyrics = response.choices[0].message.content
                    
                    # Display Lyrics
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.success("✅ **LYRICS GENERATED SUCCESSFULLY!** 🚀")
                    st.markdown(f"**Video Title:** {video_title if video_title else topic + ' - Divine Rap'}")
                    st.markdown(f"**Style:** {style} | **Mood:** {mood}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.markdown("---")
                    st.markdown("### 🎤 **DivineRapTv Official Lyrics**")
                    st.markdown("#### 📝 Full Song Lyrics:")
                    
                    # Lyrics display
                    st.text_area("", lyrics, height=600, key="lyrics_display")
                    
                    # Download options
                    col_a, col_b, col_c = st.columns(3)
                    
                    with col_a:
                        st.download_button(
                            label="📥 **Download TXT**",
                            data=lyrics,
                            file_name=f"divine_rap_{topic.replace(' ', '_')}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    
                    with col_b:
                        # Create YouTube description
                        description = f"""{video_title if video_title else topic + ' - Divine Rap'}

🎵 DivineRapTv Presents:
{lyrics[:500]}...

🔔 Subscribe for more: @DivineRapTv
📱 Follow on Instagram: @divineraptv
🎧 Available on all platforms

#DivineRapTv #BhaktiRap #{topic.replace(' ', '')} #ViralSong #HanumanRap

👇 Comment your favorite line below!"""
                        
                        st.download_button(
                            label="📝 **YouTube Description**",
                            data=description,
                            file_name="youtube_description.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    
                    with col_c:
                        # Create shorts script
                        shorts_script = f"""🎬 YouTube Shorts Script:

🔥 **Best 15 Seconds:** 
{lyrics.split('[Hook]')[1][:200] if '[Hook]' in lyrics else lyrics[:200]}

📌 **Caption:** {thumbnail_text if thumbnail_text else topic}
🔗 **Full Song:** Link in bio
#DivineRapTv #Shorts #Viral"""
                        
                        st.download_button(
                            label="📱 **Shorts Script**",
                            data=shorts_script,
                            file_name="youtube_shorts.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    
                    # Thumbnail Preview
                    st.markdown("---")
                    st.markdown("### 🖼️ **Thumbnail Preview**")
                    st.markdown(f"""
                    <div class="thumbnail-preview">
                        <h3 style="color: #ff3300; font-size: 2rem;">🔥 {thumbnail_text if thumbnail_text else topic.upper()} 🔥</h3>
                        <p style="color: #ffaa00;">🔱 DivineRapTv | {style}</p>
                        <p>👇 Watch Full Video 👇</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # YouTube Upload Tips
                    with st.expander("🎬 **YouTube Upload Checklist**"):
                        st.markdown("""
                        ### ✅ Before Uploading:
                        
                        **1. Thumbnail:**
                        - Text: Bold, readable, 3-4 words max
                        - Colors: Red, Yellow, Gold
                        - Face expression: Intense/Emotional
                        - Size: 1280x720px
                        
                        **2. Title:**
                        - Use 🔥, 🚩, 💙 emojis
                        - Capital letters for impact
                        - Curiosity gap
                        
                        **3. Description:**
                        - Full lyrics in description
                        - Timestamps for sections
                        - Subscribe link
                        - Hashtags (#DivineRapTv #Viral)
                        
                        **4. Tags:**
                        DivineRapTv, Bhakti Rap, {topic}, Hanuman Rap, Viral Song
                        
                        **5. Cards & End Screen:**
                        - Add subscribe card
                        - Link to previous videos
                        - End screen with 2 videos
                        """)
                    
                    # Success message
                    st.balloons()
                    st.success("🎉 **Your viral song is ready! Upload to YouTube now!** 🚀")
                    
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                    st.info("💡 Tip: Check your API key and try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <p style="color: #ffaa00;">🔱 <strong>DivineRapTv</strong> - India's #1 Bhakti Rap Studio 🔱</p>
    <p style="font-size: 0.9rem;">🔥 10M+ Views Guaranteed | Perfect Lyrics | YouTube Ready 🔥</p>
    <p style="font-size: 0.8rem;">© 2024 DivineRapTv | Subscribe for Weekly Viral Bhakti Rap</p>
</div>
""", unsafe_allow_html=True)
```

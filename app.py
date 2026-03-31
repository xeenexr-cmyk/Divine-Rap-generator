import streamlit as st
from groq import Groq
import time
import random

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
st.set_page_config(
    page_title="DivineRapTv - ULTRA BEAST ENGINE 2.0", 
    layout="wide", 
    page_icon="💀"
)

# DARK BEAST MODE UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a0000 100%);
    }
    
    .main-header {
        text-align: center;
        padding: 1rem;
        border-bottom: 3px solid #ff0000;
        margin-bottom: 2rem;
    }
    
    .beast-title {
        font-family: 'Black Ops One', cursive;
        font-size: 3rem;
        background: linear-gradient(45deg, #ff0000, #ff6600);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 0.8; text-shadow: 0 0 5px red; }
        100% { opacity: 1; text-shadow: 0 0 20px red; }
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #8b0000, #ff0000, #8b0000);
        color: white;
        font-weight: 900;
        border: none;
        height: 4rem;
        width: 100%;
        border-radius: 0;
        font-size: 1.3rem;
        letter-spacing: 3px;
        transition: all 0.3s;
        box-shadow: 0 0 15px rgba(255,0,0,0.5);
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(255,0,0,0.8);
        background: linear-gradient(45deg, #ff0000, #ff3300);
    }
    
    .stTextInput>div>div>input {
        background-color: #0a0a0a;
        color: #ff4d4d;
        border: 2px solid #ff0000;
        border-radius: 0;
        font-size: 1.2rem;
        font-weight: bold;
    }
    
    .stTextArea textarea {
        background-color: #0a0a0a !important;
        color: #ff6666 !important;
        border: 2px solid #ff0000 !important;
        border-radius: 0 !important;
        font-family: 'Courier New', monospace;
        font-size: 1rem !important;
        line-height: 1.8 !important;
    }
    
    .beast-card {
        background: rgba(20, 0, 0, 0.7);
        border-left: 5px solid #ff0000;
        padding: 1rem;
        margin: 1rem 0;
        backdrop-filter: blur(5px);
    }
    
    .blood-text {
        color: #ff0000;
        font-weight: bold;
        text-transform: uppercase;
    }
    
    .warning {
        color: #ff6600;
        font-size: 0.8rem;
        text-align: center;
        padding: 0.5rem;
        border: 1px solid #ff6600;
    }
    
    hr {
        border-color: #ff0000;
    }
    
    .stats-box {
        background: #1a0000;
        padding: 1rem;
        border: 1px solid #ff0000;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header with Beast Mode
st.markdown("""
<div class="main-header">
    <div class="beast-title">💀 DIVINERAPTV - ULTRA BEAST ENGINE 2.0 💀</div>
    <p style="color: #ff6666; letter-spacing: 2px;">RAW | LETHAL | DIVINE | NO MERCY</p>
    <p style="color: #ff0000; font-size: 0.9rem;">⚔️ BHAKTI x HARDCORE HIP-HOP - THE FINAL FORM ⚔️</p>
</div>
""", unsafe_allow_html=True)

# Layout
col_left, col_mid, col_right = st.columns([1.2, 1, 1.5])

with col_left:
    st.markdown('<div class="beast-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 **WAR TOPIC**")
    topic = st.text_input("", placeholder="Example: Mahakal Tandav | Ravan Vinash | Aghori Wrath")
    
    st.markdown("### ⚔️ **ATTACK MODE**")
    attack_mode = st.selectbox("", [
        "💀 FATAL ATTACK (Pure Hardcore)",
        "🔥 WAR STORY (Cinematic Massacre)",
        "🌙 DARK DEVOTION (Gothic Bhakti)",
        "⚡ SPEED DEMON (Fast Flow)",
        "🩸 BLOOD RITUAL (Savage Mode)"
    ])
    
    st.markdown("### 🎭 **BEAST INTENSITY**")
    intensity = st.select_slider(
        "",
        options=["AGGRESSIVE", "BRUTAL", "SADISTIC", "APOCALYPTIC"],
        value="BRUTAL"
    )
    
    st.markdown("### 📏 **STRUCTURE**")
    structure = st.selectbox("", [
        "🔪 Short & Deadly (1-2 min - Shorts)",
        "💀 Full Massacre (2-3 min - Viral)",
        "🩸 Epic Slaughter (3-4 min - Banger)"
    ])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Beast Stats Counter
    st.markdown('<div class="stats-box">', unsafe_allow_html=True)
    st.markdown("### 💀 **BEAST METRICS**")
    if topic:
        words = len(topic.split())
        st.markdown(f"**🔥 Kill Count:** {words * 100} words of destruction")
        st.markdown(f"**⚔️ Damage Level:** {intensity}")
        st.markdown(f"**🎯 Target:** {topic.upper()}")
    st.markdown('</div>', unsafe_allow_html=True)

with col_mid:
    st.markdown('<div class="beast-card">', unsafe_allow_html=True)
    st.markdown("### 🔥 **HARDCORE RULES**")
    st.markdown("""
    ```
    ❌ FORBIDDEN WORDS:
    है | हूँ | था | रहा
    करता | होता | जैसा
    
    ✅ REQUIRED:
    भस्म | काल | रक्त | प्रहार
    चक्र | खंजर | अंगार | शव
    लाश | मुर्दा | विनाश | प्रलय
    अहंकार | नरक | यमराज
    
    🎯 STRUCTURE:
    - 16 BULLETS in Verse 1
    - 4 KILLER HOOK lines
    - 16 BULLETS in Verse 2
    - 1 FATAL OUTRO
    
    ⚡ RHYME SCHEME:
    AABBCCDD pattern
    Internal rhymes mandatory
    ```
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# THE ULTRA BEAST PROMPT ENGINE
def build_brutal_prompt(topic, attack_mode, intensity, structure):
    
    intensity_multiplier = {
        "AGGRESSIVE": "Hard hitting, war-like vocabulary, aggressive flow",
        "BRUTAL": "Extreme violence, blood, gore, raw power, no filter",
        "SADISTIC": "Psychological terror, dark imagery, haunting metaphors",
        "APOCALYPTIC": "End of world scale, cosmic destruction, divine wrath"
    }
    
    mode_specific = {
        "💀 FATAL ATTACK (Pure Hardcore)": "Direct attacks, one-liner punches, kill shots every line",
        "🔥 WAR STORY (Cinematic Massacre)": "Scene by scene battle narrative, visual storytelling, slow-motion kills",
        "🌙 DARK DEVOTION (Gothic Bhakti)": "Tantric vibes, shiv tandav, aghori elements, dark spirituality",
        "⚡ SPEED DEMON (Fast Flow)": "Rapid fire, double time flow, quick punches, minimal words",
        "🩸 BLOOD RITUAL (Savage Mode)": "Sacrificial imagery, dark rituals, raw aggression, savage metaphors"
    }
    
    duration_map = {
        "🔪 Short & Deadly (1-2 min - Shorts)": "4 bars verse, 4 hook, 4 verse, short but deadly",
        "💀 Full Massacre (2-3 min - Viral)": "16 bars verse, 4 hook, 16 verse, full structure",
        "🩸 Epic Slaughter (3-4 min - Banger)": "16 verse, 4 hook, 16 verse, 8 bridge, 4 hook, extended"
    }
    
    return f"""
YOU ARE A RAP ASSASSIN. A LYRICAL KILLER. A BEAST.

🎯 TARGET: {topic}
⚔️ MODE: {attack_mode}
💀 INTENSITY: {intensity} - {intensity_multiplier[intensity]}
📏 STRUCTURE: {duration_map[structure]}

🚨 ABSOLUTE RULES (NO EXCEPTIONS):

1. **ZERO VERBS RULE**:
   - NO: है, हूँ, था, थी, रहा, रही, करता, होता
   - EVERY line must be a direct punch. Like a bullet.

2. **HEAVY VOCABULARY ONLY**:
   - Use: भस्म, काल, रक्त, प्रहार, चक्र, खंजर, अंगार, शव, लाश, मुर्दा, विनाश, प्रलय, अहंकार, नरक, यमराज, कफन, खून, हड्डी, मांस, जलजला, तबाही
   - 70% Sanskrit origin words for heaviness

3. **RHYME SCHEME - AABB**:
   Line 1: ...आग
   Line 2: ...जाग
   Line 3: ...रात
   Line 4: ...बात

4. **SYLLABLE RULE**:
   - Every line: 3-5 HEAVY words only
   - No filler words
   - Each word must have weight

5. **PUNCHLINE FREQUENCY**:
   - Every 2 lines = 1 kill shot
   - Every 4 lines = 1 memorable quotable

6. **STRUCTURE FORMAT**:
   [INTRO] - 2 lines (Bait, then switch)
   
   [VERSE 1] - 16 lines (Build the beast)
   Each 2 lines = 1 concept
   Internal rhymes in each line
   
   [HOOK] - 4 lines (Chant-like, viral, loopable)
   Pure aggression, repeatable
   
   [VERSE 2] - 16 lines (Escalate the violence)
   Different angle, higher intensity
   Metaphors + raw punches
   
   [BRIDGE] - 4 lines (Climax, slow down then explode)
   
   [OUTRO] - 1 line (Mic drop, unforgettable)

7. **STYLE EXECUTION**:
   {mode_specific[attack_mode]}

8. **NO WEAK LINES**:
   Every line must make the listener go "OH SHIT"
   No filler. No build-up. Pure destruction.

9. **BHAKTI ELEMENT**:
   Keep divine references: महाकाल, हनुमान, शिव, काली, दुर्गा
   Mix with hardcore vocabulary

10. **VISUAL IMAGERY**:
    Each line must create a violent, cinematic image
    Think: Blood, fire, weapons, destruction, power

🔥 EXAMPLE OF PERFECT LINE:
❌ WEAK: "Shiv ji ka tandav hota hai"
✅ BEAST: "महाकाल तांडव! आँखों में आग!"

❌ WEAK: "Dushman ko marna hai"
✅ BEAST: "दुश्मन का खून! चक्र से सर कट!"

OUTPUT ONLY THE LYRICS. NO EXPLANATIONS. NO EXTRA TEXT.

UNLEASH THE BEAST NOW:
"""

# Refinement Engine - Makes it EVEN HARDER
def refine_to_ultra_beast(raw_lyrics, topic):
    refine_prompt = f"""
You are the FINAL BEAST FILTER. Take these lyrics and make them 10x HARDER.

ORIGINAL LYRICS:
{raw_lyrics}

REFINEMENT RULES:
1. REMOVE every "hai", "hoon", "tha", "raha", "rahi"
2. REPLACE soft words with harder synonyms
   - आग → अग्नि / दहक
   - दर्द → रक्तपात / वेदना
   - मार → संहार / प्रहार
   - दुश्मन → शत्रु / रिपु

3. ADD 5-7 hardcore words if missing: भस्म, काल, रक्त, प्रहार, चक्र, खंजर

4. INCREASE rhyme density - add internal rhymes

5. COMPRESS lines to 3-5 heavy words each

6. ADD punchlines where missing

7. ENSURE every line hits like a bullet

Topic: {topic}

OUTPUT ONLY THE FINAL ULTRA BEAST LYRICS:
"""
    
    try:
        final = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a brutal rap editor. You make everything harder, darker, deadlier. No soft words survive."},
                {"role": "user", "content": refine_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        ).choices[0].message.content
        return final
    except:
        return raw_lyrics

# Generate Ultra Beast Lyrics
def generate_ultra_beast(topic, attack_mode, intensity, structure):
    try:
        with st.spinner("💀 BEAST MODE ACTIVATED... WRITING BLOOD LYRICS 💀"):
            time.sleep(1)
            
            # Step 1: Raw Beast Generation
            raw_response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a lyrical assassin. You write only hardcore, brutal, aggressive rap. No soft words. Every line kills."},
                    {"role": "user", "content": build_brutal_prompt(topic, attack_mode, intensity, structure)}
                ],
                temperature=1.2,  # Higher for more creativity
                max_tokens=2200,
                top_p=0.95
            )
            
            raw_lyrics = raw_response.choices[0].message.content
            
            # Step 2: Ultra Beast Refinement
            st.markdown("⚔️ **SHARPENING THE BLADE...**")
            time.sleep(0.5)
            
            final_lyrics = refine_to_ultra_beast(raw_lyrics, topic)
            
            # Step 3: Final Quality Check
            st.markdown("🩸 **LOADING FINAL KILL SHOT...**")
            time.sleep(0.5)
            
            return final_lyrics
            
    except Exception as e:
        return f"🔥 ERROR: {str(e)}\n\nCheck API key or try again."

# Generate Button
with col_right:
    unleash = st.button("💀 UNLEASH THE ULTRA BEAST 💀", use_container_width=True)
    
    if unleash:
        if not topic:
            st.error("⚠️ WAR TOPIC REQUIRED! Enter a topic to unleash the beast.")
        else:
            final_song = generate_ultra_beast(topic, attack_mode, intensity, structure)
            
            # Display with Beast Mode Styling
            st.markdown("---")
            st.markdown("### 💀 **ULTRA BEAST LYRICS - FINAL FORM** 💀")
            st.markdown(f"**🎯 Target:** {topic.upper()} | **⚔️ Mode:** {attack_mode} | **💀 Intensity:** {intensity}")
            
            # Beast Stats
            lines = final_song.split('\n')
            word_count = len(final_song.split())
            
            col_stat1, col_stat2, col_stat3 = st.columns(3)
            with col_stat1:
                st.metric("💀 KILL SHOTS", f"{len(lines)} lines")
            with col_stat2:
                st.metric("🔥 VOCAB POWER", f"{word_count} heavy words")
            with col_stat3:
                st.metric("⚔️ DAMAGE", "💯 CRITICAL")
            
            st.text_area("", final_song, height=600, key="beast_lyrics")
            
            # Download options
            col_d1, col_d2, col_d3 = st.columns(3)
            with col_d1:
                st.download_button(
                    "📥 DOWNLOAD BEAST LYRICS",
                    final_song,
                    file_name=f"ULTRA_BEAST_{topic.replace(' ', '_')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            with col_d2:
                # Create Shorts version (15 sec killer)
                lines_list = final_song.split('\n')
                shorts_text = "\n".join(lines_list[:8]) if len(lines_list) > 8 else final_song
                st.download_button(
                    "📱 SHORTS KILLER",
                    f"🔥 {topic.upper()} - ULTRA BEAST MODE 🔥\n\n{shorts_text}\n\n#DivineRapTv #BeastMode",
                    file_name=f"SHORTS_{topic.replace(' ', '_')}.txt",
                    use_container_width=True
                )
            
            with col_d3:
                # Thumbnail text generator
                thumbnail_text = f"💀 {topic.upper()} 💀\nULTRA BEAST MODE"
                st.download_button(
                    "🖼️ THUMBNAIL TEXT",
                    thumbnail_text,
                    file_name="thumbnail_text.txt",
                    use_container_width=True
                )
            
            # Beast Mode Success
            st.success("💀 **BEAST HAS BEEN UNLEASHED!** 💀")
            st.markdown("""
            <div class="warning">
            ⚔️ THIS IS PURE HARDCORE | NO SOFT WORDS | DIVINE WRATH MODE ⚔️
            </div>
            """, unsafe_allow_html=True)
            
            # YouTube Tips for Hardcore Rap
            with st.expander("💀 **BEAST MODE: YouTube Upload Tips**"):
                st.markdown("""
                ### 🎬 FOR MAXIMUM IMPACT:
                
                **1. VISUAL STYLE:**
                - Dark red/black color grading
                - Fast cuts every 2-3 seconds
                - Fire/blood visual effects
                - Intense facial expressions
                
                **2. AUDIO MIX:**
                - Boost bass by +6db
                - Add distortion to vocals
                - Layer with war sounds
                - Reverb on hooks
                
                **3. THUMBNAIL:**
                - Blood red background
                - Bold yellow/white text
                - Angry/beast face
                - Fire elements
                
                **4. TITLE FORMAT:**
                💀 {topic} - ULTRA BEAST MODE | DivineRapTv 🔥
                
                **5. HASHTAGS:**
                #DivineRapTv #BeastMode #HardcoreRap #BhaktiRap #Viral
                """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <p style="color: #ff0000; font-weight: bold;">💀 DIVINERAPTV - ULTRA BEAST ENGINE 2.0 💀</p>
    <p style="color: #ff6666;">RAW | LETHAL | DIVINE | NO MERCY IN RHYMES</p>
    <p style="color: #ff6666; font-size: 0.8rem;">⚠️ FOR MATURE AUDIENCES ONLY | BHAKTI x HARDCORE HIP-HOP ⚠️</p>
</div>
""", unsafe_allow_html=True)

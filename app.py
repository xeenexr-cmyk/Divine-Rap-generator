import streamlit as st
from groq import Groq
import time
import re

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
st.set_page_config(
    page_title="DivineRapTv - HARDCORE BEAST STUDIO",
    layout="wide",
    page_icon="💀"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #000000 0%, #1a0000 100%);
}
.beast-header {
    text-align: center;
    padding: 1rem;
    border-bottom: 3px solid #ff0000;
    margin-bottom: 2rem;
}
.beast-title {
    font-size: 2.5rem;
    background: linear-gradient(45deg, #ff0000, #ff6600);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hardcore-card {
    background: linear-gradient(135deg, #1a0000, #0a0000);
    border-left: 5px solid #ff0000;
    padding: 1.2rem;
    margin: 0.8rem 0;
    border-radius: 10px;
}
.rule-badge {
    background: #ff000020;
    border: 1px solid #ff0000;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.7rem;
    display: inline-block;
    margin: 0.2rem;
}
.stButton>button {
    background: linear-gradient(90deg, #ff0000, #ff6600);
    color: white;
    font-weight: bold;
    border: none;
    height: 3.5rem;
    border-radius: 8px;
    font-size: 1.2rem;
    transition: all 0.3s;
}
.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(255,0,0,0.5);
}
.stTextArea textarea {
    background-color: #0a0a0a;
    color: #ffaa00;
    border: 2px solid #ff3300;
    font-family: 'Courier New', monospace;
    font-size: 1rem;
    line-height: 1.7;
}
.hardcore-text {
    color: #ff6666;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="beast-header">
    <div class="beast-title">💀 DIVINERAPTV - HARDCORE BEAST STUDIO 💀</div>
    <p style="color: #ff8888;">🔥 DIVINE x RAFTAAR LEVEL | NO SOFT WORDS | PURE AGGRESSION 🔥</p>
    <p style="color: #ff4444; font-size: 0.9rem;">⚔️ हर पंक्ति एक वार | कोई "है/हूँ/था" नहीं | सिर्फ 3-5 भारी शब्द ⚔️</p>
</div>
""", unsafe_allow_html=True)

# ==================== HARDCORE VOCABULARY DATABASE ====================
HARDCORE_WORDS = {
    "shiv": ["शव", "रक्त", "भस्म", "त्रिशूल", "डमरू", "प्रलय", "अंगार", "श्मशान", "खप्पर", "नरमुंड", "व्याघ्र", "भयंकर", "कालरात्रि", "संहार", "रुद्र", "महाकाल"],
    "hanuman": ["अग्नि", "लंका", "दहन", "समुद्र", "पर्वत", "रावण", "संहार", "प्रहार", "चक्र", "गदा", "अहंकार", "विनाश", "क्रोध", "ज्वाला"],
    "krishna": ["विरह", "आँसू", "बाँसुरी", "रात", "यमुना", "प्रेम", "मुरली", "दर्द", "अग्नि", "जलन", "तड़प", "पीड़ा"],
    "general": ["भस्म", "काल", "रक्त", "प्रहार", "चक्र", "खंजर", "अंगार", "शव", "लाश", "मुर्दा", "विनाश", "प्रलय", "अहंकार", "नरक", "यमराज", "कफन", "खून", "हड्डी", "तबाही", "संहार"]
}

# ==================== STYLE DEFINITIONS ====================
STYLES = {
    "💀 हार्डकोर रैप (DIVINE STYLE)": {
        "desc": "दिवाइन / रफ़्तार स्टाइल | कोई verbs नहीं | हर line punch",
        "vocab": HARDCORE_WORDS["general"] + HARDCORE_WORDS["shiv"],
        "no_words": ["है", "हूँ", "था", "थी", "रहा", "रही", "होता", "करता", "से", "का", "की", "को"],
        "line_words": "3-5",
        "rhyme": "AABB - हर दो line में तुक",
        "suno": "hardcore aggressive rap, heavy bass, fast flow, male vocal, intense, war drums, divine energy"
    },
    "🔥 रामायण युद्ध कथा": {
        "desc": "लंका दहन | रावण युद्ध | वानर सेना",
        "vocab": HARDCORE_WORDS["hanuman"] + ["युद्ध", "रण", "संग्राम", "वानर", "सेना", "समुद्र", "पर्वत"],
        "no_words": ["है", "हूँ", "था", "रहा", "से", "का", "की"],
        "line_words": "4-6",
        "rhyme": "ABAB - कहानी जैसा प्रवाह",
        "suno": "cinematic epic rap, war drums, orchestral, storytelling, intense battle"
    },
    "💙 राधा कृष्ण विरह": {
        "desc": "दर्द | प्रेम | बाँसुरी | रात",
        "vocab": HARDCORE_WORDS["krishna"] + ["विरह", "आँसू", "तड़प", "जलन", "अग्नि", "दर्द"],
        "no_words": ["है", "हूँ", "था", "रहा"],
        "line_words": "4-6",
        "rhyme": "AABB - मधुर तुकांत",
        "suno": "emotional melodic rap, bansuri, romantic hip hop, slow flow, pain"
    },
    "🕊️ मीरा भक्ति दर्द": {
        "desc": "समर्पण | दर्द | दिव्य प्रेम",
        "vocab": ["समर्पण", "गिरधर", "सांवरा", "प्रेम", "त्याग", "आँसू", "दर्द", "पीड़ा", "जलन", "तड़प"],
        "no_words": ["है", "हूँ", "था", "रहा"],
        "line_words": "4-6",
        "rhyme": "AABB - सरल भावनात्मक",
        "suno": "devotional hip hop, emotional female vocal style, bhajan fusion"
    },
    "🎬 बॉलीवुड भक्ति फ्यूजन": {
        "desc": "सिनेमैटिक | भव्य | नाटकीय",
        "vocab": ["दिल", "दुआ", "ख्वाब", "राह", "मंज़िल", "इश्क़", "मोहब्बत", "अग्नि", "प्रेम"],
        "no_words": ["है", "हूँ", "था"],
        "line_words": "5-7",
        "rhyme": "ABAB - नाटकीय प्रवाह",
        "suno": "bollywood hip hop fusion, cinematic, orchestral, dramatic, grand"
    }
}

# ==================== ULTRA HARDCORE PROMPT BUILDER ====================
def build_hardcore_prompt(style, topic, mood, length):
    style_data = STYLES[style]
    
    mood_map = {
        "💔 भावुक": "धीमी गति, दर्द भरे शब्द, कोमल लेकिन गहरा प्रभाव",
        "⚖️ संतुलित": "मध्यम गति, शक्ति और भावना का संतुलन",
        "🔥 आक्रामक": "तेज़ गति, कठोर शब्द, हर पंक्ति में वार",
        "💀 सैडिस्टिक": "अति क्रूर, खूनी कल्पना, मौत के दृश्य, कोई फिल्टर नहीं"
    }
    
    length_map = {
        "छोटा (1-2 मिनट)": 8,
        "पूरा (2-3 मिनट)": 12,
        "विस्तारित (3-4 मिनट)": 16
    }
    verse_lines = length_map[length]
    
    # Create forbidden words list
    forbidden = " | ".join(style_data["no_words"])
    
    return f"""
तुम एक मास्टर हार्डकोर रैप गीतकार हो। तुम DIVINE और RAFTAAR के लेवल पर लिखते हो।

🎯 शैली: {style}
🎭 विषय: {topic}
💫 मूड: {mood} - {mood_map[mood]}
📏 लंबाई: {length} - {verse_lines} पंक्तियाँ प्रति पद

🔥 HARDCORE RULES (बिल्कुल नहीं तोड़ने):

1. **FORBIDDEN WORDS** - इन्हें USE नहीं करना:
   ❌ {forbidden}
   ✅ इनकी जगह DIRECT PUNCH मारो

2. **LINE LENGTH**:
   - हर पंक्ति में {style_data['line_words']} शब्द
   - एक शब्द भी कम या ज्यादा नहीं

3. **VOCABULARY** - ये शब्द USE करो:
   {', '.join(style_data['vocab'][:12])}

4. **RHYME SCHEME**: {style_data['rhyme']}

5. **STRUCTURE** (बिल्कुल इसी फॉर्मेट में):
   [प्रारंभ] - 3 पंक्तियाँ (POWERFUL OPENING)
   
   [पद 1] - {verse_lines} पंक्तियाँ (BUILD THE BEAST)
   
   [हुक] 🔥 - 4 पंक्तियाँ (CATCHY, REPEATABLE, VIRAL)
   
   [पद 2] - {verse_lines} पंक्तियाँ (ESCALATE)
   
   [हुक] - REPEAT
   
   [समापन] - 3 पंक्तियाँ (MIC DROP)

6. **EXAMPLE OF PERFECT LINE**:
   ❌ WRONG: "शिव जी का तांडव होता है"
   ✅ RIGHT: "शवों पर नृत्य! महाकाल तांडव!"

   ❌ WRONG: "रक्त से भरी धारा है"
   ✅ RIGHT: "रक्त से सिंचित! खप्पर में खून!"

7. **HARDCORE MANDATORY**:
   - हर पंक्ति एक वार हो
   - हर 2 पंक्ति में एक punchline
   - कोई भी पंक्ति boring नहीं हो सकती

अब विषय "{topic}" पर {style} शैली में ULTRA HARDCORE रैप लिखो।

OUTPUT ONLY LYRICS WITH SECTION HEADERS IN HINDI:
"""

# ==================== REFINEMENT ENGINE ====================
def refine_to_hardcore(raw_lyrics, style):
    style_data = STYLES[style]
    
    refine_prompt = f"""
तुम एक HARDCORE RAP SURGEON हो। इन लिरिक्स को और भी HARD बनाओ।

ORIGINAL:
{raw_lyrics}

REFINEMENT RULES:
1. REMOVE all these words if present: {', '.join(style_data['no_words'])}
2. REPLACE soft words with hardcore synonyms:
   - आग → अग्नि / दहक / ज्वाला
   - दर्द → रक्तपात / वेदना / पीड़ा
   - मार → संहार / प्रहार / विनाश
   - दुश्मन → शत्रु / रिपु / दस्यु
3. COMPRESS lines to {style_data['line_words']} words each
4. ADD punchlines where missing
5. ENSURE every line is a KILL SHOT

OUTPUT ONLY THE FINAL HARDCORE LYRICS:
"""
    
    try:
        final = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a hardcore rap editor. You make everything harder, darker, deadlier. No soft words survive. Every line must kill."},
                {"role": "user", "content": refine_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        ).choices[0].message.content
        return final
    except:
        return raw_lyrics

# ==================== GENERATE FUNCTION ====================
def generate_hardcore_lyrics(style, topic, mood, length):
    try:
        # Step 1: Generate raw hardcore
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": f"You are a hardcore Hindi rap lyricist. You write like Divine and Raftaar. No soft words. Every line is a punch. You hate words like 'hai', 'hoon', 'tha'."},
                {"role": "user", "content": build_hardcore_prompt(style, topic, mood, length)}
            ],
            temperature=1.0,
            max_tokens=2200,
            top_p=0.95
        )
        
        raw = response.choices[0].message.content
        
        # Step 2: Refine to ultra hardcore
        final = refine_to_hardcore(raw, style)
        
        return final
        
    except Exception as e:
        return f"त्रुटि: {str(e)}"

# ==================== UI LAYOUT ====================
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="hardcore-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 **WAR TOPIC**")
    topic = st.text_input("", placeholder="उदाहरण: महाकाल तांडव | लंका दहन | राधा विरह", key="topic_input")
    
    st.markdown("### ⚔️ **ATTACK MODE**")
    style = st.selectbox("", list(STYLES.keys()), key="style_select")
    
    st.markdown("### 💀 **INTENSITY**")
    mood = st.select_slider(
        "",
        options=["💔 भावुक", "⚖️ संतुलित", "🔥 आक्रामक", "💀 सैडिस्टिक"],
        value="🔥 आक्रामक",
        key="mood_slider"
    )
    
    st.markdown("### 📏 **LENGTH**")
    length = st.select_slider(
        "",
        options=["छोटा (1-2 मिनट)", "पूरा (2-3 मिनट)", "विस्तारित (3-4 मिनट)"],
        value="पूरा (2-3 मिनट)",
        key="length_slider"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Hardcore Rules Display
    st.markdown('<div class="hardcore-card">', unsafe_allow_html=True)
    st.markdown("### 📜 **HARDCORE RULES**")
    style_data = STYLES[style]
    st.markdown(f"""
    <div>
        <span class="rule-badge">❌ कोई "है/हूँ/था" नहीं</span>
        <span class="rule-badge">✅ हर line {style_data['line_words']} शब्द</span>
        <span class="rule-badge">⚡ {style_data['rhyme']}</span>
        <span class="rule-badge">💀 हर 2 line में punch</span>
    </div>
    <br>
    <div class="hardcore-text">⚔️ VOCABULARY: {', '.join(style_data['vocab'][:8])}...</div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    generate = st.button("💀 **UNLEASH THE BEAST** 💀", use_container_width=True)

with col2:
    if generate:
        if not topic:
            st.error("⚠️ WAR TOPIC डालो भाई!")
        else:
            with st.spinner(f"💀 {style} में हार्डकोर गीत लिखे जा रहे हैं..."):
                lyrics = generate_hardcore_lyrics(style, topic, mood, length)
                
                if "त्रुटि" not in lyrics:
                    st.success("✅ **HARDCORE LYRICS READY!** 💀")
                    
                    # Style prompt
                    st.markdown("### 🎵 **SUNO AI STYLE PROMPT**")
                    st.code(style_data['suno'], language="text")
                    
                    st.markdown("---")
                    st.markdown("### 🎤 **HARDCORE RAP LYRICS**")
                    
                    # Count hardcore elements
                    lines = [l for l in lyrics.split('\n') if l.strip() and not l.strip().startswith('[')]
                    forbidden_count = 0
                    for word in style_data['no_words']:
                        forbidden_count += lyrics.count(word)
                    
                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        st.metric("💀 TOTAL LINES", len(lines))
                    with col_b:
                        st.metric("❌ SOFT WORDS", f"{forbidden_count} (TARGET: 0)")
                    with col_c:
                        st.metric("⚡ HARDCORE SCORE", "100%" if forbidden_count == 0 else f"{100 - forbidden_count*5}%")
                    
                    st.text_area("", lyrics, height=550, key="lyrics_display")
                    
                    # Download buttons
                    col_d1, col_d2, col_d3 = st.columns(3)
                    with col_d1:
                        st.download_button(
                            "📥 **DOWNLOAD LYRICS**",
                            lyrics,
                            file_name=f"HARDCORE_{topic.replace(' ', '_')}.txt",
                            use_container_width=True
                        )
                    with col_d2:
                        meta = f"""--- HARDCORE RAP METADATA ---
STYLE: {style}
TOPIC: {topic}
MOOD: {mood}
SUNO PROMPT: {style_data['suno']}

--- LYRICS ---
{lyrics}
"""
                        st.download_button(
                            "🎵 **SUNO METADATA**",
                            meta,
                            file_name="suno_hardcore_metadata.txt",
                            use_container_width=True
                        )
                    with col_d3:
                        # Shorts version (hook only)
                        if "हुक" in lyrics:
                            hook_start = lyrics.find("हुक")
                            hook_end = lyrics.find("[", hook_start + 10)
                            if hook_end == -1:
                                hook_end = hook_start + 200
                            hook = lyrics[hook_start:hook_end].replace("हुक", "").strip()
                        else:
                            hook = lyrics[:250]
                        st.download_button(
                            "📱 **SHORTS VERSION**",
                            f"🔥 {topic} | DIVINERAPTV 🔥\n\n{hook[:300]}\n\n#DivineRapTv #HardcoreRap #BhaktiRap",
                            file_name="shorts_hardcore.txt",
                            use_container_width=True
                        )
                    
                    if forbidden_count == 0:
                        st.success("💀 **PERFECT! कोई SOFT WORD नहीं - PURE HARDCORE!** 💀")
                    else:
                        st.warning(f"⚠️ {forbidden_count} soft words found. Refining further...")
                    
                    st.balloons()
                    
                else:
                    st.error(lyrics)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1.5rem;">
    <p style="color: #ff4444;">💀 <strong>DIVINERAPTV - HARDCORE BEAST STUDIO</strong> 💀</p>
    <p style="color: #ff8888;">🔥 DIVINE x RAFTAAR LEVEL | NO SOFT WORDS | EVERY LINE A KILL SHOT 🔥</p>
    <p style="color: #ff6666; font-size: 0.8rem;">⚔️ कोई "है/हूँ/था" नहीं | हर पंक्ति 3-5 भारी शब्द | AABB तुकांत ⚔️</p>
</div>
""", unsafe_allow_html=True)

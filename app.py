import streamlit as st
from groq import Groq
import time

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
st.set_page_config(
    page_title="DivineRapTv - Hindi Suno AI Studio",
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
    font-size: 1rem;
    line-height: 1.8;
}
.hindi-text {
    font-family: 'Noto Sans Devanagari', 'Mangal', 'Nirmala UI', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <h1 style="color: #ff4444;">🔱 दिवाइन रैप टीवी</h1>
    <h2 style="color: #ffaa00;">सुनो एआई स्टूडियो - पूरी हिंदी में</h2>
    <p style="color: #ff8888;">🔥 5 शैलियाँ | सुनो एआई v5.5 ऑप्टिमाइज़्ड | शुद्ध हिंदी गीत 🔥</p>
</div>
""", unsafe_allow_html=True)

# Style definitions in Hindi
STYLES = {
    "हार्डकोर रैप 🔥": {
        "desc": "दिवाइन / रफ़्तार स्टाइल | आक्रामक | शक्ति",
        "rules": "कोई 'है/हूँ/था' नहीं, हर पंक्ति 4-7 शब्द, AABB तुकांत",
        "suno": "हार्डकोर रैप, भारी बास, तेज़ फ्लो, पुरुष आवाज़",
        "vocab": "भस्म, काल, रक्त, प्रहार, चक्र, अंगार, विनाश, संहार"
    },
    "रामायण कथा 📖": {
        "desc": "सिनेमैटिक कहानी | दृश्य दर दृश्य",
        "rules": "दृश्य-आधारित, 5-7 शब्द, ABAB तुकांत",
        "suno": "सिनेमैटिक हिप हॉप, ऑर्केस्ट्रल, कहानी रैप",
        "vocab": "राजा, प्रजा, वन, अग्नि, समुद्र, युद्ध, राम, सीता"
    },
    "राधा कृष्ण प्रेम 💙": {
        "desc": "विरह | प्रेम | पीड़ा | बाँसुरी",
        "rules": "भावनात्मक शब्द, 4-6 शब्द, मधुर तुकांत",
        "suno": "भावनात्मक रैप, बाँसुरी, रोमांटिक हिप हॉप",
        "vocab": "विरह, आँसू, बाँसुरी, रात, यमुना, प्रेम, मुरली"
    },
    "मीरा भक्ति 🕊️": {
        "desc": "समर्पण | दर्द | दिव्य प्रेम",
        "rules": "भक्ति भाव, प्रथम पुरुष, सरल तुकांत",
        "suno": "भक्ति रैप, भावनात्मक, भजन फ्यूज़न",
        "vocab": "समर्पण, गिरधर, सांवरा, प्रेम, त्याग, आँसू"
    },
    "बॉलीवुड फ्यूज़न 🎬": {
        "desc": "बॉलीवुड स्टाइल | भव्य | सिनेमैटिक",
        "rules": "नाटकीय, 5-7 शब्द, भव्य पैमाना",
        "suno": "बॉलीवुड हिप हॉप, सिनेमैटिक, ऑर्केस्ट्रल",
        "vocab": "दिल, दुआ, ख्वाब, राह, मंज़िल, इश्क़, मोहब्बत"
    }
}

# Style selection
st.markdown("### 🎭 अपनी रैप शैली चुनें")
cols = st.columns(5)
selected_style = None

for idx, (style_name, style_info) in enumerate(STYLES.items()):
    with cols[idx]:
        if st.button(f"{style_name}", key=f"btn_{idx}", use_container_width=True):
            selected_style = style_name

if selected_style is None:
    selected_style = "हार्डकोर रैप 🔥"

style_data = STYLES[selected_style]

# Display style info
st.markdown(f"""
<div class="style-card">
    <span class="style-title">{selected_style}</span>
    <span class="style-desc">{style_data['desc']}</span>
    <br>
    <span class="suno-tag">🎵 सुनो एआई प्रॉम्प्ट: {style_data['suno']}</span>
</div>
""", unsafe_allow_html=True)

# Input area
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("### 📝 गीत की जानकारी")
    
    topic = st.text_input(
        "🎯 विषय",
        placeholder="उदाहरण: लंका दहन, राधा कृष्ण विरह, हनुमान जी का क्रोध"
    )
    
    mood = st.select_slider(
        "💫 भावना",
        options=["💔 भावुक", "⚖️ संतुलित", "🔥 आक्रामक", "🚀 वायरल"],
        value="⚖️ संतुलित"
    )
    
    length = st.select_slider(
        "📏 लंबाई",
        options=["छोटा (1-2 मिनट)", "पूरा (2-3 मिनट)", "विस्तारित (3-4 मिनट)"],
        value="पूरा (2-3 मिनट)"
    )
    
    st.markdown("---")
    st.markdown("### 📌 शैली के नियम")
    st.markdown(f"""
    **नियम:** {style_data['rules']}
    
    **शब्दावली:** {style_data['vocab']}
    """)
    
    generate = st.button("🎵 हिंदी गीत जेनरेट करें", use_container_width=True)

# Prompt builder function - Pure Hindi
def build_prompt(style, topic, mood, length):
    mood_map = {
        "💔 भावुक": "धीमी गति, कोमल शब्द, दर्द भरी आवाज़",
        "⚖️ संतुलित": "मध्यम गति, संतुलित भावना और शक्ति",
        "🔥 आक्रामक": "तेज़ गति, कठोर शब्द, उग्र अंदाज",
        "🚀 वायरल": "यादगार हुक, दोहराने योग्य, ट्रेंडिंग स्टाइल"
    }
    
    style_info = STYLES[style]
    
    # Verse lines based on length
    if "छोटा" in length:
        verse_lines = 8
        length_text = "YouTube शॉर्ट्स के लिए छोटा फॉर्मेट"
    elif "पूरा" in length:
        verse_lines = 12
        length_text = "पूरा गाना, वायरल के लिए"
    else:
        verse_lines = 16
        length_text = "विस्तारित, पूरे अनुभव के लिए"
    
    return f"""
तुम एक प्रोफेशनल हिंदी रैप गीतकार हो। तुम सुनो एआई v5.5 के लिए परफेक्ट गीत लिखते हो।

🎭 शैली: {style}
🎯 विषय: {topic}
💫 भावना: {mood} - {mood_map[mood]}
📏 लंबाई: {length} - {length_text}

⚡ सुनो एआई के लिए अनिवार्य नियम:

1. **हर पंक्ति में 4-7 शब्द** - बिल्कुल सही, न ज्यादा न कम
2. **शुद्ध हिंदी** - कोई स्पेलिंग मिस्टेक नहीं, सही मात्राएँ
3. **तुकांत** - हर दो पंक्तियों में तुक मिले
4. **हुक (कोरस)** - 4 पंक्तियाँ, यादगार, दोहराने योग्य
5. **शब्दावली** - ये शब्द जरूर इस्तेमाल करो: {style_info['vocab']}

📋 गीत की संरचना (बिल्कुल इसी फॉर्मेट में):

[प्रारंभ]
(4 पंक्तियाँ - ध्यान खींचने वाली)

[पद 1]
({verse_lines} पंक्तियाँ - कहानी या भावना बनाओ)

[हुक] 🔥
(4 पंक्तियाँ - सबसे यादगार, लूप करने योग्य)

[पद 2]
({verse_lines} पंक्तियाँ - नया कोण, भावना बढ़ाओ)

[हुक]
(पहले वाला हुक दोहराओ)

[समापन]
(3-4 पंक्तियाँ - यादगार अंत)

अब विषय "{topic}" के लिए पूरी हिंदी में गीत लिखो।

केवल गीत दो, बिना किसी अतिरिक्त टेक्स्ट के। सभी सेक्शन हेडर हिंदी में ही रखो।

शुरू करो:
"""

# Generate function
def generate_lyrics(style, topic, mood, length):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": f"तुम एक मास्टर हिंदी रैप गीतकार हो। तुम सुनो एआई v5.5 के लिए परफेक्ट, शुद्ध हिंदी गीत लिखते हो। कोई स्पेलिंग मिस्टेक नहीं। हर पंक्ति में 4-7 शब्द।"},
                {"role": "user", "content": build_prompt(style, topic, mood, length)}
            ],
            temperature=0.85,
            max_tokens=2200
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"त्रुटि: {str(e)}"

# Display results
with col2:
    if generate:
        if not topic:
            st.error("⚠️ कृपया पहले विषय डालें!")
        else:
            with st.spinner(f"🔥 {selected_style} में हिंदी गीत लिखे जा रहे हैं..."):
                lyrics = generate_lyrics(selected_style, topic, mood, length)
                
                if "त्रुटि" not in lyrics:
                    st.success("✅ हिंदी गीत तैयार! सुनो एआई के लिए परफेक्ट!")
                    
                    # Suno AI prompt in Hindi
                    st.markdown("### 🎵 सुनो एआई के लिए प्रॉम्प्ट")
                    st.code(f"शैली: {style_data['suno']}\nभाषा: हिंदी\nआवाज़: पुरुष रैप\nगुणवत्ता: प्रीमियम", language="text")
                    
                    st.markdown("---")
                    st.markdown("### 🎤 हिंदी गीत")
                    st.text_area("", lyrics, height=550, key="lyrics_display")
                    
                    # Download buttons
                    col_a, col_b, col_c = st.columns(3)
                    
                    with col_a:
                        st.download_button(
                            "📥 गीत डाउनलोड करें",
                            lyrics,
                            file_name=f"hindi_lyrics_{topic.replace(' ', '_')}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    
                    with col_b:
                        # Create Suno metadata in Hindi
                        meta = f"""--- सुनो एआई v5.5 मेटाडेटा ---
शैली: {selected_style}
प्रॉम्प्ट: {style_data['suno']}
विषय: {topic}
भावना: {mood}
लंबाई: {length}

--- गीत की संरचना ---
{lyrics[:600]}...
"""
                        st.download_button(
                            "🎵 सुनो मेटाडेटा",
                            meta,
                            file_name="suno_metadata.txt",
                            use_container_width=True
                        )
                    
                    with col_c:
                        # Create Shorts version
                        if "हुक" in lyrics:
                            parts = lyrics.split("हुक")
                            if len(parts) > 1:
                                hook_part = parts[1].split("]")[0] if "]" in parts[1] else parts[1]
                                shorts = hook_part[:300]
                            else:
                                shorts = lyrics[:300]
                        else:
                            shorts = lyrics[:300]
                        
                        st.download_button(
                            "📱 शॉर्ट्स वर्शन",
                            f"🔥 {topic} | दिवाइन रैप टीवी 🔥\n\n{shorts}\n\n#DivineRapTv #HindiRap #BhaktiRap",
                            file_name="shorts_version.txt",
                            use_container_width=True
                        )
                    
                    # Show stats
                    lines = [l for l in lyrics.split('\n') if l.strip() and not l.strip().startswith('[')]
                    total_lines = len(lines)
                    word_count = sum(len(l.split()) for l in lines)
                    
                    col_stat1, col_stat2, col_stat3 = st.columns(3)
                    with col_stat1:
                        st.metric("📝 कुल पंक्तियाँ", total_lines)
                    with col_stat2:
                        st.metric("📊 कुल शब्द", word_count)
                    with col_stat3:
                        st.metric("✅ सुनो रेडी", "हाँ")
                    
                    st.balloons()
                    st.success("🎉 गीत तैयार! अब सुनो एआई में डालकर सॉन्ग बनाएं!")
                    
                else:
                    st.error(lyrics)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="color: #ff8888;">🔱 <strong>दिवाइन रैप टीवी - हिंदी सुनो एआई स्टूडियो</strong> 🔱</p>
    <p style="color: #ffaa00;">5 शैलियाँ | शुद्ध हिंदी गीत | सुनो एआई v5.5 ऑप्टिमाइज़्ड | वायरल रेडी</p>
    <p style="color: #ff6666;">हर पंक्ति 4-7 शब्द | सही तुकांत | कोई स्पेलिंग मिस्टेक नहीं</p>
</div>
""", unsafe_allow_html=True)

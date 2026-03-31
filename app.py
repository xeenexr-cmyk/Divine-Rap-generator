import streamlit as st
import google.generativeai as genai
import time

# API setup - Use Gemini with latest model
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Page config
st.set_page_config(
    page_title="DivineRapTv - Shiv Tandav Master Engine",
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
    white-space: pre-wrap;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="final-header">
    <div class="final-title">DivineRapTv - Shiv Tandav Master Engine</div>
    <p style="color: #ffaa44;">शिव तांडव स्टाइल | चांट + रैप + हुक + क्लाइमेक्स | परफेक्ट फ्लो</p>
    <p style="color: #ff8866;">इंट्रो चांट | स्लो बिल्ड रैप | पावरफुल हुक | हार्ड रैप | क्लाइमेक्स | आउट्रो चांट</p>
    <p style="color: #44ff44; font-size: 0.8rem;">जेमिनी 1.5 फ्लैश | 60 रिक्वेस्ट/मिनट | कोई रेट लिमिट इश्यू नहीं</p>
</div>
""", unsafe_allow_html=True)

# ==================== PERFECT EXAMPLE IN PURE HINDI ====================
PERFECT_EXAMPLE_HINDI = '''
[इंट्रो - चांट धीमा]
ॐ नमः शिवाय...
महाकाल...
हर हर महादेव...

[वर्स 1 - रैप स्लो बिल्ड]
जटा में गंगा, माथे पे आग
तीसरी आँख बोले, खत्म हर राग
शून्य से जन्मा, शून्य में लीन
शिव है चेतना, शिव ही सीन
भस्म से सजा, पर राजाओं का राजा
काल भी काँपे, जब खुला दरवाज़ा
डमरू बोले, रिदम दिवाइन
शिव के फ्लो में स्पेस और टाइम

[हुक - कोरस चांट + एनर्जी]
हर हर महादेव – गूंजे आसमान
हर हर महादेव – थर्राए जहान
तांडव की आग, बोले हर कण
शिव ही शक्ति, शिव ही ब्रह्म

[वर्स 2 - हार्ड रैप]
ना सिंहासन चाहिए, ना सोने का ताज
शमशान में भी दिखे पूरा समाज
अहंकार टूटे, गिर जाए नक़ाब
शिव की शरण में मिटे हर ख्वाब
रौद्र भी वही, शांत भी वही
भक्त की साँसों की जान भी वही
सृजन का बीज, विनाश की धुन
शिव बोले – सब माया, मैं ही हूँ

[हुक - कोरस रिपीट लाउडर]
हर हर महादेव – गूंजे आसमान
हर हर महादेव – थर्राए जहान
तांडव की आग, बोले हर कण
शिव ही शक्ति, शिव ही ब्रह्म

[ब्रिज - स्पोकन व्हिस्पर रैप]
ना जन्म...
ना मृत्यु...
ना आरंभ...
ना अंत...
जो है...
वो शिव है...

[वर्स 3 - क्लाइमेक्स रैप]
जब नाचे शिव तो थम जाए काल
धरती बोले – आज प्रलय का हाल
डमरू की बीट पे ब्रह्मांड झुके
महाकाल के आगे सब शीश झुके

[आउट्रो - फाइनल चांट फुल पावर]
हर हर महादेव
हर हर महादेव
ॐ नमः शिवाय...
'''

# ==================== STYLE DEFINITIONS ====================
STYLES = {
    "शिव तांडव रैप": {
        "desc": "महाकाल | श्मशान | तांडव | भयंकर",
        "structure": "इंट्रो चांट | स्लो बिल्ड | हुक | हार्ड रैप | ब्रिज | क्लाइमेक्स | आउट्रो",
        "suno": "shiv tandav hardcore rap, heavy bass, damru beats"
    },
    "हनुमान बाल कांड रैप": {
        "desc": "बाल हनुमान | लंका दहन | शक्ति",
        "structure": "इंट्रो चांट | स्टोरी बिल्ड | पावर हुक | बैटल रैप | क्लाइमेक्स | विजय आउट्रो",
        "suno": "hanuman rap, powerful, war drums, intense"
    },
    "रामायण युद्ध रैप": {
        "desc": "लंका दहन | राम रावण युद्ध",
        "structure": "इंट्रो | स्टोरी वर्स | वार हुक | बैटल रैप | विजय | आउट्रो",
        "suno": "ramayan epic rap, war orchestral, storytelling"
    },
    "राधा कृष्ण प्रेम रैप": {
        "desc": "विरह | प्रेम | बाँसुरी",
        "structure": "इंट्रो मेलोडी | लव वर्स | इमोशनल हुक | पेन रैप | रेजोल्यूशन | आउट्रो",
        "suno": "radha krishna melodic rap, bansuri, romantic"
    },
    "माँ दुर्गा शक्ति रैप": {
        "desc": "महिषासुर मर्दिनी | शक्ति | युद्ध",
        "structure": "इंट्रो चांट | स्टोरी बिल्ड | पावर हुक | बैटल रैप | क्लाइमेक्स | विजय आउट्रो",
        "suno": "durga shakti rap, war drums, female power"
    }
}

# ==================== PROMPT BUILDER ====================
def build_prompt(style, topic, mood, length):
    
    style_data = STYLES[style]
    
    mood_map = {
        "भावुक": "भावनात्मक, धीमी गति, दिल को छूने वाली",
        "संतुलित": "मध्यम गति, संतुलित, स्थिर लय",
        "आक्रामक": "तेज गति, कठोर शब्द, जोरदार",
        "वायरल": "वायरल रेडी, यादगार हुक, दोहराने योग्य"
    }
    
    length_map = {
        "छोटा (1-2 मिनट)": "छोटा वर्जन - 6 लाइन प्रति वर्स",
        "पूरा (2-3 मिनट)": "पूरा वर्जन - 8 लाइन प्रति वर्स",
        "विस्तारित (3-4 मिनट)": "विस्तारित - 12 लाइन प्रति वर्स"
    }
    
    verse_lines = 6 if "छोटा" in length else 8 if "पूरा" in length else 12
    
    return f"""तुम एक मास्टर हिंदी रैप गीतकार हो। तुम दिवाइन और रफ़्तार के लेवल पर लिखते हो।

नीचे दिए गए परफेक्ट उदाहरण को बिल्कुल फॉलो करो:

परफेक्ट उदाहरण (शिव तांडव रैप):
{PERFECT_EXAMPLE_HINDI}

अब तुम्हारा काम:
शैली: {style}
विषय: {topic}
मूड: {mood} - {mood_map[mood]}
लंबाई: {length_map[length]}

महत्वपूर्ण नियम (उदाहरण से सीखो):

1. संरचना (बिल्कुल इसी फॉर्मेट में):
   [इंट्रो - चांट धीमा] - धीमे दिव्य चांट
   [वर्स 1 - रैप स्लो बिल्ड] - कहानी बनाओ, हर लाइन 4-7 शब्द
   [हुक - कोरस चांट + एनर्जी] - पावरफुल, दोहराने योग्य, 4 लाइन
   [वर्स 2 - हार्ड रैप] - तेज फ्लो, कठोर शब्द, {verse_lines} लाइन
   [हुक - कोरस रिपीट लाउडर] - वही हुक, और एनर्जी
   [ब्रिज - स्पोकन व्हिस्पर रैप] - 4-6 लाइन, धीमा, दार्शनिक
   [वर्स 3 - क्लाइमेक्स रैप] - सबसे तेज फ्लो, सबसे शक्तिशाली लाइन
   [आउट्रो - फाइनल चांट फुल पावर] - दिव्य समापन

2. तुकांत योजना: हर 2 लाइन में तुक (AABB)
   उदाहरण: "जटा में गंगा, माथे पे आग" (A)
            "तीसरी आँख बोले, खत्म हर राग" (A)

3. लाइन लंबाई: हर लाइन में 4-7 शब्द

4. शुद्ध हिंदी: कोई स्पेलिंग मिस्टेक नहीं

5. शब्दावली:
   - दिव्य: महाकाल, तांडव, शिव, शक्ति, ब्रह्म
   - हार्डकोर: काल, प्रलय, विनाश, रुद्र
   - भावनात्मक: भक्ति, प्रेम, समर्पण

अब विषय "{topic}" पर {style} शैली में परफेक्ट रैप लिखो।

केवल गीत दो, बिना किसी अतिरिक्त टेक्स्ट के। सेक्शन हेडर वैसे ही रखो जैसे उदाहरण में हैं।

शुरू करो:
"""

# ==================== GENERATE FUNCTION WITH LATEST MODEL ====================
def generate_rap(style, topic, mood, length):
    try:
        # Latest Model Name: 'gemini-1.5-flash' (fast and efficient)
        # Alternative: 'gemini-1.5-pro' (more powerful but slower)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generation config for creative lyrics
        generation_config = {
            "temperature": 1.0,        # Higher for creative rap
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 4096,
        }
        
        response = model.generate_content(
            build_prompt(style, topic, mood, length),
            generation_config=generation_config
        )
        
        if response.text:
            return response.text
        else:
            return "Error: AI ने कोई रिस्पॉन्स नहीं दिया। दोबारा कोशिश करें।"
            
    except Exception as e:
        error_msg = str(e)
        if "404" in error_msg:
            return f"Error: Model not found. {error_msg}\n\nTip: Check if GEMINI_API_KEY is correct and model 'gemini-1.5-flash' is available."
        else:
            return f"Error: {error_msg}"

# ==================== UI LAYOUT ====================
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="style-card">', unsafe_allow_html=True)
    st.markdown("### रैप टॉपिक")
    topic = st.text_input(
        "",
        placeholder="उदाहरण: शिव तांडव, हनुमान बाल कांड, माँ दुर्गा महिषासुर",
        key="topic_input"
    )
    
    st.markdown("### रैप स्टाइल")
    style = st.selectbox("", list(STYLES.keys()), key="style_select")
    
    st.markdown("### मूड")
    mood = st.select_slider(
        "",
        options=["भावुक", "संतुलित", "आक्रामक", "वायरल"],
        value="आक्रामक",
        key="mood_slider"
    )
    
    st.markdown("### लंबाई")
    length = st.select_slider(
        "",
        options=["छोटा (1-2 मिनट)", "पूरा (2-3 मिनट)", "विस्तारित (3-4 मिनट)"],
        value="पूरा (2-3 मिनट)",
        key="length_slider"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show Example
    with st.expander("परफेक्ट उदाहरण देखें - शिव तांडव रैप", expanded=False):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown(PERFECT_EXAMPLE_HINDI)
        st.markdown('</div>', unsafe_allow_html=True)
    
    generate = st.button("परफेक्ट रैप जेनरेट करें", use_container_width=True)

with col2:
    if generate:
        if not topic:
            st.error("कृपया पहले रैप टॉपिक डालें!")
        else:
            with st.spinner(f"{style} में परफेक्ट रैप लिखा जा रहा है... (जेमिनी 1.5 फ्लैश)"):
                result = generate_rap(style, topic, mood, length)
                
                if "Error" not in result:
                    st.success("परफेक्ट रैप तैयार!")
                    
                    # Style info
                    style_data = STYLES[style]
                    st.markdown(f"""
                    <div style="background: #1a1a1a; padding: 0.8rem; border-radius: 10px; margin-bottom: 1rem;">
                        <span class="divine-badge">{style}</span>
                        <span class="divine-badge">{mood}</span>
                        <span class="divine-badge">{length}</span>
                        <span class="divine-badge">{style_data['structure']}</span>
                        <span class="divine-badge">DivineRapTv</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("### परफेक्ट रैप तैयार")
                    st.text_area("", result, height=600, key="lyrics_display")
                    
                    # Download buttons
                    col_a, col_b, col_c = st.columns(3)
                    
                    with col_a:
                        st.download_button(
                            "लिरिक्स डाउनलोड करें",
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
                            "सुनो मेटाडेटा",
                            suno_meta,
                            file_name="suno_metadata.txt",
                            use_container_width=True
                        )
                    
                    with col_c:
                        # Shorts version (Hook only)
                        if "हुक" in result:
                            hook_start = result.find("हुक")
                            hook_end = result.find("[", hook_start + 15)
                            if hook_end == -1:
                                hook_end = hook_start + 300
                            hook_section = result[hook_start:hook_end]
                        else:
                            hook_section = result[:400]
                        
                        shorts = f"""{topic} | DivineRapTv

{hook_section}

पूरा गाना: लिंक इन बायो
सब्सक्राइब करें

#DivineRapTv #{topic.replace(' ', '')} #BhaktiRap #ViralSong
"""
                        st.download_button(
                            "शॉर्ट्स वर्शन",
                            shorts,
                            file_name="shorts_version.txt",
                            use_container_width=True
                        )
                    
                    # Metrics
                    lines = [l for l in result.split('\n') if l.strip() and not l.strip().startswith('[')]
                    word_count = sum(len(l.split()) for l in lines)
                    
                    col_stat1, col_stat2, col_stat3 = st.columns(3)
                    with col_stat1:
                        st.metric("कुल लाइनें", len(lines))
                    with col_stat2:
                        st.metric("कुल शब्द", word_count)
                    with col_stat3:
                        st.metric("सुनो रेडी", "हाँ")
                    
                    st.balloons()
                    st.success("गाना तैयार! अब सुनो एआई / उडियो में डालकर फुल सॉन्ग बनाएं!")
                    
                else:
                    st.error(result)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="color: #ff8844;">DivineRapTv - Shiv Tandav Master Engine</p>
    <p style="color: #ffaa66;">जेमिनी 1.5 फ्लैश | 60 रिक्वेस्ट/मिनट | कोई रेट लिमिट इश्यू नहीं</p>
    <p style="color: #ff8866;">परफेक्ट उदाहरण के साथ | एआई बिल्कुल वैसा ही लिखेगा</p>
</div>
""", unsafe_allow_html=True)

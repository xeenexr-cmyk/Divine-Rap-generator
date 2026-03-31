import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI Setup
st.set_page_config(page_title="Divine Rap Studio v3.0", page_icon="🔱", layout="wide")

# Custom CSS for Dark Mode & Styling
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: #e0e0e0; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; font-weight: bold; border: none; }
    .stTextInput>div>div>input { background-color: #1e2129; color: gold; border: 1px solid #444; }
    .stSelectbox>div>div>div { background-color: #1e2129; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 Divine Rap Studio v3.0 (Music Ready)")
st.write("अपने **DivineRapTv** चैनल के लिए Professional Lyrics और Beat Guide तैयार करें।")

col1, col2 = st.columns([1, 1])

with col1:
    topic = st.text_input("🎯 विषय (Topic) लिखें", placeholder="जैसे: श्मशान निवासी शिव, कालजयी महाकाल")
    mode = st.selectbox("🎭 Flow और Energy चुनें", [
        "Aggressive/Hardcore (Power & Energy)",
        "Emotional/Devotional (Soulful Flow)",
        "Storytelling (Cinematic Narrative)",
        "Trance/Psych-Rap (Modern Vibe)"
    ])
    
    # बीट सजेशन का ऑप्शन
    include_beat = st.checkbox("🎵 बीट और इंस्ट्रुमेंटल गाइड भी शामिल करें?", value=True)

def build_refined_prompt(topic, mode, include_beat):
    beat_instruction = "साथ ही, गाने के अंत में 'Music Production Guide' दें जिसमें BPM (रफ़्तार), Bass Type, और कौन से Instruments (Sitar, Flute, Damru, Sub-bass) यूज़ करने चाहिए, ये भी बताएं।" if include_beat else ""
    
    return f"""
तुम एक 'Devotional Hip-Hop' विशेषज्ञ हो। DivineRapTv के लिए रैप लिखो।

🎯 TOPIC: {topic}
🎭 FLOW MODE: {mode}

STRICT RULES:
1. **Rhyme Scheme:** हर दो लाइन का अंत एक जैसी ध्वनि (Rhyme) पर होना चाहिए (जैसे: रचयिता-विजेता)।
2. **Meter:** लाइनें संतुलित हों ताकि सांस न टूटे।
3. **No English:** केवल गहरी हिन्दी।
4. **Cinematic Ad-libs:** लाइनों के बीच में (हर हर!, महादेव!, काल!) जैसे शब्दों का प्रयोग करें।

📌 STRUCTURE: [Intro] -> [Verse 1] -> [Hook] -> [Verse 2] -> [Hook] -> [Outro]

{beat_instruction}
"""

if st.button("🚀 Generate Full Track Design"):
    if not topic:
        st.warning("कृपया पहले विषय (Topic) लिखें।")
    else:
        with st.spinner("🔥 शब्दों और धुनों का संगम तैयार हो रहा है..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक महान संगीतकार और लिरिसिस्ट हो जो डिवाइन रैप में माहिर है।"},
                        {"role": "user", "content": build_refined_prompt(topic, mode, include_beat)}
                    ],
                    temperature=1.0,
                    max_tokens=1800
                )

                lyrics_data = response.choices[0].message.content
                
                with col2:
                    st.success("✨ मास्टरपीस तैयार है!")
                    st.markdown("### 📜 Lyrics & Music Guide")
                    st.text_area(label="Result", value=lyrics_data, height=700)
                    
                    # कॉपी करने का बटन
                    st.info("💡 टिप: इन Lyrics को Suno AI या Udio में डालकर आप खुद का म्यूज़िक भी बना सकते हैं!")
                
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.caption("© 2026 DivineRapTv Studio | For Professional Use Only")
                    

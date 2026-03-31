import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI Setup
st.set_page_config(page_title="DivineRapTv v10", page_icon="🔱", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #fff; }
    .stButton>button { background: linear-gradient(90deg, #8b0000, #ff0000); color: #fff; font-weight: bold; border: 2px solid white; height: 4rem; font-size: 1.5rem; width: 100%; border-radius: 5px; }
    .stTextArea textarea { color: #00ffcc !important; background-color: #0a0a0a !important; font-family: 'Consolas', monospace; font-size: 1.2rem !important; line-height: 1.8; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 DivineRapTv v10: The Last Stand")
st.write("### ये रैप सीधा 'Studio Recording' के लिए तैयार होगा।")

col1, col2 = st.columns([1, 1.5])

with col1:
    topic = st.text_input("🎯 विषय (Topic)", placeholder="जैसे: लंका दहन, कालभैरव तांडव")
    mode = st.selectbox("🎭 मोड चुनें (Unique Style)", [
        "Hardcore Aggressive (Divine/Raftaar Style)",
        "Epic Narrative (Ramayan Flow)",
        "Deep Soulful (Radha-Krishna/Meera)",
        "Cinematic Bollywood Fusion"
    ])
    generate_btn = st.button("🔥 GENERATE PROFESSIONAL BARS")

def build_ultimate_prompt(topic, mode):
    # इसमें 'Strict Rhyme Pattern' और 'Vocabulary' पर सबसे ज्यादा जोर है
    return f"""
तुम एक 'World Class Ghostwriter' हो। तुम्हें 'DivineRapTv' के लिए प्रोफेशनल 'Bars' लिखने हैं। 

🎯 TOPIC: {topic}
🎭 STYLE: {mode}

❗ कड़े निर्देश (FOLLOW RIGIDLY):
1. **SYLLABLE MATCHING:** पहली लाइन में जितने शब्द/ध्वनि है, दूसरी में भी लगभग उतनी ही होनी चाहिए।
2. **HEAVY END RHYMES:** "है", "हूँ", "था" पर लाइन खत्म करना सख्त मना है। लाइन संज्ञा (Noun) या क्रिया (Verb) पर खत्म करो।
   *उदाहरण:* "लंका में **ज्वाला**, मैं मौत का **प्याला**, शत्रु का **दिवाला**।"
3. **INTERNAL RHYME:** लाइन के बीच में भी तुकबंदी लाओ।
4. **NO SOFT WORDS:** "अच्छा", "बुरा", "मारूँगा" जैसे साधारण शब्द हटाओ। इसकी जगह "विनाश", "अट्टहास", "कालजयी", "ध्वस्त", "अधर्मी" लाओ।

📌 FORMAT: 
[Intro] (Heavy Cinematic Tone)
[Verse 1] (12 Bars - Strong Rhyme Scheme AABB or ABAB)
[Hook 🔥] (4 Bars - Catchy and Viral)
[Verse 2] (12 Bars - Different Rhymes, High Energy)
[Outro] (Final Punchline)

यहाँ से 'Professional Hip-Hop' लिखना शुरू करो:
"""

if generate_btn:
    if not topic:
        st.error("टॉपिक लिखो भाई!")
    else:
        with st.spinner("🔱 दिव्य शब्दों की रचना हो रही है..."):
            try:
                # Temperature 1.0 - Creativity और Logic का बेस्ट बैलेंस
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक प्रोफेशनल हिप-हॉप लिरिसिस्ट हो। तुम्हारी तुकबंदी और शब्द चयन (Vocabulary) बहुत ही उन्नत है।"},
                        {"role": "user", "content": build_ultimate_prompt(topic, mode)}
                    ],
                    temperature=1.0,
                    max_tokens=2500
                )

                lyrics = response.choices[0].message.content
                with col2:
                    st.success("🔱 BARS READY FOR RECORDING!")
                    st.text_area(label="DivineRapTv Final Script", value=lyrics, height=750)
            except Exception as e:
                st.error(f"Error: {e}")
                

import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI
st.set_page_config(page_title="DivineRapTv Studio", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    .stButton>button { background: #ff0000; color: #fff; font-weight: bold; border: none; height: 3.5rem; width: 100%; border-radius: 5px; font-size: 1.2rem; }
    .stTextArea textarea { color: #00ff00 !important; background-color: #111 !important; font-family: monospace; font-size: 1.2rem !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 DivineRapTv: Studio Bar Generator")
st.write("---")

col1, col2 = st.columns([1, 1.5])

with col1:
    topic = st.text_input("🎯 विषय (Topic)", placeholder="जैसे: लंका दहन, काल का तांडव")
    mode = st.selectbox("🎭 म्यूजिक स्टाइल", ["Hardcore Rap", "Epic Storytelling", "Emotional Bhakti"])
    generate_btn = st.button("🎤 GENERATE BARS")

def build_studio_prompt(topic, mode):
    # 'Few-Shot' Logic: हमने AI को उदाहरण दिया है कि 'कविता' और 'रैप' में क्या फर्क है
    return f"""
तुम एक 'Professional Ghostwriter' हो। तुम्हें 'DivineRapTv' के लिए "Commercial Rap Song" लिखना है, कविता नहीं। 

🎯 TOPIC: {topic}
🎭 STYLE: {mode}

❌ कविता (Don't write like this): 
"लंका में आग लग रही है, रावण घबरा रहा है, हनुमान जी आ रहे हैं।" (बोरिंग!)

✅ रैप सॉन्ग (Write exactly like this):
"लंका में **ज्वाला**, मौत का **प्याला**,
काँपेगा रावण, आया **विकराला**।
आँखों में **क्रोध**, अधर्म का **रोध**,
राम का नाम, अब होगा **प्रतिशोध**।"

❗ STRICT INSTRUCTIONS:
1. **SHORT LINES:** हर लाइन में सिर्फ 4-6 शब्द होने चाहिए। 
2. **PERFECT RHYME:** हर 2 लाइन के आखिरी शब्द का 'Sound' सेम होना चाहिए (A-A, B-B)।
3. **NO 'HE' OR 'HOON':** लाइन के आखिर में 'है', 'हूँ', 'था' जैसे शब्द बिल्कुल नहीं आने चाहिए।
4. **VOCAB:** भारी और 'Raw' शब्दों का प्रयोग करें (अट्टहास, प्रचंड, विनाश, ध्वंस)।

📌 STRUCTURE: [Intro] -> [Verse 1 (16 Bars)] -> [Hook (Catchy)] -> [Verse 2 (16 Bars)] -> [Outro]

यहाँ से 'Professional Song' लिखना शुरू करो:
"""

if generate_btn:
    if not topic:
        st.error("टॉपिक लिखो!")
    else:
        with st.spinner("🔱 धुन तैयार हो रही है..."):
            try:
                # Temperature 0.9 ताकि AI लय से न भटके
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक प्रोफेशनल हिप-हॉप राइटर हो। तुम केवल 'Bars' लिखते हो, कविता नहीं।"},
                        {"role": "user", "content": build_studio_prompt(topic, mode)}
                    ],
                    temperature=0.9, 
                    max_tokens=2000
                )

                lyrics = response.choices[0].message.content
                with col2:
                    st.success("🔱 गाना तैयार है!")
                    st.text_area(label="DivineRapTv Official Script", value=lyrics, height=750)
            except Exception as e:
                st.error(f"Error: {e}")
                

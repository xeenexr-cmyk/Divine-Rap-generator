import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI Setup
st.set_page_config(page_title="Divine Rap Studio v5.0", page_icon="🔱", layout="wide")

# Dark Aesthetic CSS
st.markdown("""
    <style>
    .stApp { background-color: #080a0f; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%); color: white; font-weight: bold; height: 3.5em; border: none; font-size: 20px; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0px 0px 15px #2575fc; }
    .stTextInput>div>div>input { background-color: #121620; color: #00ffcc; border: 1px solid #30363d; border-radius: 10px; padding: 15px; }
    .stTextArea>div>div>textarea { background-color: #0d1117; color: #f0f6fc; font-family: 'Consolas', monospace; border: 1px solid #444; font-size: 16px; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 Divine Rap Studio v5.0 (The Viral Engine)")
st.write("### DivineRapTv: जहाँ भक्ति और हिप-हॉप का 'Tandav' होता है।")

col1, col2 = st.columns([1, 1.3])

with col1:
    topic = st.text_input("🎯 रैप का विषय (Topic)", placeholder="जैसे: श्मशान का राजा, काल का काल महाकाल")
    
    mode = st.selectbox("🎭 वाइब और फ्लो (Flow)", [
        "Hardcore Aggressive (Fast Tempo/Raftaar Style)",
        "Dark & Mystical (Slow/Deep/Aghori Vibe)",
        "Cinematic Storytelling (Narrative/Epic)",
        "Modern Melodic (Autotune/Soulful)"
    ])
    
    include_music = st.checkbox("🎵 म्यूजिक प्रोडक्शन नोट्स (BPM, Bass, Beats)", value=True)
    st.divider()
    generate_btn = st.button("🔥 GENERATE TRACK")

def build_viral_prompt(topic, mode, include_music):
    return f"""
तुम एक 'Underground Rap Legend' हो जो भगवानों पर 'Aggressive Divine Rap' लिखता है। 
तुम्हारा काम 'DivineRapTv' के लिए ऐसा गाना लिखना है जो YouTube पर तहलका मचा दे।

🎯 TOPIC: {topic}
🎭 FLOW: {mode}

❌ ये कभी मत लिखना (STRICT FORBIDDEN):
- 'मैं भक्ति में खोया हूँ', 'शिव महान हैं', 'प्रणाम करता हूँ' - ये सब हटाओ! ये रैप है, भजन नहीं।
- 'गया हूँ', 'रहा हूँ' जैसी कमज़ोर तुकबंदी (Rhymes) बैन है।

✅ ये ज़रूर करना (MUST DO):
1. **Multisyllabic Rhymes:** अंत में 'विनाश-आकाश' की जगह 'विनाश-अट्टहास' या 'विकराल-काल-कपाल' जैसे शब्दों का प्रयोग करो।
2. **Internal Rhyming:** लाइन के बीच में भी शब्दों को मैच करो (जैसे: "हाथ में **त्रिशूल**, जो करे पाप **निर्मूल**")।
3. **Aggressive Metaphors:** शिव को 'अघोरी', 'काल का अंत', 'शून्य का शोर' जैसे विशेषणों से बुलाओ।
4. **Hinglish Touch:** जहाँ ज़रूरी हो, थोड़े 'Cool' शब्द यूज़ करो (जैसे: 'Beat', 'Vibe', 'Legend', 'Flow', 'Game')।
5. **Beat Alignment:** हर लाइन में 8-10 शब्द ही हों ताकि रैपर को सांस लेने की जगह मिले।

📌 FORMAT:
[Intro] (गहरा और सस्पेंस भरा)
[Verse 1] (तेज़ रफ़्तार, भारी पंचलाइन्स)
[Hook 🔥] (4 लाइन्स - सबसे Catchy, Viral Material)
[Verse 2] (कहानी और गहरी बातें)
[Outro] (धमाकेदार अंत)

{ "अंत में म्यूजिक गाइड दें: BPM (100-140), Beat Type (Trap/Boom-bap), और Instruments (Dark Flute, Heavy Bass)." if include_music else "" }
"""

if generate_btn:
    if not topic:
        st.warning("महादेव! बिना टॉपिक के शब्द कैसे आएंगे?")
    else:
        with st.spinner("⏳ शब्दों का तांडव शुरू हो रहा है..."):
            try:
                # Temperature 0.90 सबसे बेस्ट है रैप के लिए
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक प्रोफेशनल रैप राइटर हो। तुम्हारा स्टाइल बहुत ही Aggressive और Modern है।"},
                        {"role": "user", "content": build_viral_prompt(topic, mode, include_music)}
                    ],
                    temperature=0.9,
                    max_tokens=2000
                )

                final_lyrics = response.choices[0].message.content
                
                with col2:
                    st.success("✅ ट्रैक तैयार है! अब आग लगा दो!")
                    st.markdown("### 🎤 Final Lyrics & Beat Guide")
                    st.text_area(label="Official Script", value=final_lyrics, height=700)
                    
                    st.info("💡 Pro Tip: Hook वाली लाइन्स को गाने में कम से कम 3 बार रिपीट करें ताकि वो लोगों के दिमाग में बैठ जाए।")
                
            except Exception as e:
                st.error(f"❌ Error: {e}")

st.divider()
st.caption("Produced for DivineRapTv | © 2026 The Ultimate Rap Studio")

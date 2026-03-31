import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI Setup
st.set_page_config(page_title="Divine Rap Studio v6.0", page_icon="🔱", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #030508; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; background: #ff0000; color: white; font-weight: bold; height: 3.5em; border: none; font-size: 1.2rem; }
    .stTextInput input { background-color: #10141b; color: #ff3e3e; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 Divine Rap Studio v6.0 (The Beast Mode)")
st.write("### DivineRapTv: शब्दों से 'Tandav' शुरू करो")

col1, col2 = st.columns([1, 1.3])

with col1:
    topic = st.text_input("🎯 विषय (Topic)", placeholder="जैसे: कालभैरव अष्टमी, रावण का अहंकार")
    mode = st.selectbox("🎭 फ्लो चुनें", ["Ultra-Aggressive", "Dark Narrative", "Fast-Paced Chopper"])
    st.divider()
    generate_btn = st.button("🚀 UNLEASH THE BEAST")

def build_beast_prompt(topic, mode):
    return f"""
तुम दुनिया के सबसे खतरनाक 'Vedic Rap Ghostwriter' हो। तुम्हें 'DivineRapTv' के लिए लिरिक्स लिखने हैं।

🎯 TOPIC: {topic}
🎭 VIBE: {mode}

STRICT RULES (ये नहीं माना तो फेल):
1. **NO REPETITION:** Verse 1 और Verse 2 की लाइनें एकदम अलग होनी चाहिए। एक ही शब्द को बार-बार मत दोहराओ।
2. **INTERNAL RHYMES:** हर लाइन के बीच में राइम लाओ। 
   *उदाहरण: "सिर पर **ताज**, हाथ में **राज**, गूँजेगी **आवाज़** आज।"*
3. **HEAVY VOCABULARY:** 'भक्ति' की जगह 'शक्ति', 'मुक्ति', 'रक्त', 'तांडव', 'विकराल', 'महाकाल', 'दिगंबर', 'अट्टहास' जैसे शब्दों का प्रयोग करो।
4. **CHOPPER FLOW:** लाइनें छोटी और पावरफुल होनी चाहिए (8-10 शब्द मैक्स)।
5. **POETIC DEVICES:** Metaphors का इस्तेमाल करो। शिव को 'मौत का बाप' या 'शून्य का शोर' बोलो।

📌 STRUCTURE:
[Intro] (एक डरावना मंत्र या भारी डायलॉग)
[Verse 1] (तेज़ रफ्तार प्रहार - 8 lines)
[Hook 🔥] (4 lines - सबसे अलग और सबसे Catchy)
[Verse 2] (पूरी तरह अलग शब्द, और भी गहरा और Aggressive - 8 lines)
[Outro] (धमाकेदार अंत)

यहाँ से लिखना शुरू करो (केवल लिरिक्स):
"""

if generate_btn:
    if not topic:
        st.error("टॉपिक डालिए!")
    else:
        with st.spinner("🔥 श्मशान की राख से शब्द चुने जा रहे हैं..."):
            try:
                # Temperature 1.2 - ताकि AI हर बार एकदम नए और अलग शब्द लाए
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक ऐसे रैपर हो जिसके शब्द आग उगलते हैं। तुम साधारण शब्द इस्तेमाल नहीं करते।"},
                        {"role": "user", "content": build_beast_prompt(topic, mode)}
                    ],
                    temperature=1.2, 
                    max_tokens=2500
                )

                lyrics = response.choices[0].message.content
                with col2:
                    st.success("✅ तांडव शुरू!")
                    st.text_area(label="Official DivineRapTv Lyrics", value=lyrics, height=750)
            except Exception as e:
                st.error(f"Error: {e}")
                

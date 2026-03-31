import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# UI
st.set_page_config(page_title="Ultimate Bhakti Rap Studio", page_icon="🔥")

st.title("🔥 Ultimate Bhakti Rap Studio 🎤")

topic = st.text_input("🎯 विषय लिखें", placeholder="जैसे: शिव तांडव, राधा कृष्ण विरह, राम बालकांड")

mode = st.selectbox("🎭 Mode चुनें", [
    "Hardcore Rap",
    "Ramayan Story Rap",
    "Radha Krishna Virah Rap",
    "Meera Bhakti Rap",
    "Bollywood Bhakti Rap"
])

# 🔥 MASTER PROMPT FUNCTION
def build_prompt(topic, mode):
    return f"""
तुम भारत के सबसे बड़े Bollywood lyricist + divine rap writer हो।

तुम्हारा काम:
ऐसा rap song लिखो जो सुनते ही रोंगटे खड़े कर दे।

❗ STRICT RULES:
- केवल शुद्ध हिन्दी (एक भी English शब्द नहीं)
- हर लाइन cinematic और powerful हो
- कोई भी लाइन repeat नहीं होगी
- lyrics में energy + emotion + rhythm होना चाहिए
- साधारण वाक्य बिल्कुल नहीं लिखने

🎯 Topic: {topic}
🎭 Mode: {mode}

🔥 STYLE CONTROL:

Hardcore Rap:
- शब्द: काल, अग्नि, विनाश, प्रलय, शक्ति
- tone: आक्रामक + तेज + powerful punchlines
- हर 2 लाइन में impact होना चाहिए

Ramayan Story:
- पूरी कहानी rap flow में
- दृश्य बदलते रहें (scene transitions)

Radha Krishna:
- विरह + प्रेम + तड़प
- imagery: चाँद, रात, बांसुरी, आँसू

Meera Bhakti:
- समर्पण + दर्द + भक्ति
- आत्मा की पुकार

Bollywood Bhakti:
- modern cinematic feel
- दिल छूने वाला + musical flow

🔥 MOST IMPORTANT:
Hook ऐसा लिखो जो लोग बार-बार गुनगुनाएं और reels में use करें

📌 OUTPUT FORMAT:

[Intro]

[Verse 1] (कम से कम 6 लाइन)

[Hook] 🔥 (सबसे powerful, 4 लाइन max)

[Verse 2] (कम से कम 6 लाइन)

[Hook]

[Outro]

❗ EXTRA:
हर लाइन ऐसी हो जैसे फिल्म का डायलॉग हो
"""

# Generate button
if st.button("🚀 Generate Song"):

    if topic.strip() == "":
        st.warning("⚠️ कृपया विषय लिखें")
    else:
        with st.spinner("🔥 Divine Masterpiece बन रहा है..."):

            try:
                prompt = build_prompt(topic, mode)

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "तुम एक महान हिन्दी गीतकार और रैपर हो"},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=1.3,
                    max_tokens=2000
                )

                lyrics = response.choices[0].message.content

                st.success("✅ गीत तैयार हो गया!")

                st.markdown("## 🎤 Generated Lyrics:")
                st.code(lyrics)

            except Exception as e:
                st.error(f"❌ Error: {e}")

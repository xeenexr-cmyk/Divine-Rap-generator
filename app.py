import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="🔥 Bhakti Rap Studio", layout="centered")

st.title("🔥 Bhakti + Emotional Rap Generator 🎤")

# Inputs
topic = st.text_input("🎯 विषय", placeholder="शिव सती प्रेम, राधा कृष्ण विरह, राम बालकांड")
mode = st.selectbox("🎭 Mode", [
    "Devotional Rap",
    "Emotional Prem Bhakti",
    "Story (Ramayan Style)",
    "Bollywood Bhakti Rap"
])
mood = st.selectbox("🔥 मूड", ["Aggressive", "Emotional", "Spiritual", "Sad"])
keywords = st.text_input("🧠 कीवर्ड", placeholder="प्रेम, विरह, अग्नि, तप")

def build_prompt():

    return f"""
तुम भारत के एक महान कवि, गीतकार और रैपर हो।

विषय: {topic}
मूड: {mood}
शैली: {mode}
कीवर्ड: {keywords}

🎯 लक्ष्य:
ऐसा गीत लिखो जो दिल को छू जाए और इंसान द्वारा लिखा हुआ लगे।

🔴 भाषा नियम:
- केवल शुद्ध और सुंदर हिन्दी
- कोई Hinglish या English शब्द नहीं
- सरल लेकिन काव्यात्मक भाषा

🔥 भाव के अनुसार लिखो:

अगर विषय प्रेम/विरह है:
→ गहराई, दर्द, तड़प दिखाओ

अगर भक्ति है:
→ समर्पण, श्रद्धा, शक्ति

अगर कहानी है:
→ घटनाओं को क्रम में बताओ

📌 संरचना:

[इंट्रो]
(2 पंक्तियाँ – वातावरण बनाओ)

[अंतरा 1]
(4-5 पंक्तियाँ – भाव या कहानी शुरू)

[हुक]
(2-3 पंक्तियाँ – बहुत catchy और दोहराने योग्य)

[अंतरा 2]
(4-5 पंक्तियाँ – भाव की गहराई)

[हुक]

[आउट्रो]
(2 पंक्तियाँ – गहरा अंत)

⚡ अत्यंत महत्वपूर्ण:
- हर पंक्ति अलग हो (कोई दोहराव नहीं)
- पंक्तियाँ छोटी और प्रभावशाली हों
- तुकबंदी (rhyme) बनी रहे
- गीत में भावनात्मक गहराई हो
- ऐसा लगे जैसे कोई सच्चा कवि लिख रहा है

अब पूरा गीत लिखो।
"""

# Generate
if st.button("🚀 पूरा गीत बनाओ"):

    with st.spinner("⚡ भावनात्मक गीत तैयार हो रहा है..."):

        try:
            prompt = build_prompt()

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=1.4,
                max_tokens=1200
            )

            lyrics = response.choices[0].message.content

            st.success("✅ गीत तैयार हो गया!")

            st.markdown("## 🎤 Generated Lyrics:")
            st.code(lyrics)

        except Exception as e:
            st.error(f"❌ Error: {e}")

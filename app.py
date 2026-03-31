import streamlit as st
from groq import Groq

st.set_page_config(page_title="Divine AI Content Factory", layout="centered")

st.title("🔥 Divine AI Content Factory (Hindi Pro MAX) 🎤")

# ================= INPUT =================
topic = st.text_input("🎯 विषय लिखें (जैसे: शिव तांडव, लंका दहन)")

style = st.selectbox("🎵 शैली चुनें", ["रैप", "बॉलीवुड", "भक्ति रैप"])

mood = st.selectbox("🔥 मूड चुनें", ["आक्रामक", "भावनात्मक", "प्रेरणादायक"])

keywords = st.text_input("🧠 कीवर्ड (optional)", placeholder="जैसे: अग्नि, काल, शक्ति")

# ================= GENERATE =================
if st.button("🚀 पूरा गाना बनाओ"):

    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    prompt = f"""
तुम एक महान बॉलीवुड गीतकार और रैप लेखक हो।

तुम्हारा काम है एक उच्च स्तर का हिन्दी गीत लिखना।

विषय: {topic}
शैली: {style}
मूड: {mood}
कीवर्ड: {keywords}

🔴 सख्त नियम:
- पूरा गीत केवल शुद्ध हिन्दी (देवनागरी) में हो
- कोई अंग्रेज़ी या हिंग्लिश शब्द नहीं
- हर पंक्ति प्रभावशाली और भावपूर्ण हो
- कोई भी लाइन साधारण या दोहराई हुई न हो

🎯 लक्ष्य:
- ऐसा लगे जैसे असली फिल्म का गाना है
- सुनते ही रोंगटे खड़े हो जाएं
- हुक (Hook) वायरल होने लायक हो

🎬 लेखन शैली:
- रूपक का उपयोग (अग्नि, काल, आकाश, आत्मा, विनाश, सृजन)
- गहराई और भावना हो
- रैप में punchlines हो
- सिनेमैटिक feel हो

📌 संरचना:

[इंट्रो]
2 पंक्तियाँ (गहरी और रहस्यमयी शुरुआत)

[अंतरा 1]
5 पंक्तियाँ (कहानी + build up)

[हुक]
3 पंक्तियाँ (बहुत catchy + viral)

[अंतरा 2]
5 पंक्तियाँ (और intense + powerful)

[हुक]
(पहले से बेहतर impact)

[आउट्रो]
2 पंक्तियाँ (भावनात्मक समापन)

⚡ विशेष:
- हुक ऐसा हो जो reels/shorts में viral हो सके
- हर लाइन cinematic लगे

अब एक शानदार गीत लिखो।
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=1.4
        )

        lyrics = response.choices[0].message.content

        st.success("✅ गाना तैयार हो गया!")

        st.markdown("### 🎤 Generated Lyrics:")
        st.write(lyrics)

    except Exception as e:
        st.error("❌ Error आया:")
        st.write(e)

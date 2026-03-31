import streamlit as st
from groq import Groq

# ================= PAGE =================
st.set_page_config(page_title="Divine AI Lyrics Generator", layout="centered")

st.title("🔥 Bollywood Level AI Lyrics Generator 🎤")

# ================= INPUT =================
topic = st.text_input("🎯 विषय लिखें (जैसे: शिव तांडव, लंका दहन)")

style = st.selectbox("🎵 शैली चुनें", ["रैप", "बॉलीवुड", "भक्ति रैप"])

mood = st.selectbox("🔥 मूड चुनें", ["आक्रामक", "भावनात्मक", "प्रेरणादायक"])

keywords = st.text_input("🧠 कीवर्ड (optional)", placeholder="जैसे: अग्नि, काल, शक्ति")

# ================= GENERATE =================
if st.button("🚀 पूरा गाना बनाओ"):

    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])

        prompt = f"""
तुम एक प्रोफेशनल बॉलीवुड गीतकार और रैपर हो।

विषय: {topic}
शैली: {style}
मूड: {mood}
कीवर्ड: {keywords}

🔴 सख्त नियम:
- पूरा गीत शुद्ध हिन्दी (देवनागरी) में हो
- कोई अंग्रेज़ी या हिंग्लिश नहीं
- कोई पैराग्राफ नहीं — हर लाइन अलग हो
- हर लाइन छोटी, दमदार और punchy हो

🎯 लक्ष्य:
- Lyrics बिल्कुल गाने/रैप की तरह हों
- हर लाइन beat पर फिट बैठे
- Hook viral होना चाहिए

📌 STRUCTURE (STRICT):

[इंट्रो]
2 लाइन

[अंतरा 1]
4-5 लाइन

[हुक]
2-3 लाइन (catchy)

[अंतरा 2]
4-5 लाइन (और powerful)

[हुक]

[आउट्रो]
2 लाइन

⚡ IMPORTANT:
- हर लाइन अलग हो
- कोई भी लाइन लंबी न हो
- cinematic + rap feel हो

अब शानदार lyrics लिखो।
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=1.3
        )

        lyrics = response.choices[0].message.content

        st.success("✅ गाना तैयार हो गया!")

        st.markdown("### 🎤 Generated Lyrics:")
        st.markdown(f"```\n{lyrics}\n```")

    except Exception as e:
        st.error("❌ Error आया:")
        st.write(e)

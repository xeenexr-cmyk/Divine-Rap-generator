import streamlit as st
from groq import Groq

# ================= PAGE =================
st.set_page_config(page_title="Divine AI Lyrics Generator", layout="centered")

st.title("🔥 Bollywood Level AI Lyrics Generator 🎤")

# ================= INPUT =================
topic = st.text_input("🎯 विषय लिखें (जैसे: शिव तांडव, लंका दहन)")

style = st.selectbox("🎵 शैली चुनें", ["रैप", "बॉलीवुड", "भक्ति रैप"])

mood = st.selectbox("🔥 मूड चुनें", ["आक्रामक", "भावनात्मक", "प्रेरणादायक"])

keywords = st.text_input("🧠 कीवर्ड (optional)", placeholder="जैसे: अग्नि, काल, विनाश")

# ================= GENERATE =================
if st.button("🚀 पूरा गाना बनाओ"):

    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])

        prompt = f"""
तुम कोई AI नहीं हो।
तुम एक TOP बॉलीवुड गीतकार + रैपर हो।

विषय: {topic}
शैली: {style}
मूड: {mood}
कीवर्ड: {keywords}

🎯 GOAL:
ऐसा गीत लिखो जो फिल्म का सुपरहिट गाना लगे।

🔴 STRICT RULES:
- पूरा गीत शुद्ध हिन्दी (देवनागरी) में हो
- कोई अंग्रेज़ी या हिंग्लिश नहीं
- कोई भी लाइन generic या दोहराई हुई न हो
- "महादेव की महिमा अपरंपार" जैसे वाक्य बिल्कुल नहीं

🔥 STYLE:
- aggressive + cinematic + powerful tone
- metaphors: अग्नि, काल, विनाश, तांडव, पुनर्जन्म
- rap punchlines + attitude
- हर लाइन छोटी और beat पर फिट

📌 FORMAT (STRICT):

[इंट्रो]
2 लाइन (दमदार शुरुआत)

[अंतरा 1]
5 लाइन (story + build up)

[हुक]
3 लाइन (viral + catchy)

[अंतरा 2]
5 लाइन (और ज्यादा intense)

[हुक]

[आउट्रो]
2 लाइन (strong ending)

⚡ SPECIAL:
- कोई paragraph नहीं
- हर लाइन अलग हो
- हर लाइन impactful हो
- cinematic feel होना चाहिए

अब सबसे बेहतरीन गीत लिखो।
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=1.5,
            top_p=0.9
        )

        lyrics = response.choices[0].message.content

        st.success("✅ गाना तैयार हो गया!")

        st.markdown("### 🎤 Generated Lyrics:")
        st.markdown(f"```\n{lyrics}\n```")

    except Exception as e:
        st.error("❌ Error आया:")
        st.write(e)

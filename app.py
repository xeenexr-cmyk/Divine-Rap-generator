import streamlit as st
from groq import Groq

st.set_page_config(page_title="Divine AI Lyrics Generator", layout="centered")

st.title("🔥 Bollywood Level AI Lyrics Generator 🎤")

# INPUT
topic = st.text_input("🎯 विषय लिखें")
style = st.selectbox("🎵 शैली", ["रैप", "बॉलीवुड", "भक्ति रैप"])
mood = st.selectbox("🔥 मूड", ["आक्रामक", "भावनात्मक", "प्रेरणादायक"])
keywords = st.text_input("🧠 कीवर्ड", placeholder="अग्नि, काल, तांडव")

if st.button("🚀 पूरा गाना बनाओ"):

    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])

        prompt = f"""
तुम एक LEGENDARY बॉलीवुड गीतकार + रैपर हो।

विषय: {topic}
मूड: {mood}
कीवर्ड: {keywords}

🎯 TARGET:
यह गाना ऐसा हो कि सुनते ही रोंगटे खड़े हो जाएं।

🔴 RULES:
- केवल शुद्ध हिन्दी
- कोई generic लाइन नहीं
- कोई repetition नहीं
- हर लाइन powerful punch हो

🔥 WRITING STYLE:
- cinematic + dark + aggressive
- हर लाइन में impact
- rap punchlines mandatory

📌 FORMAT:

[इंट्रो]
2 लाइन (shock entry)

[अंतरा 1]
5 लाइन (build + imagery)

[हुक]
3 लाइन (🔥 VIRAL — सबसे powerful)

[अंतरा 2]
5 लाइन (peak intensity)

[हुक]

[आउट्रो]
2 लाइन (emotional + powerful end)

⚡ VERY IMPORTANT:
- Hook सबसे powerful होना चाहिए
- हर line अलग और short हो
- ऐसा लगे live performance rap है

अब ऐसा गीत लिखो जो viral हो सके।
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=1.6,
            top_p=0.95
        )

        lyrics = response.choices[0].message.content

        # 🔥 HOOK BOOST (extra power)
        hook_prompt = f"इस गीत के लिए 3 और ज्यादा powerful viral hook लाइन लिखो:\n{lyrics}"

        hook_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": hook_prompt}],
            temperature=1.7
        )

        hooks = hook_response.choices[0].message.content

        st.success("✅ गाना तैयार हो गया!")

        st.markdown("### 🎤 Generated Lyrics:")
        st.markdown(f"```\n{lyrics}\n```")

        st.markdown("### 🔥 Viral Hook Upgrade:")
        st.markdown(f"```\n{hooks}\n```")

    except Exception as e:
        st.error("❌ Error आया:")
        st.write(e)

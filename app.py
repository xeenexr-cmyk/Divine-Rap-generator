import streamlit as st
from groq import Groq
import os

# API KEY (Streamlit Secrets me add karo: GROQ_API_KEY)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="🔥 Bollywood Lyrics Generator", layout="centered")

st.title("🔥 Bollywood Level AI Lyrics Generator 🎤")

# Inputs
topic = st.text_input("🎯 विषय (Topic)", placeholder="Shiv Tandav, Lanka Dahan")
style = st.selectbox("🎵 शैली (Style)", ["Rap", "Bollywood", "Sad", "Devotional"])
mood = st.selectbox("🔥 मूड (Mood)", ["Aggressive", "Emotional", "Dark", "Motivational"])
keywords = st.text_input("🧠 कीवर्ड (optional)", placeholder="अग्नि, काल, विनाश")

# Generate Button
if st.button("🚀 पूरा गाना बनाओ"):

    with st.spinner("⚡ Cinematic lyrics generate ho rahe hain..."):

        # 🔥 MAIN PROMPT (Human-like + Bollywood level)
        prompt = f"""
तुम एक TOP Bollywood lyricist + underground rapper हो।

विषय: {topic}
स्टाइल: {style}
मूड: {mood}
कीवर्ड: {keywords}

🎯 GOAL:
ऐसा गाना लिखो जो इंसान ने लिखा लगे, AI नहीं।

🔴 RULES:
- केवल शुद्ध और natural हिन्दी
- कोई robotic tone नहीं
- rhyme + flow maintain करो
- repetition बिल्कुल नहीं

🔥 STYLE:
- cinematic + emotional + aggressive mix
- storytelling feel हो
- rap flow natural हो

📌 STRUCTURE:

[इंट्रो]
(2 लाइन – strong entry)

[अंतरा 1]
(4-5 लाइन – कहानी)

[हुक]
(2-3 लाइन – catchy + viral)

[अंतरा 2]
(4-5 लाइन – peak intensity)

[हुक]

[आउट्रो]
(2 लाइन – deep ending)

⚡ VERY IMPORTANT:
- Hook सबसे catchy होना चाहिए
- lines छोटी और impactful हो
- Divine / Raftaar level flow हो

अब पूरा powerful cinematic गीत लिखो।
"""

        try:
            # 🎤 Lyrics Generation
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=1.6,
                max_tokens=1200
            )

            lyrics = response.choices[0].message.content

            st.success("✅ गाना तैयार हो गया!")

            st.markdown("## 🎤 Generated Lyrics:")
            st.markdown(f"```\n{lyrics}\n```")

            # 🔥 Hook Upgrade
            hook_prompt = f"""
इस गाने के लिए 5 ultra catchy hook lines लिखो।

Song:
{lyrics}
"""

            hook_res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": hook_prompt}],
                temperature=1.8
            )

            st.markdown("## 🔥 Viral Hook Ideas:")
            st.markdown(f"```\n{hook_res.choices[0].message.content}\n```")

        except Exception as e:
            st.error(f"❌ Error: {e}")

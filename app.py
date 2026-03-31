import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🔥 Ultimate Bhakti Rap Studio 🎤")

topic = st.text_input("🎯 विषय", placeholder="राम बालकांड, राधा कृष्ण विरह, मीरा प्रेम")
mode = st.selectbox("🎭 Mode", [
    "Hardcore Rap",
    "Ramayan Story Rap",
    "Radha Krishna Virah Rap",
    "Meera Bhakti Rap",
    "Bollywood Bhakti Rap"
])

def build_prompt():

    # 🔥 HARDCORE RAP
    if mode == "Hardcore Rap":
        return f"""
Divine + Raftaar style hardcore rap likho.

Topic: {topic}

- aggressive tone
- strong rhyme + punchlines
- street vibe

Structure: Intro, Verse, Hook, Verse, Hook, Outro
"""

    # 📖 RAMAYAN STORY RAP
    elif mode == "Ramayan Story Rap":
        return f"""
रामचरितमानस (बालकांड) की शैली में rap likho.

Topic: {topic}

- कहानी flow में हो
- हर scene describe करो
- poetic + rap mix

Example flow:
जन्म → बाल लीलाएँ → गुरु → सीता स्वयंवर

Language: शुद्ध हिन्दी
"""

    # 💔 RADHA KRISHNA VIRAH
    elif mode == "Radha Krishna Virah Rap":
        return f"""
राधा कृष्ण के विरह और प्रेम पर गहरा emotional rap लिखो.

Topic: {topic}

- दर्द, तड़प, अधूरापन
- poetic imagery (चाँद, रात, बांसुरी)
- हर line दिल को छू जाए

NO boring lines.
"""

    # 🙏 MEERA BHAKTI
    elif mode == "Meera Bhakti Rap":
        return f"""
मीरा के कृष्ण प्रेम का दर्द और समर्पण rap style में लिखो.

Topic: {topic}

- पूर्ण समर्पण
- दर्द + भक्ति
- आत्मा का पुकार

Language: pure हिन्दी
"""

    # 🎬 BOLLYWOOD STYLE
    elif mode == "Bollywood Bhakti Rap":
        return f"""
Modern Bollywood devotional rap likho.

Topic: {topic}

- cinematic feel
- emotional + catchy
- Arijit + Divine fusion

Hook viral होना चाहिए
"""

# Generate
if st.button("🚀 Generate Song"):

    with st.spinner("🔥 Creating masterpiece..."):

        try:
            prompt = build_prompt()

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=1.6,
                max_tokens=1200
            )

            lyrics = response.choices[0].message.content

            st.success("✅ Song Generated!")

            st.markdown("## 🎤 Lyrics:")
            st.code(lyrics)

        except Exception as e:
            st.error(f"❌ Error: {e}")

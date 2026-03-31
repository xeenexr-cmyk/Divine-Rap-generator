import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🔥 Ultimate Bhakti Rap Studio 🎤")

topic = st.text_input("🎯 विषय", placeholder="हनुमान, राधा कृष्ण, शिव तांडव")

mode = st.selectbox("🎭 Mode", [
    "Hardcore Rap",
    "Ramayan Story Rap",
    "Radha Krishna Virah Rap",
    "Meera Bhakti Rap",
    "Bollywood Bhakti Rap"
])

def build_prompt():

    return f"""
तुम एक professional Bollywood lyricist + divine rapper हो।

तुम्हारा काम:
ऐसा गीत लिखो जो सुनने वाले को goosebumps दे।

STRICT RULES:
- केवल शुद्ध हिन्दी (NO English, NO Hinglish)
- lyrics poetic + powerful + cinematic हों
- हर लाइन नई हो (NO repetition)
- Hook सबसे ज्यादा catchy और viral होना चाहिए
- flow natural rap जैसा हो

Topic: {topic}
Mode: {mode}

SPECIAL INSTRUCTIONS:

Hardcore Rap:
- काल, विनाश, अग्नि, शक्ति जैसे शब्द
- aggressive energy + punchlines

Ramayan Story:
- कहानी flow में (scene by scene)
- narration + rap fusion

Radha Krishna:
- विरह, प्रेम, तड़प
- imagery: बांसुरी, चाँद, रात

Meera Bhakti:
- समर्पण, दर्द, कृष्ण प्रेम
- आत्मा की पुकार

Bollywood:
- modern + emotional + musical
- Arijit + Divine feel

OUTPUT FORMAT:

[Intro]

[Verse 1]

[Hook]  ← 🔥 सबसे powerful हिस्सा

[Verse 2]

[Hook]

[Outro]
"""

if st.button("🚀 Generate Song"):

    with st.spinner("🔥 Divine Masterpiece बन रहा है..."):

        try:
            prompt = build_prompt()

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=1.4,
                max_tokens=2000
            )

            lyrics = response.choices[0].message.content

            st.success("✅ Song Generated!")

            st.markdown("## 🎤 Lyrics:")
            st.code(lyrics)

        except Exception as e:
            st.error(f"❌ Error: {e}")

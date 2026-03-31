import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🔥 Ultimate Bhakti Rap Studio 🎤")

topic = st.text_input("🎯 विषय", placeholder="शिव तांडव, राधा कृष्ण विरह, राम बालकांड")

mode = st.selectbox("🎭 Mode", [
    "Hardcore Rap",
    "Ramayan Story Rap",
    "Radha Krishna Virah Rap",
    "Meera Bhakti Rap",
    "Bollywood Bhakti Rap"
])

def build_prompt():

    base_rules = """
IMPORTANT RULES:
- ONLY शुद्ध हिन्दी (NO English / Hinglish words)
- हर लाइन powerful और meaningful हो
- repeat lines बिल्कुल नहीं
- cinematic feel हो
- rhyming strong हो
"""

    if mode == "Hardcore Rap":
        return f"""
{base_rules}

Divine + Raftaar level hardcore rap लिखो

Topic: {topic}

- aggressive energy
- punchlines, attitude
- metaphors (काल, अग्नि, विनाश)

Structure:
[Intro]
[Verse 1]
[Hook]
[Verse 2]
[Hook]
[Outro]
"""

    elif mode == "Ramayan Story Rap":
        return f"""
{base_rules}

रामचरितमानस की तरह storytelling rap लिखो

Topic: {topic}

- पूरी कहानी flow में
- scene by scene progression
- poetic + rap fusion

Structure:
[Intro]
[कथा भाग 1]
[Hook]
[कथा भाग 2]
[Hook]
[Outro]
"""

    elif mode == "Radha Krishna Virah Rap":
        return f"""
{base_rules}

राधा कृष्ण के प्रेम और विरह पर deep emotional rap लिखो

Topic: {topic}

- दर्द, तड़प, अधूरापन
- imagery: चाँद, रात, बांसुरी, विरह

Hook बहुत emotional होना चाहिए
"""

    elif mode == "Meera Bhakti Rap":
        return f"""
{base_rules}

मीरा की तरह कृष्ण भक्ति का दर्द लिखो

Topic: {topic}

- समर्पण + प्रेम + त्याग
- आत्मा की पुकार

lines दिल को छूनी चाहिए
"""

    elif mode == "Bollywood Bhakti Rap":
        return f"""
{base_rules}

Modern Bollywood devotional rap लिखो

Topic: {topic}

- cinematic + emotional
- Arijit + Divine fusion feel
- viral hook

song सुनते ही goosebumps आए
"""

# Generate
if st.button("🚀 Generate Song"):

    with st.spinner("🔥 Masterpiece बन रहा है..."):

        try:
            prompt = build_prompt()

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=1.3,
                max_tokens=1500
            )

            lyrics = response.choices[0].message.content

            st.success("✅ Song Generated!")

            st.markdown("## 🎤 Lyrics:")
            st.code(lyrics)

        except Exception as e:
            st.error(f"❌ Error: {e}")

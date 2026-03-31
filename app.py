import streamlit as st
from groq import Groq

# API Key setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page Configuration
st.set_page_config(page_title="DivineRapTv 10/10 Engine", layout="wide", page_icon="🔱")

# Custom CSS for DivineRapTv Branding
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; border-radius: 10px; height: 3em; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #262730; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 DivineRapTv - ULTIMATE 10/10 RAP ENGINE 🔥")
st.subheader("Bhakti + Rap + Emotion | All-In-One AI Writer")

# --- INPUT SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("🎯 Enter Topic (जैसे: शिव तांडव, लंका दहन, कृष्ण विरह)", placeholder="Apna topic likho...")

with col2:
    # Based on your Exact Requirement Image
    style = st.selectbox("🎭 Select Writing Style", [
        "Hardcore Rap (Divine/Raftaar Style) 🔥", 
        "Ramayan Story Rap (Katha Flow) 📖", 
        "Radha-Krishna Prem (Virah/Melodic) ❤️", 
        "Meera Bhakti Pain (Soulful) 😭", 
        "Bollywood Bhakti Fusion (Commercial) 🎶"
    ])

generate = st.button("🚀 GENERATE 10/10 MASTERPIECE")

# --- STEP 1: THE BRAINSTORMER (GHOSTWRITER) ---
def build_prompt(topic, style):
    # Defining Persona based on Style
    if "Hardcore" in style:
        persona = "तुम एक Aggressive Street Rapper हो। शब्द भारी, कड़क और शक्तिशाली होने चाहिए।"
        vibe = "Heavy Bass, Fast Flow, Punchlines, Power."
    elif "Story" in style:
        persona = "तुम एक आधुनिक कथा-वाचक हो। शब्दों में वर्णन और चित्रण (Imagery) होनी चाहिए।"
        vibe = "Narrative, Storytelling, Flowing, Cinematic."
    elif "Prem" in style:
        persona = "तुम एक Melodic Poet हो। शब्दों में कोमलता, प्रेम और समर्पण होना चाहिए।"
        vibe = "Soft, Rhyming, Heartfelt, Devotional Love."
    elif "Pain" in style:
        persona = "तुम मीरा और सूरदास के आधुनिक रूप हो। शब्दों में विरह, आंसू और तड़प होनी चाहिए।"
        vibe = "Emotional, Sad, Soulful, Deep Pain."
    else:
        persona = "तुम एक Commercial Hit-maker हो। शब्द आसान, Catchy और Danceable होने चाहिए।"
        vibe = "Energy, Hook-heavy, Easy to Sing, Popular."

    return f"""
{persona} तुम 'DivineRapTv' के लिए सबसे खतरनाक Rap लिख रहे हो।

🎯 TOPIC: {topic}
🎭 STYLE: {style}
🎸 VIBE: {vibe}

❗ STRICT RULES:
- Language: Hindi/Hinglish Mix.
- Lines: Short & Crisp (4-6 words max).
- Rhyme: Perfect AA-BB pattern.
- NO Fillers: "है/हूँ/था/गा" जैसे फालतू शब्द हटाओ। सीधा प्रहार करो।
- Vocabulary: Topic के हिसाब से शुद्ध और गहरे शब्दों का चुनाव करो।

STRUCTURE:
[Intro] (2 Powerful Lines)
[Verse 1] (12 Lines - Build the story/power)
[Hook] (4 Lines - Most Catchy, Mantra-like, Viral material)
[Verse 2] (12 Lines - Take it to the next level)
[Hook] (Repeat)
[Outro] (1 Deep Ending Line)

लिखना शुरू करो:
"""

# --- STEP 2: THE REFINER (LYRICS IMPROVER) ---
def refine_prompt(raw):
    return f"""
इन lyrics को सुधारो और 10/10 बनाओ:
{raw}

RULES FOR IMPROVEMENT:
1. Rhyme Scheme को और सटीक (tight) करो।
2. कमजोर लाइनों को 'Banger' पंचलाइन से बदलो।
3. शब्दों का वजन बढ़ाओ (Use synonyms of Power/Emotion)।
4. 'Flow' चेक करो ताकि रैपर सांस न फूले।

Improved Lyrics:
"""

# --- STEP 3: THE VIRAL DOCTOR (FINAL POLISH) ---
def validate_prompt(refined):
    return f"""
Final Check for DivineRapTv Channel:
{refined}

TASK:
1. 'Hook' को महा-शक्तिशाली बनाओ (इसमें कोई मंत्र या भगवान का नाम लय में जोड़ो)।
2. 'Intro' में सस्पेंस डालो।
3. पूरे गाने को एक 'Masterpiece' का रूप दो।

Final 10/10 Version:
"""

# --- GENERATION ENGINE ---
def generate_song(topic, style):
    try:
        # Step 1: Raw Draft
        raw_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम Raw Rap Writer हो"},
                      {"role": "user", "content": build_prompt(topic, style)}],
            temperature=0.8
        )
        raw = raw_res.choices[0].message.content

        # Step 2: Refinement
        refined_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम Expert Lyrics Improver हो"},
                      {"role": "user", "content": refine_prompt(raw)}],
            temperature=0.7
        )
        refined = refined_res.choices[0].message.content

        # Step 3: Final Polish
        final_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम Viral Rap Doctor हो"},
                      {"role": "user", "content": validate_prompt(refined)}],
            temperature=0.6
        )
        return final_res.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# --- OUTPUT DISPLAY ---
if generate:
    if not topic:
        st.error("⚠️ अरे भाई! पहले Topic तो डालो।")
    else:
        with st.spinner(f"🔥 {style} के हिसाब से 10/10 Masterpiece बन रहा है..."):
            final_lyrics = generate_song(topic, style)
            
            st.success("✅ YOUR DIVINE RAP IS READY! 🔥")
            st.text_area("🎤 Final Lyrics for DivineRapTv", final_lyrics, height=600)

            st.download_button(
                label="📥 Download Master Lyrics",
                data=final_lyrics,
                file_name=f"{topic}_divineraptv.txt",
                mime="text/plain"
            )

st.markdown("---")
st.caption("Powered by DivineRapTv 10/10 Engine | Master of Bhakti Rap")

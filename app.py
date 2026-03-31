import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="DivineRapTv BEAST ENGINE", layout="wide", page_icon="🔱")

# Ultra Dark UI for Hardcore Feel
st.markdown("""
    <style>
    .main { background-color: #050505; color: #ff0000; }
    .stButton>button { width: 100%; background: linear-gradient(45deg, #8b0000, #ff0000); color: white; border-radius: 2px; height: 4em; font-weight: 900; border: none; letter-spacing: 2px; }
    .stTextInput>div>div>input { background-color: #111; color: #ff4b4b; border: 1px solid #444; font-size: 1.2em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 DivineRapTv - THE BEAST ENGINE 10/10 🔥")
st.subheader("Bhakti x Hardcore Hip-Hop | Raw. Lethal. Divine.")

col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("🎯 Enter War Topic", placeholder="Example: Aghori Tandav, Ravan Vinash...")

with col2:
    style = st.selectbox("🎭 Select Attack Mode", [
        "FATAL ATTACK (Divine/Aggressive) 🔥", 
        "WAR STORY (Cinematic Fast Flow) 📖", 
        "DARK DEVOTION (Gothic/Heavy) 💀"
    ])

generate = st.button("🚀 UNLEASH THE BEAST")

# --- THE HARDCORE PROMPT ENGINE ---
def build_prompt(topic, style):
    return f"""
तुम एक 'Cold-Blooded Hip-Hop Ghostwriter' हो। तुम्हें कविता और 'है/हूँ' जैसे शब्दों से नफरत है।

🎯 TOPIC: {topic}
🎭 STYLE: {style}

❗ FATAL ERROR - NEVER USE:
- "है", "हूँ", "था", "थी", "रहा", "रही", "होता", "करती" (Delete them all!)
- "जैसे", "जैसा", "तैसे" (No Similes)

✅ MANDATORY RAP RULES:
1. NO VERBS: सीधा शब्द मारो। (Example: Don't say 'Shiv tandav karta hai', say 'महाकाल तांडव! आँखों में आग!')
2. SYLLABLE ATTACK: हर लाइन में सिर्फ 3 से 4 भारी शब्द।
3. RHYME CRUNCH: हर 2 लाइन में धाकड़ internal और end rhyme (AABB)।
4. VOCABULARY: Use words like: 'भस्म', 'काल', 'रक्त', 'प्रहार', 'चक्र', 'मंजर', 'खंजर', 'अंगार'।

STRUCTURE:
[Intro] - 2 Breathless Lines
[Verse 1] - 16 Short Power Lines (Aggressive Flow)
[Hook] - 4 Lines (High Pitch Chant - Viral Power)
[Verse 2] - 16 Short Power Lines (Punchlines & Metaphors)
[Outro] - 1 Brutal Mic Drop Line
"""

def refine_prompt(raw):
    return f"""
ये lyrics अभी भी 'Soft' हैं। इन्हें 'Lethal Rap' में बदलो:
{raw}

REFINEMENT PROTOCOL:
1. हर line से "है/रहा/होता" निकालो। उसे 'Direct Punch' बनाओ।
2. शब्दों को 'भारी' (Heavy Sanskrit/Hindi) करो।
3. Flow ऐसा हो कि हर शब्द एक गोली (Bullet) की तरह लगे।
4. Rhyme Scheme को Professional Level पर सेट करो।

Final Hardcore Beast Version:
"""

def generate_song(topic, style):
    try:
        # Step 1: Raw Aggression
        raw = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम एक Raw Hip-Hop Artist हो।"},
                      {"role": "user", "content": build_prompt(topic, style)}],
            temperature=1.0 # High temperature for more creativity
        ).choices[0].message.content

        # Step 2: Beast Filter (The Surgeon)
        final = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "तुम एक Hip-Hop Assassin हो। फालतू शब्द काटो।"},
                      {"role": "user", "content": refine_prompt(raw)}],
            temperature=0.6
        ).choices[0].message.content

        return final
    except Exception as e:
        return f"Error: {str(e)}"

if generate:
    if not topic:
        st.error("⚠️ Topic daalo pehle!")
    else:
        with st.spinner("🔥 The Beast is writing..."):
            final_lyrics = generate_song(topic, style)
            st.success("✅ THE BEAST HAS SPOKEN! 🎤")
            st.text_area("🎤 Final Hardcore Rap for DivineRapTv", final_lyrics, height=600)
            st.download_button("📥 Download Lethal Rap", final_lyrics, file_name=f"{topic}_hardcore.txt")

st.markdown("---")
st.caption("DivineRapTv | 10/10 Beast Engine | No Mercy in Rhymes")

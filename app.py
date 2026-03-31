import streamlit as st
import google.generativeai as genai
from PIL import Image
import requests
from io import BytesIO

# CONFIG
st.set_page_config(page_title="AI Content Factory 🔥", layout="wide")

# API KEY
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🔥 Divine AI Content Factory (Ultimate Pro)")

tabs = st.tabs([
    "🎤 Lyrics Generator",
    "🎬 Hook Generator",
    "📱 Caption + Hashtags",
    "🖼️ Image Generator"
])

# =========================
# 🎤 LYRICS GENERATOR
# =========================
with tabs[0]:
    st.header("🎤 Bollywood Level Lyrics Generator")

    topic = st.text_input("Enter Topic")
    style = st.selectbox("Style", ["Rap", "Bollywood", "Devotional"])
    mood = st.selectbox("Mood", ["Aggressive", "Emotional", "Powerful"])
    keywords = st.text_input("Keywords (optional)")

    if st.button("Generate Lyrics"):
        prompt = f"""
        Write a FULL professional Hindi {style} song.

        Topic: {topic}
        Mood: {mood}
        Keywords: {keywords}

        Requirements:
        - Bollywood level quality
        - Deep meaningful lyrics
        - NO repetition
        - Strong rhyming
        - Emotional storytelling

        Structure:
        Intro
        Verse 1
        Hook
        Verse 2
        Hook
        Outro
        """

        res = model.generate_content(prompt)
        st.write(res.text)

# =========================
# 🎬 HOOK GENERATOR
# =========================
with tabs[1]:
    st.header("🔥 Viral Hook Generator")

    hook_topic = st.text_input("Hook Topic")

    if st.button("Generate Hook"):
        prompt = f"""
        Create 5 viral Hindi hooks for topic: {hook_topic}

        - Short
        - Catchy
        - Emotional or powerful
        """

        res = model.generate_content(prompt)
        st.write(res.text)

# =========================
# 📱 CAPTION + HASHTAGS
# =========================
with tabs[2]:
    st.header("📱 Caption + Hashtags Generator")

    caption_topic = st.text_input("Content Topic")

    if st.button("Generate Caption"):
        prompt = f"""
        Write a viral Instagram caption in Hinglish for: {caption_topic}

        Also give:
        - 10 hashtags
        - SEO optimized
        """

        res = model.generate_content(prompt)
        st.write(res.text)

# =========================
# 🖼️ IMAGE GENERATOR
# =========================
with tabs[3]:
    st.header("🖼️ AI Image Generator")

    img_prompt = st.text_input("Enter Image Prompt")
    ratio = st.selectbox("Aspect Ratio", ["1:1", "9:16", "16:9"])

    if st.button("Generate Image"):
        try:
            url = f"https://image.pollinations.ai/prompt/{img_prompt}"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))

            st.image(img, caption="Generated Image")

        except Exception as e:
            st.error(f"Error: {e}")

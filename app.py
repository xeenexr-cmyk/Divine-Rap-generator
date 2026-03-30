import streamlit as st
import google.generativeai as genai
import moviepy.editor as mp
import requests
from PIL import Image
from io import BytesIO

# CONFIG
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Divine Rap AI Studio", layout="wide")
st.title("🎤 Divine Rap AI Content Factory (Stable Pro)")

menu = st.sidebar.selectbox("Choose Tool", [
    "Script Generator",
    "Image Generator",
    "Video Builder",
    "Text → Video",
    "Caption + Hashtags",
    "Hook Generator"
])

# -------------------------------
# 1. SCRIPT
# -------------------------------
if menu == "Script Generator":
    prompt = st.text_input("Enter topic")

    if st.button("Generate Script"):
        res = model.generate_content(
            f"Write devotional rap lyrics on: {prompt}"
        )
        st.write(res.text)

# -------------------------------
# 2. IMAGE GENERATOR (2K / 4K)
# -------------------------------
elif menu == "Image Generator":
    prompt = st.text_input("Enter image idea")

    ratio = st.selectbox("Aspect Ratio", ["1:1", "9:16", "16:9"])
    quality = st.selectbox("Quality", ["HD", "2K", "4K"])

    if st.button("Generate Image"):
        url = f"https://image.pollinations.ai/prompt/{prompt}"
        img = Image.open(BytesIO(requests.get(url).content))

        if ratio == "9:16":
            size = (720,1280) if quality=="HD" else (1440,2560) if quality=="2K" else (2160,3840)
        elif ratio == "16:9":
            size = (1280,720) if quality=="HD" else (2560,1440) if quality=="2K" else (3840,2160)
        else:
            size = (1024,1024)

        img = img.resize(size)

        st.image(img)
        img.save("image.png")

        with open("image.png", "rb") as f:
            st.download_button("Download Image", f)

# -------------------------------
# 3. VIDEO BUILDER
# -------------------------------
elif menu == "Video Builder":
    images = st.file_uploader("Upload images", accept_multiple_files=True)

    if st.button("Create Video") and images:
        files = []

        for i, img in enumerate(images):
            name = f"img_{i}.png"
            with open(name, "wb") as f:
                f.write(img.read())
            files.append(name)

        clips = [mp.ImageClip(f).set_duration(2) for f in files]
        video = mp.concatenate_videoclips(clips)

        video.write_videofile("video.mp4", fps=24)
        st.video("video.mp4")

# -------------------------------
# 4. TEXT → VIDEO
# -------------------------------
elif menu == "Text → Video":
    prompt = st.text_input("Enter idea")

    if st.button("Generate Video"):
        scenes = model.generate_content(
            f"Create 3 cinematic scenes for: {prompt}"
        ).text.split("\n")

        files = []

        for i, scene in enumerate(scenes[:3]):
            url = f"https://image.pollinations.ai/prompt/{scene}"
            name = f"scene_{i}.png"

            with open(name, "wb") as f:
                f.write(requests.get(url).content)

            files.append(name)
            st.image(name, caption=scene)

        clips = [mp.ImageClip(f).set_duration(2) for f in files]
        video = mp.concatenate_videoclips(clips)

        video.write_videofile("final.mp4", fps=24)
        st.video("final.mp4")

# -------------------------------
# 5. CAPTION + HASHTAGS
# -------------------------------
elif menu == "Caption + Hashtags":
    prompt = st.text_input("Enter topic")

    if st.button("Generate"):
        res = model.generate_content(
            f"Generate YouTube title, description and comma-separated tags for: {prompt}"
        )
        st.write(res.text)

# -------------------------------
# 6. HOOK GENERATOR
# -------------------------------
elif menu == "Hook Generator":
    prompt = st.text_input("Enter topic")

    if st.button("Generate Hooks"):
        res = model.generate_content(
            f"Generate 5 viral hooks for: {prompt}"
        )
        st.write(res.text)

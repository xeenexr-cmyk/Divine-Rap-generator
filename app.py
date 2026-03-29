import streamlit as st
import google.generativeai as genai
from moviepy.editor import ImageClip, concatenate_videoclips, TextClip, CompositeVideoClip
import requests
from PIL import Image
from io import BytesIO

# CONFIG
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Divine Rap AI Studio", layout="wide")
st.title("🎤 Divine Rap AI Content Factory (ULTIMATE)")

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
        res = model.generate_content(f"Write devotional rap lyrics on: {prompt}")
        st.write(res.text)

# -------------------------------
# 2. IMAGE GENERATOR
# -------------------------------
elif menu == "Image Generator":
    prompt = st.text_input("Enter image idea")

    ratio = st.selectbox("Aspect Ratio", ["1:1", "9:16", "16:9"])

    if st.button("Generate Image"):
        url = f"https://image.pollinations.ai/prompt/{prompt}"
        img = Image.open(BytesIO(requests.get(url).content))

        if ratio == "9:16":
            img = img.resize((720,1280))
        elif ratio == "16:9":
            img = img.resize((1280,720))
        else:
            img = img.resize((1024,1024))

        st.image(img)

        img.save("img.png")
        with open("img.png", "rb") as f:
            st.download_button("Download", f)

# -------------------------------
# 3. VIDEO BUILDER
# -------------------------------
elif menu == "Video Builder":
    images = st.file_uploader("Upload images", accept_multiple_files=True)

    if st.button("Create Video"):
        files = []

        for i, img in enumerate(images):
            name = f"img_{i}.png"
            with open(name, "wb") as f:
                f.write(img.read())
            files.append(name)

        clips = []

        for f in files:
            clip = ImageClip(f).set_duration(2).resize((720,1280)).fadein(0.5).fadeout(0.5)
            clips.append(clip)

        video = concatenate_videoclips(clips)
        video.write_videofile("video.mp4", fps=24)

        st.video("video.mp4")

# -------------------------------
# 4. TEXT → VIDEO (WITH SUBTITLE)
# -------------------------------
elif menu == "Text → Video":
    prompt = st.text_input("Enter idea")

    if st.button("Generate Video"):
        scenes = model.generate_content(
            f"Create 3 cinematic scenes for: {prompt}"
        ).text.split("\n")

        clips = []

        for i, scene in enumerate(scenes[:3]):
            url = f"https://image.pollinations.ai/prompt/{scene}"
            img_path = f"scene_{i}.png"

            with open(img_path, "wb") as f:
                f.write(requests.get(url).content)

            image_clip = ImageClip(img_path).set_duration(2).resize((720,1280))

            text_clip = TextClip(scene[:40], fontsize=40, color='white', size=(700,200))
            text_clip = text_clip.set_position(("center","bottom")).set_duration(2)

            final = CompositeVideoClip([image_clip, text_clip])
            clips.append(final.fadein(0.5).fadeout(0.5))

            st.image(img_path, caption=scene)

        video = concatenate_videoclips(clips)
        video.write_videofile("final.mp4", fps=24)

        st.video("final.mp4")

        with open("final.mp4", "rb") as f:
            st.download_button("Download Video", f)

# -------------------------------
# 5. CAPTION
# -------------------------------
elif menu == "Caption + Hashtags":
    prompt = st.text_input("Enter topic")

    if st.button("Generate"):
        res = model.generate_content(
            f"Generate YouTube title, description and comma-separated tags for: {prompt}"
        )
        st.write(res.text)

# -------------------------------
# 6. HOOK
# -------------------------------
elif menu == "Hook Generator":
    prompt = st.text_input("Enter topic")

    if st.button("Generate Hooks"):
        res = model.generate_content(
            f"Generate 5 viral hooks for: {prompt}"
        )
        st.write(res.text)

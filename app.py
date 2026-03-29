import streamlit as st
import google.generativeai as genai
from moviepy.editor import ImageClip, concatenate_videoclips
import requests
from PIL import Image
from io import BytesIO

# CONFIG
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Divine Rap AI Studio", layout="wide")
st.title("🎤 Divine Rap AI Content Factory (Ultra Version)")

menu = st.sidebar.selectbox("Choose Tool", [
    "Script Generator",
    "Image Generator",
    "Video Builder",
    "Text → Video",
    "Caption + Hashtags",
    "Hook Generator"
])

# -------------------------------
# 1. SCRIPT GENERATOR
# -------------------------------
if menu == "Script Generator":
    prompt = st.text_input("Enter topic")

    if st.button("Generate Script"):
        res = model.generate_content(
            f"Write a powerful devotional rap lyrics on: {prompt}"
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
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        # Resolution logic
        if ratio == "9:16":
            if quality == "HD":
                size = (720,1280)
            elif quality == "2K":
                size = (1440,2560)
            else:
                size = (2160,3840)

        elif ratio == "16:9":
            if quality == "HD":
                size = (1280,720)
            elif quality == "2K":
                size = (2560,1440)
            else:
                size = (3840,2160)

        else:
            size = (1024,1024)

        img = img.resize(size)

        st.image(img, caption=f"{ratio} - {quality}")

        img.save("generated.png")
        with open("generated.png", "rb") as f:
            st.download_button("Download Image", f, file_name="image.png")

# -------------------------------
# 3. VIDEO BUILDER
# -------------------------------
elif menu == "Video Builder":
    images = st.file_uploader("Upload images", accept_multiple_files=True)

    if st.button("Create Video"):
        image_files = []

        for i, img in enumerate(images):
            file_name = f"img_{i}.png"
            with open(file_name, "wb") as f:
                f.write(img.read())
            image_files.append(file_name)

        clips = [ImageClip(img).set_duration(2).resize((720,1280)) for img in image_files]
        video = concatenate_videoclips(clips)

        video.write_videofile("output.mp4", fps=24)

        st.video("output.mp4")

        with open("output.mp4", "rb") as f:
            st.download_button("Download Video", f, file_name="video.mp4")

# -------------------------------
# 4. TEXT → VIDEO
# -------------------------------
elif menu == "Text → Video":
    prompt = st.text_input("Enter idea")

    if st.button("Generate Video"):
        scenes = model.generate_content(
            f"Create 3 cinematic scenes for: {prompt}"
        ).text.split("\n")

        image_files = []

        for i, scene in enumerate(scenes[:3]):
            url = f"https://image.pollinations.ai/prompt/{scene}"
            img_data = requests.get(url).content

            file_name = f"scene_{i}.png"
            with open(file_name, "wb") as f:
                f.write(img_data)

            image_files.append(file_name)
            st.image(file_name, caption=scene)

        clips = [ImageClip(img).set_duration(2).resize((720,1280)) for img in image_files]
        video = concatenate_videoclips(clips)

        video.write_videofile("final.mp4", fps=24)

        st.video("final.mp4")

        with open("final.mp4", "rb") as f:
            st.download_button("Download Video", f, file_name="divine_video.mp4")

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

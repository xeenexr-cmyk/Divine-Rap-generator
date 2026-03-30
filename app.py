import streamlit as st
import google.generativeai as genai
from moviepy.editor import ImageClip, concatenate_videoclips
import requests
from PIL import Image
from io import BytesIO

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Divine Rap AI Generator")

menu = st.sidebar.selectbox("Menu", [
    "Script",
    "Image",
    "Video",
    "Text to Video"
])

# SCRIPT
if menu == "Script":
    prompt = st.text_input("Enter topic")

    if st.button("Generate"):
        res = model.generate_content(prompt)
        st.write(res.text)

# IMAGE
elif menu == "Image":
    prompt = st.text_input("Enter image idea")

    if st.button("Generate Image"):
        url = f"https://image.pollinations.ai/prompt/{prompt}"
        img = Image.open(BytesIO(requests.get(url).content))

        img = img.resize((720,1280))

        st.image(img)

# VIDEO
elif menu == "Video":
    images = st.file_uploader("Upload images", accept_multiple_files=True)

    if st.button("Create Video") and images:
        files = []

        for i, img in enumerate(images):
            name = f"img_{i}.png"
            with open(name, "wb") as f:
                f.write(img.read())
            files.append(name)

        clips = [ImageClip(f).set_duration(2) for f in files]
        video = concatenate_videoclips(clips)

        video.write_videofile("video.mp4", fps=24)
        st.video("video.mp4")

# TEXT TO VIDEO
elif menu == "Text to Video":
    prompt = st.text_input("Enter idea")

    if st.button("Generate Video"):
        scenes = model.generate_content(prompt).text.split("\n")

        files = []

        for i, scene in enumerate(scenes[:3]):
            url = f"https://image.pollinations.ai/prompt/{scene}"
            name = f"scene_{i}.png"

            with open(name, "wb") as f:
                f.write(requests.get(url).content)

            files.append(name)
            st.image(name)

        clips = [ImageClip(f).set_duration(2) for f in files]
        video = concatenate_videoclips(clips)

        video.write_videofile("final.mp4", fps=24)
        st.video("final.mp4")

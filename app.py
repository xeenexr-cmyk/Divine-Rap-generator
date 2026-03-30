import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO
import moviepy.editor as mp

st.set_page_config(page_title="Divine Rap AI Factory", layout="wide")
st.title("🎤 Divine Rap AI Content Factory (Hybrid Pro MAX 🔥)")

menu = st.sidebar.selectbox("Choose Tool", [
    "Script Generator",
    "Hook Generator",
    "Caption + Hashtags",
    "Image Generator",
    "Image → Video",
    "Text → Video"
])

# -------------------------------
# SCRIPT
# -------------------------------
def generate_script(topic):
    lines = [
        f"{topic} 🔥 Mahadev ka tandav, duniya hil jayegi",
        f"Har Har Mahadev 🚩 Aaj bhakti rap suno dil se",
        f"{topic} ⚡ Shiv ki shakti, har andhera tod degi",
        f"Mahadev ka naam lo, darr khud bhaag jayega",
    ]
    return "\n".join(random.sample(lines, 3))

# -------------------------------
# HOOK
# -------------------------------
def generate_hooks(topic):
    hooks = [
        "⚡ 3 sec me dimag hil jayega!",
        "🚩 Ye sunke ro padoge...",
        "🔥 Shiv bhakt ho to ye zarur dekho!",
        "😳 Aisa rap pehle kabhi nahi suna!",
        "💥 Ye video skip mat karna!"
    ]
    return "\n".join(random.sample(hooks, 3))

# -------------------------------
# CAPTION
# -------------------------------
def generate_caption(topic):
    return f"{topic} 🔱\n\nHar Har Mahadev 🙏\n\n#mahadev #shiv #bhakti #shorts #viral #hindurap"

# -------------------------------
# IMAGE
# -------------------------------
def generate_image(prompt):
    url = f"https://image.pollinations.ai/prompt/{prompt}"
    return Image.open(BytesIO(requests.get(url).content))

# -------------------------------
# SCRIPT UI
# -------------------------------
if menu == "Script Generator":
    topic = st.text_input("Enter topic")
    if st.button("Generate Script"):
        st.write(generate_script(topic))

# -------------------------------
# HOOK UI
# -------------------------------
elif menu == "Hook Generator":
    topic = st.text_input("Enter topic")
    if st.button("Generate Hooks"):
        st.write(generate_hooks(topic))

# -------------------------------
# CAPTION UI
# -------------------------------
elif menu == "Caption + Hashtags":
    topic = st.text_input("Enter topic")
    if st.button("Generate Caption"):
        st.write(generate_caption(topic))

# -------------------------------
# IMAGE GENERATOR (RATIO + QUALITY)
# -------------------------------
elif menu == "Image Generator":
    prompt = st.text_input("Enter image idea")

    ratio = st.selectbox("Aspect Ratio", ["1:1", "9:16", "16:9"])
    quality = st.selectbox("Quality", ["HD", "2K", "4K"])

    if st.button("Generate Image"):
        img = generate_image(prompt)

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
# IMAGE → VIDEO
# -------------------------------
elif menu == "Image → Video":
    images = st.file_uploader("Upload images", accept_multiple_files=True)

    if st.button("Create Video") and images:
        files = []

        for i, img in enumerate(images):
            name = f"img_{i}.png"
            with open(name, "wb") as f:
                f.write(img.read())
            files.append(name)

        clips = [mp.ImageClip(f).set_duration(2).resize((720,1280)) for f in files]
        video = mp.concatenate_videoclips(clips)

        video.write_videofile("video.mp4", fps=24)
        st.video("video.mp4")

        with open("video.mp4", "rb") as f:
            st.download_button("Download Video", f)

# -------------------------------
# TEXT → VIDEO
# -------------------------------
elif menu == "Text → Video":
    topic = st.text_input("Enter topic")

    if st.button("Generate Video"):
        scenes = [
            f"{topic} divine energy",
            f"{topic} powerful shiva form",
            f"{topic} cosmic tandav"
        ]

        files = []

        for i, scene in enumerate(scenes):
            img = generate_image(scene)
            name = f"scene_{i}.png"
            img.save(name)
            files.append(name)
            st.image(name, caption=scene)

        clips = [mp.ImageClip(f).set_duration(2).resize((720,1280)) for f in files]
        video = mp.concatenate_videoclips(clips)

        video.write_videofile("final.mp4", fps=24)
        st.video("final.mp4")

        with open("final.mp4", "rb") as f:
            st.download_button("Download Video", f)

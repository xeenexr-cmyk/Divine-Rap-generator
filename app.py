import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO
import moviepy.editor as mp

st.set_page_config(page_title="Divine Rap AI Factory", layout="wide")
st.title("🎤 Divine Rap AI Content Factory (Ultimate 🔥)")

menu = st.sidebar.selectbox("Choose Tool", [
    "Auto Song Generator",
    "Hook Generator",
    "Caption + Hashtags",
    "Image Generator",
    "Image → Video",
    "Text → Video"
])

# -------------------------------
# AUTO SONG GENERATOR
# -------------------------------
def generate_song(topic, style):
    intro = f"🎤 {topic}\n\n"

    if style == "Rap":
        verse = [
            "Beat pe aaya Mahadev ka flow",
            "Trinetra khule to lage sab slow",
            "Damru ki dhun me universe lost",
            "Shiv naam le, tu ban ja boss"
        ]
        hook = ["🔥 Har Har Mahadev!", "🚩 Bam Bam Bhole!", "⚡ Shiv on the beat!"]

    elif style == "Bhajan":
        verse = [
            "Shiv Shambhu mere mann me base",
            "Har pal tera naam hi jape",
            "Kailash pati tum ho sahara",
            "Bhakton ka tum ho ujiyara"
        ]
        hook = ["🙏 Har Har Mahadev", "🕉️ Om Namah Shivay", "🌼 Jai Shiv Shankar"]

    elif style == "Emotional":
        verse = [
            "Sati ka prem kabhi mita nahi",
            "Virah me bhi wo jhuka nahi",
            "Aansu me bhi bhakti thi",
            "Unki kahani alag hi thi"
        ]
        hook = ["💔 Mahadev...", "😢 Sati...", "🙏 Shiv Shambhu"]

    else:  # Tandav
        verse = [
            "Tandav kare jab Mahakaal",
            "Hil jaaye pura brahmand saal",
            "Agni jale aur dharti hile",
            "Shiv ka roop sabko jala de"
        ]
        hook = ["🔥 Tandav!", "⚡ Mahakaal!", "💥 Har Har Mahadev!"]

    song = intro
    song += "🎶 Verse 1:\n" + "\n".join(random.sample(verse, 3)) + "\n\n"
    song += "🎧 Hook:\n" + random.choice(hook) + "\n\n"
    song += "🎶 Verse 2:\n" + "\n".join(random.sample(verse, 3)) + "\n\n"
    song += "🎧 Hook:\n" + random.choice(hook) + "\n\n"
    song += "✨ Outro:\nMahadev ka naam hi antim satya hai 🙏"

    return song

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
# UI
# -------------------------------

if menu == "Auto Song Generator":
    topic = st.text_input("Enter topic")
    style = st.selectbox("Select Style", ["Rap", "Bhajan", "Emotional", "Tandav"])

    if st.button("Generate Full Song"):
        st.write(generate_song(topic, style))

elif menu == "Hook Generator":
    topic = st.text_input("Enter topic")
    if st.button("Generate Hooks"):
        st.write(generate_hooks(topic))

elif menu == "Caption + Hashtags":
    topic = st.text_input("Enter topic")
    if st.button("Generate Caption"):
        st.write(generate_caption(topic))

elif menu == "Image Generator":
    prompt = st.text_input("Enter image idea")

    ratio = st.selectbox("Aspect Ratio", ["1:1", "9:16", "16:9"])

    if st.button("Generate Image"):
        img = generate_image(prompt)

        if ratio == "9:16":
            size = (720,1280)
        elif ratio == "16:9":
            size = (1280,720)
        else:
            size = (1024,1024)

        img = img.resize(size)
        st.image(img)

        img.save("image.png")
        with open("image.png", "rb") as f:
            st.download_button("Download Image", f)

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
            st.image(name)

        clips = [mp.ImageClip(f).set_duration(2).resize((720,1280)) for f in files]
        video = mp.concatenate_videoclips(clips)

        video.write_videofile("final.mp4", fps=24)
        st.video("final.mp4")

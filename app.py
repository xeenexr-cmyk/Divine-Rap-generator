import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO
import moviepy.editor as mp

st.set_page_config(page_title="Divine Rap AI Factory", layout="wide")
st.title("🎤 Divine Rap AI Content Factory (Creator Control 🔥)")

menu = st.sidebar.selectbox("Choose Tool", [
    "Smart Rap Generator",
    "Hook Generator",
    "Caption + Hashtags",
    "Image Generator",
    "Image → Video",
    "Text → Video"
])

# -------------------------------
# 🔥 SMART RAP GENERATOR
# -------------------------------
def generate_rap(topic, mood, keywords):
    words = keywords.split(",")

    aggressive_lines = [
        "जब गूंजे तेरा नाम, धरती भी कांपे",
        "तेरे तांडव से समय भी थम जाए",
        "तेरी शक्ति से हर डर मिट जाए",
        "तेरे क्रोध में पूरा संसार जल जाए"
    ]

    emotional_lines = [
        "तेरी यादों में दिल ये रोता है",
        "तेरे बिना सब अधूरा लगता है",
        "तेरा नाम ही अब सहारा है",
        "तेरी भक्ति में सुकून मिलता है"
    ]

    devotional_lines = [
        "तेरा नाम ही मेरी पहचान बने",
        "तेरे चरणों में ये जीवन ढले",
        "हर सांस में बस तू ही रहे",
        "तेरी भक्ति ही मेरा रास्ता बने"
    ]

    if mood == "Aggressive":
        base = aggressive_lines
    elif mood == "Emotional":
        base = emotional_lines
    else:
        base = devotional_lines

    def create_line():
        word = random.choice(words).strip() if words else topic
        return f"{word} का असर जब दिल पे छाए,\n{random.choice(base)}"

    verse1 = create_line() + "\n" + create_line()
    verse2 = create_line() + "\n" + create_line()

    hook = random.choice([
        "🔥 हर हर महादेव!",
        "🚩 जय बजरंगबली!",
        "⚡ जय श्री राम!"
    ])

    song = f"🎤 {topic}\n\n"
    song += "🎶 Verse 1:\n" + verse1 + "\n\n"
    song += "🎧 Hook:\n" + hook + "\n\n"
    song += "🎶 Verse 2:\n" + verse2 + "\n\n"
    song += "🎧 Hook:\n" + hook + "\n\n"
    song += "✨ Outro:\nतेरा नाम ही मेरी शक्ति है 🙏"

    return song

# -------------------------------
# HOOK
# -------------------------------
def generate_hooks(topic):
    hooks = [
        "⚡ ये वीडियो skip मत करना!",
        "🔥 3 सेकंड में दिमाग हिल जाएगा!",
        "🚩 हर भक्त को ये सुनना चाहिए!",
        "😳 ऐसा पहले कभी नहीं देखा!",
        "💥 ये सच आपको हिला देगा!"
    ]
    return "\n".join(random.sample(hooks, 3))

# -------------------------------
# CAPTION
# -------------------------------
def generate_caption(topic):
    return f"{topic} 🔱\n\nHar Har Mahadev 🙏\n\n#mahadev #hanuman #shiv #shorts #viral"

# -------------------------------
# IMAGE
# -------------------------------
def generate_image(prompt):
    url = f"https://image.pollinations.ai/prompt/{prompt}"
    return Image.open(BytesIO(requests.get(url).content))

# -------------------------------
# UI
# -------------------------------

if menu == "Smart Rap Generator":
    topic = st.text_input("Enter topic")
    mood = st.selectbox("Select Mood", ["Aggressive", "Emotional", "Devotional"])
    keywords = st.text_input("Enter keywords (comma separated)", "Shiv, Sati, Tandav")

    if st.button("Generate Rap"):
        st.write(generate_rap(topic, mood, keywords))

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

    if st.button("Generate Image"):
        img = generate_image(prompt)
        img = img.resize((720,1280))
        st.image(img)

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
            f"{topic} cinematic shiva",
            f"{topic} tandav fire"
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

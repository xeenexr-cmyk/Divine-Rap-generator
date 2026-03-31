import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO
import moviepy.editor as mp

st.set_page_config(page_title="Divine Rap AI Factory", layout="wide")
st.title("🎤 Divine Rap AI Content Factory (Bollywood Pro 🔥)")

menu = st.sidebar.selectbox("Choose Tool", [
    "Bollywood Song Generator",
    "Hook Generator",
    "Caption + Hashtags",
    "Image Generator",
    "Image → Video",
    "Text → Video"
])

# -------------------------------
# 🎤 BOLLYWOOD SONG GENERATOR
# -------------------------------
def generate_song(topic, style):
    import random

    title = f"🎤 {topic}\n\n"

    # Different style tones
    if style == "Emotional":
        verse_lines = [
            "तेरे बिना ये जीवन अधूरा सा लगे",
            "तेरी यादों में हर पल दिल ये जले",
            "आँखों में तेरी छवि बस जाती है",
            "हर सांस में बस तेरा नाम ही रहे"
        ]

    elif style == "Bhajan":
        verse_lines = [
            "तेरा नाम ही मेरी पूजा बने",
            "तेरे चरणों में ये जीवन ढले",
            "हर पल तेरा ही ध्यान रहे",
            "मेरे मन में बस तू ही बसे"
        ]

    elif style == "Tandav":
        verse_lines = [
            "जब तांडव करे तू, धरती भी डरे",
            "तेरी ज्वाला से ये जग सारा जले",
            "तेरी शक्ति से ब्रह्मांड हिले",
            "तेरे क्रोध से समय भी थमे"
        ]

    else:  # Rap
        verse_lines = [
            "तेरे नाम की गूंज हर जगह फैले",
            "तेरी शक्ति से हर डर ये भागे",
            "जब तू साथ हो तो किस बात का डर",
            "तेरे नाम से ही जीत ये मिले"
        ]

    hook_lines = [
        "🔥 हर हर महादेव!",
        "🚩 बम बम भोले!",
        "⚡ जय शिव शंकर!"
    ]

    # Create verses
    verse1 = "\n".join(random.sample(verse_lines, 3))
    verse2 = "\n".join(random.sample(verse_lines, 3))

    hook = random.choice(hook_lines)

    outro = "✨ तेरे नाम में ही मेरी दुनिया, महादेव 🙏"

    # Final Song
    song = title
    song += "🎶 Verse 1:\n" + verse1 + "\n\n"
    song += "🎧 Hook:\n" + hook + "\n\n"
    song += "🎶 Verse 2:\n" + verse2 + "\n\n"
    song += "🎧 Hook:\n" + hook + "\n\n"
    song += outro

    return song

# -------------------------------
# HOOK GENERATOR
# -------------------------------
def generate_hooks(topic):
    hooks = [
        "⚡ ये सुनकर दिमाग हिल जाएगा!",
        "🔥 ये वीडियो skip मत करना!",
        "🚩 हर शिव भक्त के लिए जरूरी!",
        "😳 ऐसा पहले कभी नहीं देखा!",
        "💥 ये सच आपको हिला देगा!"
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

if menu == "Bollywood Song Generator":
    topic = st.text_input("Enter topic")
    style = st.selectbox("Select Style", ["Rap", "Bhajan", "Emotional", "Tandav"])

    if st.button("Generate Full Bollywood Song"):
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

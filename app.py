import streamlit as st
import base64
import os
from openai import OpenAI
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip, VideoFileClip

# API Key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🎤 Divine Rap Generator (AI)")

prompt = st.text_input("Enter your Divine Rap Idea")

# STEP 1: Scene Generation
def generate_scenes(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Create exactly 3 short cinematic scenes (one line each) for: {prompt}"}
        ]
    )
    scenes = response.choices[0].message.content.split("\n")
    scenes = [s.strip("- ").strip() for s in scenes if s.strip()]
    return scenes[:3]

# STEP 2: Image Generation
def generate_image(scene, i):
    result = client.images.generate(
        model="gpt-image-1",
        prompt=scene,
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    file_name = f"scene_{i}.png"
    with open(file_name, "wb") as f:
        f.write(image_bytes)

    return file_name

# STEP 3: Video Creation
def create_video(images):
    clips = []
    for img in images:
        clip = ImageClip(img).set_duration(3)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    video.write_videofile("output.mp4", fps=24)

    return "output.mp4"

# STEP 4: Add Music
def add_music(video_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip("music/bg.mp3").subclip(0, video.duration)

    final = video.set_audio(audio)
    final.write_videofile("final.mp4", fps=24)

    return "final.mp4"

# MAIN
if st.button("Generate Divine Video"):
    if not prompt:
        st.warning("Please enter a prompt")
    else:
        st.write("⚡ Generating Scenes...")
        scenes = generate_scenes(prompt)

        images = []
        for i, scene in enumerate(scenes):
            st.write(f"🎬 {scene}")
            img = generate_image(scene, i)
            images.append(img)

        st.write("🎥 Creating Video...")
        video = create_video(images)

        st.write("🎵 Adding Music...")
        final_video = add_music(video)

        st.success("✅ Done!")
        st.video(final_video)

from moviepy import ImageClip, concatenate_videoclips, AudioFileClip, TextClip, CompositeVideoClip
from gtts import gTTS

# 🎤 Gujarati voice
text_voice = "Nanji... tame mane muki ne kem jata rahya? Ak na ak divas badha ne javu j pade... pan hu hamesha tari sathe j chu."
tts = gTTS(text=text_voice, lang='gu')
tts.save("voice.mp3")

# 📸 Images
clip1 = ImageClip("grandfather.jpg").with_duration(6).resized(height=720)
clip1 = clip1.with_position("center").resized(lambda t: 1 + 0.05*t)

clip2 = ImageClip("father.jpg").with_duration(6).resized(height=720)
clip2 = clip2.with_position("center").resized(lambda t: 1 + 0.05*t)

# 💬 Text (FIXED FINAL)
text1 = TextClip(
    text="Papa... tame mane muki ne kem jata rahya?",
    font_size=40,
    color="white"
).with_position(("center", "bottom")).with_duration(6)

text2 = TextClip(
    text="Ak na ak divas badha ne javu j pade... hu hamesha tari sathe chu",
    font_size=35,
    color="yellow"
).with_position(("center", "bottom")).with_duration(6)

# 🎥 Scenes
scene1 = CompositeVideoClip([clip1, text1])
scene2 = CompositeVideoClip([clip2, text2])

# 🔗 Combine
video = concatenate_videoclips([scene1, scene2], method="compose")

# 🔊 Audio
audio = AudioFileClip("voice.mp3")
video = video.with_audio(audio)

# 📤 Export
video.write_videofile(
    "final_video.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)
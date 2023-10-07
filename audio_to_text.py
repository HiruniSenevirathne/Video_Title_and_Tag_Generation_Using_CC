import sys
sys.path.append('./ffmpeg-master-latest-win64-gpl/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe')
import speech_recognition as sr
from pydub import AudioSegment
import os

# pip3 install SpeechRecognition                                                            
# pip3 install pydub

# Load the video file
# video = AudioSegment.from_file("videoplayback.mp4", format="mp4")
# audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
# audio.export("audio.wav", format="wav")




# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Open the audio file
with sr.AudioFile("videoplayback.wav") as source:
    audio_text = r.record(source)
# Recognize the speech in the audio
text = r.recognize_google(audio_text, language='en-US')
print(text)
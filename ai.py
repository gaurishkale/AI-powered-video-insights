import moviepy as  mp
import speech_recognition as sr

video_path = r'uploads\EVM_ Bharat Ki Misaal (Language_ English _ 45 Sec.).mp4'
audio_path = 'audio.wav'

print("Converting video to audio.Please wait...")
video = mp.VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)


recognizer = sr.Recognizer()

with sr.AudioFile(audio_path) as source:
    print("Recognizing...")
    audio = recognizer.record(source)


try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)

    text_file_path = 'text.txt'
    with open(text_file_path, 'w') as f:
        f.write(text)
    print("Text saved to", text_file_path)    



except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
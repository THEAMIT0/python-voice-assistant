import pyttsx3
import pywhatkit
import wikipedia
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import time
import webbrowser

# Text to Speech
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Record audio without PyAudio
def record_audio(filename="audio.wav", duration=2, fs=44100):
    print("Listening...")
    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )
    sd.wait()
    write(filename, fs, recording)

# Speech recognition
def listen():
    record_audio()

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile("audio.wav") as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()

    except Exception as e:
        print("Error:", e)
        return ""

# Main Program
speak("Hello. Voice Assistant is online. How can I help you?")

while True:
    command = listen()

    if not command:
        continue

    if "exit" in command or "stop" in command:
        speak("Goodbye")
        break

    elif "show time" in command:
        current_time = time.strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "play" in command:
        song = command.replace("play", "").strip()
        if song:
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)
    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

# Open Google
    elif "open google" in command:
         speak("Opening Google")
         webbrowser.open("https://www.google.com")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=2)
            speak(info)
        except:
            speak("I could not find information.")

    else:
        speak("I did not understand.")
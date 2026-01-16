"""
Project Title: Voice Assistant using Python

Description:
This project is a basic voice assistant developed using Python.
It listens to voice commands and performs simple tasks such as:
- Greeting the user
- Telling current time and date
- Searching information on the web
- Exiting on command

Technologies Used:
- Python
- SpeechRecognition
- pyttsx3
- Webbrowser module

This project demonstrates basic concepts of speech recognition,
task automation, and user interaction.
"""
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand.")
        return ""

# Greeting
speak("Hello! I am your voice assistant.")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {date}")

    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        break

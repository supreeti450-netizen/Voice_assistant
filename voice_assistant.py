"""
Project Title: Voice Assistant using Python

Description:
This project is a basic voice assistant developed using Python.
It listens to voice commands and performs simple tasks such as:
- Greeting the user
- Telling current time and date
- Searching the web
- Exiting on command

Technologies Used:
- Python
- SpeechRecognition
- pyttsx3
- datetime
- webbrowser
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys

# Initialize text-to-speech engine (safe setup)
try:
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
except:
    engine = None

def speak(text):
    print("Assistant:", text)
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except:
            pass

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

# Greeting
speak("Hello! I am your voice assistant.")

while True:
    command = listen()

    if command == "":
        continue

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query != "":
            webbrowser.open("https://www.google.com/search?q=" + query)
            speak("Here are the search results.")

    elif "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye! Have a nice day.")
        sys.exit()

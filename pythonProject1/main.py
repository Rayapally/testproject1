import speech_recognition as sr
import pyttsx3
import nltk
from nltk.corpus import wordnet
from datetime import datetime
import webbrowser
import os


# Initialize Text-to-Speech (TTS)
engine = pyttsx3.init()

# Initialize Speech Recognition
recognizer = sr.Recognizer()
# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet():
    current_time = datetime.now().strftime("%H:%M:%S")
    if datetime.now().hour < 12:
        speak(f"Good morning! It's currently {current_time}")
    elif 12 <= datetime.now().hour < 18:
        speak(f"Good afternoon! It's currently {current_time}")
    else:
        speak(f"Good evening! It's currently {current_time}")

# Function to perform a Google search
def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Function to open a website
def open_website(url):
    webbrowser.open(url)

# Function to tell a joke
def tell_joke():
    joke = "Why don't scientists trust atoms? Because they make up everything!"
    speak(joke)


# Main loop
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        # Recognize speech
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        # Perform actions based on user input
        if "hello" in command:
            greet()
        elif "search" in command:
            query = command.split("search")[-1].strip()
            google_search(query)
        elif "open website" in command:
            url = command.split("open website")[-1].strip()
            open_website(url)
        elif "tell me a joke" in command:
            tell_joke()
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to help with that.")

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import openai

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input and convert to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return None
        except sr.RequestError:
            speak("Couldn't connect to the recognition service.")
            return None

def process_command(command):
    """Process voice commands and execute tasks."""
    if not command:
        return

    if 'wikipedia' in command:
        query = command.replace('wikipedia', '')
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)

    elif 'play' in command:
        song = command.replace('play', '')
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)

    elif 'time' in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    elif 'search' in command:
        query = command.replace('search', '')
        speak(f"Searching {query} on Google.")
        pywhatkit.search(query)
        
    elif 'exit' in command:
        speak("Goodbye! Have a great day sir.")
        exit()

    else:
        speak("oops sorry buddy i m not know much about that.")

# Main loop
if __name__ == "__main__":
    speak("Hello, my self mark, i m an ai chatbot built for killing your troubles, so  how can i assist you buddy?")
    while True:
        user_command = listen()
        if user_command:
            process_command(user_command)
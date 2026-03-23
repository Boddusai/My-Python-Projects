import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia

# Initialize speech engine
engine = pyttsx3.init()

# Set voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Wish user
def wish_user():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am your voice assistant. How can I help you?")


# Take voice input
def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You said:", query)
        return query.lower()

    except Exception:
        print("Say that again please...")
        return "none"


# Main program
if __name__ == "__main__":
    wish_user()

    while True:
        query = take_command()

        # Wikipedia search
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        # Open YouTube
        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        # Open Google
        elif "open google" in query:
            webbrowser.open("https://google.com")

        # Open Gmail
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com")

        # Tell time
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        # Tell date
        elif "date" in query:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        # Play music (change path)
        elif "play music" in query:
            music_dir = "C:\\Users\\Public\\Music"  # change this path
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        # Open Notepad
        elif "open notepad" in query:
            os.system("notepad")

        # Google search
        elif "search" in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        # Exit assistant
        elif "exit" in query or "stop" in query or "bye" in query:
            speak("Goodbye. Have a nice day!")
            break
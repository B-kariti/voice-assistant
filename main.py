
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen to the user's voice
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""

    except sr.RequestError:
        print("Could not connect. Check your internet.")
        return ""


def process_command(command):

    if "time" in command:
        time_now = datetime.datetime.now()
        speak(f"The current time is {time_now.strftime('%H:%M')}")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif "open github" in command:
        webbrowser.open("https://www.github.com")
        speak("Opening GitHub.")

    elif "open school portal" in command:
        webbrowser.open("https://portal.dkut.ac.ke/")  
        speak("Opening the school portal.")

    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        speak("Opening Gmail.")

    elif "play music" in command:
        webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=3e0f8b6e2f4a4b7a")  
        speak("Playing music.")

    else:
        speak("Sorry, I can't perform that action. Please try again.")

speak("how u doing my G or may i say sweetie, Am Bruce your voice assistant, How many i help?")

while True:
    command = listen()

    if "exit" in command or "stop" in command:
        speak("Goodbye!")
        break

    if command:
        process_command(command)

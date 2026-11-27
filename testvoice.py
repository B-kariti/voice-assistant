import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

for voice in voices:
    print("Voice:", voice.name)

engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 150)

print("Starting speech...")
engine.say("Hello. Can you hear me?")
engine.runAndWait()
print("Speech finished.")
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

## Uncomment below to list available voices
# for i, voice in enumerate(voices):
#     print(f"{i}: {voice.name} ({voice.id})")

engine.setProperty('voice', voices[0].id)
    
def say(text):
    engine.say(text)
    engine.runAndWait()
    
def takeCommmands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"Bhuvan: {query}")
        return query
    except sr.UnknownValueError:
        say("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        say("Speech service is unavailable.")
        return None
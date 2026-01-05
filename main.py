import os
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
    
if __name__ == "__main__":
    print("SAGE AI")
    say("Hello, I am SAGE AI, your personal assistant.")
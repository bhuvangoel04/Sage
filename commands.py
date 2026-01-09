import os
from speech import say
import webbrowser

def processCommand(command):
    if "exit" in command or "quit" in command:
        say("Goodbye Bhuvan, see you soon.")
        return "EXIT"

    elif "open notepad" in command:
        say("Opening Notepad")
        os.system("notepad")
    elif "open youtube" in command:
        say("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        
    elif "hello" in command:
        say("Hello Bhuvan")

    else:
        say("I am still learning that command")

    return "CONTINUE"
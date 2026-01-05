import os
from speech import say

def processCommand(command):
    if "exit" in command or "quit" in command:
        say("Goodbye Bhuvan")
        exit()

    elif "open notepad" in command:
        say("Opening Notepad")
        os.system("notepad")

    elif "hello" in command:
        say("Hello Bhuvan")

    else:
        say("I am still learning that command")

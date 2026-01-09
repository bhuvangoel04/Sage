from speech import say
from apps import open_app
from websites import open_site

def processCommand(command):

    if "exit" in command or "quit" in command or "bye" in command:
        say("Goodbye Bhuvan, see you soon.")
        return "EXIT"

    if command.startswith("open "):
        target = command.replace("open ", "").strip()

        if open_app(target): # try to open an app first otherwise treat it as website
            say(f"Opening {target}")
            return "CONTINUE"

        say(f"Opening {target}")
        open_site(target)
        return "CONTINUE"

    if "hello" in command or "hi" in command:
        say("Hello Bhuvan")
        return "CONTINUE"

    say("I am still learning that command")
    return "CONTINUE"

from speech import say, takeCommmands
from commands import processCommand


if __name__ == "__main__":
    say("Hello Bhuvan, What can I do for you today?")
    print("SAGE AI at your service!")
    while True:
        cmd = takeCommmands()
        if cmd:
            processCommand(cmd.lower())
from speech import say, takeCommands
from commands import processCommand


if __name__ == "__main__":
    say("Hello Bhuvan, What can I do for you today?")
    print("SAGE AI at your service!")
    while True:
        cmd = takeCommands()
        if cmd:
            result = processCommand(cmd.lower())
            if result == "EXIT":
                break
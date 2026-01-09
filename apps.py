import os
import subprocess
import shutil

APPS = {
    "notepad": "notepad",
    "calculator": "calc",
    "command prompt": "cmd",
    "vscode": "code",
    "vs code": "code",
    "visual studio code": "code",
}

def open_app(app_name):
    app_name = app_name.lower()

    if app_name in APPS:
        command = APPS[app_name]

        # Check if command exists in PATH
        if shutil.which(command):
            subprocess.Popen(command)
            return True

        # Fallback for VS Code
        vscode_path = r"C:\Users\{}\AppData\Local\Programs\Microsoft VS Code\Code.exe".format(os.getlogin())
        if os.path.exists(vscode_path):
            subprocess.Popen(vscode_path)
            return True

    return False

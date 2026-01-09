import os
import subprocess
import shutil

APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "command prompt": "cmd.exe",
    "vscode": "code.cmd", 
    "vs code": "code.cmd",
    "visual studio code": "code.cmd",
}

def open_app(app_name):
    app_name = app_name.lower().strip()
    if app_name not in APPS:
        return False

    command = APPS[app_name]
    full_path = shutil.which(command)
    # Check if command exists in PATH
    if full_path:
        subprocess.Popen([full_path])
        return True

    # Fallback for VS Code
    if "code" in command:
        vscode_path = os.path.join(os.getenv('LOCALAPPDATA'), 
                                   "Programs", "Microsoft VS Code", "Code.exe")
        if os.path.exists(vscode_path):
            subprocess.Popen([vscode_path])
            return True

    return False

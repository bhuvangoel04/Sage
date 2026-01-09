import os

APPS = {
    "notepad": "notepad",
    "calculator": "calc",
    "command prompt": "cmd",
    "vscode": "code",
    "vs code": "code",
    "visual studio code": "code",
}

def open_app(app_name):
    if app_name in APPS:
        os.system(APPS[app_name])
        return True
    return False

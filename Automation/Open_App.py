import pyautogui as gui
import subprocess
import time

def open_App(text):
    try:
        # Try opening app directly via subprocess
        subprocess.run(text)
    except Exception as e:
        # If direct open fails, simulate search via Start menu
        gui.press("win")
        time.sleep(0.1)
        gui.write(text)
        time.sleep(0.1)
        gui.press("enter")



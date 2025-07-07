import subprocess
import pyautogui as ui
import time

def play_music_on_spotify(song_name):
    # Launch Spotify
    subprocess.Popen("spotify")
    time.sleep(6)

    # Focus search bar and search song
    ui.hotkey("ctrl", "l")
    time.sleep(1)
    ui.write(song_name)
    ui.press("enter")
    time.sleep(2)

    # Move mouse to the play button (center of green circle)
    ui.moveTo(809, 381, duration=0.3)  # <-- Replace with your actual coordinates
    ui.click()


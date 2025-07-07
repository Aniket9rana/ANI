import time
import pywhatkit as kt
import random
from DLG import playsong, playing_dlg
from NetHyTech_Pyttsx3_Speak import speak


def play_music_on_youtube(text):
    playdlg = random.choice(playsong)
    speak(playdlg,3)
    kt.playonyt(text)
    time.sleep(3)
    playdlg =random.choice(playing_dlg)
    speak(playdlg+text,3)

while True:
    try:
        user_input = input("Enter the song name to play on YouTube (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        play_music_on_youtube(user_input)
    except Exception as e:
        print(f"An error occurred: {e}")
        break
# pip install SpeechRecognition==3.14.3
# pip install pyaudio
# pip install mtranslate colorama

import speech_recognition as sr
import os
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

def Translate_hindi_to_english(text):
    english_text = translate(text, "en-in")
    return english_text

def Speech_To_Text_Python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 40000
    recognizer.dynamic_energy_adjustment_damping = 0.016
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.2
    recognizer.operation_timeout = None
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.GREEN + "Bolo bhai..", flush=True)

        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.LIGHTBLACK_EX + "Recognizing...", end="", flush=True)
                recognizer_text = recognizer.recognize_google(audio, language='hi-IN').lower()
                if recognizer_text:
                    trans_text = Translate_hindi_to_english(recognizer_text)
                    print("\r" + Fore.BLUE + "Ani : " + trans_text)

                else:
                   continue
            except sr.UnknownValueError:
                print("\r" + Fore.RED + "Sorry, didn’t catch that.")
            except Exception as e:
                print("\r" + Fore.RED + f"Error: {e}")
            finally:
                print("\r", end="", flush=True)
                os.system("cls" if os.name == "nt" else "clear")


Speech_To_Text_Python()

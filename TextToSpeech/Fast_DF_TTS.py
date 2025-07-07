import os
import subprocess
import tempfile
from playsound import playsound #pip install playsound==1.2.2
import threading

def speak(text:str,voice:str="en-IN-NeerjaNeural")->None:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
            output_file = temp_file.name
        command = f"edge-tts --voice {voice} --text \"{text}\" --write-media \"{output_file}\""
        subprocess.run(command, shell=True, check=True)

        threading.Thread(target=playsound, args=(output_file,)).start()

    except Exception as e:
        print(f"⚠️ Error during speech synthesis or playback: {e}")


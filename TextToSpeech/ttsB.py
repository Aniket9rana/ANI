import requests 
from playsound import playsound  # pip install playsound==1.2.2
import os
from typing import Union

def generate_audio(message: str, voice: str = "Joanna") -> Union[bytes, None]:
    # Corrected URL
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.content
    except Exception as e:
        print(f"⚠️ Error fetching audio: {e}")
        return None
    

def speak(message: str, voice: str = "Joanna", folder: str = "", extension: str = ".mp3") -> Union[str, None]:
    try:
        result_content = generate_audio(message, voice)
        if not result_content:
            print("❌ Failed to get audio.")
            return None

        file_path = os.path.join(folder, f"{voice}{extension}")
        with open(file_path, "wb") as file:
            file.write(result_content)

        playsound(file_path)
        os.remove(file_path)

        return file_path
    except Exception as e:
        print(f"⚠️ Error during speech synthesis or playback: {e}")
        return None

# ✅ Test
speak("Hello sir, I am Jarvis and I am online and fully operational.")
speak("How are you doing today, Aniket?")
speak("I am here to assist you with any tasks you need help with.")
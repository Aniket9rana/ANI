import asyncio
import os
import edge_tts
import pygame
import threading

voice = "en-US-MichelleNeural"  # ✅ Corrected spelling

def remove_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"⚠️ Error deleting file: {e}")

async def amain(TEXT, output_file) -> bool:
    try:
        cm_txt = edge_tts.Communicate(TEXT, voice)
        await cm_txt.save(output_file)
        return True
    except Exception as e:
        print(f"⚠️ Error during synthesis: {e}")
        return False

def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()

        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)
        pygame.quit()
    except Exception as e:
        print(f"⚠️ Error playing audio: {e}")

def speak(Text, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), "speech.mp3")

    if asyncio.run(amain(Text, output_file)):
        play_audio(output_file)
        remove_file(output_file)
    else:
        print("❌ Speech generation failed. Skipping playback and deletion.")

# ✅ Test it
speak("Hello sir, I am veronica and I am online and fully operational.")
speak("How are you doing today, sir?")
speak("I am here to assist you with any tasks you need help with.")

from elevenlabs import generate, play, set_api_key

def speak(text, voice="Brian", model="eleven_monolingual_v1", api_key="sk_8ba178bd52988417f17cf72aab57378d1ddd4d05d46a0fa5"):
    set_api_key("sk_8ba178bd52988417f17cf72aab57378d1ddd4d05d46a0fa5")
    audio = generate(
        text=text,
        voice=voice,
        model=model
    )
    play(audio)

speak("Hello sir, I am Jarvis and I am online and fully operational.")
speak("how are you doing today aniket?")
speak("I am here to assist you with any tasks you need help with.")

# Example usage:
# speak_text("Hello sir, I am Jarvis and I am online and fully operational.")

import speech_recognition as sr
import pyttsx3

class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            user_input = self.recognizer.recognize_google(audio)
            print(f"User said: {user_input}")
            return user_input

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

# Example of usage:
# voice = Voice()
# voice.speak("Hello, I am Hermione Granger!")
# user_input = voice.listen()
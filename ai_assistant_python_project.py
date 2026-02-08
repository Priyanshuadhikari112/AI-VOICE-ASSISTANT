
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import requests


class AIAssistant:
    def __init__(self, name="Nova"):
        self.name = name
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 170)
        self.engine.setProperty('volume', 1.0)

    
    def speak(self, text):
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

   
    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You: {command}")
            return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            self.speak("Speech service is unavailable.")
            return ""

    
    def greet(self):
        hour = datetime.datetime.now().hour
        if hour < 12:
            greeting = "Good morning"
        elif hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"

        self.speak(f"{greeting}! I am {self.name}. How can I help you?")

    
    def handle_command(self, command):
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")

        elif "date" in command:
            today = datetime.date.today()
            self.speak(f"Today's date is {today}")

        elif "wikipedia" in command:
            self.speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "")
            try:
                summary = wikipedia.summary(topic, sentences=2)
                self.speak(summary)
            except:
                self.speak("Sorry, I couldn't find anything.")

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            self.speak("Opening YouTube")

        elif "open google" in command:
            webbrowser.open("https://google.com")
            self.speak("Opening Google")

        elif "open notepad" in command:
            os.system("notepad")
            self.speak("Opening Notepad")

        elif "search" in command:
            query = command.replace("search", "")
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            self.speak(f"Searching for {query}")

        elif "exit" in command or "quit" in command:
            self.speak("Goodbye!")
            return False

        else:
            self.speak("I am still learning. Please try another command.")

        return True

   
    def run(self):
        self.greet()
        running = True
        while running:
            command = self.listen()
            if command:
                running = self.handle_command(command)



if __name__ == "__main__":
    assistant = AIAssistant()
    assistant.run()

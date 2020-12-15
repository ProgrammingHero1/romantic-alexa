import sys

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine. setProperty("rate", 158)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"
    return command


if __name__ == "__main__":
    while True:
        wakeup = takecommand().lower()
        #you can wake up the assistant using a keyword. The assistant will wait until you say that specific keyword
        if 'assistant' in wakeup:
            talk('Tell me')
            #here the assistant will take your command
            command = takecommand().lower()

            if 'play' in command:
                song = command.replace('play', '')
                talk('Playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk(time)
            elif 'who is' or 'what is' in command:
                person = command.replace('who is', '')
                person = command.replace('what is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'joke' in command:
                talk(pyjokes.get_joke())
            elif 'turn off' or 'shutdown' in command:
                talk('Ok, see you later')
                sys.exit(-1)
            #if the command is not recognized it will ask for the keyword again, like Alexa or Google Assistant
            else:
                pass

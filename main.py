import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import psutil
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def News():
    URL = 'https://www.aajtak.in/rssfeeds?id=home'
    CLIENT = urlopen(URL)
    
    XML_PAGE = CLIENT.read()
    soup_page= soup(XML_PAGE,"xml")
    news_list = soup_page.findAll("item")
    for news in news_list:
        print(news.title.text)
        talk(news.description.text)
        print('-'*10)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
   
    r = sr.Recognizer()                                                                                  
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except Exception as e:
        talk('say again sure i will do it')
        query = take_command()
    query = query.lower()
    return query


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'tell news' in command:
        News()

    elif "Introduce yourself" in command:
        talk("Okay,Let me start by The time I was born,,")
        talk("I was a dream of a boy dreaming to make a perfect virtual assistant")
        talk("He soon established the company named ROGER industries")
        talk("Slowly,I came to life")
        talk("I started learning various things like calculations,General knowldge etc etc")
        talk("Now I am capable of doing various things like Beatboxing,opening applications,Cracking jokes,Playing music etc.")
        talk("Okay,thats a wrap I wont say more ")

    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()

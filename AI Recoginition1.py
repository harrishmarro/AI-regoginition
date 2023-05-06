# -*- coding: utf-8 -*-

import speech_recognition as sr
import pyaudio
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from langdetect import detect
import pyjokes
import pyowm
import time
from translate import Translator
global command
command=''
global c
c=1


r = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
engine.say("hi I am mister your personal assistant")
engine.runAndWait()
engine.say("what can i do for u")
engine.runAndWait()
def conversion(command1):
    translator= Translator(from_lang="tamil",to_lang="english")
    translation = translator.translate(command1)
    print(translation)
    return translation
def analyse(source):
    audio = r.listen(source)
    command1 = r.recognize_google(audio,language="ta-IN")
    command=conversion(command1)
    command=command.lower()
    return command
def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def recogonize(r):
    command='' 
    try:
        with sr.Microphone() as source:
            print('speak something: ')
            engine.say("i am listening")
            engine.runAndWait()
            command=analyse(source)
            engine.runAndWait()
            if 'mister' in command:
                command=command.replace("mister",'')
                print('you said: {}'.format(command))
                return command
    except:
        pass
    return command

def play_siri():
    reply=recogonize(r)
    if 'play' in reply:
       song=reply.replace('play','')
       talk('playing'+song)
       pywhatkit.playonyt(song)
       time.sleep(10)
    elif 'time' in reply:
        time1=datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is'+time1)
        print(time1)
    elif 'tell me about' in reply:
        person=reply.replace('tell me about','')
        info=wikipedia.summary(person, 2)
        talk(info)
    elif 'thank you'in reply:
        talk('no mention its my job') 
    elif 'translate'in reply:
        trans=reply.replace("hey translate",'')
        find=detect(trans)
        print(find)
    elif 'joke'in reply:
       talk(pyjokes.get_joke())
    elif 'weather' in reply:
        city='CHENNAI'
        owm=pyowm.OWM('d210f7ffe0c6dd3832e90f9c1ccbb9f6')
        mgr=owm.weather_manager()
        location=mgr.weather_at_place(city+',IND')
        weather=location.weather
        k=weather.status
        print(weather)
        print(weather.temperature('celsius'))
        p=weather.temperature('celsius')
        talk('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius and feels like %s' % (city, k, p['temp_max'], p['temp_min'],p['feels_like']))
    elif 'nothing' in reply:
        talk("i am going to sleep")
        global c
        c=0
    elif 'off' in reply:
        c=0
    elif 'whats your life span'in reply:
        talk("my life span is 2,37,972 years")
while True:
    play_siri()
    if c==0:
        print(" ok")
        break
    

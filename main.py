import speech_recognition as sr
import webbrowser
import datetime
import os
import time
from time import ctime
import random
from gtts import gTTS


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            Mya_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Mya_speak("sorry, I didn't get that")
        except sr.RequestError:
            Mya_speak('Sorry, my speech service is down')
        return voice_data
    
def Mya_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    print(audio_file)
    os.remove(audio_file)
    
    
     
def respond(voice_data):
    if 'what is your name' in voice_data:
        Mya_speak('My name is Mya. How can I help you?')
    if 'how are you' in voice_data:
        Mya_speak('I am fine. Thank you')
    if 'where are you' in voice_data:
        Mya_speak('I am in your computer')
    if 'what time is it' in voice_data:
        Mya_speak(ctime())
    if 'what is the time' in voice_data:
        Mya_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for, dear?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Mya_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        Mya_speak('Here is the location of ' + location)
    if 'Mya exit' in voice_data:
        exit()
        
        
time.sleep(1)
Mya_speak("Hello, I am Mya. How can I help you?")

while 1:
    voice_data = record_audio()
    respond(voice_data)

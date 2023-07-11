
# ?pip install pyaudio
# ?pip install pyttsx3
# ?pip install wikipedia
# ?pip install smtplib
# ?pip install random
# ?pip install sys
# ?pip install speechRecognition
#? .
#? .
#? .
#? .
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random
import time
import subprocess
import sys
import requests
from bs4 import BeautifulSoup
from pywikihow import RandomHowTo, search_wikihow
import pywhatkit

from email.message import EmailMessage


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

is_paused = False
# *Greet when it started.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!")

    elif hour>=12 and hour<18:
        Speak("Good Afternoon!")   

    else:
        Speak("Good Evening!")

    Speak("Hello, I am Jarvis , How can i help you .")  

# *For exit the programm.
goodbyes = ['You are Great!', 'Thanks for using me!', 'Nice meeting with you!']
    
# *For taking all commands and listen the user voices.
def TakeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        Speak("Say that aganin please") 
        return "None"
    return query

#& Using For location finding by google.
def My_Location():

    op = "https://goo.gl/maps/z56P6phYWZM7tpt89"

    Speak("Checking....")
    webbrowser.open(op)
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    print(f"Sir , You Are Now In {state , country} .")
    Speak(f"Sir , You Are Now In {state , country} .")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

# *Function to send an email.
def send_email(sender_email, sender_password, recipient_email, subject, content):
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(content)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("Email sent successfully.")
    Speak("Email sent successfully.")

# ~Using Dictionary to mapping recipent names and their email id's.

recipient_mapping = {
    "official mail": "garg33269@gmail.com",
    "manju garg": "manjugarg2580@gmail.com",
    "webit": "webytube73@gmail.com",
    "joker": "arpitgarg887@gmail.com",
    "kinshu": "kinshu6237@gmail.com",
    # *Add more recipient mappings as needed.
}

# & Fetch sender's email and password 
# & Here you will add your email id and password which you want to use to send email to other recipents.
# & You make sure that you cant use your original password for privicy concern.
# & you can use google 'less secure apps' feature.


sender_email = "arpitgarg5689@gmail.com"
sender_password = "wkaohztjzrmbjala"

if __name__ == "__main__":
    wishMe()  
# Main program loop
while True:
    query = TakeCommand().lower()

         # *Set the path to the Chrome executable
         # ~Which browser you want to use to execute.
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        
        # *Configure the web browser to use Chrome
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    if query:
        if "write an email" in query:
              print("To whom do you want to send the email?")
              Speak("To whom do you want to send the email?")

              recipient_name = TakeCommand().lower()
              recipient_email = recipient_mapping.get(recipient_name)
  
              if recipient_email:
                  print("What's the subject of the email?")
                  Speak("What's the subject of the email?")
                  subject = TakeCommand().lower()
  
                  print("What's the content of the email?")
                  Speak("What's the content of the email?")
                  content = TakeCommand().lower()
  
                  send_email(sender_email, sender_password, recipient_email, subject, content)
              else:
                  print("Sorry, the recipient's email address is not found.")
                  Speak("Sorry, the recipient's email address is not found.")
        
        
        if 'thoda ruko' in query:
            is_paused = True
            Speak("Jarvis will be stopped!")
        elif 'start' in query:
            is_paused = False
            Speak("Jarvis will be started!")


        # *Logic for executing tasks based on query
        if 'search on wikipedia' in query:
            Speak('Searching Wikipedia...')
            query = TakeCommand().lower()
            query = query.replace("wikipedia", "")
            page = wikipedia.page(query)
            url = page.url
            webbrowser.open(url)
            results = wikipedia.summary(query, sentences=1)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)
        
        elif 'search on google' in query:
            Speak('What would you like to search for?')
            search_query = TakeCommand().lower()
            url = f'https://www.google.com/search?q={search_query}'
            webbrowser.open(url)


        elif 'play music' in query:
        # Specify the URL you want to open
            url = "https://www.youtube.com/watch?v=DbiRVNeZPnw&list=PLpmsNGoQrkhF1nNjDVXAcyVsNnLOdw_1h&pp=gAQBiAQB8AUB"
            webbrowser.get('chrome').open(url)

        elif 'my location' in query:
            My_Location()     

        elif 'youtube search' in query:
            Query = query.replace("jarvis","")
            query = Query.replace("search on youtube","")
            YouTubeSearch(query)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            Speak(f"Sir, the time is {strTime}") 

        elif 'speed test' in query:
            webbrowser.get('chrome').open("fast.com")         

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")  

        elif 'open amazon' in query:
            webbrowser.get('chrome').open("amazon.in")

        elif'open flipkart' in query:
            webbrowser.get('chrome').open("flipkart.com")

        elif'open meesho' in query:
            webbrowser.get('chrome').open("meesho.com")

        elif'open myntra' in query:
            webbrowser.get('chrome').open("myntra.com")

        elif 'open code' in query:
            codePath = "C:\\Users\\gomti\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

    # Normal features to use
        elif 'namaste' in query:
            Speak("Namaste!")
            continue
    
        elif 'kaise ho' in query:
            Speak("I am good, thanks for asking!")
            continue
    
        elif 'exit' in query:
            Speak(random.choice(goodbyes))
            sys.exit()
        
        else:
            print("No query matched")
        
    
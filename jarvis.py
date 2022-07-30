import pyttsx3
import wikipedia
import webbrowser
import speech_recognition as sr
import pyaudio
import datetime
## from googlesearch import search

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait

def qquery():
    Hello()

    while True:
        query = command().lower()
        if "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue
        elif "from wikipedia" in query:
            speak("Checking the wikipedia")
            print("Checking the wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            ## speak(result)
            print(result)
            continue
        elif "search google" in query:
            speak("what do you want to search")
            print("search")
            query = query.replace("google", "")
            ##search(query)
            continue
        elif "open rule34" in query:
            speak("opening rule34")
            webbrowser.open("https://www.reddit.com/r/rule34/")
            continue
        elif "open instagram" in query:
            speak("opening instagram")
            webbrowser.open("www.instagram.com")
            continue
        elif "open my instagram" in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/hrnjicaedis/")
            continue
        elif "open reddit" in query:
            speak ("opening Reddit")
            webbrowser.open("www.reddit.com")
            continue
        elif "open youtube" in query:
            speak("opening youtube")
            print("opening youtube")
            webbrowser.open("www.youtube.com")
            continue
        elif "which day it is" in query:
            tellDay()
            continue
         
        elif "tell me the time" in query:
            tellTime()
            continue
        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop Assistant")
            continue

        elif "bye" in query:
            speak ("bye bye")
            exit()

        
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try: 
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
         
        return Query

def tellDay():
    day = datetime.datetime.today().weekday() + 1
     
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime(self):
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    self.Speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")

def Hello():
    speak("hello sir I am your desktop assistant. Tell me how may I help you")


if __name__ == '__main__':
     
    qquery()
from time import strftime

import speech_recognition as sr
import os
import webbrowser
import openai
import datetime

from wikipedia import languages


def say(text):
    os.system(f"say '{text}'")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
          print("Recognizing...")
          query = r.recognize_google(audio, language="en-in")
          print(f"User said: {query}")
          return query
        except Exception as e:
          return "Some Error Occurred. Sorry from Jarvis"



if __name__ == "__main__":
    print("PyCharm")
    say("Hello, I am Jarvis ")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["Instagram", "https://www.instagram.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "open music" in query:
            musicpath = "/Users/navneetkumarrajpoot/Desktop/flute-traditional-v1-251387.mp3"
            os.system(f"open {musicpath}")

        if "the time" in query:
            musicpath = "/Users/navneetkumarrajpoot/Desktop/flute-traditional-v1-251387.mp3"
            strftime = datetime.datetime.now(). strftime("%H:%M:%S")
            say(f"Sir the time is {strftime}")


        if "open slack".lower() in query.lower():
            os.system(f"open /Applications/Slack.app")

        if "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        #if query:
            #say(query)
        #else:
            #say("I didn't catch that. Please try again.")





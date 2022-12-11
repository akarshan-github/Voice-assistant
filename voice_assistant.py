
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia


print('Hey,I am opticron your personal Voice assistant')

voice_eng=pyttsx3.init()
voices=voice_eng.getProperty('voices')
voice_eng.setProperty('voice','voices[1].id')

def speak(text):
    voice_eng.say(text)
    voice_eng.runAndWait()

def Greet():
    hr=datetime.datetime.now().hour
    if hr>=0 and hr<12:
        speak("Good Morning,from opticron")
        print("Good Morning,from opticron")
    elif hr>=12 and hr<=16:
        speak("Good Afternoon,from opticron")
        print("Good Afternoon,from opticron")
    elif hr>16 and hr<=20:
        speak("Good Evening,from opticron")
        print("Good Evening,from opticron")
    else:
        speak("Good Night,from opticron")
        print("Good Night,from opticron")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            user_request=r.recognize_google(audio,language='en-in')
            print(f"user said:{user_request}\n")

        except Exception as e:
            speak("Sorry i am unable to understand, please say that again")
            return "None"
        return user_request

speak("Hey,I am opticron your personal Voice assistant")
Greet()

if __name__=='__main__':


    while True:
        speak("Tell me how can opticron help you?")
        user_request = takeCommand().lower()
        if user_request==0:
            continue
        
        if "good bye" in user_request or "ok bye" in user_request or "stop" in user_request:
            speak('Good Bye your personal assistant Opticron is shutting down')
            print('Good Bye your personal assistant Opticron is shutting down')
            break
        if "my name" in user_request:
            speak('thats a nice name')
            print('thats a nice name')
            time.sleep(5)

        if "your name" in user_request:
            speak('i am opticron your personal voice assistant,whats your name')
            print('i am opticron, your personal voice assistant,whats your name')
            name_request = takeCommand()
            speak('thats a nice name')
            print('thats a nice name')
            time.sleep(5)

        if 'wikipedia' in user_request:
            speak('Searching Wikipedia...')
            user_request =user_request.replace("wikipedia", "")
            wiki_load = wikipedia.summary(user_request, sentences=4)
            speak("According to Wikipedia")
            print(wiki_load)
            speak(wiki_load)

        elif 'youtube' in user_request:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("I have opened Youtube,have a good time Youtubing")
            time.sleep(5)

        elif 'google' in user_request:
            webbrowser.open_new_tab("https://www.google.com")
            speak("I have opened google chrome,happy googling")
            time.sleep(5)

        elif 'gmail' in user_request:
            webbrowser.open_new_tab("gmail.com")
            speak("I have opened google mail,happy mailing")
            time.sleep(5)

        elif "weather" in user_request:
            weather_api="8ef61edcf1c576d65d836254e11ea420"
            weather_base_Url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            name_of_city=takeCommand()
            complete_url=weather_base_Url+"appid="+weather_api+"&q="+name_of_city
            response = requests.get(complete_url)
            obj=response.json()
            if obj["cod"]!="404":
                weather_obj=obj["main"]
                temperature_now = weather_obj["temp"]
                humidity_now = weather_obj["humidity"]
                z = obj["weather"]
                weather_description = z[0]["description"]
                speak(f" Temperature in {name_of_city}  now is " +
                      str(temperature_now) +
                      "kelvin, \n  humidity in {name_of_city} in percentage is " +
                      str(humidity_now) +
                      "\n weather description in {name_of_city} is  " +
                      str(weather_description))
                print(f" Temperature in {name_of_city}  now = " +
                      str(temperature_now) +
                      "kelvin, \n  humidity in {name_of_city} in percentage now = " +
                      str(humidity_now) +
                      "\n weather description in {name_of_city} now = " +
                      str(weather_description))

            else:
                speak("city being requested is not known")



        elif 'time' in user_request:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time now is {strTime}")

        elif 'who are you' in user_request or 'what can you do' in user_request:
            speak('I am opticron your persoanl voice assistant.I am programmed to perform minor tasks'
                  ' why to type when i can open youtube for you,google chrome can also be opened by me,need to mail someone,i can open gmail for you,want to ask something from stackoverflow,i can also open stackoverflow for you ,want to know time ,dont worry opticron can do it for you,feeling lazy to capture an image, opticron can do it for you,also can search wikipedia,want to go for a date opticron can tell about the weather for you' 
                  'depending on your city , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in user_request or "who created you" in user_request or "who discovered you" in user_request:
            speak("I was built by Akarshan ")
            print("I was built by Akarshan")

        elif "open stackoverflow" in user_request:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in user_request:
            news_from_toi = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'love' in user_request:
            speak('I love you too')
            print('I Love you')

        elif 'song' in user_request:
            speak('Playing vande matram')
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=e41Bwihtke8")
            time.sleep(60)

        elif "camera" in user_request or "take a photo" in user_request:
            ec.capture(0,"robo camera","img.jpg")

        elif 'iitj' in user_request:
            webbrowser.open_new_tab("https://www.iitj.ac.in/")
            speak('Here is website of iitj')
            time.sleep(5)

        elif 'search'  in user_request:
            user_request = user_request.replace("search", "")
            webbrowser.open_new_tab(user_request)
            time.sleep(5)

        elif 'ask' in user_request:
            speak('Opticron can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res_answer = client.query(question)
            answer_to_question = next(res_answer.results).text
            speak(answer_to_question)
            print(answer_to_question)


        elif "log off" in user_request or "sign out" in user_request:
            speak("Ok , opticron will will log off  your pc  in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3) 
import streamlit as st
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import speech_recognition as sr
import pyttsx3
import datetime


# Add your code here...
# Define the Streamlit app
stop_opticron = False

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://hssbend.com/wp-content/uploads/2019/03/amazon-echo-dot.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


def start_engine():
    voice_eng=pyttsx3.init()
    voices=voice_eng.getProperty('voices')
    voice_eng.setProperty('voice','voices[1].id')
    return voice_eng

def speak(voice_eng,text):
    voice_eng.say(text)
    voice_eng.runAndWait()

def Greet(voice_eng):
    hr=datetime.datetime.now().hour
    if hr>=0 and hr<12:
        speak(voice_eng,"Good Morning,from opticron")
        #print("Good Morning,from opticron")
        st.write("Good Morning,from opticron")
    elif hr>=12 and hr<=16:
        speak(voice_eng,"Good Afternoon,from opticron")
        # print("Good Afternoon,from opticron")
        st.write("Good Afternoon,from opticron")
    elif hr>16 and hr<=20:
        speak(voice_eng,"Good Evening,from opticron")
        # print("Good Evening,from opticron")
        st.write("Good Evening,from opticron")
    else:
        speak(voice_eng,"Good Night,from opticron")
        # print("Good Night,from opticron")
        st.write("Good Evening,from opticron")

def takeCommand(voice_eng):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #print("Listening...")
        st.write("Listening...")
        audio=r.listen(source)

        try:
            user_request=r.recognize_google(audio,language='en-in')
            # print(f"user said:{user_request}\n")
            st.write(f"user said:{user_request}\n")

        except Exception as e:
            speak(voice_eng,"Sorry i am unable to understand, please say that again")
            return "None"
        return user_request



def main():
    st.title("Opticron - Your Personal Voice Assistant")
    st.write("just say 'Ok bye' or 'stop' to stop opticron")
    #col1, col2, col3 = st.columns(3)
    # col1, col2,col3 = st.columns(3)

    if st.button("Run Opticron"):
        #print('Hey,I am opticron your personal Voice assistant')
        st.write('Hey,I am opticron your personal Voice assistant')
        voice_eng = start_engine()
        speak(voice_eng,"Hey,I am opticron your personal Voice assistant")
        Greet(voice_eng)
        run_opticron(voice_eng)


    # run_button = col1.button("Run Opticron", key="run_button")
    # stop_button = col2.button("Stop Opticron", key="stop_button")
    # if run_button:
    #     stop_opticron = False
    #     st.write('Hey,I am opticron your personal Voice assistant')
    #     voice_eng = start_engine()
    #     speak(voice_eng, "Hey,I am opticron your personal Voice assistant")
    #     Greet(voice_eng)
    #     run_opticron(voice_eng)
    #
    # if stop_button:
    #     stop_opticron = True
    #     st.write('Good Bye your personal assistant Opticron is shutting down')

# Define your Opticron code as a function
def run_opticron(voice_eng):
        while not stop_opticron:
            speak(voice_eng,"Tell me how can opticron help you?")
            user_request = takeCommand(voice_eng).lower()
            if user_request == 0:
                continue

            if "good bye" in user_request or "ok bye" in user_request or "stop" in user_request:
                speak(voice_eng,'Good Bye your personal assistant Opticron is shutting down')
                # print('Good Bye your personal assistant Opticron is shutting down')
                st.write('Good Bye your personal assistant Opticron is shutting down')
                break

            if "my name" in user_request:
                speak(voice_eng,'thats a nice name')
                # print('thats a nice name')
                st.write('Good Bye your personal assistant Opticron is shutting down')
                time.sleep(5)

            if "your name" in user_request:
                speak(voice_eng,'i am opticron your personal voice assistant,whats your name')
                # print('i am opticron, your personal voice assistant,whats your name')
                st.write('i am opticron, your personal voice assistant,whats your name')
                name_request = takeCommand(voice_eng)
                speak(voice_eng,'thats a nice name')
                # print('thats a nice name')
                st.write('thats a nice name')
                time.sleep(5)

            elif 'youtube' in user_request:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak(voice_eng,"I have opened Youtube,have a good time Youtubing")
                st.write("I have opened Youtube,have a good time Youtubing")
                time.sleep(5)

            elif 'google' in user_request:
                webbrowser.open_new_tab("https://www.google.com")
                speak(voice_eng,"I have opened google chrome,happy googling")
                st.write("I have opened google chrome,happy googling")
                time.sleep(5)

            elif 'gmail' in user_request:
                webbrowser.open_new_tab("gmail.com")
                speak(voice_eng,"I have opened google mail,happy mailing")
                st.write("I have opened google mail,happy mailing")
                time.sleep(5)

            elif "weather" in user_request:
                weather_api = "8ef61edcf1c576d65d836254e11ea420"
                weather_base_Url = "https://api.openweathermap.org/data/2.5/weather?"
                speak(voice_eng,"whats the city name")
                name_of_city = takeCommand(voice_eng)
                complete_url = weather_base_Url + "appid=" + weather_api + "&q=" + name_of_city
                response = requests.get(complete_url)
                obj = response.json()
                if obj["cod"] != "404":
                    weather_obj = obj["main"]
                    temperature_now = weather_obj["temp"]
                    humidity_now = weather_obj["humidity"]
                    z = obj["weather"]
                    weather_description = z[0]["description"]
                    speak(voice_eng,f" Temperature in {name_of_city}  now is " +
                          str(temperature_now) +
                          f"kelvin, \n  humidity in {name_of_city} in percentage is " +
                          str(humidity_now) +
                          f"\n weather description in {name_of_city} is  " +
                          str(weather_description))
                    # print(f" Temperature in {name_of_city}  now = " +
                    #       str(temperature_now) +
                    #       f"kelvin, \n  humidity in {name_of_city} in percentage now = " +
                    #       str(humidity_now) +
                    #       f"\n weather description in {name_of_city} now = " +
                    #       str(weather_description))
                    st.write(f" Temperature in {name_of_city}  now = " +
                          str(temperature_now) +
                          f"kelvin, \n  humidity in {name_of_city} in percentage now = " +
                          str(humidity_now) +
                          f"\n weather description in {name_of_city} now = " +
                          str(weather_description))

                else:
                    speak(voice_eng,"city being requested is not known")
                    st.write("city being requested is not known")
                time.sleep(5)



            elif 'time' in user_request:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(voice_eng,f"the time now is {strTime}")
                st.write(f"the time now is {strTime}")
                time.sleep(5)

            elif 'who are you' in user_request or 'what can you do' in user_request:
                speak(voice_eng,'I am opticron your persoanl voice assistant.I am programmed to perform minor tasks'
                      ' why to type when i can open youtube for you,google chrome can also be opened by me,need to mail someone,i can open gmail for you,want to ask something from stackoverflow,i can also open stackoverflow for you ,want to know time ,dont worry opticron can do it for you,feeling lazy to capture an image, opticron can do it for you,also can search wikipedia,want to go for a date opticron can tell about the weather for you'
                      'depending on your city , get top headline news from times of india and you can ask me computational or geographical questions too!')
                time.sleep(2)


            elif "who made you" in user_request or "who created you" in user_request or "who discovered you" in user_request:
                speak(voice_eng,"I was built by Akarshan ")
                # print("I was built by Akarshan")
                st.write("I was built by Akarshan")

            elif "open stackoverflow"  in user_request:
                webbrowser.open_new_tab("https://stackoverflow.com/")
                speak(voice_eng,"Here is stackoverflow")
                st.write("Here is stackoverflow")
                time.sleep(6)

            elif 'news' in user_request:
                news_from_toi = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak(voice_eng,'Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)

            elif 'love' in user_request:
                speak(voice_eng,'I love you too')
                # print('I Love you')
                st.write('I Love you')

            elif 'song' in user_request:
                speak(voice_eng,'Playing vande matram')
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=e41Bwihtke8")
                time.sleep(60)


            elif 'iitj' in user_request:
                webbrowser.open_new_tab("https://www.iitj.ac.in/")
                speak(voice_eng,'Here is website of iitj')
                st.write('Here is website of iitj')
                time.sleep(5)

            elif 'search' in user_request:
                user_request = user_request.replace("search", "")
                webbrowser.open_new_tab(user_request)
                time.sleep(5)

            elif 'ask' in user_request:
                speak(voice_eng,
                    'Opticron can answer to computational and geographical questions and what question do you want to ask now')
                question = takeCommand(voice_eng)
                app_id = "R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res_answer = client.query(question)
                answer_to_question = next(res_answer.results).text
                speak(voice_eng,answer_to_question)
                # print(answer_to_question)
                st.write(answer_to_question)


            elif "log off" in user_request or "sign out" in user_request:
                speak(voice_eng,"Ok , opticron will will log off  your pc  in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

        time.sleep(3)

if __name__ == "__main__":
    main()

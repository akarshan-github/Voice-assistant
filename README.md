# Voice-assistant

Want to build own personal voice assistant like Apple Siri, Microsoft Cortana and Google assistant .

To design a voice assistant that can perform the following task :
Open YouTube, Gmail, Google chrome and stack overflow. Predict current time, take a photo, search Wikipedia to abstract required data, predict weather in different cities, get top headline news from Times of India and can answer computational and geographical questions too.


##DEMO VIDEO - https://drive.google.com/file/d/1RU7j8bkHTvX3GsqHeQmb3JfChtaqvUzt/view?usp=sharing

Steps for execution:


At first we have to install the necessary packages using the pip command.
Pip install SpeechRecognition
Pip install pyttsx3==2.71
Pip install ecapture
Pip install wikipedia
Pip install datetime
Pip install wolframalpha
Pip install requests

At first we start the voice engine for text to speech recognition using the pyttsx3.init() function from pyttsx3 library.We set the voice id.

Then we have defined the speak(text) function which takes in the text as a parameter and converts the text to speech using the engine which we have started above.

We define the Greet() function which greets the user 
In this function we have used the datetime.datetime.hour() function to extract the hour from the current datetime and then according to the conditions greet the user
For ex , // if hour is between 0 - 12 then greet good morning
//if hour between 12-16 then greet good afternoon
//if hour  between 16 - 20 then greet good evening
//if hour else than these then greet good night
	
Now we have written the takecommand function which uses the recognizer and listen module from the speech recognition package and depending on the request made by the user returns the statement of the user by converting it into text form by receiving speech from the user.If the module does not understand the speech ,then it displays the appropriate message that Soory unable to recognize text ,please say it again.

Now when the program starts its execution from the main programme then it says its name i.e opticron and greet() function is called which greets the user.

Now takecommand() function is called which takes command from the user in form of speech and converts it into text and returns it.We have stored in the variable user_request.

If certain keywords are found in the user_request then accordingly actions are performed

If ‘your name’ keyword is found then the opticron says that “My name is Opticron,whats your name”. And aska us to say our name.Suppose we say that “My name is akarshan”,then it responds that ,nice name.
Likewise if ‘news’ keyword is found in the user_request then it opens the times of india website by using open_new_tab() function from the webbrowser package.
If ‘time’ keyword is found then the current time is spokenm and displayed by opticron.
If ‘google’,’gmail’,’youtube’ is found in the user_request then it opens the site according to our speech and speeks that the site is open now.
If we say that ‘who made you’ then appropriate message that ‘Akarshan made me.’

If ‘song’ keyword is present in our speech then ‘vande matram’ song is being played.

If ‘iitj’ keyword is present in our speech then IIT Jodhpur website is opened.

If ‘camera’ keyword is found in our speech then robo camera is opened and captures our photo.

If ‘weather’ keyword is found in our speech then it asks for the city name and displays the weather of the city.

For this we have used the open weather api.the city name combined with base url and api key of openweather generates a link that connect its to the server and extracts the required json object.Then it is being converted into a python object by using the .json() function .Now from this object the main parameters such as the temperature,humity and weather description are extracted from the weather and using the speak() function we have made opticron to say it and display also.

If ‘ask’ keyword is found in our speech then the message that’ i can answer computational and geogpahical questions’   is displayed.Now if ask 5 + 2 in speech then it connects to wolframalpha using the api and wolframalpha package and displays and speeks the answer as 7.

If you say ‘I Love You’ to opticron then it displays and speaks the ‘I love you too’ message.

Finally, if you say ‘Good bye’ to opticron,then it says the message that ‘Goodbye ,opticron is shutting down’ and program completes the execution using the break functionality.



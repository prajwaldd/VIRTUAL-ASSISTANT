import smtplib
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import time
import psutil
import pyjokes
import os
import pyautogui
import random
import time
from textblob import TextBlob

engine = pyttsx3.init()

def get_sentiment(sentx):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed text
        analysis = TextBlob(sentx)
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return ('positive')
        elif analysis.sentiment.polarity == 0:
            return ('neutral')
        else:
            return ('negative')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day

    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Yash!")
    # time_()
    # # date()
    # hour = datetime.datetime.now().hour
    # if hour >=6 and hour<12:
    #     speak("Good Morning Sir")
    # elif hour >=12 and hour<18:
    #     speak("Good Afternoon Sir!")
    # elif hour >=18 and hour <24:
    #     speak("Good Evening Sir!")
    # else:
    #     speak("Good Night Sir!")
    speak("Jarvis at your service. Please tell me how can I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('Your email', 'Your password')
    server.sendmail('Your email', to, content)
    server.close()

def jokes():
    speak(pyjokes.get_joke())

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/HP/Desktop/ss.png")

wishme()
if __name__ == '__main__':

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()
        elif 'date' in query:
            date()
        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")

        elif "who are you" in query:
            speak("I am JARVIS 1.0 , Personal AI assistant. I am created by Yash ,I can help you in various activities ,")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                to = (reciept)
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")

        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'open youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)
        elif 'search google' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)
        
        elif 'joke' in query:
            jokes()

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        elif 'go offline' in query:
            speak("Going offline sir")
            quit()

        elif 'word' in query:
            speak("opening MS Word")
            word = r'Word path'
            os.startfile(word)

        elif "write a note" in query:
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done taking the note')
            else:
                file.write(note)
                
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")


        elif 'play songs' in query:
            video ='********'
            audio = '******'
            speak("What songs should i play? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())
        
            if 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)
                
            speak("select a random number")
            rand = (TakeCommand().lower())
            while('number' not in rand and rand != 'random'):                      
                speak("I could not understand you. Please Try again.")          
                rand = (TakeCommand().lower())

            if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                                    
            elif 'random' in rand:
                    rand = random.randint(1,219)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue

        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif "sentiment" in query:
            speak("Analysing sentiment")
            sentx=TakeCommand()
            get_sentiment(sentx)


        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.nl / maps / place/" + location + "")

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        # elif 'sentiment' in query:
        #     speak("Analysing sentiment")
        #     from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        #     import speech_recognition as sr
        #     recognizer=sr.Recognizer()
        #     with sr.Microphone() as source:
        #         print('Clearing background noise...')
        #         recognizer.adjust_for_ambient_noise(source,duration=1)
        #         print('Waiting for your message...')
        #         recordedaudio=recognizer.listen(source)
        #         print('Done recording..')

        #     try:
        #         print('Printing the message..')
        #         text=recognizer.recognize_google(recordedaudio,language='en-US')
        #         print('Your message:{}'.format(text))
        #     except Exception as ex:
        #         print(ex)

        #     Sentence=[str(text)]
        #     analyser=SentimentIntensityAnalyzer()
        #     for i in Sentence:
        #         v=analyser.polarity_scores(i)
        #         print(v)
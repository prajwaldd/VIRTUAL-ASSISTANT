from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys
import pyautogui
import pyttsx3
import wolframalpha
import psutil
import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import webbrowser as wb
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import time
import requests
from bs4 import BeautifulSoup

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
  
    speak("Jarvis at your service. Please tell me how can I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('coc.full.rusher@gmail.com', 'password')
    server.sendmail('yashcharizard@gmail.com', to, content)
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

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            R.pause_threshold = 1
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(f"You said: {text}\n")
        except Exception as e:
            print(e)   
            print("Unable to Recognize your voice.") 
            return "None"

        text = text.lower()
        return text

    def JARVIS(self):
        wishMe()
        while True:
            self.query = self.STT()
            query=self.query
            if 'good bye' in self.query or 'goodbye' in query:
                speak("Jarvis signing off. Thank you for your time.")
                sys.exit()

            elif 'open google' in query:
                webbrowser.open('www.google.co.in')
                speak("opening google")

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")

            elif 'search google' in query:
                speak("What should I search?")
                Search_term = self.STT()
                wb.open('https://www.google.com/search?q='+Search_term)

            elif 'music' in query or "play song" in query:
                speak("Here you go with music")
                # music_dir = "G:\\Song"
                music_dir = r"C:\Users\HP\Desktop\Yash_folder\SONGS"
                songs = os.listdir(music_dir)
                print(songs)   
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                wb.open("https://www.google.com/maps/place/" + location + "")

            elif 'wikipedia' in query:
                speak("Searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)

            elif 'sentiment' in query:
                speak("Analysing sentiment")
                speak("Kindly tell me the sentence")
                input = self.STT()
                Sentence=[str(input)]
                analyser=SentimentIntensityAnalyzer()
                for i in Sentence:
                    v=analyser.polarity_scores(i)
                    print(v)

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")   
                speak(f"Sir, the time is {strTime}")

            elif 'email to yash' in query:
                try:
                    speak("What should I say?")
                    content = self.STT()
                    to = "Receiver email address"   
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'word' in query:
                speak("opening MS Word")
                word = r'C:\Users\HP\Desktop\YASH THE GREAT\OLD projects\New Microsoft Word Document.docx'
                os.startfile(word)

            elif "write a note" in query:
                speak("What should i write, sir")
                note = self.STT()
                file = open('note.txt', 'w')
                speak("Sir, Should i include date and time")
                dt = self.STT()
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

            elif 'how are you' in query:
                speak("I am fine, Sir Thanks for asking")
                speak("How are you Sir?")
                if 'fine' in query or "good" in query: 
                    speak("It's good to know that your fine")

            elif "who am i" in query:
                speak("If you can talk, then definitely you are a human")
            elif 'joke' in query:
                jokes()

            elif "don't listen" in query or "stop listening" in query:
                speak("for how much seconds you want me to stop listening commands")
                a = int(self.STT())
                time.sleep(a)
                print(a)

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by AIML students of group 3.")

            elif "calculate" in query:
             
                app_id = "Wolframalpha api id"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif 'ppt' in query:
                speak("opening Power Point presentation")
                power = r"C:\Users\HP\Desktop\YASH THE GREAT\OLD projects\New Microsoft Office PowerPoint Presentation.pptx"
                os.startfile(power)
 
            elif 'is love' in query:
                speak("It is 7th sense that destroy all other senses")

            elif "i love you" in query:
                speak("I love you too")

            elif 'log out' in query:
                os.system("shutdown -l")
            elif 'restart' in query:
                os.system("shutdown /r /t 1")
            elif 'shutdown' in query:
                os.system("shutdown /s /t 1")

            elif 'temperature' in query:
                city= query.split("in",1)
                soup= BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+in+{city[1]}").text,"html.parser")
                region=soup.find("span",class_="BNeawe tAd8D AP7Wnd")
                temp=soup.find("div", class_="BNeawe iBp4i AP7Wnd")
                day=soup.find("div", class_="BNeawe tAd8D AP7Wnd")
                weather = day.text.split("m",1)
                temperature = temp.text.split("C",1)
                speak("Its Currently"+weather[1]+" and "+ temperature[0]+"Celcius"+"in"+region.text)
                print("Its Currently"+weather[1]+" and "+ temperature[0]+" Celcius"+" in"+region.text)
 












FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=6 color='green'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))
        


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
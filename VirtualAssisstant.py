import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywintypes
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 150)
print(type(engine))
print(engine)

def speak(text): #to speak. Text to Speech
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    # minute= int(datetime.datetime.now().minute)
    if (hour>=0 and hour<12):
        print("Good Morning Boss!")
        speak("Good Morning Boss!")        
    elif(hour>=12 and hour<18):
        print("Good Afternoon Boss")
        speak("Good Afternoon Boss")
    else:
        print("Good Evening Boss")
        speak("Good Evening Boss")
    print("I am your Virtual Assistant, How may I help you?")    
    speak("I am your Virtual Assistant, How may I help you?")
    

def takeCommand(): #it takes microphone input from the user and return the string output
     r=sr.Recognizer()    #recogniser class helps in recognising the audio
     with sr.Microphone() as source:
         print("I am Listening Please Speak")
         speak("I am Listening Please Speak")
         r.pause_threshold = 0.5 #it refers to the amount of time gap after which the audio is supposed to be complete
         r.energy_threshold =300 #To differentiate noise vs human voice
         audio=r.listen(source) #digitaldata of whatsoever hs been spoken will be stored in audio
     try:
      print("Recognising...")
      speak("Recognising...")
      query=r.recognize_google(audio,language="en-in")
      print("User Said:",query)
     except Exception as e:
         
      print("Say that again please!")
      speak("Say that again please!")
      return "None"
     return query
wishMe()
def com():
    if 1:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'facebook' in query:
            webbrowser.open("fb.com")
        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'google' in query:
            query=query.replace("google","")
            query=query.replace("search","")
            webbrowser.open("https://google.com/search?q=%s" % query)
        elif (('music' in query) or ("song" in query)):
            music_dir= 'D:\\OldSongs' #\\ slash is to escape the character
            songs=os.listdir(music_dir)  #listdir is used to enlist all the songs of mentioned directory
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) #song[0] will play the first song. using random module, song can be shuffled
        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M")
            speak("sir, the time is")
            speak(time)
            print(time)
        elif 'sleep' in query:
            speak("Thank you")
            exit()
        else:
            com()
            
com()
exit()

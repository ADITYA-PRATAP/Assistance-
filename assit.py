import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import pywhatkit
import wikipedia as googleScrap
import subprocess



engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print(voices[0].id)

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak("good morning")
    elif hour>=12 and hour<17:
        speak("good afternoon")
    else:
        speak("good evening")

    speak('i am your  Adsid assitance how can i help you')

def takeCommand():
    '''
    takes command to user and convert in text
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio=r.listen(source) 
        
    try:
        print("recoginzing")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)

        print("say that again please...")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aditya224496@gmail.com', 'aditya@@')
    server.sendmail('aditya224496@gmail.com', to, content)
    server.close()

if __name__== "__main__":
    
    wishme() 
    while True:
#if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak(" wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
           webbrowser.open("google.com") 
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='E:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%I:%m:%S")
            speak( f"The time is{strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\Aditya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to aditya' in query:
            try: 
                speak("What should I say?")
                content = takeCommand()
                to = "aditya224496@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend aditya bhai. I am not able to send this email")  

        elif "fine" in query or "good" in query or'perfect' in query :
             speak('nice, how can i help you ')
        elif "bye" in query or "ok bye" in query or'nothing' in query or'thank you' in query:
             speak("thank you for using in ")
             sys.exit()
        elif "what is your name" in query:
             speak("my name is adsid your asistance")
                     
        elif "how are you" in query:
             speak("i fine ,thank you for asking what about you")
        elif "play" in query:
            song= query.replace('play', '')
            pywhatkit.playonyt(song)
        
            
        elif 'google search' in query:
            query=query.replace("   is"," ")
            query=query.replace("google search","")
            speak("this is what i found on the web")
            pywhatkit.search(query)
            try:
               
                result= googleScrap.summary(query,2)
                speak(result)

            except:
                speak("no speakable data available")
        elif "note" in query or "remember this" in query:
            speak("what would you like me to write down?")
            date = datetime.datetime.now()
            file_name = str(date).replace(":", "-") + "-note.query"
            note_query = takeCommand()
            with open(file_name, "w") as f:
                f.write(note_query)

            subprocess.Popen(["notepad.exe", file_name])
            speak("I have made a note of that")
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)         # 0 f0r male voice and 1 for female voice
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():       ## func to wish
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak('good after noon')
    else:
        speak("good evevning")

    speak("I am jarvis sir. please tell me how may i help you")
def takecommand():          # y func hmaar audio ko lera h aur usee string m convert karra h
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("recognising")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"user said : {query}\n")

        except Exception as e:
            # print(e)

            print(" say that again please")
            return "none"
        return query
def sendEmail(to, content):
     server = smtplib.SMTP('smntp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login("your emial" , " your password here")
     server.sendmail('your gamail id' , to ,content)
     server.close()
        
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()     
        if 'ok you can go now jarvis ':
             speak('ok sir')
             break
        else:
## logic for executing tasks
            if 'wikipedia' in  query:
                    speak('searching wikipedia...')
                    query = query.replace("wikedia","")
                    results = wikipedia.summary(query,sentences=2)
                    speak('according to wikipedia')
                    print(results)
                    speak(results)

            elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
            elif 'open google' in query:
                    webbrowser.open("google.com")
            elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")
                # elif 'open watsapp' in query:
                #     webbrowser.open("watsapp.com")
            elif 'play music' in query:
                    music_dir = ''  # music directory
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir , songs[0]))
            elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"sir ,  the time is {strTime}")
            elif 'open code' in query:
                codepath = "C:\\Users\\welcome\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
            elif 'send email' in query:
                try:
                    speak("what sshould i say")
                    content = takecommand()
                    to = " "      ## email id of your
                    sendEmail(to,content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak('sorry sir ,i am not bale to send the email')









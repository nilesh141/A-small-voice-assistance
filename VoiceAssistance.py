import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio)    
            print(data)
            return data
        except sr.UnknownValueError:
            print("Could not get it! Closing. Thank You")      
            
def txtspeech(x):
    txtspchObj=pyttsx3.init()
    voices=txtspchObj.getProperty('voices')
    txtspchObj.setProperty('voice',voices[1].id)
    rate=txtspchObj.getProperty('rate')
    txtspchObj.setProperty('rate',125)
    txtspchObj.say(x)
    txtspchObj.runAndWait()
#txtspeech("Hauray Krishna Prabhuji. How can I help you?")
#("Hauray krishna maataa ji")

if __name__=='__main__':

    if sptext().lower()=="hare krishna":
        #print("Parikshan Saphal")
        while True:
                data1=sptext().lower()
                if "your name" in data1 or "aapka naam" in data1:
                    name="Vishakha"
                    txtspeech(name)
                elif "old are you" in data1 or "your age" in data1 or "aap kitne sal" in data1 or "aapki umr" in data1:
                    age="One year"
                    txtspeech(age)
                elif "time now" in data1 or "kitne baje hai" in data1 or "samay hai" in data1:
                    time=datetime.datetime.now().strftime("%I%M%p")
                    txtspeech(time)
                elif "youtube" in data1:
                    webbrowser.open("https://www.youtube.com/")
                elif "joke" in data1:
                    joke1=pyjokes.get_joke(language="en",category="neutral")
                    txtspeech(joke1)
                elif "play song" in data1:
                    addrs="D:\Libraries\Music\Classical"
                    songList=os.listdir(addrs)
                    print(songList)
                    os.startfile(os.path.join(addrs,songList[0])) 
                elif "close" in data1 or "exit" in data1 :
                    txtspeech("Jay Shree Raam. Thank You")
                    break
                time.sleep(7)
    else:
        print("Dhanyavaad")



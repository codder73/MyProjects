import os
import pyautogui
import time
import pyttsx3
import selenium
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init('sapi5')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

if __name__ == '__main__':
    while True:
        wishMe()
        c = input('Enter what do you want to open in on web: ')
        # takeCommand()
        # a = takeCommand().lower()
        a = c.lower()
        if a == 'p':
            ch_path = r"C:\Program Files\Google\Chrome\Application"
            ch_open = os.listdir(ch_path)
            print(ch_open)
            os.startfile(os.path.join(ch_path, ch_open[1]))
            time.sleep(2)
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Tab')
            pyautogui.keyUp('Tab')
            pyautogui.keyUp('Tab')
            pyautogui.keyUp('Tab')
            pyautogui.keyUp('Tab')
            pyautogui.keyDown('Enter')
            
        elif a == 'exit':
            break
        
        elif a == 's':
            ch_path = r"C:\Program Files\Google\Chrome\Application"
            ch_open = os.listdir(ch_path)
            print(ch_open)
            os.startfile(os.path.join(ch_path, ch_open[1]))
            time.sleep(2)
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Enter')
            
        else:
            ch_path = r"C:\Program Files\Google\Chrome\Application"
            ch_open = os.listdir(ch_path)
            os.startfile(os.path.join(ch_path, ch_open[1]))
            time.sleep(2)
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Tab')
            pyautogui.keyDown('Enter')
            time.sleep(1)
            
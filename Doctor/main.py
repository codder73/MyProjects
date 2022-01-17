"""Giving data and gui are left only (made by pyttsx3)"""
'''microphone should be there'''
import pyttsx3
import speech_recognition as sr
import datetime
from gtts import gTTS
import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

    

def speak2(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Patient said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def disease():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am shushruta. Please tell me how may I help you")    
    speak("From which disease you are suffering from?")
    print("From which disease you are suffering from?")   


if __name__=="__main__":
    disease()
    takeCommand()
    patient = takeCommand().lower()
if 'fever' in patient:
    with open("fever.txt") as r:
        a= r.read()
        print(a)
        speak(a)
elif "acne" in patient:
    with open('Acne.txt') as r:
        a= r.read()
        print(a)
elif "acute cholecystitis" in patient:
    with open('acute_cholecystitis.txt') as r:
        a= r.read()
        print(a)
elif "allergy" or "allergies" in patient:
    with open('allergy.txt') as r:
        a= r.read()
        print(a)
elif "anal cancer" in patient:
    with open('anal_cancer.txt') as r:
        a= r.read()
        print(a)
elif "anaphylaxis" in patient:
    with open('anaphylaxis.txt') as r:
        a= r.read()
        print(a)
elif "angioedema" in patient:
    with open('angioedema.txt') as r:
        a= r.read()
        print(a)
elif "ankylosing spondylitis" in patient:
    with open('Ankylosing_spondylitis.txt') as r:
        a= r.read()
        print(a)
elif "anorexia nervosa" in patient:
    with open('Anorexia nervosa.txt') as r:
        a= r.read()
        print(a)
elif "anxiety disorders in children" in patient:
    with open('anxiety disorders in children.txt') as r:
        a= r.read()
        print(a)
elif "appendicitis" in patient:
    with open('appendicitis.txt') as r:
        a= r.read()
        print(a)
elif "arthritis" in patient:
    with open('arthritis.txt') as r:
        a= r.read()
        print(a)
elif "asbestosis" in patient:
    with open('asbestosis.txt') as r:
        a= r.read()
        print(a)
elif "asthma" in patient:
    with open('asthma.txt') as r:
        a= r.read()
        print(a)
elif "atopic eczema" in patient:
    with open('atopic eczema.txt') as r:
        a= r.read()
        print(a)
elif "autistic spectrum disorder (asd)" or "autistic spectrum disorder" or "autistic spectrum" in patient:
    with open('autistic spectrum disorder.txt') as r:
        a= r.read()
        print(a)
elif "bacterial vaginosis" in patient:
    with open('bacterial vaginosis.txt') as r:
        a= r.read()
        print(a)
elif "bile duct cancer" or "cholangiocarcinoma" in patient:
    with open('bile duct cancer.txt') as r:
        a= r.read()
        print(a)
elif "binge eating" in patient:
    with open('binge eating.txt') as r:
        a= r.read()
        print(a)
elif "" in patient:
    with open('.txt') as r:
        a= r.read()
        print(a)
elif "" in patient:
    with open('.txt') as r:
        a= r.read()
        print(a)
elif "" in patient:
    with open('.txt') as r:
        a= r.read()
        print(a)
elif "" in patient:
    with open('.txt') as r:
        a= r.read()
        print(a)
elif "" in patient:
    with open('.txt') as r:
        a= r.read()
        print(a)
elif "" in patient:
    with open('.txt') as r:
        a= r.read()
        print(a)
elif "" in patient:
    with open('.txt') as r:
        a= r.read()
        print(a)
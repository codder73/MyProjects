from traceback import print_tb
from nltk.util import pr
import pyttsx3
import nltk
from nltk import word_tokenize

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# if __name__ == '__main__':
#     print()
from gtts import gTTS
from IPython.display import Audio

def speak(text):
    gTTS.speak(text)

tts = gTTS('Magnus Carlsen is the number one chess player in the world')
speak(tts)
tts.save('1.wav')
sound_file = '1.wav'
Audio(sound_file, autoplay=True)
import os
import pyttsx3

pyttsx3.speak("Opening visual studio...")
vs_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
vs_open = os.listdir(vs_path)
os.startfile(os.path.join(vs_path, vs_open[26]))

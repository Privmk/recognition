import pyttsx3
import os

path=os.getcwd() + "\outtext.txt"
outtext = open(path,"r")
text=outtext.read()
outtext.close()

speak_engine = pyttsx3.init()
speak_engine.say(text)
speak_engine.runAndWait()

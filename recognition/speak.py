import speech_recognition
import os

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	audio = robot_ear.listen(mic)
try:
	text = robot_ear.recognizer_google(audio)
except:
	text = "PC: I don't understand"

path=os.getcwd() + "\outtext.txt"
outtext = open(path,"w+")
outtext.write(text)
outtext.close()
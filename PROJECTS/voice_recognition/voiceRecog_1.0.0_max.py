#1.0.0

import speech_recognition as sr
from googlesearch import search


with sr.Microphone() as source:
    r = sr.Recognizer()
    audio = r.listen(source)

try:
    sQ = r.recognize_google(audio)
    print("I'm searching the web for: " + sQ)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


qR = search(sQ, tld='com', lang='en', num=3, start=0, stop=3, pause=2)

for i in qR:
    print(i)
    print("")




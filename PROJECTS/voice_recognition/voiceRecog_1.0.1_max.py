#1.0.1

import speech_recognition as sr

# use the audio file as the audio source
with sr.Microphone() as source:
    r = sr.Recognizer()
    audio = r.listen(source)

try:
    print("I heard you say: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



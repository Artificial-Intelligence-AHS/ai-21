import speech_recognition as sr
#SUPER BASIC IDK WHY I COMMIT THIS!!!! -Max G.

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print(f"You said " + audio)

except sr.UnknownValueError:
    pass
except sr.RequestError as e:
    print(f"Oops: {e}")



#add stuff here.


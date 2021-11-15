# Voice Recognition
A voice assistent robot activated by voice running in background that is directly made for a high school student. Learn how the different libraries and APIs work and how to use them and apply them to such a proje

Currently our plan is to use external APIs and libaries to build this project so we have a basic voice recognition system. Once completed we will be able to build our own model 

- Research some needed process to start or libaries needed
- Maybe some starters: `https://realpython.com/python-speech-recognition/`

# Voice Commands that you want to set and its result

|Command|Result|
|-|-|
|What is your name|**My Name is Sphinx**|
|Who created you?|**AI Club at AHS**|


# Different Libaries and APIs to use
- https://cloud.google.com/speech-to-text
- https://pypi.org/project/SpeechRecognition/
- https://cloud.google.com/speech-to-text/docs/libraries

# Google Cloud Platform
Using the speech-to-text API, all contributers have access to the program. 

Access: https://console.cloud.google.com/speech/transcriptions/create?project=voice-recognition-330818
https://cloud.google.com/speech-to-text/docs/samples/speech-transcribe-onprem
## Access to the `key.json` file is limited
Check Discord for link 

### Exporting the key.json file to environment variables

**WINDOWS**
`set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH`
`set GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"`
**MAC**
`export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"`
`export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"`

# Audio Files

We are going to first convert the files to a .wav format in order to display them into with a spectogram.
https://audio.online-convert.com/convert-to-wav


Using the spectogram we are going to find the average
The sampling frequency or sampling rate, fs, is the average number of samples obtained in one second, thus fs = 1/T. In other words, fs is the inverse of the sampling period, T.

# Links
https://cloud.google.com/speech-to-text/docs/speech-adaptation
https://cloud.google.com/speech-to-text/docs/class-tokens
https://cloud.google.com/speech-to-text/docs/boost


## Contributers

- @Rishik2019
- @Maxgoodman07
- @Gtadia
- @z-ghazanfar
- @Kunal2341
- @Artificial-Intelligence-AHS

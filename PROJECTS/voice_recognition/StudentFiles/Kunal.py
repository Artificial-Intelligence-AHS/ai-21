"""
Things to do 
- Fill out the project section in the github: Link: https://github.com/Artificial-Intelligence-AHS/ai-21/projects/1
- Create an Archetiure Diagram for this project
- Edit the readme file to include the project description
- Create a requirements.txt file to include all the libraries needed for the project
"""
"""
GOOGLE CLOUD PLATFORM PYTHON CODE
"""
#speech_file = '/Users/kunal/Documents/AI-21/ai-21/PROJECTS/voice_recognition/audioFiles/3.wav'
speech_file = './PROJECTS/voice_recognition/audioFiles/4.wav'

import json
from google.oauth2 import service_account
from google.cloud import speech
import io

key_path = '../keys/voice-recognition-gcp-key.json'
#hello
with open(key_path, 'r') as j:
    service_account_info = json.loads(j.read())
credentials = service_account.Credentials.from_service_account_info(service_account_info)
client = speech.SpeechClient(credentials=credentials)


#client = speech.SpeechClient()

with io.open(speech_file, "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code="en-US",
    sample_rate_hertz=8000,
    #speechContexts = [speech.SpeechContext(phrases=["sphinx"])]
)

response = client.recognize(config=config, audio=audio)

# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print(u"Transcript: {}".format(result.alternatives[0].transcript))



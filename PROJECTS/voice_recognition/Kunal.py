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
"""
# Imports the Google Cloud client library
from google.cloud import speech


# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

audio = speech.RecognitionAudio(uri=gcs_uri)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))"""





"""Transcribe the given audio file asynchronously."""
from google.cloud import speech
import os
from google.oauth2 import service_account
import json

print(os.getcwd())

local_file_path = './PROJECTS/voice_recognition/audioFiles/1.mp3'
key_path = '/Users/kunal/Documents/AI-21/keys/voice-recognition-key.json'
print(os.path.exists(key_path))

service_account_info = json.loads(key_path)
credentials = service_account.Credentials.from_service_account_info(service_account_info)
client = speech.SpeechClient(credentials=credentials)

#client = speech_v1p1beta1.SpeechClient(transport=transport, credentials=credentials)
#client = speech_v1p1beta1.SpeechClient(transport=transport)
#client = speech.SpeechClient()

with open(speech_file, "rb") as audio_file:
    content = audio_file.read()

print(content)

"""
    Note that transcription is limited to a 60 seconds audio file.
    Use a GCS file for audio longer than 1 minute.
"""
audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code="en-US",
)


operation = client.long_running_recognize(config=config, audio=audio)

print("Waiting for operation to complete...")
response = operation.result(timeout=20)

# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print(u"Transcript: {}".format(result.alternatives[0].transcript))
    print("Confidence: {}".format(result.alternatives[0].confidence))


average = sum(signalData) / len(signalData)
print("Average: {}".format(average))

# MY CODE
totalSumNonZero = 0
ct = 0
for num in signalData:
    if num != 0:
        totalSumNonZero+=num
        ct+=1
averageNonZero = totalSumNonZero / ct
print("Average Non Zero: {}".format(averageNonZero))


totalSumNonZero = 0
ct = 0
for num in signalData:
    if num > 10:
        totalSumNonZero+=num
        ct+=1
averageNonZero = totalSumNonZero / ct
print("Average Non Zero: {}".format(averageNonZero))
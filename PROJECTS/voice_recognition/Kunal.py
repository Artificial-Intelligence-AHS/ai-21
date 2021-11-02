
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
    print("Transcript: {}".format(result.alternatives[0].transcript))
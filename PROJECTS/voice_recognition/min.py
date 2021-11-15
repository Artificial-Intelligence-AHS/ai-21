"""
1. I want there to be a keyword that activates the voice recognizer
so that it doesn't respond to you until you say it.
"""


# Imports the Google Cloud client library
from google.cloud import speech  # is equal to from google.cloud.speech  (Is like a file system) 


# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw" # gs is google's file system (it's like C://)

audio = speech.RecognitionAudio(uri=gcs_uri)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)

# Detects speech in the audio filea
response = client.recognize(config=config, audio=audio)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
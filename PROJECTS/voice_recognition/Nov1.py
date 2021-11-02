"""
This is the program of what we went over on Nov 1.
Uses the files in the ./audio_files folder.
Not completed in order to direct you in the correct direction.
"""

"""
Google Cloud Platform
Google Cloud Speech API Activation --> Check README.md
"""

# The following is GCPs code for speech recognition on local file

"""
Transcribe a short audio file using synchronous speech recognition on-prem

local_file_path: The path to local audio file, e.g. /path/audio.wav
"""
from google.oauth2 import service_account
from google.cloud import speech_v1p1beta1
import grpc
import os
import json
import io

api_endpoint = '0.0.0.0:10000'

local_file_path = './PROJECTS/voice_recognition/audioFiles/1.mp3'
key_path = '../keys/voice-recognition-key.json'
print(os.path.isfile(key_path))



# Create a gRPC channel to your server
channel = grpc.insecure_channel(target=api_endpoint)
transport = speech_v1p1beta1.services.speech.transports.SpeechGrpcTransport(
    channel=channel
)

#service_account_info = json.loads(key_path)
#credentials = service_account.Credentials.from_service_account_info(service_account_info)
#client = speech_v1p1beta1.SpeechClient(transport=transport, credentials=credentials)
client = speech_v1p1beta1.SpeechClient(transport=transport)


# The language of the supplied audio
language_code = "en-US"

# Sample rate in Hertz of the audio data sent
sample_rate_hertz = 16000

# Encoding of audio data sent. This sample sets this explicitly.
# This field is optional for FLAC and WAV audio formats.
encoding = speech_v1p1beta1.RecognitionConfig.AudioEncoding.LINEAR16
config = {
    "encoding": encoding,
    "language_code": language_code,
    "sample_rate_hertz": sample_rate_hertz,
}
with io.open(local_file_path, "rb") as f:
    content = f.read()
audio = {"content": content}

response = client.recognize(request={"config": config, "audio": audio})
for result in response.results:
    # First alternative is the most probable result
    alternative = result.alternatives[0]
    print(f"Transcript: {alternative.transcript}")


#Create an account and get the key
# https://beta.openai.com/examples
import os
import openai

def getkey():
    try:
        return open("../keys/openAIKey.txt", "r")
    except FileNotFoundError:
        print("File not found")
        return None

openai.api_key = "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"

response = openai.Completion.create(
  engine="davinci",
  prompt="Human: why does min never know how to work github on vs?\
          \nAI:",
  temperature=0.9, # 0.9 is the default value for temperature and 0.5 is the default value for top_p
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=["\n", " Human:", " AI:"]
)

print(response)


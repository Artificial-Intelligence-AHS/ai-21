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

openai.api_key = getkey()

response = openai.Completion.create(
  engine="davinci",
  prompt="The following is a conversation with an AI assistant. The assistant is \
          helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are \
          you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: \
          I'd like to cancel my subscription.\nAI:",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=["\n", " Human:", " AI:"]
)

print(response)


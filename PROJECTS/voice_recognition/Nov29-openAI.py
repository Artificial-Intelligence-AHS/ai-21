#Create an account and get the key
# https://beta.openai.com/examples
import os
import openai

def getkey():
  try:
    with open("../keys/openAIKey.txt") as f:
      contents = f.readlines()
    return contents
    except FileNotFoundError:
        print("File not found")
        return None
print(getkey())
"""
openai.api_key = getkey()

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

"""
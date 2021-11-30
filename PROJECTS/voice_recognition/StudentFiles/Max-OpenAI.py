import os
import openai
chatlog = ''
while True:
    question = input('Human: ')

    openai.api_key = ""

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
      engine="davinci",
      prompt = chatlog + f"\nHuman: {question}\nAI:",
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=2,
      stop=["\n", "Human: ", "AI:"]
    )

    print(
          f"AI Response: {response['choices'][0]['text']}"
        )
    chatlog = chatlog + f"\nHuman: {question}\nAI:"

    chatlog = chatlog + f" {response['choices'][0]['text']}"
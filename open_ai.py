import os
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "We are giving the name of food, and you have to determine the country of origin."
    },
    {
      "role": "user",
      "content": "Spagetti"
    },
    {
      "role": "assistant",
      "content": "Italy"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
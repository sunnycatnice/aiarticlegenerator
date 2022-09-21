#simple python progam using openai to generate web articles using GPT-3
#use python 3.10

import os
import openai

openai.api_key = "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"

print(openai.api_key)

response = openai.Completion.create(
  model="text-davinci-001",
  prompt="Scrivi un articolo sul nuovo iphone 14 pro. Pro e contro.",
  temperature=0.4,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#extract the text from the response
text = response['choices'][0]['text']
#print the text
# print (text)

#save the text to a file
file = open("output.txt", "w")
file = file.write(text)
print ("file saved!")

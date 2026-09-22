# Streaming
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model = "gpt-4.1",
    messages=[
        {
            "role":"system",
            "content":"You are a AI tutor"
        },
        {
            "role":"user",
            "content":"What is OpenAI in detail"
        }
        
    ],
    temperature=1,
    max_tokens=256,
    stream=True
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0,
    # n=2
)

# print(response.choices[0].message.content)
for _ in response:
    print(_.choices[0].delta.content,end=" ")
    # print("-"*50)
# Single response

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model = "gpt-4.1",
    messages=[
        {
            "role":"system",
            "content":"You are an AI teacher"
        },
        {
            "role":"user",
            "content":"Who is OpenAI"
        }
        
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].message.content)
# In context learningh

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


response = client.chat.completions.create(
    model = "gpt-4.1",
    messages=[
        {
            "role":"system",
            "content":"You are a python tutor"
        },
        {
            "role":"user",
            "content":"Explain what is the role of sum() function in python"
        },
        {
            "role":"assistant",
            "content":"The sum() function does "
        },
        {
            "role":"user",
            "content":"Explain what the len() function does"
        }
        
    ],
    temperature=0.5,
    max_tokens=200,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0,
    # n=1
)

print(response.choices[0].message.content)

# for _ in response.choices:
#     print(_.message.content)
#     print("-"*50)
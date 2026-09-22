# Multiple response

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model = "gpt-4.1",
    messages=[
        {
            "role":"system",
            "content":"You are a cake baker"
        },
        {
            "role":"user",
            "content":"get me a recipe to bake a cake"
        }
        
    ],
    # temperature=1,
    max_tokens=200,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0,
    n=2
)

# print(response.choices[0].message.content)
for _ in response.choices:
    print(_.message.content)
    print("-"*50)
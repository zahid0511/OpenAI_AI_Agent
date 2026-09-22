# Code explanation

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


instructions = '''
            explain what this python code is doing in one sentence:
            
            num = int(input("Enter a number: "))

            factorial = 1

            for i in range(1, num + 1):
                factorial *= i

            print("Factorial of", num, "is", factorial)

'''

response = client.chat.completions.create(
    model = "gpt-4.1",
    messages=[
        {
            "role":"system",
            "content":"You are a python tutor"
        },
        {
            "role":"user",
            "content":instructions
        }
        
    ],
    # temperature=1,
    max_tokens=200,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0,
    n=1
)

# print(response.choices[0].message.content)
for _ in response.choices:
    print(_.message.content)
    print("-"*50)
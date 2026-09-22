# Sentiment analysis

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model = "gpt-4.1",
    messages=[
        {
            "role":"user",
            "content":"analyze the sentiment of the text and classify \
            positive ,negative, neutral: "
                
            "GOOD,I like the way the course is designed. It is a quick recap of all java concepts. Thanks"
            
            "The quizes can be better. "
            
            "The exam result is very poor for the final year students"
            
            
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
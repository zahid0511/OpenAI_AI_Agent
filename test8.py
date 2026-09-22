# Streaming
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.audio.transcriptions.create(
    
    model="whisper-1",
    file=open("sample.mp3","rb"),
    language='en',
    response_format='text'
)

print(response)


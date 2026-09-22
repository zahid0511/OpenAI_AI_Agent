# Content moderation

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def sep():
    print("-"*50)



response = client.moderations.create(
    model = "omni-moderation-latest",
    # input = "My favourite movie is Terminator",
    # input = "My favourite movie is kill bill",
    input="I hate myself and want to harm myself"

)

print(response)
sep()
print(response.results[0].flagged)
sep()
print(response.results[0].categories)
sep()
print(response.results[0].category_scores)
sep()
print(response.results[0].categories.self_harm_intent)



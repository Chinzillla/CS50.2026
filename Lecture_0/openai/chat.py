import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

prompt = input("Prompt: ")

response = client.responses.create(
    input=prompt,
    model="gpt-5"
)

print(response.output_text)
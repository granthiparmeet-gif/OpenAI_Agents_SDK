from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found")



client = OpenAI()

response = client.responses.create(
    model = "gpt-4.1-mini",
    input= "How many planets are there in the solar system"
)

print(response.output_text)
from pydantic import BaseModel
import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List

load_dotenv()

api_key=os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key is not available")

client = OpenAI()

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {
            "role": "system",
            "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
        },
        {"role": "user", "content": "how can I solve 8x + 7 = -23"},
    ],
    text_format=MathReasoning,
)

math_reasoning = response.output_parsed

print(math_reasoning)
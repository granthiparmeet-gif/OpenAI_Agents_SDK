from agents import WebSearchTool
import os
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()


api_key=os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Problem with API key")

news_agent= Agent(
    name=" News Agent",
    model="gpt-4o-mini",
    instructions= "You are a news agent, Provide news on the given topic. Compile the information as a single paragraph, no markdown just plain text",
    tools=[WebSearchTool()]
)

while True:
    topic = input("Please enter the topic you would like to know information about. or 'quit' to exit")
    if topic.lower()=="quit":
        break



news_agent= Runner.run_sync(news_agent,input=topic)

print("\n Result:")
print(news_agent.final_output)
print("\n"+"-"*50 +"\n")

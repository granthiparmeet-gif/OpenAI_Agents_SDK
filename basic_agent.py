import os
import asyncio
from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

api_key=os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Problems with API key")

print_agent=Agent(
    name="Printing Agent",
    instructions="You are a echo bot, you return the same text that you receive as an input"
)

async def main():

    print("Echo agent is running , Type something and it will echo back")
    print("Type 'exit'to stop")

    while True:
        user_input = input("You:")

        if user_input.lower()== "exit" :
            print("Exiting echo agent")
            break

        try:
            result = await Runner.run(print_agent, user_input)
            print(f"Agent: {result.final_output}")
        except Exception as e:
            print(f"Error : {e}")


if __name__=="__main__":
    asyncio.run(main())
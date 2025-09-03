from fastapi import FastAPI, Query
from agents import Agent, Runner, function_tool
from dotenv import load_dotenv



load_dotenv()
app= FastAPI(title='Simple Tool Agent')

@function_tool
def calculator(expr:str):
    """Calculate the basic math expression"""
    return str(eval(expr))

@function_tool
def weather(city:str):
    """Returns a fake weather information"""
    city=city.lower()

    if city=='paris':
        return "18°C cloudy"
    elif city=='london':
        return "22°C sunny"
    else:
        return None
    
@app.get("/ask")
async def ask(q:str =Query(..., description= "User question/ prompt")):
    agent = Agent(
    name="Simple Tool Agent",
    instructions="You are an assistant. You can use the calculator and weather tools whenever required.",
    tools=[calculator, weather],
    model= 'gpt-4o-mini',
)

    result= await Runner.run(agent,input=q)
    return {"answer": result.final_output}
    

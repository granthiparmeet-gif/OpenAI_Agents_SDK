from fastapi import APIRouter
from agents import Runner
from .agent import agent

router= APIRouter()

@router.get("/article")
async def article(topic:str):
    result = await Runner.run(agent, f"Write about {topic} using the crew.")
    return {"result": result.final_output}
from fastapi import FastAPI, Query
from agents import Runner
from .agent import agent

app = FastAPI(title="SDK + MCP External Integration")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/weather")
async def weather(city: str = Query(..., description="City name, e.g. paris")):
    result = await Runner.run(agent, f"Check weather for {city} using mcp_weather")
    return {"weather": result.final_output}
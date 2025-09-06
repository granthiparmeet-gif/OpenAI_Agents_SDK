from fastapi import FastAPI, Query
from agents import Runner
from .agent import agent

app = FastAPI(title="SDK + AutoGen Hybrid")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/debate")
async def debate(q: str = Query(..., description="Question or claim to debate")):
   
    result = await Runner.run(agent, f"Debate this and return the judged answer: {q}")
    return {"result": result.final_output}
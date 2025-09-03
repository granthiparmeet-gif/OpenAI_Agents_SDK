import os
from fastapi import FastAPI, Query
from dotenv import load_dotenv
from app.workflow import wf


load_dotenv()

app =FastAPI(title="SDK and Langgraph App")

@app.get("/run")
async def run (input: str = Query(...)):
    return await wf.ainvoke({"input": input})
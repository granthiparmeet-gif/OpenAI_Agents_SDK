from fastapi import FastAPI
from .routes import router
from dotenv import load_dotenv
import os

load_dotenv()

print("DEBUG API KEY:", os.getenv("OPENAI_API_KEY"))

app = FastAPI(title="SDK + CrewAI")
app.include_router(router)


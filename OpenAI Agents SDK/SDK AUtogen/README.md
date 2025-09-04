# Agents SDK + AutoGen — Hybrid

This project integrates **OpenAI Agents SDK** with **AutoGen AgentChat**.

##  Project Structure
- app/
  - config.py — load env vars
  - tools.py — defines `autogen_debate` tool
  - agent.py — sets up Agent with tools
  - main.py — FastAPI app
- .env.example — template for secrets
- .gitignore — ignore env/cache files
- requirements.txt — dependencies

##  Setup
```bash
cd 4_sdk_autogen
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
cp .env.example .env
# add your OPENAI_API_KEY to .env
```

## ▶ Run
```bash
uvicorn app.main:app --reload --port 8300
```


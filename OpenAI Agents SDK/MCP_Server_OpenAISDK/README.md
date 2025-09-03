Agents SDK + MCP (FastAPI)

This app shows how to use the OpenAI Agents SDK with:
- a local function tool (MCP-like), and
- optional MCP servers (stdio or SSE).

# INSTALLATION
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# SETUP

cp .env.example .env

# edit .env and add OPENAI_API_KEY

# RUN

uvicorn app.main:app --reload --port 8300

Browse:
- http://localhost:8300/health
- http://localhost:8300/weather?city=paris




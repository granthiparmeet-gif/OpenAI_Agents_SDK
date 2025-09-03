# SDK + LangGraph Example (FastAPI)

This is a minimal example showing how to use the **OpenAI Agents SDK** with **LangGraph** and **FastAPI**.

---

##  Quickstart

### 1. Clone & Install
```bash
git clone https://github.com/granthi-parmeet-gif/sdk-langgraph-app.git
cd sdk-langgraph-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Set Environment
Copy `.env.example` → `.env` and set your `OPENAI_API_KEY`.

```bash
cp .env.example .env
```

### 3. Run the Server
```bash
uvicorn main:app --reload --port 8000
```

### 4. Try It
```bash
curl "http://localhost:8000/run?input=hello"
# -> {"result":"Processed hello"}

curl "http://localhost:8000/run?input=fail"
# -> {"result":"Fallback: fail"}
```

---

##  Structure
```
sdk-langgraph-app/
├── main.py          # FastAPI entrypoint
├── requirements.txt # Dependencies
├── .env.example     # API key example
├── README.md
└── app/
    ├── __init__.py
    ├── workflow.py  # LangGraph workflow
    └── tools.py     # Custom tools
```

---

## Notes
- `api_tool` is a registered function tool. It fails on `"fail"`, triggering LangGraph’s fallback.
- Agent uses `tool_use_behavior="stop_on_first_tool"` so tool output is treated as final.
- Extend with more tools or add streaming with `Runner.run_streamed`.

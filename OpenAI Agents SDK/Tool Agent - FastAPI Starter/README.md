# Simple Tool Agent - FastAPI Starter

This project demonstrates a simple OpenAI Agents SDK setup with FastAPI. It includes two basic tools: a calculator and a weather lookup. The project is useful as a starter for experimenting with tool-using agents.

## Quickstart

1. Clone the repository and navigate to the project folder:
```
git clone https://github.com/granthiparmeet-gif/openai_agents_sdk.git
cd openai_agents_sdk/1_simple_agent
```

2. Create and activate a virtual environment:
```
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Configure your environment variables:
- Copy the example environment file:
```
cp .env.example .env
```
- Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-key-here
```

5. Run the FastAPI app:
```
uvicorn app.main:app --reload --port 8300
```

Then open your browser at: http://localhost:8300/docs

## Project Structure
```
1_simple_agent/
├── app/
│   ├── __init__.py
│   └── main.py
├── requirements.txt
├── .env.example
└── README.md

```


## Example Usage

- Calculator:
  ```
  http://localhost:8300/ask?q=2+3*5
  → {"answer": "17"}
  ```

- Weather:
  ```
  http://localhost:8300/ask?q=weather+in+nyc
  → {"answer": "22°C sunny"}
  ```
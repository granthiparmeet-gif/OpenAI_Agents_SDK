# SDK + CrewAI Project

This project demonstrates how to integrate **FastAPI**, **OpenAI SDK**, and **CrewAI** to create a workflow with multiple AI agents (Writer + Editor). The app exposes an endpoint `/article` where you can generate refined articles on any given topic.

---

## Features
- FastAPI server for handling requests
- OpenAI SDK with agent + tools
- CrewAI workflow with sequential process (Writer drafts, Editor refines)
- REST endpoint to generate articles dynamically

---

## Project Structure
sdk-crewai-app/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entry point
│   ├── routes.py            # API routes (article endpoint)
│   ├── crew.py              # CrewAI setup (Writer, Editor, Crew)
│   ├── agent.py             # OpenAI agent setup with AssistantTool
│   └── utils.py             # (Optional) helper functions
├── requirements.txt         # Dependencies
├── .env.example             # Environment variables template
├── README.md                # Documentation
└── run.sh                   # Run script

---

## Installation

1. Clone the repo:
```bash
git clone https://github.com/yourusername/sdk-crewai-app.git
cd sdk-crewai-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create your `.env` file:
```bash
cp .env.example .env
```
Update `.env` with your **OpenAI API key**.

---

## Running the App

```bash
./run.sh
```

The API will be available at:  
👉 http://127.0.0.1:8000/article?topic=AI

---


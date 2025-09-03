from typing import TypedDict, Any, Dict
from agents import Agent, Runner
from langgraph.graph import StateGraph, END
from .tools import api_tool

class State(TypedDict, total=False):
    input: str
    result: str

agent = Agent(
    name = "SDK+ Langgraph Agent",
    instructions= "Call the API tool once and use its output as the final answer",
    tools=[api_tool],
    model="gpt-40-mini",
    tool_use_behavior="stop_on_first_tool"
)

async def try_api(state: State) -> Dict[str, Any]:
    try:
        result = await Runner.run(agent, state["input"])
        final = result.final_output

        if isinstance(final, str) and final:
            return {"result":final}
        return {}
    
    except Exception:
        return {}
    
def fallback(state:State) -> Dict[str, Any]:
    return {"result": f"Fallback: {state['input']}"}

graph = StateGraph(State)
graph.add_node("api", try_api)
graph.add_node("fallback", fallback)

graph.set_entry_point("api")
graph.add_conditional_edges(
    "api",
    lambda s: "ok" if "result" in s else "fail",
    {
        "ok": END,
        "fail": "fallback"
    }
)

graph.add_edge("fallback", END)

wf = graph.compile()
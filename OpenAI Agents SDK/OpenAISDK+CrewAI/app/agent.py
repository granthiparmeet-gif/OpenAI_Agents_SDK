from agents import Agent, function_tool
from .crew import run_crew


@function_tool
def run_crew_tool(topic: str):
    """Kick off the CrewAI workflow to generate/refine an article."""
    return run_crew(topic)
    

agent = Agent(
    name="CrewAgent",
    instructions="Use the crew to draft and refine articles.",
    model="gpt-4o-mini",
    tools=[run_crew_tool],
)


from crewai import Agent, Crew, Process
from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model = "gpt-4o-mini")

writer = Agent(
    role="writer",
    llm=llm,
    goal="Draft Articles"
)

editor= Agent(
    role= "Editor", 
    llm=llm,
    goal="Refine Articles"
)

crew= Crew([writer, editor], process=Process.sequential)

def run_crew(topic):
    return crew.kickoff(inputs={"topic": topic})






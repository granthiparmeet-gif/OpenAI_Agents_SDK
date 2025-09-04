from agents import Agent, ModelSettings
from .tools import autogen_debate

agent = Agent(
    name="SDK+AutoGen Hybrid",
    instructions=(
        "You orchestrate debates by calling the `autogen_debate` tool. "
        "Return the judged, validated answer."
    ),
    tools=[autogen_debate],
    # Make the call deterministic: choose the debate tool then stop.
    model_settings=ModelSettings(temperature=0, tool_choice="autogen_debate"),
    tool_use_behavior="stop_on_first_tool",
)
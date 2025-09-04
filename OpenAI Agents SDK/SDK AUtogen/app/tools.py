import os
from agents import function_tool
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient


@function_tool
async def autogen_debate(q: str) -> str:
    """
    Run a short 'pro vs con' debate using AutoGen AgentChat and return the judged final answer.

    Args:
        q: The question or claim to debate.
    """
  
    model = OpenAIChatCompletionClient(model="gpt-4o-mini")

   
    pro = AssistantAgent("pro", model)
    con = AssistantAgent("con", model)
    judge = AssistantAgent("judge", model)


    pro_out = await pro.run(task=f"You argue IN FAVOR. Be concise.\nClaim: {q}")
    con_out = await con.run(task=f"You argue AGAINST. Be concise.\nClaim: {q}")

    # Judge decides
    final = await judge.run(
        task=(
            "You are a fair judge. Consider both sides and return a concise, validated answer.\n\n"
            f"PRO:\n{pro_out}\n\nCON:\n{con_out}\n\nFinal judged answer only:"
        )
    )

    return str(final)

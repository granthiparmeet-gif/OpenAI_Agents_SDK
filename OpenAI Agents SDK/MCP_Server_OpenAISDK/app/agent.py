from agents import Agent, ModelSettings
from .tools import mcp_weather
from .mcp import build_mcp_servers


mcp_servers = build_mcp_servers()

agent = Agent(
    name="SDK+MCP Agent",
    instructions=(
        "You are a helpful assistant. "
        "Prefer using the registered tools for accurate answers."
    ),
    tools=[mcp_weather],           
    mcp_servers=mcp_servers,       
    
    model_settings=ModelSettings(tool_choice="mcp_weather"),  
    tool_use_behavior="stop_on_first_tool",                   
)
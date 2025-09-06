from agents import function_tool

@function_tool
def mcp_weather(city: str) -> str:
    """
    Return a mock weather string for a city.
    This simulates an MCP server tool registered locally.
    """
    data = {
        "paris": "18°C cloudy",
        "nyc": "22°C sunny",
        "london": "16°C light rain",
        "delhi": "31°C humid",
    }
    return data.get(city.lower(), "unknown")
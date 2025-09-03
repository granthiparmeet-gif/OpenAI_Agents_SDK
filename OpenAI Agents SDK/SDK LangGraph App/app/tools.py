from agents import function_tool

@function_tool
def api_tool(x:str) -> str:
    """Processes input text. raises a value error if the input is 'fail'.
    Args:
        x: Input strings to process.
    """

    if x == "fail":
        raise ValueError("API Failed")
    return f"Processed {x}"

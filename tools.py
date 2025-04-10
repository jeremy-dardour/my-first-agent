from typing import Any
from smolagents import tool, Tool


class FinalAnswerTool(Tool):
    name = "final_answer"
    description = "Provides a final answer to the given problem."
    inputs = {'answer': {'type': 'any', 'description': 'The final answer to the problem'}}
    output_type = "any"

    def forward(self, answer: Any) -> Any:
        return answer

    def __init__(self, *args, **kwargs):
        self.is_initialized = False


# Define a simple tool that our agent can use
@tool
def fake_search_tool(query: str) -> str:
    """
    Returns dummy information about a topic.
    Args:
        query (str): The user query to look into:
    """
    # In a real application, this would connect to a search API
    # For this demo, we'll just return a simple response
    return f"Here's what I found about '{query}': This is simulated search result data."

@tool
def calculator_tool(expression: str) -> int:
    """
    Evaluate a mathematical expression.
    Args:
        expression (str): The user mathematical expression to calculate:
    """
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

__all__ = ["fake_search_tool", "calculator_tool"]
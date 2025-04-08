import gradio as gr
from smolagents import CodeAgent, tool, LiteLLMModel

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

# Create our agent with tools
agent = CodeAgent(
    name="MyFirstAgent",
    model=LiteLLMModel(
        model_id="ollama_chat/qwen2:7b"
    ),
    description="A simple agent that can answer questions and perform calculations.",
    tools=[calculator_tool, fake_search_tool]
)

def process_query(query):
    """Process a user query using our agent."""
    if not query.strip():
        return "Please enter a question or request."
    
    # Let the agent process the query
    response = agent.run(query)
    return response

# Create a Gradio interface
demo = gr.Interface(
    fn=process_query,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything..."),
    outputs=gr.Textbox(lines=5),
    title="AI Agent Demo",
    description="A simple AI agent built with smolagents and Gradio. Try asking questions or using the calculator with expressions like '2 + 2'."
)

# Launch the app
if __name__ == "__main__":
    demo.launch()

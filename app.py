import yaml
from smolagents import CodeAgent, HfApiModel
from tools import FinalAnswerTool, fake_search_tool, calculator_tool
from Gradio_UI import GradioUI


model = HfApiModel(
max_tokens=2096,
temperature=0.5,
model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
custom_role_conversions=None,
)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
    

# Create our agent with tools
agent = CodeAgent(
    name="MyFirstAgent",
    model=model,
    description="A simple agent that can answer questions and perform calculations.",
    tools=[calculator_tool, fake_search_tool, FinalAnswerTool()],
    max_steps=5,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    prompt_templates=prompt_templates,
)

# Launch the app
if __name__ == "__main__":
    GradioUI(agent).launch()

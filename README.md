# My first Agent

A simple AI agent built with smolagents and Gradio

## Setup

1. Make sure you have Python 3.12+ installed
2. Make sure you have [uv](https://docs.astral.sh/uv/) intalled
3. Install the required dependencies:
```bash
uv sync
```
4. Install Ollama
5. Download qwen2:7b

## Running the Application

To start the Gradio web interface, run:

```bash
uv run app.py
```

The application will be available at http://127.0.0.1:7860 by default.

## Features

- AI agent powered by smolagents library
- Two built-in tools:
  - Search tool (simulated)
  - Calculator tool for mathematical expressions
- Web-based UI powered by Gradio

## Example Queries

Try asking the agent:
- "Search for information about climate change"
- "Calculate 15 * 24 + 7"
- "What is 42 divided by 6?"

## Customizing

To extend this application:
1. Add new tools to the agent in `app.py`
2. Modify the agent's behavior and capabilities
3. Enhance the Gradio interface with additional components
4. Update the requirements.txt file if you add new dependencies

## About smolagents

smolagents is a lightweight library for building simple AI agents with tool-using capabilities. It provides a straightforward way to create agents that can use tools to accomplish tasks.

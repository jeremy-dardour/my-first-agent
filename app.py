import gradio as gr

def greet(name):
    return f"Hello, {name}!"

# Create a simple Gradio interface
demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=1, placeholder="Enter your name..."),
    outputs="text",
    title="Gradio Demo Application",
    description="A simple Gradio application that greets the user."
)

# Launch the app
if __name__ == "__main__":
    demo.launch()

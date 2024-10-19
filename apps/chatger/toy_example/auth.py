import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")


demo.launch(
    # share=True,
    auth=('1chooo', '1234'),
    auth_message='Welcome to Chatter!',
)

import gradio as gr
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import pandas as pd

def greet(name):
    return "Hello " + name + "!"

def generate_gradient():
    gradient = gr.Interface(
        fn=greet,
        inputs=[
            gr.Textbox(type="text", label="Text Input"),
        ],
        outputs = [
            gr.Textbox(type="text", label="Text Input"),
        ],
        title="gradient test",
        description=(
            ""
        ),
        allow_flagging="never",
    )
    
    return gradient


def plot_example():
    months = ["January", "February", "March", "April", "May"]
    month = months[0]
    m = months.index(month)
    start_day = 30 * m
    final_day = 30 * (m + 1)
    x = np.arange(start_day, final_day + 1)
    pop_count = {"USA": 350, "Canada": 40, "Mexico": 300, "UK": 120}
    r = 1.54
    r = sqrt(r)
    df = pd.DataFrame({"day": x})
    
    countries = ['USA', 'Canada']
    for country in countries:
        df[country] = x ** (r) * (pop_count[country] + 1)

    fig = plt.figure()
    plt.plot(df["day"], df[countries].to_numpy())
    plt.title("Outbreak in " + month)
    plt.ylabel("Cases")
    plt.xlabel("Days since Day 0")
    plt.legend(countries)
    
    return fig

def greet_2(name):
    output = "Hello " + name + "!"
    fig = plot_example()
    return output, fig

def generate_gradient_2():

    gradient_2 = gr.Interface(
        fn=greet_2,
        inputs=[
            gr.Textbox(type="text", label="Text Input"),
        ],
        outputs=[
            gr.Textbox(type="text", label="Text Output"),
            gr.Plot(label="Plot")  # Add the plot as an output
        ],
        title="gradient test2",
        description="",
        allow_flagging="never",
    )

    return gradient_2

if __name__ == "__main__":
    demo = gr.Blocks()

    gradient = generate_gradient()
    gradient_2 = generate_gradient_2()

    with demo:
        gr.TabbedInterface(
            [gradient, gradient_2], 
            ["gradient", "gradient_2 Haha"]
        )

    demo.launch(
        share=True, 
        server_name="0.0.0.0", 
        server_port=6006,
        debug=True,
    ) 

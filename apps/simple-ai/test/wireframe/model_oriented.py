# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/23
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import gradio as gr
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import pandas as pd
import sklearn

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
        title="Gradient Boosting for classification",
        description=(
            "This algorithm builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. In each stage n_classes_ regression trees are fit on the negative gradient of the loss function, e.g. binary or multiclass log loss. Binary classification is a special case where only a single regression tree is induced."
        ),
        allow_flagging="never",
    )
    
    return gradient

def plot_test():
    fig = gr.Plot(
        label="Plot",
        show_label=True,
        
    )
    
    return fig

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
        title="A random forest regressor",
        description="A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree.",
        allow_flagging="never",
    )

    return gradient_2

def main():
    demo = gr.Blocks(
        title='AI For Beginner',
    )

    gradient = generate_gradient()
    gradient_2 = generate_gradient_2()

    with demo:
        with gr.Row():
            our_info = gr.Markdown("""\
            # AI For Beginner
            Enabling everyone unfamiliar with programming languages \
            to easily engage with AI and open the doors to the world of the future.
            """)
        gr.TabbedInterface(
            [gradient, gradient_2], 
            ["Gradient Boosting for classification", "A random forest regressor"]
        )
        with gr.Row():
            data_preprocessing = gr.Markdown("""\
            # Data pre-processing
            """)
        with gr.Row():
            sklearn_parameters = gr.Markdown("""\
            # `sklearn` parameters
            """)
        with gr.Row():
            train_history = gr.Markdown("""\
            # Train History
            """)
        with gr.Row():
            example = gr.Markdown("""\
            # Example
            """)

    demo.launch(
        share=True, 
        server_name="0.0.0.0", 
        server_port=6006,
        debug=True,
    ) 

if __name__ == "__main__":
    main()

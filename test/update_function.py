'''
Create Date: 2023/09/01
Author: @1chooo
Version: v0.0.3
'''

import gradio as gr

demo = gr.Blocks(
    title='Refinaid',
)

def update_parameters(dataset):
    if dataset == "Titanic":
        parameters = ["Param1", "Param2", "Param3"]
    elif dataset == "Diabetes":
        parameters = ["ParamA", "ParamB", "ParamC"]
    elif dataset == "House Prices":
        parameters = ["ParamX", "ParamY", "ParamZ"]
    else:
        parameters = []
    return parameters

dataset_choices = [
    "Titanic", 
    "Diabetes", 
    "House Prices",
]

with demo:
    our_heading = gr.Markdown("# Simple AI - Bridging the Gap with AI For Everyone")

    with gr.Tab("Preprocessing"):
        our_heading = gr.Markdown("## Preprocessing")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Dataset")
                
                dataset_dropdown = gr.Dropdown(
                    label="Select Dataset", 
                    choices=dataset_choices,
                    interactive=True,
                )
                gr.Markdown("### Pick up Parameters")
                parameters_dropdown = gr.Dropdown(
                    label="Select Mutiple Parameters", 
                    choices=[], 
                    interactive=True,
                    multiselect=True,
                )

    dataset_dropdown.change(
        fn=update_parameters,
        inputs=dataset_dropdown,
        outputs=parameters_dropdown,
    )

demo.launch(
    # enable_queue=True,
    # share=True, 
    server_name="127.0.0.1", 
    server_port=6006,
    debug=True,
) 
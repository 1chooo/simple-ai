'''
Create Date: 2023/09/01
Author: @1chooo
Version: v0.0.3
'''

import gradio as gr

demo = gr.Blocks(
    title='Refinaid',
)

with demo:
    our_heading = gr.Markdown("# Simple AI - Bridging the Gap with AI For Everyone")

    with gr.Tab("Preprocessing"):
        our_heading = gr.Markdown("## Preprocessing")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Dataset")
                gr.Markdown("### Inputs")
                gr.Markdown("### Missing Values Handling")
                gr.Markdown(f"### Data Split\nTotal value should be 100%")
            with gr.Column():
                gr.ScatterPlot(label="Data Visualization")

    with gr.Tab("Training"):
        our_heading = gr.Markdown("## Training")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Data You have picked!!!")
                gr.DataFrame(
                    headers=[
                        "Parameters",
                        "Value"
                    ],
                    row_count=(7, "fixed"),
                    col_count=(2, "fixed"),
                    interactive=False,
                )
            with gr.Column():
                gr.Dropdown(label="Select Model", interactive=True)
        with gr.Row():
            train_btn = gr.Button(
                value="Train"
            )
        with gr.Row():
            gr.Markdown("## Training Result")
        with gr.Row():
            train_df = gr.DataFrame(
                headers=["Accuracy", "Recall", "Precision", "F1"], 
                interactive=True, 
                row_count=(1, "fixed"), 
                col_count=(4, "fixed")
            )

        with gr.Row():
            train_img1 = gr.Plot(interactive=True)
            train_img2 = gr.Plot(interactive=True)
            train_img3 = gr.Plot(interactive=True)

    with gr.Tab("Results"):
        our_heading = gr.Markdown("## Results")
        with gr.Row():
            gr.Textbox("hi")
            gr.Textbox("hi")
        with gr.Row():
            gr.Textbox("hello")
            gr.Textbox("hello")

demo.launch(
    # enable_queue=True,
    # share=True, 
    server_name="127.0.0.1", 
    server_port=6006,
    debug=True,
) 
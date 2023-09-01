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
        parameters = []  # 如果選擇了未知的數據集，則將 parameters 清空
    return parameters

with demo:
    our_heading = gr.Markdown("# Simple AI - Bridging the Gap with AI For Everyone")

    with gr.Tab("Preprocessing"):
        our_heading = gr.Markdown("## Preprocessing")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Dataset")
                dataset_choices = [
                    "Titanic", 
                    "Diabetes", 
                    "House Prices",
                ]
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
                gr.Markdown("### Missing Values Handling")
                miss_value_chkbox = gr.Radio(
                    label="Select a Method", 
                    choices=[
                        "Drop Nan", 
                        "By Columns"
                    ], 
                    interactive=True,
                )
                gr.Markdown(f"### Data Split\nTotal value should be 100%")
                data_scale_dd = gr.Radio(
                    choices=[
                        "None", 
                        "Standard", 
                        "Min-Max"
                    ], 
                    label="Please select a method", 
                    interactive=True,
                )
                training_slider = gr.Slider(
                    label="Training Set", 
                    minimum=0, 
                    maximum=100, 
                    step=5,
                )
                validation_slider = gr.Slider(
                    label="Validation Set", 
                    minimum=0, 
                    maximum=100, 
                    step=5,
                )
                testing_slider = gr.Slider(
                    label="Testing Set", 
                    minimum=0, 
                    maximum=100, 
                    step=5,
                )
                submit_dataset_setting_btn = gr.Button(
                    value="Submit Setting"
                )
            with gr.Column():
                with gr.Row():
                    gr.ScatterPlot(
                        label="Data Visualization")
                with gr.Row():
                    x_axis_dropdown = gr.Dropdown(
                        label="X Axis", 
                        choices=[
                            "這會隨著上面 dataset 選擇更新", 
                        ], 
                        interactive=True,
                    )
                    y_axis_dropdown = gr.Dropdown(
                        label="Y Axis", 
                        choices=[
                            "這會隨著上面 dataset 選擇更新", 
                        ], 
                        interactive=True,
                    )

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

    # 綁定事件處理函數
    dataset_dropdown.change(
        fn=update_parameters,
        # inputs=dataset_dropdown,
        outputs=parameters_dropdown,
    )

demo.launch(
    # enable_queue=True,
    # share=True, 
    server_name="127.0.0.1", 
    server_port=6006,
    debug=True,
) 
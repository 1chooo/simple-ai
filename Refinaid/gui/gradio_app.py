import gradio as gr

explanatory_text = {
                    "header":{"title":"# AI for Beginner", "body":"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. "}, 
                    "preprocess":{"title":"## What is preprocessing?", "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."},
                    "training":{"title":"## What is model training?", "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."},
                    "result":{"title":"## What is the result?", "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."}
                    
}

dropdown_options = {
                    "datasets": ["ds1", "ds2", "ds3"],
                    "inputs": ["ip1", "ip2", "ip3"],
                        "data_scalings": ["Standard", "Min-Max"]
}

def submit_setting_btn_click(dataset:str, inputs:list, miss_value:bool, data_scaling:str, training:int, validation:int, testing:int):
    print(dataset, inputs, miss_value, data_scaling, training, validation, testing)
    if dataset == None or dataset == "":
        raise gr.Error("Invalid Dataset")
        return
    if inputs == None or inputs == []:
        raise gr.Error("Invalid Multiple Inputs")
        return
    if data_scaling == None or data_scaling == "":
        raise gr.Error("Invalid Data Scaling")
        return
    try:
        if training + validation + testing != 100:
            raise gr.Error("Invalid Data Split")
            return
    except:
        raise gr.Error("Invalid Data Split")
        return
    gr.Info("Setting Updated")


with gr.Blocks() as demo:
    gr.Markdown(f"{explanatory_text['header']['title']}\n{explanatory_text['header']['body']}")
    with gr.Tab("Preprocess"):
        gr.Markdown(f"{explanatory_text['preprocess']['title']}\n{explanatory_text['preprocess']['body']}")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Dataset")
                dataset_dd = gr.Dropdown(label="Select Dataset", choices=dropdown_options["datasets"])
                gr.Markdown("### Inputs")
                inputs_dd = gr.Dropdown(label="Select Mutiple Inputs", choices=dropdown_options["inputs"], multiselect=True)
                # with gr.Accordion("Options"):
                gr.Markdown(f"### Missing Values Handling")
                miss_value_chkbox = gr.Checkbox(label="Enable")
                gr.Markdown(f"### Data Scaling")
                data_scale_dd = gr.Dropdown(choices=dropdown_options["data_scalings"], label="Please select a method")
                gr.Markdown(f"### Data Split\nTotal should be 100%")
                train_sldr = gr.Slider(label="Training Set", minimum=0, maximum=100, step=5)
                valid_sldr = gr.Slider(label="Validation Set", minimum=0, maximum=100, step=5)
                test_sldr = gr.Slider(label="Testing Set", minimum=0, maximum=100, step=5)
                submit_set_btn = gr.Button(value="Submit Setting")
            with gr.Column():
                gr.ScatterPlot(label="Data Visualization")
                with gr.Row():
                    gr.Dropdown(label="X Axis", choices=dropdown_options["datasets"])
                    gr.Dropdown(label="Y Axis", choices=dropdown_options["datasets"])
    with gr.Tab("Training"):
        gr.Markdown(f"{explanatory_text['training']['title']}\n{explanatory_text['training']['body']}")
        with gr.Row():
            gr.Textbox("hi")
            gr.Textbox("hi")
        with gr.Row():
            gr.Textbox("hello")
            gr.Textbox("hello")
    with gr.Tab("Result"):
        gr.Markdown(f"{explanatory_text['result']['title']}\n{explanatory_text['result']['body']}")
        with gr.Row():
            gr.Textbox("hi")
            gr.Textbox("hi")
        with gr.Row():
            gr.Textbox("hello")
            gr.Textbox("hello")
    submit_set_btn.click(fn=submit_setting_btn_click, inputs=[dataset_dd, inputs_dd, miss_value_chkbox, data_scale_dd, train_sldr, valid_sldr, test_sldr])

demo.launch(enable_queue=True, debug=True)


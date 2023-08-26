'''
Create Date: 2023/08/25
Author: @VincentLi1216
Email: sunnus.tw@gmail.com
Version: v0.0.1
'''
import gradio as gr

explanatory_text = {
                    "header":{"title":"# AI for Beginner", "body":"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. "}, 
                    "preprocess":{"title":"## What is preprocessing?", "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."},
                    "training":{"title":"## What is model training?", "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."},
                    "result":{"title":"## What is the result?", "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."}
                    
}

'''
DecisionTreeClassifier

第一個選項為default

criterion: {"gini", "entropy", "log_loss"} ->選單
max_depth: {none, or int} ->輸入框(valueError handling)
min_samples_split: {2, 3, 4, ......, 20}->滑桿
min_samples_leaf: {1, 2, ......, 19, 20} ->滑桿
max_features: {"auto", "sqrt", "log2"} ->選單
max_leaf_nodes: {none, or int} ->輸入框(valueError handling)
'''

dropdown_options = {
                    "datasets": ["ds1", "ds2", "ds3"],
                    "inputs": ["ip1", "ip2", "ip3"],
                    "data_scalings": ["Standard", "Min-Max"],
                    "models": ["Decision Tree Classifier", "model2", "model3"],
                    "plots": ["plot1", "plot2", "plot3"],
                    "model_parameters":{
                                        "decision_tree_classifier": {
                                              "criterion": ["gini", "entropy", "log_loss"],
                                              "max_features": ["auto", "sqrt", "log2"]
                                        }
                    }

}

model_parameters = {
                    "decision_tree_classifier": {
                                               "criterion": None,
                                               "max_depth": None,
                                               "min_samples_split": None,
                                               "min_samples_leaf": None,
                                               "max_features": None,
                                               "max_leaf_nodes": None
                    }
}


model_mapping = {
                "Decision Tree Classifier": "decision_tree_classifier"
}

current_model = "decision_tree_classifier"

# components = [gr.Text, gr.Text]
# for i in range(len(components)):
#     components[i] = components[i].update(visible=True)

# return com for com in components



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
    update_list = [dataset_dd, inputs_dd]
    return *[component.update(visible=False) for component in update_list],

with gr.Blocks() as demo:
    gr.Markdown(f"{explanatory_text['header']['title']}\n{explanatory_text['header']['body']}")
    with gr.Tab("Preprocess"):
        gr.Markdown(f"{explanatory_text['preprocess']['title']}\n{explanatory_text['preprocess']['body']}")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Dataset")
                dataset_dd = gr.Dropdown(label="Select Dataset", choices=dropdown_options["datasets"], interactive=True)
                gr.Markdown("### Inputs")
                inputs_dd = gr.Dropdown(label="Select Mutiple Inputs", choices=dropdown_options["inputs"], multiselect=True)
                # with gr.Accordion("Options"):
                gr.Markdown(f"### Missing Values Handling")
                miss_value_chkbox = gr.Checkbox(label="Enable")
                gr.Markdown(f"### Data Scaling")
                data_scale_dd = gr.Dropdown(choices=dropdown_options["data_scalings"], label="Please select a method", interactive=True)
                gr.Markdown(f"### Data Split\nTotal should be 100%")
                train_sldr = gr.Slider(label="Training Set", minimum=0, maximum=100, step=5)
                valid_sldr = gr.Slider(label="Validation Set", minimum=0, maximum=100, step=5)
                test_sldr = gr.Slider(label="Testing Set", minimum=0, maximum=100, step=5)
                submit_set_btn = gr.Button(value="Submit Setting")
            with gr.Column():
                gr.ScatterPlot(label="Data Visualization")
                with gr.Row():
                    x_axis_dd = gr.Dropdown(label="X Axis", choices=dropdown_options["datasets"])
                    y_axis_dd = gr.Dropdown(label="Y Axis", choices=dropdown_options["datasets"])

    with gr.Tab("Training"):
        gr.Markdown(f"{explanatory_text['training']['title']}\n{explanatory_text['training']['body']}")
        with gr.Row():
            with gr.Column():
                gr.Textbox(label="Data Summary")
                model_dd = gr.Dropdown(label="Select Model", choices=dropdown_options["models"])
    
                dtc_md = gr.Markdown("### Decision Tree Classifier", interactive=True)
                dtc_criterion_dd = gr.Dropdown(label="criterion", choices=dropdown_options["model_parameters"]["decision_tree_classifier"]["criterion"], interactive=True)
                gr.Textbox(label="max_depth", interactive=True)
                gr.Slider(label="min_samples_split", minimum=2, maximum=20, step=1, interactive=True)
                gr.Slider(label="min_samples_leaf", minimum=1, maximum=20, step=1, interactive=True)
                gr.Dropdown(label="max_features", choices=dropdown_options["model_parameters"]["decision_tree_classifier"]["max_features"], interactive=True)
                gr.Textbox(label="max_leaf_nodes", interactive=True)
                

                gr.Slider(label="Learning Rate", minimum=0.0001, maximum=0.1, step=0.0001, interactive=True)

                gr.Button(value="Train")
            with gr.Column():
                plot_dd = gr.Dropdown(label="Select Plot", choices=dropdown_options["plots"])
                gr.Plot()

    with gr.Tab("Result"):
        gr.Markdown(f"{explanatory_text['result']['title']}\n{explanatory_text['result']['body']}")
        with gr.Row():
            gr.Textbox("hi")
            gr.Textbox("hi")
        with gr.Row():
            gr.Textbox("hello")
            gr.Textbox("hello")
    gr.Examples(
                [["Titanic", ["PassengerId", "Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"], True, "standard", 70, 10, 20]],
                [dataset_dd, inputs_dd, miss_value_chkbox, data_scale_dd, train_sldr, valid_sldr, test_sldr]
    )
    submit_set_btn.click(fn=submit_setting_btn_click, inputs=[dataset_dd, inputs_dd, miss_value_chkbox, data_scale_dd, train_sldr, valid_sldr, test_sldr], outputs=[dataset_dd, inputs_dd])

demo.launch(enable_queue=True, debug=True)



'''
Create Date: 2023/08/25
Author: @VincentLi1216
Email: sunnus.tw@gmail.com
Version: v0.0.1
'''
import gradio as gr
from Refinaid.Action.ML_configurations import DatasetConfig, DecisionTreeModelConfig, KNNModelConfig
from Refinaid.Action.Model import training

explanatory_text = {
                    "header":{"title":"# AI for Beginner", "body":"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. "}, 
                    "preprocess":{"title":"## What is preprocessing?", "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."},
                    "training":{"title":"## What is model training?", "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."},
                    "result":{"title":"## What is the result?", "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."}
                    
}


dropdown_options = {
                    "datasets": ["ds1", "ds2", "ds3"],
                    "inputs": ["ip1", "ip2", "ip3"],
                    "miss_value": ["Drop Nan", "By Columns"],
                    "data_scalings": ["None", "Standard", "Min-Max"],
                    "models": ["Decision Tree Classifier", "K Neighbor Classifier"],
                    "plots": ["plot1", "plot2", "plot3"],
                    "model_parameters":{
                                        "decision_tree_classifier": {
                                              "criterion": ["gini", "entropy", "log_loss"],
                                              "max_features": ["None", "sqrt", "log2"]},
                                        "k_neighbors_classifier": {
                                            "weights": ["uniform", "distance"],
                                            "algorithm": ["auto", "ball_tree", "kd_tree", "brute"]}
                                        
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
                "Decision Tree Classifier": "decision_tree_classifier",
                "K Neighbor Classifier": "k_neighbors_classifier",
                "Standard": "standard",
                "Min-Max": "min-max",
                "By Columns": "by_columns",
                "None": None,
                "Drop Nan": None
                
}

model_components = {}

current_model = "decision_tree_classifier"

dataset_config = None


def model_dd_change(model_dd):

    comp_output_list = []
    selected_model = model_mapping[model_dd]
    # print(model_dd)
    # print(selected_model)

    for key in model_components.keys():
        if key not in ["all", "model_selector"]:
            if key == selected_model:
                for i in range(len(model_components[key])):
                    # print(f"key:{key}\ni:{i}\nitem:{model_components[key][i]}")
                    comp_output_list.append(model_components[key][i].update(visible=True))
            else:
                for i in range(len(model_components[key])):
                    # print(f"key:{key}\ni:{i}\nitem:{model_components[key][i]}")
                    comp_output_list.append(model_components[key][i].update(visible=False))
    # print(comp_output_list)
                

    return *comp_output_list,


def submit_setting_btn_click(dataset:str, inputs:list, miss_value:bool, data_scaling:str, training:int, validation:int, testing:int):
    # print(dataset, inputs, miss_value, data_scaling, training, validation, testing)

    global model_components
    global dataset_config

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

    data_summary_text = ""
    for parameter in ["dataset", "inputs", "miss_value", "data_scaling", "training", "validation", "testing"]:
        variable_value = locals()[parameter]
        # rm \n if it is the last line
        if parameter == "testing":
            #todo add output column
            #todo change to dataframe
            data_summary_text += f"{parameter}: {variable_value}"
        else:
            data_summary_text += f"{parameter}: {variable_value}\n"

    # print(dataset, inputs, model_mapping[miss_value], model_mapping[data_scaling], [training/100, validation/100, testing/100])
    dataset_config=DatasetConfig(dataset, inputs, model_mapping[miss_value], model_mapping[data_scaling], [training/100, validation/100, testing/100])
    
    gr.Info("Setting Updated")
    return data_summary.update(value=data_summary_text)

def train_btn_click(select_model,tdtc_md, dtc_criterion_dd, dtc_max_depth_tb, dtc_min_samples_split_sldr, dtc_min_samples_leaf_sldr, dtc_max_features_dd, dtc_max_leaf_nodes_tb, knc_md, knc_althm_dd, knc_n_nbr_sldr, knc_weights_dd):
    output_list = []

    if select_model == "Decision Tree Classifier":
        dtc_max_features_dd = dtc_max_features_dd if dtc_max_features_dd != "None" else None
        model_config = DecisionTreeModelConfig(dtc_criterion_dd, dtc_min_samples_split_sldr, dtc_min_samples_leaf_sldr, dtc_max_features_dd, eval(dtc_max_depth_tb), eval(dtc_max_leaf_nodes_tb))
    elif select_model == "K Neighbor Classifier":
        model_config = KNNModelConfig(knc_n_nbr_sldr, knc_weights_dd, knc_althm_dd)
    
    figures, evaluations = training(dataset_config, model_config)

    evaluations = list(map(str,evaluations))

    img_components = [train_img1, train_img2, train_img3]

    output_list.append(train_df.update(value=[evaluations]))

    for i, component in enumerate(img_components):
        if figures[i] != None:
            output_list.append(component.update(value=figures[i], visible=True))
        else:
            output_list.append(component.update(visible=False))

    return *output_list,
    

    


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
                miss_value_chkbox = gr.Radio(label="Select a Method", choices=dropdown_options["miss_value"], interactive=True)
                gr.Markdown(f"### Data Scaling")
                data_scale_dd = gr.Radio(choices=dropdown_options["data_scalings"], label="Please select a method", interactive=True)
                gr.Markdown(f"### Data Split\nTotal value should be 100%")
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
                data_summary = gr.Textbox(label="Data Summary", lines=7, interactive=True)
                model_dd = gr.Dropdown(label="Select Model", choices=dropdown_options["models"], interactive=True)
            with gr.Column():
                # decision_tree_classifier
                dtc_md = gr.Markdown("### Decision Tree Classifier", interactive=True, visible=False)
                dtc_criterion_dd = gr.Dropdown(label="Criterion", 
                                               choices=dropdown_options["model_parameters"]["decision_tree_classifier"]["criterion"], value="gini", interactive=True, visible=False)
                dtc_max_depth_tb = gr.Textbox(label="Max Depth", value="None", interactive=True, visible=False)
                dtc_min_samples_split_sldr = gr.Slider(label="Minimum Samples Split", minimum=2, maximum=20, step=1, value=2, interactive=True, visible=False)
                dtc_min_samples_leaf_sldr = gr.Slider(label="Minimum Samples Leaf", minimum=1, maximum=20, step=1, value=1, interactive=True, visible=False)
                dtc_max_features_dd = gr.Dropdown(label="Max Features", 
                                                  choices=dropdown_options["model_parameters"]["decision_tree_classifier"]["max_features"], value="None", interactive=True, visible=False)
                dtc_max_leaf_nodes_tb = gr.Textbox(label="Max Leaf Nodes", value="None", interactive=True, visible=False)
                
                # k_neighbors_classifier
                knc_md = gr.Markdown("### K Neighbors Classifier", interactive=True, visible=False)
                knc_n_nbr_sldr = gr.Slider(label="N Neighbors", value=5, interactive=True, minimum=1, maximum=20, step=1, visible=False)
                knc_weights_dd = gr.Dropdown(label="Weights", choices=dropdown_options["model_parameters"]["k_neighbors_classifier"]["weights"], value="uniform", interactive=True, visible=False)
                knc_althm_dd = gr.Dropdown(label="Algorithm", choices=dropdown_options["model_parameters"]["k_neighbors_classifier"]["algorithm"], value="auto", interactive=True, visible=False)


        train_btn = gr.Button(value="Train")
        gr.Markdown("## Training Result")
        train_df = gr.DataFrame(headers=["Accuracy", "Recall", "Precision", "F1"], interactive=True, row_count=(1, "fixed"), col_count=(4, "fixed"))

        with gr.Row():
            train_img1 = gr.Plot(interactive=True)
            train_img2 = gr.Plot(interactive=True)
            train_img3 = gr.Plot(interactive=True)
            
    with gr.Tab("Result"):
        gr.Markdown(f"{explanatory_text['result']['title']}\n{explanatory_text['result']['body']}")
        with gr.Row():
            gr.Textbox("hi")
            gr.Textbox("hi")
        with gr.Row():
            gr.Textbox("hello")
            gr.Textbox("hello")

    gr.Examples(
                [["Titanic", ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"], "Drop Nan", "None", 70, 10, 20]],
                [dataset_dd, inputs_dd, miss_value_chkbox, data_scale_dd, train_sldr, valid_sldr, test_sldr]
    )


    model_components = {
                        "all": [dtc_md, dtc_criterion_dd, dtc_max_depth_tb, dtc_min_samples_split_sldr, dtc_min_samples_leaf_sldr, dtc_max_features_dd, dtc_max_leaf_nodes_tb, knc_md, knc_althm_dd, knc_n_nbr_sldr, knc_weights_dd],
                        "model_selector": [model_dd],
                        "decision_tree_classifier":[dtc_md, dtc_criterion_dd, dtc_max_depth_tb, dtc_min_samples_split_sldr, dtc_min_samples_leaf_sldr, dtc_max_features_dd, dtc_max_leaf_nodes_tb],
                        "k_neighbors_classifier": [knc_md, knc_althm_dd, knc_n_nbr_sldr, knc_weights_dd]
    }

    submit_set_btn.click(fn=submit_setting_btn_click, inputs=[dataset_dd, inputs_dd, miss_value_chkbox, data_scale_dd, train_sldr, valid_sldr, test_sldr], outputs=[data_summary])
    train_btn.click(fn=train_btn_click, inputs=[model_dd, *model_components["all"]], outputs=[train_df, train_img1, train_img2, train_img3])
    
    model_dd.change(fn=model_dd_change, inputs=model_dd, outputs=model_components["all"])

demo.launch(enable_queue=True, debug=True)



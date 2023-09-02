'''
Create Date: 2023/09/02
Author: @1chooo
Version: v0.0.3
'''

import gradio as gr
from Refinaid.Action.Load import get_dataset_x_columns
from Refinaid.gui.Utils.Get import get_data_setting

def update_parameters(dataset_name) -> gr.Dropdown:
    parameters = get_dataset_x_columns(dataset_name)

    return gr.Dropdown.update(
            choices=parameters,
            value=[],
            label="Select Mutiple Parameters",
            interactive=True,
        )

def update_plot_x_parameters(dataset_name) -> gr.Dropdown:
    parameters = get_dataset_x_columns(dataset_name)

    return gr.Dropdown.update(
            choices=parameters,
            value=[],
            label="X Axis",
            interactive=True,
        )

def update_plot_y_parameters(dataset_name) -> gr.Dropdown:
    parameters = get_dataset_x_columns(dataset_name)

    return gr.Dropdown.update(
            choices=parameters,
            value=[],
            label="Y Axis",
            interactive=True,
        )

def update_model_parameters(model_name):
    output_components = []
    if model_name == 'Decision Tree Classifier':
        decision_tree_classifer_title = gr.Markdown.update(
            "### Decision Tree Classifier", 
            visible=True,
        )
        decision_tree_classifer_criterion_dropdown = gr.Dropdown.update(
            label="Criterion", 
            choices=[
                "gini", 
                "entropy", 
                "log_loss"
            ], 
            value="gini", 
            interactive=True, 
            visible=True,
        )
        decision_tree_classifer_max_depth_textbox = gr.Textbox.update(
            label="Max Depth", 
            value="None", 
            interactive=True, 
            visible=True,
        )
        decision_tree_classifer_min_samples_split_slider = gr.Slider.update(
            label="Minimum Samples Split", 
            minimum=2, 
            maximum=20, 
            step=1, 
            value=2, 
            interactive=True, 
            visible=True,
        )
        decision_tree_classifer_min_samples_leaf_slider = gr.Slider.update(
            label="Minimum Samples Leaf", 
            minimum=1, 
            maximum=20, 
            step=1, 
            value=1, 
            interactive=True, 
            visible=True,
        )
        decision_tree_classifer_max_features_dropdown = gr.Dropdown.update(
            label="Max Features", 
            choices=[
                "None", 
                "sqrt", 
                "log2"
            ], 
            value="None", 
            interactive=True, 
            visible=True,
        )
        decision_tree_classifer_max_leaf_nodes_textbox = gr.Textbox.update(
            label="Max Leaf Nodes", 
            value="None", 
            interactive=True, 
            visible=True,
        )

        k_neighbors_classifier_title = gr.Markdown.update(
            "### K Neighbors Classifier", 
            visible=False,
        )
        k_neighbors_classifier_slider = gr.Slider.update(
            label="N Neighbors", 
            value=5, 
            interactive=True, 
            minimum=1, 
            maximum=20, 
            step=1, 
            visible=False,
        )
        k_neighbors_classifier_weights_dropdown = gr.Dropdown.update(
            label="Weights", 
            choices=[
                "uniform", 
                "distance"
            ], 
            value="uniform", 
            interactive=True, 
            visible=False,
        )
        k_neighbors_classifier_algorithm_dropdown = gr.Dropdown.update(
            label="Algorithm", 
            choices=[
                "auto", 
                "ball_tree", 
                "kd_tree", 
                "brute"
            ], 
            value="auto", 
            interactive=True, 
            visible=False,
        )
    elif model_name == "K Neighbor Classifier":
        output_components = []
        decision_tree_classifer_title = gr.Markdown.update(
            "### Decision Tree Classifier", 
            visible=False,
        )
        decision_tree_classifer_criterion_dropdown = gr.Dropdown.update(
            label="Criterion", 
            choices=[
                "gini", 
                "entropy", 
                "log_loss"
            ], 
            value="gini", 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_max_depth_textbox = gr.Textbox.update(
            label="Max Depth", 
            value="None", 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_min_samples_split_slider = gr.Slider.update(
            label="Minimum Samples Split", 
            minimum=2, 
            maximum=20, 
            step=1, 
            value=2, 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_min_samples_leaf_slider = gr.Slider.update(
            label="Minimum Samples Leaf", 
            minimum=1, 
            maximum=20, 
            step=1, 
            value=1, 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_max_features_dropdown = gr.Dropdown.update(
            label="Max Features", 
            choices=[
                "None", 
                "sqrt", 
                "log2"
            ], 
            value="None", 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_max_leaf_nodes_textbox = gr.Textbox.update(
            label="Max Leaf Nodes", 
            value="None", 
            interactive=True, 
            visible=False,
        )

        k_neighbors_classifier_title = gr.Markdown.update(
            "### K Neighbor Classifier", 
            visible=True,
        )
        k_neighbors_classifier_slider = gr.Slider.update(
            label="N Neighbors", 
            value=5, 
            interactive=True, 
            minimum=1, 
            maximum=20, 
            step=1, 
            visible=True,
        )
        k_neighbors_classifier_weights_dropdown = gr.Dropdown.update(
            label="Weights", 
            choices=[
                "uniform", 
                "distance"
            ], 
            value="uniform", 
            interactive=True, 
            visible=True,
        )
        k_neighbors_classifier_algorithm_dropdown = gr.Dropdown.update(
            label="Algorithm", 
            choices=[
                "auto", 
                "ball_tree", 
                "kd_tree", 
                "brute"
            ], 
            value="auto", 
            interactive=True, 
            visible=True,
        )


    output_components.append(decision_tree_classifer_title)
    output_components.append(decision_tree_classifer_criterion_dropdown)
    output_components.append(decision_tree_classifer_max_depth_textbox)
    output_components.append(decision_tree_classifer_min_samples_split_slider)
    output_components.append(decision_tree_classifer_min_samples_leaf_slider)
    output_components.append(decision_tree_classifer_max_features_dropdown)
    output_components.append(decision_tree_classifer_max_leaf_nodes_textbox)
    output_components.append(k_neighbors_classifier_title)
    output_components.append(k_neighbors_classifier_slider)
    output_components.append(k_neighbors_classifier_weights_dropdown)
    output_components.append(k_neighbors_classifier_algorithm_dropdown)

    return *output_components,

def update_preprocessing_data(
        dataset:str, parameters:list, 
        miss_value:bool, data_scaling:str, 
        training:int, validation:int, testing:int):

    if dataset == None or dataset == "":
        raise gr.Error("Invalid Dataset")
    if parameters == None or parameters == []:
        raise gr.Error("Invalid Multiple Inputs")
    if data_scaling == None or data_scaling == "":
        raise gr.Error("Invalid Data Scaling")
    try:
        if training + validation + testing != 100:
            raise gr.Error("Invalid Data Split")
    except:
        raise gr.Error("Invalid Data Split")

    data_summary_dict = get_data_setting(
        dataset, parameters, miss_value, 
        data_scaling, training, validation, testing
    )

    return gr.DataFrame.update(
        value=data_summary_dict
        )

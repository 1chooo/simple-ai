'''
Create Date: 2023/09/02
Author: @1chooo, @ReeveWu
Version: v0.0.7
'''

import gradio as gr
from Refinaid.Action.Load import get_dataset_x_columns, get_dataset_numeric_columns
from Refinaid.Utils.Get import get_data_setting
from Refinaid.Action.ML_configurations import DatasetConfig, DecisionTreeModelConfig, KNNModelConfig
from Refinaid.Action.Model import training
from Refinaid.Action.Load import get_dataframe
import pandas as pd

def update_parameters(dataset_name: str) -> gr.Dropdown:
    parameters = get_dataset_x_columns(dataset_name)

    return gr.Dropdown.update(
            choices=parameters,
            value=[],
            label="Select Mutiple Parameters",
            interactive=True,
        )

def update_plot_x_parameters(dataset_name: str) -> gr.Dropdown:
    parameters = get_dataset_numeric_columns(dataset_name)

    return gr.Dropdown.update(
            choices=parameters,
            value=parameters[0],
            label="X Axis",
            interactive=True,
        )

def update_plot_y_parameters(dataset_name: str) -> gr.Dropdown:
    parameters = get_dataset_numeric_columns(dataset_name)

    return gr.Dropdown.update(
            choices=parameters,
            value=parameters[1],
            label="Y Axis",
            interactive=True,
        )

def update_preprocessing_visualization(dataset_dropdown, x_axis_dropdown, y_axis_dropdown):
    df = get_dataframe(dataset_dropdown)

    return gr.ScatterPlot.update(
        label="Data Visualization",
        value=df,
        x=x_axis_dropdown,
        y=y_axis_dropdown,
        title="Scatter Plot in Data Visualization",
        height=400,
        width=400,
        caption='Observe the relationship between parameters',
    )

def update_model_parameters(model_name: str):
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

def _handle_invalid_data_input(
        dataset: str, parameters: list, 
        miss_value: bool, data_scaling: str, 
        training: int, validation: int, testing: int):
    if dataset == None or dataset == "":
        raise gr.Error("Invalid Dataset")
    if parameters == None or parameters == []:
        raise gr.Error("Invalid Multiple Inputs")
    if data_scaling == None or data_scaling == "":
        raise gr.Error("Invalid Data Scaling")
    if training + validation + testing != 100:
        raise gr.Error("Invalid Data Split")

def update_preprocessing_data(
        dataset: str, parameters: list, 
        miss_value: bool, data_scaling: str, 
        training: int, validation: int, testing: int):

    _handle_invalid_data_input(
        dataset, 
        parameters, 
        miss_value,
        data_scaling, 
        training, 
        validation, 
        testing,
    )

    data_summary_dict = get_data_setting(
        dataset, parameters, miss_value, 
        data_scaling, training, validation, testing
    )

    return gr.Dataframe.update(
        value=data_summary_dict
    )

def update_training_results(
        preprocessing_data_result,
        model_dropdown,
        decision_tree_classifer_criterion_dropdown,
        decision_tree_classifer_max_depth_textbox,
        decision_tree_classifer_min_samples_split_slider,
        decision_tree_classifer_min_samples_leaf_slider,
        decision_tree_classifer_max_features_dropdown,
        decision_tree_classifer_max_leaf_nodes_textbox, 
        k_neighbors_classifier_slider,
        k_neighbors_classifier_weights_dropdown,
        k_neighbors_classifier_algorithm_dropdown,
    ) -> list:
    
    model_config = None
    
    if model_dropdown == "Decision Tree Classifier":
        decision_tree_classifer_max_features_dropdown = decision_tree_classifer_max_features_dropdown if decision_tree_classifer_max_features_dropdown != "None" else None
        model_config = DecisionTreeModelConfig(
            decision_tree_classifer_criterion_dropdown, 
            decision_tree_classifer_min_samples_split_slider, 
            decision_tree_classifer_min_samples_leaf_slider, 
            decision_tree_classifer_max_features_dropdown, 
            eval(decision_tree_classifer_max_depth_textbox), 
            eval(decision_tree_classifer_max_leaf_nodes_textbox),
        )
    elif model_dropdown == "K Neighbor Classifier":
        model_config = KNNModelConfig(
            k_neighbors_classifier_slider, 
            k_neighbors_classifier_weights_dropdown, 
            k_neighbors_classifier_algorithm_dropdown,
        )

    preprocessing_data_value = preprocessing_data_result
    dataset_config=DatasetConfig(
        preprocessing_data_value.loc[0, "Value"],
        preprocessing_data_value.loc[1, "Value"],
        preprocessing_data_value.loc[2, "Value"],
        None if preprocessing_data_value.loc[3, "Value"] == "None" else preprocessing_data_value.loc[3, "Value"],
        [
            preprocessing_data_value.loc[4, "Value"] / 100,
            preprocessing_data_value.loc[5, "Value"] / 100,
            preprocessing_data_value.loc[6, "Value"] / 100,
        ],
    )

    training_outputs = []
    figures, evaluations = training(dataset_config, model_config)
    evaluations = list(map(str,evaluations))

    training_results = gr.Dataframe.update(
        value=[evaluations],
        interactive=True,
    )

    training_outputs.append(training_results)

    train_img1 = gr.Plot(
        interactive=True
    )
    train_img2 = gr.Plot(
        interactive=True
    )
    train_img3 = gr.Plot(
        interactive=True
    )

    img_components = [
        train_img1, 
        train_img2, 
        train_img3
    ]

    for i, component in enumerate(img_components):
        if figures[i] != None:
            training_outputs.append(component.update(value=figures[i], visible=True))
        else:
            training_outputs.append(component.update(visible=False))

    return *training_outputs,

def update_training_history(
        dataset_dropdown: str,
        model_dropdown: str,
        training_results: pd.DataFrame, 
        training_history: pd.DataFrame
    ) -> gr.Dataframe:

    training_results['Dataset'] = dataset_dropdown
    training_results['Model'] = model_dropdown

    merged_training_history = pd.concat(
        [
            training_history, 
            training_results,
        ], 
        ignore_index=True
    )
    merged_training_history = merged_training_history.replace('', pd.NA).dropna(how='all').replace(pd.NA, '')

    merged_training_history.rename_axis(
        "Times", 
        axis=1, 
        inplace=True,
    )

    index_num = None
    if len(merged_training_history) == 1:
        index_num = merged_training_history.index
    else:
        index_num = merged_training_history.index + 1

    merged_training_history["Times"] = index_num
    
    training_history = gr.Dataframe.update(
        value=merged_training_history,
        interactive=True,
    )

    return training_history

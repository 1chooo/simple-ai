# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.1
'''

import gradio as gr
from Refinaid.gui.Information import PageContent
from typing import Any, Tuple

class TrainingComponent:

    def __init__(self, page_content: PageContent) -> None:
        self.page_content = page_content

    def get_training_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown
            ]:
        training_heading = gr.Markdown("## Training")

        return (
            training_heading
        )
    
    def get_picked_dataset_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown, 
                gr.Dataframe,
            ]:
        picked_dataset_header = gr.Markdown(
            "### Data You have picked!!!"
        )
        preprocessing_data_result = gr.Dataframe(
            headers=[
                "Parameters",
                "Value"
            ],
            row_count=(7, "fixed"),
            col_count=(2, "fixed"),
            interactive=False,
        )
        
        return (
            picked_dataset_header, 
            preprocessing_data_result
        )
    
    def get_model_dropdown_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Dropdown
            ]:
        choices =[
            "Decision Tree Classifier", 
            "K Neighbor Classifier",
        ]
        model_dropdown = gr.Dropdown(
            label="Select Model", 
            value="Please select the model",
            choices=choices, 
            interactive=True,
        )

        return (
            model_dropdown
        )
    
    def get_decision_tree_classifer_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown,
                gr.Dropdown,
                gr.Textbox,
                gr.Slider,
                gr.Slider,
                gr.Dropdown,
                gr.Textbox,
            ]:
        decision_tree_classifer_title = gr.Markdown(
            "### Decision Tree Classifier", 
            visible=False,
        )
        decision_tree_classifer_criterion_dropdown = gr.Dropdown(
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
        decision_tree_classifer_max_depth_textbox = gr.Textbox(
            label="Max Depth", 
            value="None", 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_min_samples_split_slider = gr.Slider(
            label="Minimum Samples Split", 
            minimum=2, 
            maximum=20, 
            step=1, 
            value=2, 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_min_samples_leaf_slider = gr.Slider(
            label="Minimum Samples Leaf", 
            minimum=1, 
            maximum=20, 
            step=1, 
            value=1, 
            interactive=True, 
            visible=False,
        )
        decision_tree_classifer_max_features_dropdown = gr.Dropdown(
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
        decision_tree_classifer_max_leaf_nodes_textbox = gr.Textbox(
            label="Max Leaf Nodes", 
            value="None", 
            interactive=True, 
            visible=False,
        )

        return (
            decision_tree_classifer_title, 
            decision_tree_classifer_criterion_dropdown,
            decision_tree_classifer_max_depth_textbox,
            decision_tree_classifer_min_samples_split_slider,
            decision_tree_classifer_min_samples_leaf_slider,
            decision_tree_classifer_max_features_dropdown,
            decision_tree_classifer_max_leaf_nodes_textbox,
        )

    def get_k_neighbors_classifier_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown, gr.Slider, gr.Dropdown, gr.Dropdown
            ]:
        k_neighbors_classifier_title = gr.Markdown(
            "### K Neighbors Classifier", 
            visible=False,
        )
        k_neighbors_classifier_slider = gr.Slider(
            label="N Neighbors", 
            value=5, 
            interactive=True, 
            minimum=1, 
            maximum=20, 
            step=1, 
            visible=False,
        )
        k_neighbors_classifier_weights_dropdown = gr.Dropdown(
            label="Weights", 
            choices=[
                "uniform", 
                "distance"
            ], 
            value="uniform", 
            interactive=True, 
            visible=False,
        )
        k_neighbors_classifier_algorithm_dropdown = gr.Dropdown(
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

        return (
            k_neighbors_classifier_title, 
            k_neighbors_classifier_slider,
            k_neighbors_classifier_weights_dropdown,
            k_neighbors_classifier_algorithm_dropdown,
        )
    
    def get_training_btn_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Button,
            ]:
        train_btn = gr.Button(
            value="Train"
        )

        return (
            train_btn
        )
    
    def get_training_results_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown, 
                gr.Dataframe,
            ]:
        training_results_header = gr.Markdown("## Training Result")
        training_results = gr.Dataframe(
            headers=["Accuracy", "Recall", "Precision", "F1"], 
            interactive=True, 
            row_count=(1, "fixed"), 
            col_count=(4, "fixed")
        )

        return (
            training_results_header,
            training_results
        )
    
    def get_training_results_plot_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Plot, 
                gr.Plot,
                gr.Plot,
            ]:
        train_img1 = gr.Plot(
            interactive=True
        )
        train_img2 = gr.Plot(
            interactive=True
        )
        train_img3 = gr.Plot(
            interactive=True
        )

        return (
            train_img1,
            train_img2,
            train_img3,
        )
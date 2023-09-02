# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/28
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.4
'''

import gradio as gr
from Refinaid.gui.Utils.Listener import background_listener
from Refinaid.gui.Example import get_preprocessing_example
from Refinaid.gui.Information import PageContent
from Refinaid.gui.Dashborad.Header import PageHeader
from Refinaid.gui.Dashborad.Preprocessing import PreprocessingComponent
from typing import Any

def build_ui(*args: Any, **kwargs: Any):

    page_content = PageContent()
    page_header = PageHeader(page_content)
    preprocessing_component = PreprocessingComponent(page_content)
    
    demo = gr.Blocks(
        title='Refinaid',
    )

    with demo:
        our_heading = page_header.get_home_header()

        with gr.Tab("Preprocessing"):
            preprocessing_heading = page_header.get_preprocessing_header()
            with gr.Row():
                with gr.Column():
                    dataset_header, dataset_dropdown = (
                        preprocessing_component.get_dataset_info()
                    )

                    select_mutiple_parameters_header, select_mutiple_parameters_dropdown = (
                        preprocessing_component.get_select_mutiple_parameters_info()
                    )

                    missing_values_handling_header, missing_value_checkbox = (
                        preprocessing_component.get_missing_values_handling_info()
                    )

                    data_scale_header, data_scale_dropdown = (
                        preprocessing_component.get_data_scale_info()
                    )

                    data_split_header, training_slider, validation_slider, testing_slider = (
                        preprocessing_component.get_data_split_info()
                    )

                    submit_dataset_setting_btn = preprocessing_component.get_submit_dataset_setting_btn()
                    
                with gr.Column():
                    preprocessing_visulize_header, preprocessing_visulize_scatter_plot = (
                            preprocessing_component.get_preprocessing_visulize_info()
                        )
                    with gr.Row():
                        x_axis_dropdown, y_axis_dropdown = (
                            preprocessing_component.get_preprocessing_visualize_axis_info()    
                        )
            with gr.Row():
                get_preprocessing_example(
                    dataset_dropdown,
                    select_mutiple_parameters_dropdown,
                    missing_value_checkbox, 
                    data_scale_dropdown, 
                    training_slider, 
                    validation_slider, 
                    testing_slider,
                )

        with gr.Tab("Training"):
            our_heading = gr.Markdown("## Training")
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Data You have picked!!!")
                    preprocessing_data_result = gr.DataFrame(
                        headers=[
                            "Parameters",
                            "Value"
                        ],
                        row_count=(7, "fixed"),
                        col_count=(2, "fixed"),
                        interactive=False,
                    )
                with gr.Column():
                    model_dropdown = gr.Dropdown(
                        label="Select Model", 
                        choices=[
                            "Decision Tree Classifier", 
                            "K Neighbor Classifier",
                        ], 
                        interactive=True
                    )
                    # Decision Tree Classifier
                    decision_tree_classifer_title = gr.Markdown(
                        "### Decision Tree Classifier", 
                        visible=False,
                    )
                    with gr.Row():
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
                    with gr.Row():
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

                    # k_neighbors_classifier
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

            with gr.Row():
                train_btn = gr.Button(
                    value="Train"
                )
            with gr.Row():
                gr.Markdown("## Training Result")
            with gr.Row():
                training_results = gr.DataFrame(
                    headers=["Accuracy", "Recall", "Precision", "F1"], 
                    interactive=True, 
                    row_count=(1, "fixed"), 
                    col_count=(4, "fixed")
                )

            with gr.Row():
                train_img1 = gr.Plot(
                    interactive=True
                )
                train_img2 = gr.Plot(
                    interactive=True
                )
                train_img3 = gr.Plot(
                    interactive=True
                )

        with gr.Tab("Results"):
            our_heading = gr.Markdown("## Results")
            with gr.Row():
                gr.Textbox("hi")
                gr.Textbox("hi")
            with gr.Row():
                gr.Textbox("hello")
                gr.Textbox("hello")

        background_listener(
            dataset_dropdown,
            select_mutiple_parameters_dropdown,
            x_axis_dropdown,
            y_axis_dropdown,
            model_dropdown,
            decision_tree_classifer_title,
            decision_tree_classifer_criterion_dropdown,
            decision_tree_classifer_max_depth_textbox,
            decision_tree_classifer_min_samples_split_slider,
            decision_tree_classifer_min_samples_leaf_slider,
            decision_tree_classifer_max_features_dropdown,
            decision_tree_classifer_max_leaf_nodes_textbox,
            k_neighbors_classifier_title,
            k_neighbors_classifier_slider,
            k_neighbors_classifier_weights_dropdown,
            k_neighbors_classifier_algorithm_dropdown,
            submit_dataset_setting_btn,
            missing_value_checkbox,
            data_scale_dropdown,
            training_slider,
            validation_slider,
            testing_slider,
            preprocessing_data_result,
            train_btn,
            training_results,
            train_img1,
            train_img2,
            train_img3,
        )

    demo.launch(
        # enable_queue=True,
        # share=True, 
        server_name="127.0.0.1", 
        server_port=6006,
        debug=True,
    ) 

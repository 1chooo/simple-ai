# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/28
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.1.0
'''

import os
import gradio as gr
from Refinaid.Utils.Listener import background_listener
from Refinaid.gui.Information import PageContent
from Refinaid.gui.Dashborad.Header import PageHeader
from Refinaid.gui.Dashborad.Preprocessing import PreprocessingComponent
from Refinaid.gui.Dashborad.Training import TrainingComponent
from Refinaid.gui.Dashborad.TrainingHistory import TrainingHistoryComponent
from Refinaid.gui.Example import PreprocessingExample
from typing import Any

def build_ui(*args: Any, **kwargs: Any) -> gr.Blocks:

    page_content = PageContent()
    page_header = PageHeader(page_content)
    preprocessing_component = PreprocessingComponent(page_content)
    training_component = TrainingComponent(page_content)
    training_history_component = TrainingHistoryComponent(page_content)
    preprocessing_example = PreprocessingExample()
    
    demo = gr.Blocks(
        title='Refinaid',

    )
    demo.favicon_path = os.sep+"static"+os.sep+"favicon.png"
    with demo:
        our_heading = page_header.get_home_header()

        with gr.Tab("Data Preprocessing"):
            preprocessing_heading = page_header.get_preprocessing_header()
            with gr.Row():
                with gr.Column():
                    (
                        dataset_header, 
                        selected_dataset_name
                    ) = preprocessing_component.get_dataset_info()

                    (
                        select_mutiple_parameters_header, 
                        select_mutiple_parameters_dropdown,
                    ) = preprocessing_component.get_select_mutiple_parameters_info()

                    (
                        missing_values_handling_header, 
                        missing_value_checkbox
                    ) = preprocessing_component.get_missing_values_handling_info()

                    (
                        data_scale_header, 
                        data_scale_dropdown
                    ) = preprocessing_component.get_data_scale_info()

                    (
                        data_split_header, 
                        training_slider, 
                        validation_slider, 
                        testing_slider
                    ) = preprocessing_component.get_data_split_info()

                    submit_dataset_setting_btn = preprocessing_component.get_submit_dataset_setting_btn()
                    
                with gr.Column():
                    (
                        preprocessing_visulize_header, 
                        preprocessing_visulize_scatter_plot
                    ) = preprocessing_component.get_preprocessing_visulize_info()
                    with gr.Row():
                        (
                            x_axis_dropdown, 
                            y_axis_dropdown
                        ) = preprocessing_component.get_preprocessing_visualize_axis_info()    
            with gr.Row():
                picked_up_data_example = preprocessing_example.get_picked_up_data_example(
                    selected_dataset_name,
                    select_mutiple_parameters_dropdown,
                    missing_value_checkbox, 
                    data_scale_dropdown, 
                    training_slider, 
                    validation_slider, 
                    testing_slider,
                )

        with gr.Tab("Training Model"):
            training_heading = training_component.get_training_info()
            with gr.Row():
                with gr.Column():
                    (
                        picked_dataset_header, 
                        preprocessing_data_result
                    ) = training_component.get_picked_dataset_info()    
                with gr.Column():
                    model_dropdown = training_component.get_model_dropdown_info()
                    # Decision Tree Classifier
                    (
                        decision_tree_classifer_title, 
                        decision_tree_classifer_criterion_dropdown,
                        decision_tree_classifer_max_depth_textbox,
                        decision_tree_classifer_min_samples_split_slider,
                        decision_tree_classifer_min_samples_leaf_slider,
                        decision_tree_classifer_max_features_dropdown,
                        decision_tree_classifer_max_leaf_nodes_textbox,
                    ) = training_component.get_decision_tree_classifer_info()

                    # k_neighbors_classifier
                    (
                        k_neighbors_classifier_title,
                        k_neighbors_classifier_slider,
                        k_neighbors_classifier_weights_dropdown,
                        k_neighbors_classifier_algorithm_dropdown,
                    ) = training_component.get_k_neighbors_classifier_info()

            train_btn = training_component.get_training_btn_info()

            (
                training_results_header,
                training_results
            ) = training_component.get_training_results_info()

            with gr.Row():
                (
                    train_img1,
                    train_img2,
                    train_img3,
                ) = training_component.get_training_results_plot_info()

        with gr.Tab("Training History"):
            (
                history_heading,
                training_history,
            ) = training_history_component.get_history_training_info()

        # with gr.Tab("Teaching"):
        #     teaching_header = gr.Markdown(
        #         "## Teaching"
        #     )

        # with gr.Tab("Demo"):
        #     demo_header = gr.Markdown(
        #         "## Demo"
        #     )

        background_listener(
            selected_dataset_name,
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
            training_history,
            preprocessing_visulize_scatter_plot,
        )

    return demo

    demo.launch(
        # enable_queue=True,
        # share=True, 
        server_name="127.0.0.1", 
        server_port=6006,
        debug=True,
        # inbrowser=True,
        # favicon_path='add_our_favicon_path',
    ) 

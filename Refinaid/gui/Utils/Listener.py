# -*- coding: utf-8 -*-
'''
Create Date: 2023/09/02
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.6
'''

from Refinaid.gui.Utils.Update import update_parameters
from Refinaid.gui.Utils.Update import update_plot_x_parameters
from Refinaid.gui.Utils.Update import update_plot_y_parameters
from Refinaid.gui.Utils.Update import update_model_parameters
from Refinaid.gui.Utils.Update import update_preprocessing_data
from Refinaid.gui.Utils.Update import update_training_results
from Refinaid.gui.Utils.Update import update_training_history
from Refinaid.gui.Utils.Update import update_preprocessing_visualization

def background_listener(
        dataset_dropdown,
        select_multiple_parameters_dropdown,
        x_axis_dropdown,
        y_axis_dropdown,
        model_dropdown,
        decision_tree_classifier_title,
        decision_tree_classifier_criterion_dropdown,
        decision_tree_classifier_max_depth_textbox,
        decision_tree_classifier_min_samples_split_slider,
        decision_tree_classifier_min_samples_leaf_slider,
        decision_tree_classifier_max_features_dropdown,
        decision_tree_classifier_max_leaf_nodes_textbox,
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
        ) -> None:
        dataset_dropdown.change(
            fn=update_parameters,
            inputs=dataset_dropdown,
            outputs=select_multiple_parameters_dropdown,
        )

        dataset_dropdown.change(
            fn=update_plot_x_parameters,
            inputs=dataset_dropdown,
            outputs=x_axis_dropdown,
        )

        dataset_dropdown.change(
            fn=update_plot_y_parameters,
            inputs=dataset_dropdown,
            outputs=y_axis_dropdown,
        )

        model_dropdown.change(
            fn=update_model_parameters,
            inputs=model_dropdown,
            outputs=[
                decision_tree_classifier_title,
                decision_tree_classifier_criterion_dropdown,
                decision_tree_classifier_max_depth_textbox,
                decision_tree_classifier_min_samples_split_slider,
                decision_tree_classifier_min_samples_leaf_slider,
                decision_tree_classifier_max_features_dropdown,
                decision_tree_classifier_max_leaf_nodes_textbox, 
                k_neighbors_classifier_title,
                k_neighbors_classifier_slider,
                k_neighbors_classifier_weights_dropdown,
                k_neighbors_classifier_algorithm_dropdown,
            ]
        )

        submit_dataset_setting_btn.click(
            fn=update_preprocessing_data, 
            inputs=[
                dataset_dropdown, select_multiple_parameters_dropdown, 
                missing_value_checkbox, data_scale_dropdown, 
                training_slider, validation_slider, testing_slider], 
            outputs=[preprocessing_data_result]
        )

        train_btn.click(
            fn=update_training_results,
            inputs=[
                preprocessing_data_result,
                model_dropdown,
                decision_tree_classifier_criterion_dropdown,
                decision_tree_classifier_max_depth_textbox,
                decision_tree_classifier_min_samples_split_slider,
                decision_tree_classifier_min_samples_leaf_slider,
                decision_tree_classifier_max_features_dropdown,
                decision_tree_classifier_max_leaf_nodes_textbox,
                k_neighbors_classifier_slider,
                k_neighbors_classifier_weights_dropdown,
                k_neighbors_classifier_algorithm_dropdown,
            ],
            outputs=[
                training_results,
                train_img1,
                train_img2,
                train_img3,
            ],
        )

        training_results.change(
            fn=update_training_history,
            inputs=[
                training_results,
                training_history,
            ],
            outputs=[
                training_history,
            ],
        )

        x_axis_dropdown.change(
            fn=update_preprocessing_visualization,
            inputs=[
                dataset_dropdown, 
                x_axis_dropdown, 
                y_axis_dropdown,
            ],
            outputs=preprocessing_visulize_scatter_plot
        )

        y_axis_dropdown.change(
            fn=update_preprocessing_visualization,
            inputs=[
                dataset_dropdown, 
                x_axis_dropdown, 
                y_axis_dropdown,
            ],
            outputs=preprocessing_visulize_scatter_plot
        )
        
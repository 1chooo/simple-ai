# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.1
'''

import gradio as gr
from Refinaid.gui.Information import PageContent
from typing import Any

class TrainingComponent:

    data_summary = None
    model_dd = None
    dtc_md = None
    dtc_criterion_dd = None
    dtc_max_depth_tb = None
    dtc_min_samples_split_sldr = None
    dtc_min_samples_leaf_sldr = None
    dtc_max_features_dd = None
    dtc_max_leaf_nodes_tb = None
    knc_md = None
    knc_n_nbr_sldr = None
    knc_weights_dd = None
    knc_althm_dd = None
    train_btn = None
    train_df = None
    train_img1 = None
    train_img2 = None
    train_img3 = None

    def __init__(self, ) -> None:
        pass

    def get_training(self, ):
        page_content = PageContent()
        gr.Markdown(f"{page_content.explanatory_text['training']['title']}\n{page_content.explanatory_text['training']['body']}")
        with gr.Row():
            with gr.Column():
                self.data_summary = gr.Textbox(label="Data Summary", lines=7, interactive=True)
                self.model_dd = gr.Dropdown(label="Select Model", choices=page_content.dropdown_options["models"], interactive=True)
            with gr.Column():
                # decision_tree_classifier
                self.dtc_md = gr.Markdown("### Decision Tree Classifier", interactive=True, visible=False)
                self.dtc_criterion_dd = gr.Dropdown(label="Criterion", 
                                            choices=page_content.dropdown_options["model_parameters"]["decision_tree_classifier"]["criterion"], value="gini", interactive=True, visible=False)
                self.dtc_max_depth_tb = gr.Textbox(label="Max Depth", value="None", interactive=True, visible=False)
                self.dtc_min_samples_split_sldr = gr.Slider(label="Minimum Samples Split", minimum=2, maximum=20, step=1, value=2, interactive=True, visible=False)
                self.dtc_min_samples_leaf_sldr = gr.Slider(label="Minimum Samples Leaf", minimum=1, maximum=20, step=1, value=1, interactive=True, visible=False)
                self.dtc_max_features_dd = gr.Dropdown(label="Max Features", 
                                                choices=page_content.dropdown_options["model_parameters"]["decision_tree_classifier"]["max_features"], value="None", interactive=True, visible=False)
                self.dtc_max_leaf_nodes_tb = gr.Textbox(label="Max Leaf Nodes", value="None", interactive=True, visible=False)
                
                # k_neighbors_classifier
                self.knc_md = gr.Markdown("### K Neighbors Classifier", interactive=True, visible=False)
                self.knc_n_nbr_sldr = gr.Slider(label="N Neighbors", value=5, interactive=True, minimum=1, maximum=20, step=1, visible=False)
                self.knc_weights_dd = gr.Dropdown(label="Weights", choices=page_content.dropdown_options["model_parameters"]["k_neighbors_classifier"]["weights"], value="uniform", interactive=True, visible=False)
                self.knc_althm_dd = gr.Dropdown(label="Algorithm", choices=page_content.dropdown_options["model_parameters"]["k_neighbors_classifier"]["algorithm"], value="auto", interactive=True, visible=False)

        with gr.Row():
            self.train_btn = gr.Button(value="Train")
        with gr.Row():
            gr.Markdown("## Training Result")
        with gr.Row():
            self.train_df = gr.DataFrame(
                headers=["Accuracy", "Recall", "Precision", "F1"], 
                interactive=True, 
                row_count=(1, "fixed"), 
                col_count=(4, "fixed")
            )

        with gr.Row():
            self.train_img1 = gr.Plot(interactive=True)
            self.train_img2 = gr.Plot(interactive=True)
            self.train_img3 = gr.Plot(interactive=True)
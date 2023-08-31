# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.1
'''

import gradio as gr
from Refinaid.gui.Information import PageContent
from Refinaid.gui.Example import get_preprocessing_example
from typing import Any

class PreprocessingComponent:

    dataset_dd = None
    inputs_dd = None
    miss_value_chkbox = None
    data_scale_dd = None
    train_sldr = None
    valid_sldr = None
    test_sldr = None
    submit_set_btn = None
    
    def __init__(self, page_content: PageContent) -> None:
        self.page_content = page_content

    def get_preprocessing(self,):
        gr.Markdown(f"{self.page_content.explanatory_text['preprocess']['title']}\n{self.page_content.explanatory_text['preprocess']['body']}")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Dataset")
                self.dataset_dd = gr.Dropdown(label="Select Dataset", choices=self.page_content.dropdown_options["datasets"], interactive=True)
                gr.Markdown("### Inputs")
                self.inputs_dd = gr.Dropdown(label="Select Mutiple Inputs", choices=self.page_content.dropdown_options["inputs"], multiselect=True)
                # with gr.Accordion("Options"):
                gr.Markdown(f"### Missing Values Handling")
                self.miss_value_chkbox = gr.Radio(label="Select a Method", choices=self.page_content.dropdown_options["miss_value"], interactive=True)
                gr.Markdown(f"### Data Scaling")
                self.data_scale_dd = gr.Radio(choices=self.page_content.dropdown_options["data_scalings"], label="Please select a method", interactive=True)
                gr.Markdown(f"### Data Split\nTotal value should be 100%")
                self.train_sldr = gr.Slider(label="Training Set", minimum=0, maximum=100, step=5)
                self.valid_sldr = gr.Slider(label="Validation Set", minimum=0, maximum=100, step=5)
                self.test_sldr = gr.Slider(label="Testing Set", minimum=0, maximum=100, step=5)
                self.submit_set_btn = gr.Button(value="Submit Setting")
            with gr.Column():
                gr.ScatterPlot(label="Data Visualization")
                with gr.Row():
                    gr.Dropdown(label="X Axis", choices=self.page_content.dropdown_options["datasets"])
                    gr.Dropdown(label="Y Axis", choices=self.page_content.dropdown_options["datasets"])
        with gr.Row():
            get_preprocessing_example(self,)
            
# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.6
'''

import gradio as gr
from Refinaid.gui.Information import PageContent
from typing import Any, Tuple
from Refinaid.Action.Load import get_dataframe

class PreprocessingComponent:
    
    def __init__(self, page_content: PageContent) -> None:
        self.page_content = page_content

    def get_dataset_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown, 
                gr.Dropdown
            ]:

        dataset_header = gr.Markdown("### Dataset")

        dataset_choices = [
            "Titanic", 
            "Diabetes", 
            "House Prices",
        ]

        dataset_dropdown = gr.Dropdown(
            label="Select Dataset", 
            value="Titanic",
            choices=dataset_choices,
            interactive=True,
        )

        return (
            dataset_header, 
            dataset_dropdown
        )
    
    def get_select_mutiple_parameters_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown, 
                gr.Dropdown
            ]:
        select_mutiple_parameters_header = gr.Markdown(
            "### Select Mutiple Parameters"
        )
        select_mutiple_parameters_dropdown = gr.Dropdown(
            label="Select Mutiple Parameters", 
            value=[
                'PassengerId', 'Pclass', 'Sex', 
                'Age', 'SibSp', 'Parch', 'Ticket', 
                'Fare', 'Cabin', 'Embarked'
            ],
            choices=[
                'PassengerId', 'Pclass', 'Sex', 
                'Age', 'SibSp', 'Parch', 'Ticket', 
                'Fare', 'Cabin', 'Embarked'
            ],
            interactive=True,
            multiselect=True,
        )

        return (
            select_mutiple_parameters_header, 
            select_mutiple_parameters_dropdown
        )
    
    def get_missing_values_handling_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown, 
                gr.Radio
            ]:

        missing_values_handling_header = gr.Markdown(
            "### Missing Values Handling"
        )
        missing_value_checkbox = gr.Radio(
            label="Select a Method", 
            value="Drop Nan",
            choices=[
                "Drop Nan", 
                "By Columns"
            ], 
            interactive=True,
        )
        return (
            missing_values_handling_header, 
            missing_value_checkbox
        )

    def get_data_scale_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown, 
                gr.Radio
            ]:
        
        data_scale_header = gr.Markdown(
            "### Data Scaling"
        )
        data_scale_dropdown = gr.Radio(
            value="None",
            choices=[
                "None",
                "Standard",
                "Min-Max"
            ],
            label="Please select a method",
            interactive=True,
        )

        return (
            data_scale_header, 
            data_scale_dropdown
        )
    
    def get_data_split_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown, 
                gr.Slider, 
                gr.Slider, 
                gr.Slider
            ]:
        data_split_header = gr.Markdown(
            "### Data Split\nTotal value should be 100%"
        )

        training_slider = gr.Slider(
            label="Training Set", 
            value=70,
            minimum=0, 
            maximum=100, 
            step=5,
            interactive=True,
        )
        validation_slider = gr.Slider(
            label="Validation Set", 
            value=10,
            minimum=0, 
            maximum=100, 
            step=5,
            interactive=True,
        )
        testing_slider = gr.Slider(
            label="Testing Set", 
            value=20,
            minimum=0, 
            maximum=100, 
            step=5,
            interactive=True,
        )

        return (
            data_split_header, 
            training_slider, 
            validation_slider, 
            testing_slider
        )

    def get_submit_dataset_setting_btn(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Button
            ]:

        submit_dataset_setting_btn = gr.Button(
            value="Submit Setting",
        )

        return (
            submit_dataset_setting_btn
        )
    
    def get_preprocessing_visulize_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown, gr.ScatterPlot
            ]:
        
        preprocessing_visulize_header = gr.Markdown(
            "### Data Visualization in Preprocessing"
        )

        preprocessing_visulize_scatter_plot = gr.ScatterPlot(
            value=get_dataframe("Titanic"),
            label="Data Visualization",
            x="PassengerId",
            y="Pclass",
        )

        return (
            preprocessing_visulize_header, 
            preprocessing_visulize_scatter_plot
        )
    
    def get_preprocessing_visualize_axis_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Dropdown, gr.Dropdown
            ]:
        x_axis_dropdown = gr.Dropdown(
            label="X Axis", 
            value='PassengerId',
            choices=['PassengerId', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'],
            interactive=True,
        )
        y_axis_dropdown = gr.Dropdown(
            label="Y Axis", 
            value='Pclass',
            choices=['PassengerId', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'],
            interactive=True,
        )

        return (
            x_axis_dropdown, 
            y_axis_dropdown
        )
    
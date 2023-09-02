# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.4
'''

import gradio as gr

def get_preprocessing_example(
        dataset_dropdown,
        parameters_dropdown,
        miss_value_checkbox, 
        data_scale_dropdown, 
        training_slider, 
        validation_slider, 
        testing_slider,) -> None:
    gr.Examples(
        [
            [
                "Titanic", 
                ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"], 
                "Drop Nan", 
                "None", 
                70, 
                10, 
                20
            ],
            [
                "Titanic", 
                ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare"], 
                "By Columns", 
                "Standard", 
                70, 
                10, 
                20
            ],
            [
                "Titanic", 
                ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare"], 
                "By Columns", 
                "Min-Max", 
                70, 
                10, 
                20
            ],
        ],
        [
            dataset_dropdown,
            parameters_dropdown,
            miss_value_checkbox, 
            data_scale_dropdown, 
            training_slider, 
            validation_slider, 
            testing_slider,
        ]
    )
    
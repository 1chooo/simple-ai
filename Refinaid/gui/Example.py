# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.2
'''

import gradio as gr

def get_preprocessing_example(preprocessing_component) -> None:
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
            preprocessing_component.dataset_dd, 
            preprocessing_component.inputs_dd, 
            preprocessing_component.miss_value_chkbox, 
            preprocessing_component.data_scale_dd, 
            preprocessing_component.train_sldr, 
            preprocessing_component.valid_sldr, 
            preprocessing_component.test_sldr
        ]
    )
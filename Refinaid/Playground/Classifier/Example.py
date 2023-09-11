# -*- coding: utf-8 -*-
'''
Create Date: 2023/09/11
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.1.4
'''

import gradio as gr

class PreprocessingExample:
    def __init__(self):
        pass

    def get_picked_up_data_example(
            self,
            dataset_dropdown,
            parameters_dropdown,
            miss_value_checkbox, 
            data_scale_dropdown, 
            training_slider, 
            validation_slider, 
            testing_slider,
        ) -> gr.Examples:
        picked_up_data_example = gr.Examples(
            examples=[
                [
                    "Titanic", 
                    [
                        "PassengerId", "Pclass", "Sex", 
                        "Age", "SibSp", "Parch", 
                        "Ticket", "Fare", "Cabin", 
                        "Embarked"
                    ], 
                    "Drop Nan", 
                    "None", 
                    70, 
                    10, 
                    20,
                ],
                [
                    "Titanic", 
                    ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare"], 
                    "By Columns", 
                    "Standard", 
                    70, 
                    10, 
                    20,
                ],
                [
                    "Titanic", 
                    ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare"], 
                    "By Columns", 
                    "Min-Max", 
                    70, 
                    10, 
                    20,
                ],
                [
                    "Diabetes", 
                    ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'], 
                    "By Columns", 
                    "Min-Max", 
                    70, 
                    10, 
                    20,
                ],
            ],
            inputs=[
                dataset_dropdown,
                parameters_dropdown,
                miss_value_checkbox, 
                data_scale_dropdown, 
                training_slider, 
                validation_slider, 
                testing_slider,
            ],
            label='Data Preprocessing Example',
        )

        return picked_up_data_example
    
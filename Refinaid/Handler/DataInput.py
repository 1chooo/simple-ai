'''
Create Date: 2023/09/04
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.8
'''

import gradio as gr

def handle_invalid_data_input(
        dataset: str, parameters: list, 
        miss_value: bool, data_scaling: str, 
        training: int, validation: int, testing: int):
    if dataset == None or dataset == "":
        raise gr.Error("Invalid Dataset")
    if parameters == None or parameters == []:
        raise gr.Error("Invalid Multiple Inputs")
    if data_scaling == None or data_scaling == "":
        raise gr.Error("Invalid Data Scaling")
    if training + validation + testing != 100:
        raise gr.Error("Invalid Data Split")

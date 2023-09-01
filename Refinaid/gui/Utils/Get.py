# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.1
'''

import pandas as pd
import gradio as gr
from Refinaid.Action.ML_configurations import DatasetConfig, DecisionTreeModelConfig, KNNModelConfig

def get_data_setting(dataset:str, inputs:list, miss_value:bool, data_scaling:str, training:int, validation:int, testing:int):
    # print(dataset, inputs, miss_value, data_scaling, training, validation, testing)

    if dataset == None or dataset == "":
        raise gr.Error("Invalid Dataset")
    if inputs == None or inputs == []:
        raise gr.Error("Invalid Multiple Inputs")
    if data_scaling == None or data_scaling == "":
        raise gr.Error("Invalid Data Scaling")
    try:
        if training + validation + testing != 100:
            raise gr.Error("Invalid Data Split")
    except:
        raise gr.Error("Invalid Data Split")

    preprocessing_inputs = [
        "dataset", 
        "inputs", 
        "miss_value", 
        "data_scaling", 
        "training", 
        "validation", 
        "testing"
    ]
    data_summary_dict = {"Parameters": [], "Value": []}
    for parameter in preprocessing_inputs:
        variable_value = locals()[parameter]
        #todo add output column
        #todo change to dataframe
        data_summary_dict["Parameters"].append(parameter)
        data_summary_dict["Value"].append(variable_value)
        
    return pd.DataFrame(data_summary_dict)

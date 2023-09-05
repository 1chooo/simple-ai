# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.8
'''

import pandas as pd
from Refinaid.Handler.DataInput import handle_invalid_data_input

def get_data_setting(
        selected_dataset_name: str, 
        inputs: list, 
        miss_value: bool, 
        data_scaling: str, 
        training: int, 
        validation: int, 
        testing: int) -> pd.DataFrame:

    handle_invalid_data_input(
        selected_dataset_name, 
        inputs, 
        miss_value,
        data_scaling, 
        training, 
        validation, 
        testing
    )

    preprocessing_inputs = [
        "selected_dataset_name", 
        "inputs", 
        "miss_value", 
        "data_scaling", 
        "training", 
        "validation", 
        "testing"
    ]

    data_summary_dict = {
        "Parameters": [], 
        "Value": []
    }

    for parameter in preprocessing_inputs:
        variable_value = locals()[parameter]
        data_summary_dict["Parameters"].append(parameter)
        data_summary_dict["Value"].append(variable_value)
        
    return pd.DataFrame(data_summary_dict)

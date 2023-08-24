# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/24
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

from os.path import join
from os.path import dirname
from os.path import abspath
import pandas as pd

def get_dataframe(dataset_name: str) -> pd.DataFrame:
    try:
        dataset_mapping = {
            'Titanic'     : 'titanic.csv',
            'House Prices': 'house_prices.csv',
            'Diabetes'    : 'diabetes.csv'
        }

        file_path = join(
            dirname(abspath(__file__)),
            '..', 
            '..', 
            'data', 
            dataset_name.lower().replace(' ', '_'),
            dataset_mapping.get(dataset_name, '')
        )

        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(e)
        return None

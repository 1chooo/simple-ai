# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/25
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import sys
from os.path import join
from os.path import dirname
from os.path import abspath

project_root = join(
    dirname(abspath(__file__)),
    '..', 
    '..'
)
sys.path.append(project_root)

import unittest
import pandas as pd
from Refinaid.Action.Load import get_dataframe

class TestGetDataFrame(unittest.TestCase):
    
    def test_get_dataframe_titanic(self,) -> None:
        df = get_dataframe('Titanic')
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_get_dataframe_house_prices(self,) -> None:
        df = get_dataframe('House Prices')
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_get_dataframe_diabetes(self,) -> None:
        df = get_dataframe('Diabetes')
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()

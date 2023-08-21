# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/21
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import unittest
from unittest.mock import MagicMock
import os
import gradio
import sklearn
import seaborn
import pandas as pd
import numpy as np
import matplotlib
import joblib
import json
import datetime
import asyncio
import threading
import pytz

class TestPackages(unittest.TestCase):
    def test_os(self):
        self.assertIsNotNone(os)

    def test_gradio(self):
        self.assertIsNotNone(gradio)

    def test_sklearn(self):
        self.assertIsNotNone(sklearn)

    def test_seaborn(self):
        self.assertIsNotNone(seaborn)

    def test_pandas(self):
        self.assertIsNotNone(pd)

    def test_numpy(self):
        self.assertIsNotNone(np)

    def test_matplotlib(self):
        self.assertIsNotNone(matplotlib)

    def test_joblib(self):
        self.assertIsNotNone(joblib)

    def test_json(self):
        self.assertIsNotNone(json)

    def test_datetime(self):
        self.assertIsNotNone(datetime)

    def test_asyncio(self):
        self.assertIsNotNone(asyncio)

    def test_threading(self):
        self.assertIsNotNone(threading)

    def test_pytz(self):
        self.assertIsNotNone(pytz)

if __name__ == '__main__':
    unittest.main()

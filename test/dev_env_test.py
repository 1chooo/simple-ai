# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/26
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.1.0
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
import boto3
import botocore
from fastapi import FastAPI

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

    def test_boto3(self):
        self.assertIsNotNone(boto3)

    def test_botocore(self):
        self.assertIsNotNone(botocore)

    def test_fastapi(self):
        self.assertIsNotNone(FastAPI)

if __name__ == '__main__':
    unittest.main()

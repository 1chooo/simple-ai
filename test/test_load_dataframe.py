# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/24
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
)
sys.path.append(project_root)

from Refinaid.Action.Load import get_dataframe
import time

start_time = time.time()
df = get_dataframe('Titanic')
print('Time used: ', time.time() - start_time)
print(df.head())
print('Time used: ', time.time() - start_time)
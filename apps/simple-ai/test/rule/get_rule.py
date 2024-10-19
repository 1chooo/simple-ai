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

from Refinaid.Rule.rule import *

get_scripts_head()
get_dataset_naming()
get_dataset_config_example()
get_decision_tree_config_example()

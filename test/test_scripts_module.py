# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/25
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

# To test the function, navigate to the 'test/' directory.
# However, if importing the 'Refinaid' package is unsuccessful,
# you can resolve this issue by adding the following code at the beginning of your test script.
# This code snippet allows you to return to the project root directory.

import sys
from os.path import join
from os.path import dirname
from os.path import abspath

# Back to the project root directory path
project_root = join(
    dirname(abspath(__file__)),
    '..',       # You may need to change the path to follow the 'test/' directory
)
sys.path.append(project_root)

# Now you can import your 'Refinaid' package successfully.
# For example:
# from Refinaid.Action.Load import get_dataframe
# ...
# ...

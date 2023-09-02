# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/21
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

from Refinaid.gui.Launch import build_ui
from typing import Any

def start_simple_ai(*args: Any, **kwargs: Any) -> None:
    '''
    Main function of the app.
    '''
    build_ui()
    
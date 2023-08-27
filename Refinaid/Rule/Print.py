# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/21
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

class AutoPrint:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        print(result)
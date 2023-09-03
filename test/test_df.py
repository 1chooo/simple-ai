# -*- coding: utf-8 -*-
'''
Create Date: 2023/09/03
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.5
'''

import pandas as pd

# 原始的 DataFrame
data = {
    "Accuracy": [0.6216216216216216, 0.8108108108108109, 0.7027027027027027, 0.7567567567567568, 0.6216216216216216],
    "Recall": [0.6153846153846154, 0.8, 0.7916666666666666, 0.88, 0.8333333333333334],
    "Precision": [0.8, 0.96, 0.76, 0.7857142857142857, 0.6666666666666666],
    "F1": [0.6956521739130435, 0.8727272727272728, 0.7755102040816326, 0.830188679245283, 0.7407407407407408],
}

df = pd.DataFrame(data)

# 使用 reset_index() 方法重置索引，將索引列添加到 DataFrame 中
df_with_index = df.reset_index()

# 打印包含索引的 DataFrame
print(df_with_index)

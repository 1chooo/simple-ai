# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/21
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

scripts_head = f"""
Add the header for every script files:
# -*- coding: utf-8 -*-
'''
Create Date: <current_date>
Author: <author>
Version: <next_published_version_num>
'''
"""

dataset_naming = f"""
Dataset naming rule:
| Shown Name   | var Name    |
|--------------|-------------|
| Titanic      | titanic     |
| Diabetes     | diabetes    |
| House Prices | house_price |
"""

params_example = {
    "dataset": "Titanic",
    "select_col": [
        "PassengerId", "Survived", "Pclass", 
        "Sex"        , "Age"     , "SibSp" , 
        "Parch"      , "Ticket"  , "Fare"  , 
        "Cabin"      , "Embarked"
    ],
    "handling_missing_value": True,
    "scaling": "standard",
    "data_split": [0.7, 0.1, 0.2],
}

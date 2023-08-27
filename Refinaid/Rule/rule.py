# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/21
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

from Refinaid.Action.ML_configurations import DatasetConfig
from Refinaid.Action.ML_configurations import DecisionTreeModelConfig
from Refinaid.Rule.Print import AutoPrint
import textwrap
from typing import Any

@AutoPrint
def get_scripts_head(*args: Any, **kwargs: Any) -> str:
    scripts_head = textwrap.dedent(
    """
    Add the header for every script files:

    # -*- coding: utf-8 -*-
    '''
    Create Date: <current_date>
    Author: <author>
    Version: <next_published_version_num>
    '''
    """
    )

    return scripts_head

@AutoPrint
def get_dataset_naming(*args: Any, **kwargs: Any) -> str:
    dataset_naming = textwrap.dedent(
    """
    Dataset naming rule:

    | Shown Name   | var Name    |
    |--------------|-------------|
    | Titanic      | titanic     |
    | Diabetes     | diabetes    |
    | House Prices | house_price |
    """
    )

    return dataset_naming

@AutoPrint
def get_dataset_config_example(*args: Any, **kwargs: Any) -> str:
    config = DatasetConfig(
        dataset="Titanic",
        select_col=[
            "PassengerId", "Survived", "Pclass", 
            "Sex"        , "Age"     , "SibSp" , 
            "Parch"      , "Ticket"  , "Fare"  , 
            "Cabin"      , "Embarked"
        ],
        handling_missing_value=True,
        scaling="standard",
        data_split=[0.7, 0.1, 0.2],
    )
    dataset_config_example = textwrap.dedent(
    f"""
    Database config example:

    Dataset: {config.dataset}
    Selected Columns: {config.select_col}
    Handling Missing Value: {config.handling_missing_value}
    Scaling: {config.scaling}
    Data Split: {config.data_split}
    """
    )

    return dataset_config_example

@AutoPrint
def get_decision_tree_config_example(*args: Any, **kwargs: Any) -> str:
    config = DecisionTreeModelConfig(
        criterion="gini", 
        min_samples_split=2, 
        min_samples_leaf=1,
    )
    decision_tree_config_example = textwrap.dedent(
    f"""
    Decision Tree Model config example:

    Criterion: {config.criterion}
    Min Samples Split: {config.min_samples_split}
    Min samples leaf: {config.min_samples_leaf}
    """
    )

    return decision_tree_config_example

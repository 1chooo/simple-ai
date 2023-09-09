# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/26
Author: @ReeveWu
Version: v0.0.1
'''

from Refinaid.Action.Data import get_training_data
from Refinaid.Action.ML_configurations import DatasetConfig, DecisionTreeModelConfig, KNNModelConfig, SVMModelConfig
from Refinaid.Action.Base import DecisionTreeWrapper, KNNWrapper, SVMWrapper
from typing import Union


def training(dataset_config: DatasetConfig,
             model_config: Union[DecisionTreeModelConfig, KNNModelConfig, SVMModelConfig]):
    X_train, X_test, y_train, y_test = get_training_data(dataset_config)

    if isinstance(model_config, DecisionTreeModelConfig):
        clf = DecisionTreeWrapper(**model_config.__dict__)
        clf.fit(X_train, y_train)
        return clf.analyze(X_test, y_test)

    elif isinstance(model_config, KNNModelConfig):
        clf = KNNWrapper(**model_config.__dict__)
        clf.fit(X_train, y_train)
        return clf.analyze(X_test, y_test)

    elif isinstance(model_config, SVMModelConfig):
        clf = SVMWrapper(**model_config.__dict__)
        clf.fit(X_train, y_train)
        return clf.analyze(X_test, y_test)


# Example
if __name__ == '__main__':
    dataset_config = DatasetConfig(
        dataset="Titanic",
        select_col=["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin",
                    "Embarked"],
        handling_missing_value="by columns",
        scaling="standard",
        data_split=[0.7, 0.1, 0.2]
    )
    model_config = DecisionTreeModelConfig(criterion="gini", min_samples_split=2, min_samples_leaf=1)

    _, indicator = training(dataset_config, model_config)
    accuracy, recall, precision, f1 = indicator
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"F1 Score: {f1:.2f}")

    model_config = SVMModelConfig(C=0.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0)

    _, indicator = training(dataset_config, model_config)
    accuracy, recall, precision, f1 = indicator
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"F1 Score: {f1:.2f}")

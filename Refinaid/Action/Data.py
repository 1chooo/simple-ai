# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/25
Author: @ReeveWu
Version: v0.0.1
'''

import pandas as pd
from Load import get_dataframe
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

object_col = {
    "titanic": [['Name', 'Ticket', 'Cabin', 'SibSp'], ['Sex', 'Embarked']]
}

y_col = {
    "titanic": ["Survived"]
}

def handling_missing_value(df: pd.DataFrame):
    return df.dropna()

def data_generating(df: pd.DataFrame, select_col: list):
    columns_onehot = list(set(select_col) & set(object_col["titanic"][0]))
    columns_label = list(set(select_col) & set(object_col["titanic"][1]))
    columns_remaining = [item for item in select_col if item not in set(columns_onehot + columns_label)]

    onehot_encoder = OneHotEncoder()
    onehot_encoded = onehot_encoder.fit_transform(df[columns_onehot])
    onehot_df = pd.DataFrame(onehot_encoded.toarray(), columns=onehot_encoder.get_feature_names_out(columns_onehot))

    label_encoder = LabelEncoder()
    for col in columns_label:
        df[col] = label_encoder.fit_transform(df[col])

    df = pd.concat([onehot_df, df[columns_label], df[columns_remaining]], axis=1)
    X = df.drop(y_col["titanic"], axis=1)
    y = df[y_col["titanic"]]

    return X, y

def data_scaling(df: pd.DataFrame, method: str):
    if method == "standard":
        standard_scaler = StandardScaler()
        standard_scaled = standard_scaler.fit_transform(df)
        return pd.DataFrame(standard_scaled, columns=df.columns)
    elif method == "min-max":
        minmax_scaler = MinMaxScaler()
        minmax_scaled = minmax_scaler.fit_transform(df)
        return pd.DataFrame(minmax_scaled, columns=df.columns)

def data_split(X: pd.DataFrame, y: pd.DataFrame, split_ratio: list):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_ratio[2])
    return X_train, X_test, y_train, y_test

def get_training_data(dataset: str, parameters: dict):
    df = get_dataframe(dataset)[parameters["select_col"]]
    df = handling_missing_value(df) if parameters["handling_missing_value"] else df
    X, y = data_generating(df, parameters["select_col"])
    X = data_scaling(X, parameters["scaling"]) if parameters["scaling"] else X
    return data_split(X, y, parameters["data_split"])

if __name__ ==  "__main__" :
    # Example
    ex_parameters = {
        "dataset": "Titanic",
        "select_col": ["PassengerId", "Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin",
                       "Embarked"],
        "handling_missing_value": True,
        "scaling": "standard",
        "data_split": [0.7, 0.1, 0.2]
    }
    X_train, X_test, y_train, y_test = get_training_data(ex_parameters["dataset"], ex_parameters)
    print("X_train:", X_train.shape)
    print("X_test:", X_test.shape)
    print("y_train:", y_train.shape)
    print("y_test:", y_test.shape)



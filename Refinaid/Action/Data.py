# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/25
Author: @ReeveWu, @1chooo
Version: v0.0.1
'''

import pandas as pd
from Load import get_dataframe
from ML_configurations import DatasetConfig
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def handling_missing_value(df: pd.DataFrame):
    return df.dropna()

def data_generating(df: pd.DataFrame, parameters: DatasetConfig):
    origin_df = df.copy()

    onehot_encoder = OneHotEncoder(sparse_output=False, drop='first')
    onehot_encoded = onehot_encoder.fit_transform(df[parameters.col_onehot])
    onehot_df = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names_out(parameters.col_onehot))

    result_df = pd.concat([onehot_df], axis=1)

    label_encoder = LabelEncoder()
    for col in parameters.col_label:
        encoded_col = label_encoder.fit_transform(df[col])
        result_df[col] = encoded_col

    df = pd.concat([result_df, origin_df[parameters.col_remaining].reset_index(drop=True)], axis=1)
    X = df.drop(parameters.y_col, axis=1)
    y = df[parameters.y_col].values.ravel()

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

def get_training_data(parameters: DatasetConfig):
    df = get_dataframe(parameters.dataset)[parameters.select_col]
    df = handling_missing_value(df) if parameters.handling_missing_value else df
    X, y = data_generating(df, parameters)
    X = data_scaling(X, parameters.scaling) if parameters.scaling else X
    return data_split(X, y, parameters.data_split)

# Example
if __name__ ==  "__main__" :
    ex_parameters = DatasetConfig(
                                  dataset="Titanic",
                                  select_col=["PassengerId", "Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"],
                                  handling_missing_value=True,
                                  scaling="standard",
                                  data_split=[0.7, 0.1, 0.2]
                                 )
    X_train, X_test, y_train, y_test = get_training_data(ex_parameters)
    print("X_train:", X_train.shape)
    print("X_test:", X_test.shape)
    print("y_train:", y_train.shape)
    print("y_test:", y_test.shape)



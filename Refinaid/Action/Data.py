# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/25
Author: @ReeveWu, @1chooo
Version: v0.0.1
'''

import numpy as np
import pandas as pd
from Load import get_dataframe
from ML_configurations import DatasetConfig
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def handling_missing_value(df: pd.DataFrame, dataset: str):
    def handle_missing_value_titanic(df: pd.DataFrame) -> pd.DataFrame:
        df['Embarked'] = df['Embarked'].fillna('S')
        df['Fare'] = df['Fare'].fillna(df['Fare'].median())
        age_avg = df['Age'].mean()
        age_std = df['Age'].std()
        age_null_count = df['Age'].isnull().sum()
        age_null_random_list = np.random.randint(age_avg - age_std, age_avg + age_std, size=age_null_count)
        df.loc[np.isnan(df['Age']), 'Age'] = age_null_random_list
        df['Age'] = df['Age'].astype(int)
        return df.dropna()

    def handle_missing_value_house_prices(df: pd.DataFrame):
        df['Alley'] = df['Alley'].fillna('No alley access')
        df['BsmtQual'] = df['BsmtQual'].fillna('No Basement')
        df['BsmtCond'] = df['BsmtCond'].fillna('No Basement')
        df['BsmtExposure'] = df['BsmtExposure'].fillna('No Basement')
        df['BsmtFinType1'] = df['BsmtFinType1'].fillna('No Basement')
        df['BsmtFinType2'] = df['BsmtFinType2'].fillna('No Basement')
        df['FireplaceQu'] = df['FireplaceQu'].fillna('FireplaceQu')
        df['GarageType'] = df['GarageType'].fillna('No Garbage')
        df['GarageFinish'] = df['GarageFinish'].fillna('No Garbage')
        df['GarageQual'] = df['GarageQual'].fillna('No Garbage')
        df['GarageCond'] = df['GarageCond'].fillna('No Garbage')
        df['PoolQC'] = df['PoolQC'].fillna('No Pool')
        df['Fence'] = df['Fence'].fillna('No Fence')
        for x in df:
            if any(df[x].isnull()):
                if df[x].dtype == 'object' or df[x].dtype == 'bool':
                    df[x] = df[x].fillna(df[x].mode()[0])
                else:
                    df[x] = df[x].fillna(df[x].mean())
        return df.dropna()


    if dataset == "Titanic":
        return handle_missing_value_titanic(df)
    elif dataset == "House Prices":
        return handle_missing_value_house_prices(df)
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
    df = handling_missing_value(df, parameters.dataset) if parameters.handling_missing_value else df
    X, y = data_generating(df, parameters)
    X = data_scaling(X, parameters.scaling) if parameters.scaling else X
    return data_split(X, y, parameters.data_split)
# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/24
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.1
'''

from os.path import join
from os.path import dirname
from os.path import abspath
import pandas as pd

def get_dataframe(dataset_name: str) -> pd.DataFrame:
    try:
        dataset_mapping = {
            'Titanic'     : 'titanic.csv',
            'House Prices': 'house_prices.csv',
            'Diabetes'    : 'diabetes.csv'
        }

        file_path = join(
            dirname(abspath(__file__)),
            '..', 
            '..', 
            'data', 
            dataset_name.lower().replace(' ', '_'),
            dataset_mapping.get(dataset_name, '')
        )

        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(e)
        return None

def get_dataset_x_columns(dataset: str) -> list:
    dataset_columns = {
        "Titanic": ['PassengerId', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
        "House Prices": ['Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType', 'SaleCondition'],
        "Diabetes": ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    }

    return dataset_columns.get(dataset)

def get_dataset_numeric_columns(dataset: str) -> list:
    dataset_columns = {
        "Titanic": ['PassengerId', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'],
        "House Prices": ['Id', 'MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold'],
        "Diabetes": ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    }

    return dataset_columns.get(dataset)


# Example
import time

if __name__ == '__main__':
    start_time = time.time()
    df = get_dataframe('Titanic')
    print('Time used: ', time.time() - start_time)
    print(df.head())
    print('Time used: ', time.time() - start_time)
    print(get_dataset_x_columns("House Prices"))

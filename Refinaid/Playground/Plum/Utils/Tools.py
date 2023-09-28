# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/24
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.5
'''

import os
import pandas as pd
from glob import glob
from os.path import join
from os.path import dirname
from os.path import abspath
import joblib
import matplotlib.pyplot as plt

def load_data() -> pd.DataFrame:
    all_data_path = join(
        dirname(abspath(__file__)),
        '..', 
        '..', 
        '..',
        '..',
        'data',
        '08_21_rain',
        '*.csv',
    )

    csv_files = glob(all_data_path)
    csv_files.sort()

    dfs_to_merge = []  # List to store DataFrames for merging
    pivot = 2016

    for file in csv_files:
        file_name = os.path.basename(file)
        year = int(file_name.split('-')[1])

        delimiter = '\t' if year >= pivot else ','  # Choose delimiter based on the year

        df = pd.read_csv(file, delimiter=delimiter)
        dfs_to_merge.append(df)

    merged_df = pd.concat(dfs_to_merge, ignore_index=True)  # Concatenate DataFrames

    return merged_df

def output_merged_data() -> None:
    merged_df = load_data()

    output_path = join(
        dirname(abspath(__file__)),
        '..', 
        '..', 
        'data',
        'merged_data',
        '20_years_data.csv',
    )
    merged_df.to_csv(
        output_path, 
        sep=',', 
        index=False, 
        encoding='utf-8-sig'
    )

    print("Merging and transforming multiple CSV files completed.")

def save_model(lr, filename, compress):
    # Get the directory path for the model file
    model_directory = dirname(abspath(filename))
    # Check if the directory exists, create if not
    if not os.path.exists(model_directory):
        os.makedirs(model_directory)

    joblib.dump(lr, filename, compress=compress)

def test_model(lr, StnPres, StnPresMax, StnPresMin, T, Tmax, Tmin, RH, RHmin, WS, WD, WSGust, WDGust):
    result = lr.predict([[StnPres, StnPresMax, StnPresMin, T, Tmax, Tmin, RH, RHmin, WS, WD, WSGust, WDGust]])
    # print(result)
    
    return result

def get_trained_result(accuracy, recall, precision, confusion) -> None:
    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("Confusion Matrix:\n", confusion)

def call_model(StnPres, StnPresMax, StnPresMin, T, Tmax, Tmin, RH, RHmin, WS, WD, WSGust, WDGust):
    model_path = join(
        dirname(abspath(__file__)),
        '..',
        '..',
        'model', 
        'plum_prediction.pkl'
    )
    modelPretrained = joblib.load(model_path)
    result = modelPretrained.predict([[
        StnPres, StnPresMax, StnPresMin, 
        T, Tmax, Tmin, 
        RH, RHmin, WS, 
        WD, WSGust, WDGust
    ]])

    result_probability = modelPretrained.predict_proba([[
        StnPres, StnPresMax, StnPresMin, 
        T, Tmax, Tmin, 
        RH, RHmin, WS, 
        WD, WSGust, WDGust
    ]])

    return result, result_probability

def get_predict_result(StnPres, StnPresMax, StnPresMin, T, Tmax, Tmin, RH, RHmin, WS, WD, WSGust, WDGust):
    result, result_probability = call_model(StnPres, StnPresMax, StnPresMin, T, Tmax, Tmin, RH, RHmin, WS, WD, WSGust, WDGust)

    result = result[0]

    if result == 1.:
        prediction = f'會下雨哦！'
        confidence = f'{result_probability[0, 0]:.10f}'
    else:
        prediction = f'不會下雨哦！'
        confidence = f'{result_probability[0, 0]:.10f}'

    return prediction, confidence

def plot_scatter_subplots(data_frame, x_columns, y_column, figsize=(16, 12)):
    num_columns = len(x_columns)
    num_rows = (num_columns + 3) // 4  # 計算所需的子圖行數

    plt.figure(figsize=figsize)

    for i, x_col in enumerate(x_columns, start=1):
        plt.subplot(num_rows, 4, i)
        plt.scatter(data_frame[x_col], data_frame[y_column])
        plt.xlabel(x_col)
        plt.ylabel(y_column)

    plt.tight_layout()
    plt.show()

# 使用範例
# x_columns = ['StnPres', 'StnPresMax', 'StnPresMin', 'T Max', 'T Min', 'Temperature', 'RH', 'RHMin', 'WS', 'WD', 'WSGust', 'WDGust']
# y_column = 'Precp'
# plot_scatter_subplots(df, x_columns, y_column)
# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/26
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.6
'''

from os.path import join
from os.path import dirname
from os.path import abspath
from Refinaid.Playground.Plum.Data.Data import data_preprocessing
from Refinaid.Playground.Plum.Model.Model import train_logistic_regression
from Refinaid.Playground.Plum.Model.Model import evaluate_model
from Refinaid.Playground.Plum.Utils.Tools import load_data
from Refinaid.Playground.Plum.Utils.Tools import save_model
from Refinaid.Playground.Plum.Utils.Tools import test_model
from Refinaid.Playground.Plum.Utils.Tools import get_trained_result
from Refinaid.Playground.Plum.Utils.Plot import plot_all_evaluation_plots

def train():
    df = data_preprocessing(load_data())

    lr, X_test, y_test, predictions = train_logistic_regression(df)
    accuracy, recall, precision, confusion = evaluate_model(y_test, predictions)

    get_trained_result(accuracy, recall, precision, confusion)

    proba = lr.predict_proba(X_test)[:, 1]

    # plot_all_evaluation_plots(confusion, accuracy, recall, precision, proba)

    # first_test = test_model(lr, 900, 1000, 850, 23, 27, 18, 34, 12, 1, 23, 2, 45)
    # second_test = test_model(lr, 900, 860, 950, 26, 31, 20, 70, 50, 3, 20, 6, 25)

    # print('First:', first_test)
    # print('Second:', second_test)

    output_model_path = join(
        dirname(abspath(__file__)),
        '..',
        '..',
        'model', 
        'plum_prediction.pkl'
    )

    save_model(lr, output_model_path, 3)

    return confusion, accuracy, recall, precision, proba

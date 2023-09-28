# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/26
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.5
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

def train_logistic_regression(df):
    X = df.drop(['Precp'], axis=1)
    y = df['Precp']
    X = X.values # conversion of X into array

    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        test_size=0.3, 
        random_state=67,
    )
    
    lr = LogisticRegression(max_iter=200)
    lr.fit(X_train, y_train)

    predictions = lr.predict(X_test)

    return lr, X_test, y_test, predictions

def evaluate_model(y_test, predictions):
    accuracy = accuracy_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    confusion = pd.DataFrame(
        confusion_matrix(y_test, predictions), 
        columns=['Predict not rain', 'Predict rain'], 
        index=['True not rain', 'True rain']
    )

    return accuracy, recall, precision, confusion

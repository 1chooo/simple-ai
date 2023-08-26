# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/26
Author: @ReeveWu
Version: v0.0.1
'''

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


class DecisionTreeWrapper:
    def __init__(self, **kwargs):
        self.model = DecisionTreeClassifier(**kwargs)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def analyze(self, X_test, y_test):
        y_pred = self.model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        return [accuracy, recall, precision, f1]


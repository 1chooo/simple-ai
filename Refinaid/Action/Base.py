# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/26
Author: @ReeveWu
Version: v0.0.1
'''

import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


class DecisionTreeWrapper:
    def __init__(self, **kwargs):
        self.model = DecisionTreeClassifier(**kwargs)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    @staticmethod
    def _indicator_analyze(y_test, y_pred):
        accuracy = accuracy_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        return [accuracy, recall, precision, f1]

    def _plot_analyze(self, X_test, y_test, y_pred):
        cm = confusion_matrix(y_test, y_pred, labels=self.model.classes_)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=self.model.classes_)
        disp.plot()
        figure_cm = plt.gcf()

        svc_disp = RocCurveDisplay.from_estimator(self.model, X_test, y_test)
        svc_disp.plot()
        figure_roc = plt.gcf()

        tree.plot_tree(self.model)
        figure_tree = plt.gcf()

        return [figure_tree, figure_cm, figure_roc]

    def analyze(self, X_test, y_test):
        y_pred = self.model.predict(X_test)

        return self._plot_analyze(X_test, y_test, y_pred), self._indicator_analyze(y_test, y_pred)








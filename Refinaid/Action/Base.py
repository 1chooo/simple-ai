# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/26
Author: @ReeveWu
Version: v0.0.1
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class ModelWrapper:
    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    @staticmethod
    def _classifier_analyze(y_test, y_pred):
        accuracy = accuracy_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        return [accuracy, recall, precision, f1]

    @staticmethod
    def _regressor_analyze(y_test, y_pred):
        mse = mean_squared_error(y_test, y_pred, squared=False)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        return [mse, mae, r2, None]

class DecisionTreeWrapper(ModelWrapper):
    def __init__(self, **kwargs):
        self.model = DecisionTreeClassifier(**kwargs)

    def fit(self, X, y):
        super().fit(X, y)
    def _plot_analyze(self, X_test, y_test, y_pred):
        tree.plot_tree(self.model)
        figure_tree = plt.gcf()

        cm = confusion_matrix(y_test, y_pred, labels=self.model.classes_)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=self.model.classes_)
        disp.plot()
        figure_cm = plt.gcf()

        svc_disp = RocCurveDisplay.from_estimator(self.model, X_test, y_test)
        svc_disp.plot()
        figure_roc = plt.gcf()
        return [figure_tree, figure_cm, figure_roc]

    def analyze(self, X_test, y_test):
        y_pred = super().predict(X_test)

        return self._plot_analyze(X_test, y_test, y_pred), super()._classifier_analyze(y_test, y_pred)

class KNNWrapper(ModelWrapper):
    def __init__(self, **kwargs):
        self.model = KNeighborsClassifier(**kwargs)

    def fit(self, X, y):
        super().fit(X, y)

    def _plot_analyze(self, X_test, y_test, y_pred):
        cm = confusion_matrix(y_test, y_pred, labels=self.model.classes_)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=self.model.classes_)
        disp.plot()
        figure_cm = plt.gcf()

        svc_disp = RocCurveDisplay.from_estimator(self.model, X_test, y_test)
        svc_disp.plot()
        figure_roc = plt.gcf()

        return [figure_cm, figure_roc, None]

    def analyze(self, X_test, y_test):
        X_test = np.ascontiguousarray(X_test)
        y_pred = super().predict(X_test)
        return self._plot_analyze(X_test, y_test, y_pred), super()._classifier_analyze(y_test, y_pred)


class SVMWrapper(ModelWrapper):
    def __init__(self, **kwargs):
        self.model = SVC(**kwargs)

    def fit(self, X, y):
        super().fit(X, y)

    def _plot_analyze(self, X_test, y_test, y_pred):
        cm = confusion_matrix(y_test, y_pred, labels=self.model.classes_)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=self.model.classes_)
        disp.plot()
        figure_cm = plt.gcf()

        svc_disp = RocCurveDisplay.from_estimator(self.model, X_test, y_test)
        svc_disp.plot()
        figure_roc = plt.gcf()

        return [figure_cm, figure_roc, None]

    def analyze(self, X_test, y_test):
        y_pred = super().predict(X_test)
        return self._plot_analyze(X_test, y_test, y_pred), super()._classifier_analyze(y_test, y_pred)


class LinearRegressionWrapper(ModelWrapper):
    def __init__(self, **kwargs):
        self.model = LinearRegression(**kwargs)

    def fit(self, X, y):
        super().fit(X, y)

    def _plot_analyze(self, X_test, y_test, y_pred):
        return [None, None, None]

    def analyze(self, X_test, y_test):
        y_pred = super().predict(X_test)
        return self._plot_analyze(X_test, y_test, y_pred), super()._regressor_analyze(y_test, y_pred)






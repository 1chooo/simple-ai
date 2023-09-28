# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/25
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.4
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_all_evaluation_plots(confusion_matrix, accuracy, recall, precision, proba):
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")

    plt.subplot(1, 3, 2)
    metrics = pd.DataFrame({
        'Metric': ['Accuracy', 'Recall', 'Precision'],
        'Score': [accuracy, recall, precision]
    })
    sns.barplot(x='Metric', y='Score', data=metrics, palette="viridis")
    plt.title("Model Evaluation Metrics")
    plt.ylim(0, 1)

    plt.subplot(1, 3, 3)
    sns.histplot(proba, bins=30, kde=True)
    plt.title("Predicted Probability Distribution")
    plt.xlabel("Predicted Probability")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

def plot_confusion_matrix(confusion_matrix):
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.show()

def plot_evaluation_metrics(accuracy, recall, precision):
    metrics = pd.DataFrame({
        'Metric': ['Accuracy', 'Recall', 'Precision'],
        'Score': [accuracy, recall, precision]
    })

    plt.figure(figsize=(8, 6))
    sns.barplot(x='Metric', y='Score', data=metrics, palette="viridis")
    plt.title("Model Evaluation Metrics")
    plt.ylim(0, 1)
    plt.show()

def plot_predicted_probability_distribution(proba):
    plt.figure(figsize=(8, 6))
    sns.histplot(proba, bins=30, kde=True)
    plt.title("Predicted Probability Distribution")
    plt.xlabel("Predicted Probability")
    plt.ylabel("Frequency")
    plt.show()
    
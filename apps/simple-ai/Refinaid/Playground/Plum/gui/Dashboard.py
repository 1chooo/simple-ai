# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/27
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.6
'''

import gradio as gr
from typing import Any
import textwrap
from Refinaid.Playground.Plum.Utils.Tools import get_predict_result
from Refinaid.Playground.Plum.gui.code_value import *
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_playground(*args: Any, **kwargs: Any):
    with gr.Row() as playground:
        gr.Markdown(
            textwrap.dedent(
            """
            以下有些天氣數值可以提供給大家使用，歡迎輸入各種數據！！！
            """
            )
        )
        
    with gr.Row() as playground:
        gr.Markdown(f"## 請輸入氣壓資訊")
    with gr.Row():
        current_pressure = gr.Slider(
            800, 1050, value=1000, label="當前氣壓值", info="800.0~1050"
        )
        today_max_pressure = gr.Slider(
            800, 1050, value=1000, label="本日最低氣壓值", info="800.0~1050"
        )
        today_min_pressure = gr.Slider(
            800, 1050, value=1000, label="本日最高氣壓值", info="800.0~1050"
        )

    with gr.Row() as playground:
        gr.Markdown(f"## 請輸入溫度資訊")
    with gr.Row() as playground:
        current_temperature = gr.Slider(
            0, 40, value=20, label="當前溫度值", info="0~40"
        )
        today_max_temperature = gr.Slider(
            0, 40, value=20, label="本日最高溫度值", info="0~40"
        )
        today_min_temperature = gr.Slider(
            0, 40, value=20, label="本日最低溫度值", info="0~40"
        )

    with gr.Row() as playground:
        gr.Markdown(f"## 輸入相對濕度資訊")
    with gr.Row() as playground:
        current_relative_humidity = gr.Slider(
            0, 100, value=20, label="當前相對濕度", info="0~100"
        )
        today_min_relative_humidity = gr.Slider(
            0, 100, value=20, label="本日最低相對濕度", info="0~100"
        )

    with gr.Row() as playground:
        gr.Markdown(f"## 請輸入風資訊")
    with gr.Row() as playground:
        current_wind_speed = gr.Slider(
            0, 10, value=5, label="當前風速", info="0.0~10.0"
        )
        current_wind_direction = gr.Slider(
            1, 360, value=20, label="當前風向", info="1~360"
        )
    with gr.Row() as playground:
        gr.Markdown("## 請輸入陣風資訊")
    with gr.Row() as playground:
        current_gust_wind_speed = gr.Slider(
            0, 10, value=5, label="當前陣風風速", info="0.0~10.0"
        )
        current_gust_wind_direction = gr.Slider(
            1, 360, value=20, label="當前陣風風向", info="1~360"
        )
    with gr.Row() as playground:
        predict_result = gr.Text(
            label="我們評估的結果",
            type="text",
        )
        predict_confidence = gr.Text(
            label="我們評估的系統信心程度",
            type="text",
        )
    with gr.Row() as playground:
        submit_set_btn = gr.Button(value="Submit Setting")
        submit_set_btn.click(
            fn=get_predict_result, 
            inputs=[
                current_pressure, today_max_pressure, today_min_pressure, 
                current_temperature, today_max_temperature, today_min_temperature, 
                current_relative_humidity, today_min_relative_humidity,
                current_wind_speed, current_wind_direction,
                current_gust_wind_speed, current_gust_wind_direction
            ], 
            outputs=[predict_result, predict_confidence]
        )
    gr.Examples(
        [
            [900, 1000, 850, 23, 27, 18, 34, 12, 1, 23, 2, 45],
            [900, 860 , 950, 26, 31, 20, 70, 50, 3, 20, 6, 25],
        ],
        inputs=[
                current_pressure, today_max_pressure, today_min_pressure, 
                current_temperature, today_max_temperature, today_min_temperature, 
                current_relative_humidity, today_min_relative_humidity,
                current_wind_speed, current_wind_direction,
                current_gust_wind_speed, current_gust_wind_direction
        ], 
        outputs=[predict_result, predict_confidence],
        fn=get_predict_result,
        # cache_examples=True,
        )
    return playground

def generate_data_process(*args: Any, **kwargs: Any):
    with gr.Row() as data_process:
        gr.Markdown(f"# 模型訓練資料遇處理過程演變")
    with gr.Row() as data_process:
        gr.Markdown(f"## 拿掉我們不需要的參數")
    with gr.Row() as data_process:
        gr.Code(
        language="python",
        value=data_preprocessing,
        lines=31,
        )
    with gr.Row() as data_process:
        gr.Code(
        language="python",
        value=drop_irrelevant_col,
        lines=3,
        )
    with gr.Row() as data_process:
        gr.Markdown(f"## 補資料集的缺失值")
    with gr.Row() as data_process:
        gr.Code(
        language="python",
        value=replace_missing_value,
        lines=6,
        )
    with gr.Row() as data_process:
        gr.Markdown(f"## 轉為 `float64` 型別")
    with gr.Row() as data_process:
        gr.Code(
        language="python",
        value=convert_float64,
        lines=5,
        )
    with gr.Row() as data_process:
        gr.Markdown(f"我們先處理降雨量，因為有降水及代表有下雨，所以只要大於大於 0 就轉換為 1 ，反之轉換為 0 。")
    with gr.Row() as data_process:
        gr.Code(
        language="python",
        value=binarize_column,
        lines=8,
        )
    with gr.Row() as data_process:
        gr.Markdown(f"## 透過平均方法補資料集的缺失值")
    with gr.Row() as data_process:
        gr.Code(
        language="python",
        value=calculate_observed_averages,
        lines=17,
        )
    with gr.Row() as data_process:
        gr.Code(
        language="python",
        value=fill_missing_values_with_averages,
        lines=8,
        )
    with gr.Row() as data_process:
        gr.Markdown(f"## 透過眾數方法補資料集的缺失值")
    with gr.Row() as data_process:
        gr.Code(
        language="python",
        value=fill_missing_values_with_most_common,
        lines=7,
        )

    return data_process

def generate_trained_process(*args: Any, **kwargs: Any):
    with gr.Row() as trained_process:
        gr.Markdown(f"# 模型訓練處理過程演變")
    with gr.Row() as trained_process:
        gr.Markdown(f"## 透過 `LogisticRegression` 訓練模型")
    with gr.Row() as trained_process:
        gr.Code(
        language="python",
        value=train_logistic_regression,
        lines=16,
        )
    with gr.Row() as trained_process:
        gr.Markdown(f"## 評估我們的模型")
    with gr.Row() as trained_process:
        gr.Code(
        language="python",
        value=evaluate_model,
        lines=11,
        )

    return trained_process

def generate_trained_results(confusion, accuracy, recall, precision, proba):
    def _plot_confusion_matrix(confusion_matrix):
        fig = plt.figure(figsize=(8, 6))
        sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="Blues")
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("True")

        return fig

    def _plot_evaluation_metrics(accuracy, recall, precision):
        metrics = pd.DataFrame({
            'Metric': ['Accuracy', 'Recall', 'Precision'],
            'Score': [accuracy, recall, precision]
        })

        fig = plt.figure(figsize=(8, 6))
        sns.barplot(x='Metric', y='Score', data=metrics, palette="viridis")
        plt.title("Model Evaluation Metrics")
        plt.ylim(0, 1)

        return fig

    def _plot_predicted_probability_distribution(proba):
        fig = plt.figure(figsize=(8, 6))
        sns.histplot(proba, bins=30, kde=True)
        plt.title("Predicted Probability Distribution")
        plt.xlabel("Predicted Probability")
        plt.ylabel("Frequency")

        return fig
    
    with gr.Row() as trained_result:
        gr.Markdown(f"# 模型訓練結果")
    with gr.Row() as trained_result:
        gr.Markdown(f"## 模型訓練視覺化結果")
    with gr.Row() as trained_result:
        gr.Plot(_plot_confusion_matrix(confusion))
        gr.Plot(_plot_evaluation_metrics(accuracy, recall, precision))
        gr.Plot(_plot_predicted_probability_distribution(proba))
    with gr.Row() as trained_result:
        gr.Markdown("""
        ## How to improve?
        * 蒐集更多數據
        * 套用數學迴歸方法，且搭配數學公式，如此還可以篩選掉原先的極端值，\
        保留對機器真正有用的學習。
        """
        )

    return trained_result

def generate_motivation(*args: Any, **kwargs: Any):
    with gr.Row() as motivation:
        gr.Markdown(
        """
        # 我們的專案緣起

        從古自今，天氣一直是影響人類生活和經濟發展的重大因素，\
        因此科學家們不斷在尋找最佳的天氣預測方法，而目前普遍的做法\
        是收集大量的觀測數據（氣溫、濕度、風向和風速、氣壓等等），\
        並利用對大氣物理過程的認識來確定未來某地點大氣層的狀態。\
        但由於大氣過程的複雜，因此現今天氣預測總是存在一定的誤差。

        身為大氣系的學生，我們想試看看利用機器學習來預測天氣，\
        就像鐵達尼號和房價預測，先給程式大量的歷史數據，從中尋找相關性高的變數，\
        讓程式去訓練出最佳的預測模式。

        我們想要預測五、六月的梅雨，所以上中央氣象局的資料庫下載了平鎮測站\
        過去 14 年五月和六月的資料。

        ## 成員介紹
        <table>
            <tr>
                <th>Name</th>
                <th>Student Number</th>
                <th>Divide and Conquer</th>
            </tr>
            <tr>
                <td>林群賀</td>
                <td>109601003</td>
                <td>data, GUI, report</td>
            </tr>
            <tr>
                <td>王采琳</td>
                <td>109601001</td>
                <td>data, code, report</td>
            </tr>
            <tr>
                <td>黃于恩</td>
                <td>109601501</td>
                <td>data, code, report</td>
            </tr>
            <tr>
                <td>林晴葳</td>
                <td>109601508</td>
                <td>data, code, report</td>
            </tr>
            <tr>
                <td>吳彥叡</td>
                <td>109601510</td>
                <td>code, report</td>
            </tr>
        </table>

        ## 一些大氣的背景知識

        <table>
            <tr>
                <th>參數</th>
                <th>概念</th>
                <th>示意圖</th>
            </tr>
            <tr>
                <td>Pressure</td>
                <td>
                    <ul>
                        <li><strong>高氣壓：</strong> 下沉氣流，空氣塊溫度會升高，變乾燥。</li>
                        <li><strong>低氣壓：</strong> 上升氣流，上升冷卻達到飽和狀態，往往會凝結降雨。</li>
                    </ul>
                </td>
                <td><a href="https://github.com/1chooo/rain-prediction/raw/main/imgs/pressure.png"><img src="https://github.com/1chooo/rain-prediction/raw/main/imgs/pressure.png" width="600" alt="Pressure Image"></a></td>
            </tr>
            <tr>
                <td>Temperature</td>
                <td>
                    <ul>
                        <li><strong>地面溫度較低：</strong> 空氣便會冷卻收縮下沉，形成高壓。</li>
                        <li><strong>地面溫度較高：</strong> 空氣就會受熱膨脹上升，形成低壓。</li>
                    </ul>
                </td>
                <td><a href="https://github.com/1chooo/rain-prediction/raw/main/imgs/temperature.png"><img src="https://github.com/1chooo/rain-prediction/raw/main/imgs/temperature.png" width="600" alt="Temperature Image"></a></td>
            </tr>
            <tr>
                <td>Wind</td>
                <td>風對降雨的影響主要是通過把海洋水汽帶到大陸形成降雨，所以迎風岸降雨較多。</td>
                <td><a href="https://github.com/1chooo/rain-prediction/raw/main/imgs/wind.png"><img src="https://github.com/1chooo/rain-prediction/raw/main/imgs/wind.png" width="600" alt="Wind Image"></a></td>
            </tr>
            <tr>
                <td>Humidity</td>
                <td>相對濕度是指單位體積空氣中，實際水蒸氣和飽和水氣含量的百分比。 相對濕度愈高，代表環境愈潮濕，也反映了降雨、有霧的可能性。</td>
                <td><a href="https://github.com/1chooo/rain-prediction/raw/main/imgs/humidity.png"><img src="https://github.com/1chooo/rain-prediction/raw/main/imgs/humidity.png" width="600" alt="Humidity Image"></a></td>
            </tr>
        </table>

        ## Data

        [中央氣象局](https://www.cwb.gov.tw/V8/C/)

        [觀測資料查詢](https://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp)
        """
        )


    return motivation

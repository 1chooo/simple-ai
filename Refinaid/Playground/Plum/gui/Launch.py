# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/24
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.6
'''

import gradio as gr
from typing import Any
import textwrap
from Refinaid.Playground.Plum.gui.Dashboard import generate_playground
from Refinaid.Playground.Plum.gui.Dashboard import generate_data_process
from Refinaid.Playground.Plum.gui.Dashboard import generate_motivation
from Refinaid.Playground.Plum.gui.Dashboard import generate_trained_process
from Refinaid.Playground.Plum.gui.Dashboard import generate_trained_results

def build_plum_playground(confusion, accuracy, recall, precision, proba):
    demo = gr.Blocks(
        title='梅雨還是沒雨？',
    )

    with demo:
        with gr.Row():
            our_heading = heading()
        with gr.Tab("專案簡介"):
            motivation = generate_motivation()
        with gr.Tab("歡迎試玩我們的模型"):
            playground = generate_playground()
        with gr.Tab("試玩歷史紀錄"):
            toy_history = generate_playground()
        with gr.Tab("我們如何訓練模型"):
            with gr.Tab("我們對資料做了哪些努力"):
                data_process = generate_data_process()
            with gr.Tab("建立訓練模型過程"):
                trained_process = generate_trained_process()
            with gr.Tab("模型訓練結果"):
                trained_result = generate_trained_results(confusion, accuracy, recall, precision, proba)

    return demo

def heading(*args: Any, **kwargs: Any) -> gr.Markdown:
    title = '梅雨還是沒雨？'
    descriptions = textwrap.dedent(
    """
    我們是一群大氣系的學生，我們想運用大氣的知識結合機器學習的技術來預測降雨的可能性，\
    即便如今大氣預測降雨的機率已行之有年，不過我們依舊願意嘗試新的方法，\
    就如同其他機器學習的預測像是我們嘗試過的鐵達尼號生存預測、房價預測、借貸評估一般，\
    在已知的數據中，得出更接近真實情況的結果預測。
    """
    )

    our_heading = gr.Markdown(
        f"""\
        # {title}
        {descriptions}
        """
    )

    return our_heading

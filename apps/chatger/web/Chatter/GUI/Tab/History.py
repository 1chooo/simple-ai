# -*- coding: utf-8 -*-
"""
Create Date: 2024/01/07
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
"""

import gradio as gr

from Chatter.GUI.Information import Header as heaader


def init_history_tab():
    with gr.Tab("Submitted History") as history_tab:
        gr.Markdown(heaader.submitted_history_page_header)

        gr.Markdown(heaader.submitted_history_page_header)

    # the next try listener and update in the background

    return history_tab

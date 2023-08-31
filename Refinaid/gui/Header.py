# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.1
'''

import gradio as gr
from Refinaid.gui.Information import PageContent
from typing import Any

def get_header(*args: Any, **kwargs: Any) -> None:
    page_content = PageContent()
    gr.Markdown(f"{page_content.explanatory_text['header']['title']}\n{page_content.explanatory_text['header']['body']}")

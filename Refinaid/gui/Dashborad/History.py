# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.4
'''

import gradio as gr
from Refinaid.gui.Information import PageContent
from typing import Any, Tuple

class HistoryComponent:

    def __init__(self, page_content: PageContent) -> None:
        self.page_content = page_content

    def get_history_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown
            ]:
        history_heading = gr.Markdown("## History")

        return (
            history_heading
        )

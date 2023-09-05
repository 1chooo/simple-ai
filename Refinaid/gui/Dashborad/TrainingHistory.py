# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.7
'''

import gradio as gr
from Refinaid.gui.Information import PageContent
from typing import Any, Tuple

class TrainingHistoryComponent:

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
    
    def get_history_training_info(
            self, *args: Any, **kwargs: Any) -> Tuple[
                gr.Markdown, 
                gr.Dataframe
            ]:
        
        history_heading = self.get_history_info()
        training_history = gr.Dataframe(
            headers=[
                "Times",
                "Dataset",
                "Model",
                "Accuracy", 
                "Recall", 
                "Precision", 
                "F1"
            ], 
            value=None,
            # row_count=(20, "fixed"),
            col_count=(7, "fixed"),
            interactive=False,
        )

        return (
            history_heading,
            training_history,
        )
    
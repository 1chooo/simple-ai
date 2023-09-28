# -*- coding: utf-8 -*-
'''
Create Date: 2023/09/27
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.1.4
'''

import os
import gradio as gr
from Refinaid.Playground.Classifier.Launch import build_classifier_playground
from Refinaid.Playground.Plum.gui.Launch import build_plum_playground

def build_and_mount_playground(app, playground_name, favicon_file, path):

    if playground_name == "classifier":
        playground = build_classifier_playground()
    elif playground_name == "plum":
        from Refinaid.Playground.Plum.Model.Train import train
        confusion, accuracy, recall, precision, proba = train()
        playground = build_plum_playground(confusion, accuracy, recall, precision, proba)
    else:
        raise ValueError("Invalid playground name")
    
    favicon_path = os.sep + "static" + os.sep + favicon_file
    playground.favicon_path = favicon_path
    app = gr.mount_gradio_app(app, playground, path=path)

    return app
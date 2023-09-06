'''
Create Date: 2023/08/25
Author: @VincentLi1216, @1chooo
Email: sunnus.tw@gmail.com
Version: v0.1.1
'''

import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import gradio as gr
from Refinaid.gui.Launch import build_ui
from typing import Any

app = FastAPI()
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request}
    )

demo = build_ui()
app = gr.mount_gradio_app(
    app, demo, path="/gradio"
)

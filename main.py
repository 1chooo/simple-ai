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

PLAYGROUND_PATH = "/gradio"

app = FastAPI()

os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

demo = build_ui()
app = gr.mount_gradio_app(
    app, demo, path=PLAYGROUND_PATH
)

@app.get("/", response_class=HTMLResponse)
async def page_overview(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

@app.get("/project_docs", response_class=HTMLResponse)
async def page_project_docs(request: Request):
    return templates.TemplateResponse(
        "docs.html", {"request": request}
    )

@app.get("/login", response_class=HTMLResponse)
async def page_login(request: Request, ):
    return templates.TemplateResponse(
        f"login.html", {"request": request}
    )

@app.get("/setting", response_class=HTMLResponse)
async def page_setting(request: Request, ):
    return templates.TemplateResponse(
        f"setting.html", {"request": request}
    )

@app.get("/signup", response_class=HTMLResponse)
async def page_signup(request: Request, ):
    return templates.TemplateResponse(
        f"signup.html", {"request": request}
    )

@app.get("/help", response_class=HTMLResponse)
async def page_help(request: Request, ):
    return templates.TemplateResponse(
        f"help.html", {"request": request}
    )

@app.get("/settings", response_class=HTMLResponse)
async def page_settings(request: Request, ):
    return templates.TemplateResponse(
        f"settings.html", {"request": request}
    )

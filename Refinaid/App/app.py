'''
Create Date: 2023/09/08
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.1.1
'''

import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from Refinaid.Playground.Classifier.Launch import build_ui 
from fastapi import Form, Depends, HTTPException
import gradio as gr

PLAYGROUND_PATH = "/gradio"

app = FastAPI(
    title="SIMPLE AI",
    description="Bridging the Gap with AI For Everyone",
    version="0.1.2",
    docs_url="/docs",
)

os.makedirs("static", exist_ok=True)
app.mount(
    "/static", 
    StaticFiles(directory="static"), 
    name="static",
)

templates = Jinja2Templates(directory="templates")

classifier_demo = build_ui()
classifier_demo.favicon_path = (
    os.sep + 
    "static" + 
    os.sep + 
    "favicon.png"
)
app = gr.mount_gradio_app(
    app, classifier_demo, path=PLAYGROUND_PATH,
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

@app.get("/about_us", response_class=HTMLResponse)
async def page_about_us(request: Request, ):
    return templates.TemplateResponse(
        f"about_us.html", {"request": request}
    )

@app.get("/license", response_class=HTMLResponse)
async def page_license(request: Request, ):
    return templates.TemplateResponse(
        f"license.html", {"request": request}
    )

@app.get("/teaching", response_class=HTMLResponse)
async def page_teaching(request: Request, ):
    return templates.TemplateResponse(
        f"teaching.html", {"request": request}
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

@app.get("/orders", response_class=HTMLResponse)
async def page_orders(request: Request, ):
    return templates.TemplateResponse(
        f"orders.html", {"request": request}
    )

@app.get("/playgrounds", response_class=HTMLResponse)
async def page_playgrounds(request: Request, ):
    return templates.TemplateResponse(
        f"playgrounds.html", {"request": request}
    )

@app.get("/favicon.ico")
async def favicon():
    return FileResponse(
        os.getcwd() + classifier_demo.favicon_path
    )

# -*- coding: utf-8 -*-
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
from Refinaid.Utils.BuildPlayground import build_and_mount_playground
from fastapi import Form, Depends, HTTPException

app = FastAPI(
    title="SIMPLE AI",
    description="Bridging the Gap with AI For Everyone",
    version="Refinaid-v0.1.4-beta",
    docs_url="/docs",
)

os.makedirs("static", exist_ok=True)
app.mount(
    "/static", 
    StaticFiles(directory="static"), 
    name="static",
)

templates = Jinja2Templates(
    directory="templates",
)

app = build_and_mount_playground(
    app,
    "plum",
    "favicon.ico",
    "/plum",
)

app = build_and_mount_playground(
    app,
    "classifier",
    "favicon.ico",
    "/classifier",
)

@app.get("/", response_class=HTMLResponse)
async def page_overview(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request},
    )

@app.get("/project_docs", response_class=HTMLResponse)
async def page_project_docs(request: Request):
    return templates.TemplateResponse(
        "docs.html", 
        {"request": request},
    )

@app.get("/login", response_class=HTMLResponse)
async def page_login(request: Request, ):
    return templates.TemplateResponse(
        f"login.html", 
        {"request": request},
    )

@app.get("/setting", response_class=HTMLResponse)
async def page_setting(request: Request, ):
    return templates.TemplateResponse(
        f"setting.html", 
        {"request": request},
    )

@app.get("/signup", response_class=HTMLResponse)
async def page_signup(request: Request, ):
    return templates.TemplateResponse(
        f"signup.html", 
        {"request": request},
    )

@app.get("/about_us", response_class=HTMLResponse)
async def page_about_us(request: Request, ):
    return templates.TemplateResponse(
        f"about_us.html", 
        {"request": request},
    )

@app.get("/license", response_class=HTMLResponse)
async def page_license(request: Request, ):
    return templates.TemplateResponse(
        f"license.html", 
        {"request": request},
    )

@app.get("/teaching", response_class=HTMLResponse)
async def page_teaching(request: Request, ):
    return templates.TemplateResponse(
        f"teaching.html", 
        {"request": request},
    )

@app.get("/help", response_class=HTMLResponse)
async def page_help(request: Request, ):
    return templates.TemplateResponse(
        f"help.html", 
        {"request": request},
    )

@app.get("/settings", response_class=HTMLResponse)
async def page_settings(request: Request, ):
    return templates.TemplateResponse(
        f"settings.html", 
        {"request": request},
    )

@app.get("/orders", response_class=HTMLResponse)
async def page_orders(request: Request, ):
    return templates.TemplateResponse(
        f"orders.html", 
        {"request": request},
    )

@app.get("/playgrounds_guideline", response_class=HTMLResponse)
async def page_playgrounds_introduction(request: Request, ):
    return templates.TemplateResponse(
        f"playgrounds_guideline.html", 
        {"request": request},
    )

@app.get('/favicon.ico', include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse(
        './static/favicon.ico',
    )

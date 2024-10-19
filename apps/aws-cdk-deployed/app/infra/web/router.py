import gradio as gr
from fastapi import FastAPI

from app.adapters.controllers.mock import mock_routes
from app.playground.classifier import build_classifier_demo
from app.playground.chatter_judge import build_chatter_judge_demo


def setup_routers(app: FastAPI) -> None:
    """
    Setup routers for the application

    Args:
        - app (FastAPI): FastAPI instance

    Returns:
        - None
    """
    gr.mount_gradio_app(app, build_classifier_demo(), path="/playground/classifier")
    gr.mount_gradio_app(app, build_chatter_judge_demo(), path="/playground/chtter-judge")
    app.include_router(mock_routes)

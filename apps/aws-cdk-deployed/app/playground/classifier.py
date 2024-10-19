import gradio as gr


def build_classifier_demo() -> gr.Blocks:

    with gr.Blocks(title="Classifier") as demo:

        gr.HTML("<h1 align=center>🗂️ Classifier</h1>")

    return demo

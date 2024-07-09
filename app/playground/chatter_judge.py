import gradio as gr


def build_chatter_judge_demo() -> gr.Blocks:

    with gr.Blocks(title="Chatter Judge") as demo:

        gr.HTML("<h1 align=center>🗂️ Chatter Judge</h1>")

    return demo

import gradio as gr

from Chatter.Database.models import add_question


def init_admin_tab(*args, **kwargs):
    with gr.Blocks() as demo:
        gr.Markdown(
            """<button id=logout style="font-size:30px; font-weight:bold; text-decoration: underline; font-family:Freestyle Script;">Logout</button>"""
        )
        with gr.Row():
            gr.Interface(
                fn=add_question,
                inputs=[
                    gr.Textbox(label="題目名稱"),
                    gr.Textbox(label="題目描述"),
                    gr.Textbox(label="Scope"),
                    gr.Textbox(label="輸入"),
                    gr.Textbox(label="輸出"),
                ],
                outputs="text",
            )

        demo.load(
            _js="""\
document.getElementById("logout").style.height="50px",
document.getElementById("logout").style.width="70px",
document.getElementById("logout").onclick = (() => {
    window.location.href = "http://localhost:5002/auth/logout";
}),
()=>{}""".strip(),
        )

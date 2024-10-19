# -*- coding: utf-8 -*-
"""
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
"""

from typing import Any

import gradio as gr

from Chatter.ChatBot.Chat import respond
from Chatter.GUI.Information import Header as header  # 標題資訊
from Chatter.GUI.Tab import admin as admin_set  # 管理頁面
from Chatter.Judge.Judge import execute_code
from Chatter.Utils.Race_bar import (
    draw_race_bar,
    get_question_list,
    print_all_submissions,
    print_self_submissions,
)
from Chatter.Utils.Update import (
    get_question_description,
    update_question_dropdown_and_description,
    update_scope_dropdown,
)

css_button = """button{
                float: right;
                }"""


def build_chatter_judge(*args: Any, **kwargs: Any) -> gr.Blocks:
    """構建 Chatter Judge 頁面"""

    # demo = gr.Blocks(title="Chatter Judge")  # 頁面標題

    with gr.Blocks(title="Chatter Judge", css=css_button) as demo:
        gr.Markdown(header.ee_judge_header)
        #    scale=4,
        # )  # 顯示 EE Judge 標題(icon)
        # gr.Markdown(header.ee_judge_header)  # 顯示 EE Judge 標題(先以icon替換)
        gr.Markdown(
            """<button id=logout style="font-size:30px; font-weight:bold; text-decoration: underline; font-family:Freestyle Script;">Logout</button>"""
        )  # , scale=4)
        """
        with gr.Row():
            
            gr.Button("Logout", elem_id="logout", interactive=True, variant="primary", scale=1)  # 待進一步實驗"""

        # 初始化提交和歷史記錄頁面
        with gr.Tab("Submit Your Code"):
            gr.Markdown(header.submit_page_header)

            with gr.Row():
                with gr.Column(
                    "Question part",
                    variant="compact",
                ):
                    with gr.Row():
                        selected_scope_name = gr.Dropdown(
                            label="⛳️ Select Homework",
                            interactive=True,
                        )

                        selected_question_name = gr.Dropdown(
                            label="📸 Select Question",
                            interactive=True,
                        )

                    gr.Markdown(header.question_descriptions_header)

                    question_description = gr.Markdown(
                        visible=True,
                    )

                with gr.Column(
                    variant="default",
                ):
                    gr.ChatInterface(
                        fn=respond,
                        additional_inputs=[
                            selected_scope_name,
                            selected_question_name,
                        ],
                        undo_btn=None,
                    )
                    error_advice = gr.Markdown(
                        "如果你的程式碼有錯誤，建議將會顯示在這裡", label="Code advice"
                    )

            with gr.Row(
                variant="compact",
            ):
                with gr.Column():
                    answer_code = gr.Code(
                        label="Write Your code here",
                        language="python",
                        lines=10,
                    )

                    with gr.Row():
                        gr.Button(
                            value="🗑️  Clear",
                            variant="secondary",
                        )
                        submit_code_btn = gr.Button(
                            value="Submit",
                            variant="primary",
                        )

                with gr.Column():
                    judged_result = gr.Markdown("### Results of your submission: ")

                    # chatgpt_suggestion = gr.Markdown(
                    #     f"### Review by ChatGPT: "
                    # )
                    # with gr.Row():
                    #     gr.Plot(
                    #         value=make_plot("scatter_plot"),
                    #         label="Plotttttt",
                    #         scale=4,
                    #         interactive=True,
                    #         # show_actions_button=True,
                    #     )

                    #     gr.Radio(
                    #         scale=1,
                    #         label="Plot type",
                    #         choices=[
                    #             "AC",
                    #             "WA",
                    #             "TLE",
                    #             "MLE",
                    #             "RE",
                    #             "CE",
                    #             "ChatGPT",
                    #         ],
                    #         value="AC",
                    #         interactive=True,
                    #     )

            submit_code_btn.click(
                execute_code,
                inputs=[
                    answer_code,
                    selected_scope_name,
                    selected_question_name,
                ],
                outputs=[judged_result, error_advice],
            )

            selected_question_name.change(
                fn=get_question_description,
                inputs=[
                    selected_scope_name,
                    selected_question_name,
                ],
                outputs=question_description,
            )

            selected_scope_name.change(
                fn=update_question_dropdown_and_description,
                inputs=selected_scope_name,
                outputs=[selected_question_name, question_description],
            )

        with gr.Tab("Submitted History") as history_tab:
            gr.Markdown(header.submitted_history_page_header)
            self_submissions = gr.Dataframe(
                headers=["ID", "Name", "Scope", "Question", "Status", "Time"],
            )

        # 使用 Tab 顯示不同頁面
        with gr.Tab("Race Bar") as race_bar_tab:
            gr.Markdown(header.race_bar_page_header)  # 顯示競賽列頁面標題
            all_submissions = gr.Dataframe(
                headers=["ID", "Name", "Scope", "Question", "Status", "Time"],
            )
            with gr.Row():
                plot_scope_name = gr.Dropdown(
                    label="⛳️ Select Homework", interactive=True, allow_custom_value=True
                )

                plot_question_name = gr.Dropdown(
                    label="📸 Select Question", interactive=True, allow_custom_value=True
                )
            race_bar_plot = gr.Plot()

            plot_scope_name.change(
                fn=get_question_list, inputs=plot_scope_name, outputs=plot_question_name
            )
            plot_question_name.change(
                fn=draw_race_bar,
                inputs=[plot_scope_name, plot_question_name],
                outputs=race_bar_plot,
            )
        # with gr.Tab("Judge Mechanism"):
        #     gr.Markdown(header.judge_mechanism_page_header)  # 顯示評判機制頁面標題
        # with gr.Tab("Judge Developers"):
        #     gr.Markdown(header.judger_developer_page_header)  # 顯示評判開發者頁面標題

        demo.load(
            fn=update_scope_dropdown,
            outputs=selected_scope_name,
            _js="""\
document.getElementById("logout").style.height="50px",
document.getElementById("logout").style.width="70px",
document.getElementById("logout").onclick = (() => {
    window.location.href = "http://localhost:5002/auth/logout";
}),
()=>{}""".strip(),
        )  # 加载 JS 代码处理登录逻辑

        history_tab.select(fn=print_self_submissions, outputs=self_submissions)

        race_bar_tab.select(fn=print_all_submissions, outputs=[all_submissions, plot_scope_name])

    # 暫時禁用身份驗證
    # demo.auth = auth.auth_admin
    # demo.auth_message = 'Welcome to Chatter Judge!!!'

    return demo


def build_admin_management(*args: Any, **kwargs: Any) -> gr.Blocks:
    """構建管理面板頁面"""

    admin = gr.Blocks(title="Chatter Admin", css=css_button)  # 頁面標題

    with admin:
        gr.Markdown(
            """# Admin Panel
Welcome, admin! This is the admin page for Chatter Judge.
WIP"""  # 保持英文
        )  # 顯示管理面板標題和說明
        admin_set.init_admin_tab()

    return admin


css = """h1{
            Color:rgb(255, 0 , 255);
            font-family:Freestyle Script;
            text-align:center;
            font-size:64px;
            }"""

# color無用、size直接帶html、其餘有效


def build_home_page() -> gr.Blocks:
    """構建首頁"""

    with gr.Blocks(title="Chatter Home", css=css) as home:  # 頁面標題
        # FIXME: Is really annoying that the link above will force the user to open a new tab...
        gr.Markdown(
            """# Chatter Home
Welcome! This is the home page for Chatter Judge.
[Judge](/judge/) | [Admin Panel](/admin/)"""  # 保持英文
        )  # 顯示首頁標題和連結

        # 登錄頁面
        with gr.Tab("Login"):
            gr.Markdown(
                """# Login
Welcome! This is the login page for Chatter Judge."""  # 保持英文
            )  # 顯示登錄頁面標題
            with gr.Row(elem_id="login-row"):
                # 用户名和密码输入框
                gr.Textbox(label="Username", elem_id="username", interactive=True)
                gr.Textbox(label="Password", elem_id="password", type="password", interactive=True)
                gr.Button("Login", elem_id="login", interactive=True)  # 登錄按钮

        # 註冊頁面
        with gr.Tab("Register"):
            gr.Markdown(
                """# Register
Welcome! This is the register page for Chatter Judge. (WIP)"""  # 保持英文
            )  # 顯示註冊頁面標題
            with gr.Row(elem_id="register-row"):
                # 用户名和密码输入框
                gr.Textbox(label="Username", elem_id="username", interactive=True)
                gr.Textbox(label="Password", elem_id="password", type="password", interactive=True)
                gr.Button("register", elem_id="register", interactive=True)  # 登錄按钮

        # TODO: Put this ugly js hack into a separate file
        home.load(
            _js="""\
params=new URLSearchParams(window.location.search),
params.get("msg")&&alert(params.get("msg")),
document.getElementById("login").onclick=(()=>{
    const e=document.createElement("form");
    let a=document.createElement("input");
    a.name="username",
    a.value=document.querySelector("#login-row > div > #username > label > textarea").value,
    e.appendChild(a),
    (a=document.createElement("input")).name="password",
    a.value=document.querySelector("#login-row > div > #password > label > input").value,
    e.appendChild(a),
    e.method="POST",
    e.action="/auth/login",
    e.style.display="none",
    document.body.appendChild(e),
    e.submit()
}),
document.getElementById("register").onclick=(()=>{
    const e=document.createElement("form");
    let a=document.createElement("input");
    a.name="username",
    a.value=document.querySelector("#register-row > div > #username > label > textarea").value,
    e.appendChild(a),
    (a=document.createElement("input")).name="password",
    a.value=document.querySelector("#register-row > div > #password > label > input").value,
    e.appendChild(a),
    e.method="POST",
    e.action="/auth/register",
    e.style.display="none",
    document.body.appendChild(e),
    e.submit()
}),
()=>{}""".strip()
        )  # 加载 JS 代码处理登录逻辑

    return home

from enum import Enum

import gradio as gr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from Chatter.Utils.Update import get_self_submissions, get_submissions


# TODO: copy-paste programming here, but i don't have time :p
class AnswerStatus(Enum):
    AC = 0
    WA = 1
    CE = 2
    RE = 3
    TLE = 4


async def print_self_submissions(request: gr.Request) -> gr.Markdown:
    try:
        submissions = await get_self_submissions(
            request.session["user"], 9999, 0
        )  # 示例：获取第1页，每页10条

        # 创建 DataFrame
        df = pd.DataFrame(
            [
                [
                    submission.id,
                    submission.user.username,
                    submission.question.scope.name,
                    submission.question.name,
                    AnswerStatus(submission.status).name,
                    submission.created_at,
                ]
                for submission in submissions
            ],
            columns=["ID", "Name", "Scope", "Question", "Status", "Time"],
        )

        # 如果 DataFrame 长度不为零，则进行时间转换操作
        if not df.empty:
            # 转换日期时间格式
            df["Time"] = pd.to_datetime(df["Time"])

            # 去除毫秒部分，只保留整数秒
            df["Time"] = df["Time"].dt.floor("s")

            # 转换为 UTC+8
            df["Time"] = df["Time"].dt.tz_convert("Asia/Shanghai")

        # 返回 Markdown
        return df

    except Exception as e:
        # 捕获其他异常并引发
        raise e


async def print_all_submissions():
    try:
        # 异步函数需要在事件循环中运行
        submissions = await get_submissions(9999, 0)  # 示例：获取第1页，每页10条

        # 创建 DataFrame
        df = pd.DataFrame(
            [
                [
                    submission.id,
                    submission.user.username,
                    submission.question.scope.name,
                    submission.question.name,
                    AnswerStatus(submission.status).name,
                    submission.created_at,
                ]
                for submission in submissions
            ],
            columns=["ID", "Name", "Scope", "Question", "Status", "Time"],
        )

        # 如果 DataFrame 长度不为零，则进行时间转换操作
        if not df.empty:
            # 转换日期时间格式
            df["Time"] = pd.to_datetime(df["Time"])

            # 去除毫秒部分，只保留整数秒
            df["Time"] = df["Time"].dt.floor("s")

            # 转换为 UTC+8
            df["Time"] = df["Time"].dt.tz_convert("Asia/Shanghai")

        # 傳出獨立的作業名
        unique_scopes = list(df["Scope"].unique())
        dropdown = gr.Dropdown(
            label="⛳️ Select Homework",
            choices=unique_scopes,
            interactive=True,
        )
        return df, dropdown

    except Exception as e:
        # 捕获其他异常并引发
        raise e


async def get_question_list(selected_scope):
    try:
        # 异步函数需要在事件循环中运行
        submissions = await get_submissions(9999, 0)  # 示例：获取第1页，每页10条

        # 创建 DataFrame
        df = pd.DataFrame(
            [
                [
                    submission.id,
                    submission.user.username,
                    submission.question.scope.name,
                    submission.question.name,
                    submission.status,
                    submission.created_at,
                ]
                for submission in submissions
            ],
            columns=["ID", "Name", "Scope", "Question", "Status", "Time"],
        )

        # 如果 DataFrame 长度不为零，则进行时间转换操作
        if not df.empty:
            # 转换日期时间格式
            df["Time"] = pd.to_datetime(df["Time"])

            # 去除毫秒部分，只保留整数秒
            df["Time"] = df["Time"].dt.floor("s")

            # 转换为 UTC+8
            df["Time"] = df["Time"].dt.tz_convert("Asia/Shanghai")

        # 傳出獨立的作業名
        df = df[df["Scope"] == selected_scope]
        unique_question = list(df["Question"].unique())
        dropdown = gr.Dropdown(
            label="📸 Select Question",
            interactive=True,
            choices=unique_question,
            allow_custom_value=True,
        )
        return dropdown

    except Exception as e:
        raise e

        # 捕获其他异常并引


async def draw_race_bar(selected_scope, selected_question):
    try:
        submissions = await get_submissions(9999, 0)
        df = pd.DataFrame(
            [
                [
                    submission.id,
                    submission.user.username,
                    submission.question.scope.name,
                    submission.question.name,
                    submission.status,
                    submission.created_at,
                ]
                for submission in submissions
            ],
            columns=["ID", "Name", "Scope", "Question", "Status", "Time"],
        )

        if not df.empty:
            df["Time"] = pd.to_datetime(df["Time"])
            df["Time"] = df["Time"].dt.floor("s")
            df["Time"] = df["Time"].dt.tz_convert("Asia/Shanghai")
            df = df[
                (df["Scope"] == selected_scope)
                & (df["Question"] == selected_question)
                & (df["Status"] == 0)
            ]
            df = df.groupby("Name")["Time"].min().reset_index()
            df = df.sort_values(by="Time", ascending=False)

            fig, ax = plt.subplots(figsize=(10, 6))  # 创建图和轴

            # 获取所有 bar 的数量
            num_bars = len(df)

            # 创建颜色渐变列表
            cmap = plt.cm.get_cmap("coolwarm")  # 选择颜色映射，例如 'coolwarm'
            colors = cmap(np.linspace(0, 1, num_bars))  # 生成渐变颜色
            ax.barh(df["Name"], df["Time"], color=colors)

            ax.set_xlabel("Submission Time")  # 设置 X 轴标签
            ax.set_ylabel("Name")  # 设置 Y 轴标签
            ax.set_title("Submission Times of Students")  # 设置标题

            ax.grid(True, axis="x")  # 在 X 轴上添加网格
            ax.tick_params(axis="x", rotation=45)  # 旋转 X 轴刻度标签

            min_time = df["Time"].min()
            max_time = df["Time"].max()
            time_range = (max_time - min_time).total_seconds() / 60
            time_interval = time_range / 7

            extended_min_time = min_time - (max_time - min_time) / 10
            extended_max_time = max_time + (max_time - min_time) / 10
            ax.set_xlim(left=extended_min_time, right=extended_max_time)

            selected_times = [min_time + pd.Timedelta(minutes=time_interval * i) for i in range(7)]
            ax.set_xticks(selected_times)
            ax.set_xticklabels([t.strftime("%m/%d %H:%M:%S") for t in selected_times], rotation=45)

            mid_x = -0.092
            ax.annotate(
                "Latest Commit",
                xy=(mid_x, 0.52),
                xycoords="axes fraction",
                xytext=(-0.1, 0.05),
                arrowprops=dict(arrowstyle="<-", color="black", lw=2),
                rotation=90,
            )

            ax.annotate(
                "Earliest Commit",
                xy=(mid_x, 0.49),
                xycoords="axes fraction",
                xytext=(-0.1, 0.80),
                arrowprops=dict(arrowstyle="<-", color="black", lw=2),
                rotation=90,
            )

            plt.tight_layout()

            return fig
    except:
        fig, ax = plt.subplots(figsize=(6, 3))

        # 移除坐标轴
        ax.axis('off')

        # 添加文字
        ax.text(0.5, 0.5, 'No One Success', 
                fontsize=20, ha='center', va='center', color='red')
        
        return fig
        

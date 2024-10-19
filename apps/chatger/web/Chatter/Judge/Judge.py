# -*- coding: utf-8 -*-
"""
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
"""

import os
from enum import Enum

import gradio as gr
import httpx
from sqlalchemy import select

from Chatter.ChatBot.finetune import code_advice
from Chatter.ChatBot.structure_prompt import structured_prompt
from Chatter.Database.connection import get_db
from Chatter.Database.models import InputAndOutput, Question, Submission

TIMEOUT = 15
SANDBOX_URL = os.environ["SANDBOX_URL"]


class RunStatus(str, Enum):
    SUCCESS = "success"
    COMPILE_ERROR = "compile_error"
    RUNTIME_ERROR = "runtime_error"
    TIME_LIMIT_EXCEED = "time_limit_exceed"


class AnswerStatus(Enum):
    AC = 0
    WA = 1
    CE = 2
    RE = 3
    TLE = 4


async def save_submission(
    user_id: int, code: str, question_name: str, status: int, output: bytes, ai_suggestion: str
) -> None:
    async for session in get_db():
        stmt = select(Question).where(Question.name == question_name)
        question = (await session.execute(stmt)).scalars().first()
        if not question:
            raise ValueError("Question not found")

        submission = Submission(
            user_id=user_id,
            question_id=question.id,
            code=code,
            status=status,
            output=output,
            ai_suggestion=ai_suggestion,
        )
        session.add(submission)
        await session.commit()


async def execute_code(request: gr.Request, code: str, scope: str, question_name: str):
    if not code:
        raise ValueError("Code is empty")
    if len(code) > 5000:
        # XXX: Is this a good limit?
        raise ValueError("Code is too long")
    async for session in get_db():
        stmt = (
            select(Question)
            .where(Question.name == question_name)
            .where(Question.scope.has(name=scope))
        )
        question = (await session.execute(stmt)).scalars().first()
        if not question:
            raise ValueError("Question not found")

        # TODO: Handle multiple input and output
        input_and_output: InputAndOutput = question.input_and_outputs[0]

    with httpx.Client(base_url=SANDBOX_URL) as client:
        try:
            r = client.post(
                "/",
                json={
                    "code": code,
                    "input": input_and_output.input,
                },
                timeout=TIMEOUT,
            )
        except httpx.TimeoutException:
            raise ValueError("Backend timeout")
        if r.status_code != 200:
            raise ValueError("Backend error")

        result = r.json()
        # print(result)
        run_status = RunStatus(result["status"])
        output = bytes.fromhex(result["output"]).strip()

        answer_status = None
        expected_output = input_and_output.output.strip().encode()

        if run_status == RunStatus.SUCCESS:
            answer_status = AnswerStatus.AC if output == expected_output else AnswerStatus.WA
        elif run_status == RunStatus.COMPILE_ERROR:
            answer_status = AnswerStatus.CE
        elif run_status == RunStatus.RUNTIME_ERROR:
            answer_status = AnswerStatus.RE
        elif run_status == RunStatus.TIME_LIMIT_EXCEED:
            answer_status = AnswerStatus.TLE

        assert answer_status is not None, "Unknown answer status"

        ai_suggestion = None
        if answer_status != AnswerStatus.AC:
            # TODO: Handle the case that output is not a valid utf-8 string
            prompt = f"Code:\n{code}\n\n"
            prompt += f"Output:\n{output.decode()}\n\n"
            if answer_status == AnswerStatus.WA:
                prompt += f"Expected output:\n{expected_output.decode()}\n\n"
            prompt += f"Run status:\n{result['status']}\n\n"
            prompt += f"Answer status:\n{answer_status.name}"
            print(prompt)
            # try:  #暫時取消在小樣本沒有明顯幫助
            #     ai_suggestion = await code_advice(prompt)
            # except:
            ai_suggestion = await structured_prompt(prompt)

        await save_submission(
            user_id=request.session["user"],
            code=code,
            question_name=question_name,
            status=answer_status.value,
            output=output,
            ai_suggestion=ai_suggestion,
        )

        # TODO: We need to escape the msg
        result = f"### Your code result\n{answer_status.name}\n\n"
        if run_status in (RunStatus.COMPILE_ERROR, RunStatus.RUNTIME_ERROR):
            result += "### Your Error\n"
            result += f"```python-traceback\n{output.decode()}\n```"

        return result, ai_suggestion

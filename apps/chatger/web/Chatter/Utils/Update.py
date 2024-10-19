# -*- coding: utf-8 -*-
"""
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
"""

import gradio as gr
from sqlalchemy import select

from Chatter.Database.connection import get_db
from Chatter.Database.models import Question, Scope, Submission


async def get_question_description(scope_name: str, question_name: str) -> gr.Markdown:
    description = None

    async for session in get_db():
        # select where question have same name and scope name
        stmt = (
            select(Question)
            .where(Question.name == question_name)
            .where(Question.scope.has(name=scope_name))
        )
        question: Question | None = (await session.execute(stmt)).scalars().first()
        if question:
            description = question.description
            if description:
                return gr.Markdown(description)

    return gr.Markdown("No description found for this question.")


async def update_scope_dropdown() -> gr.Dropdown:
    async for session in get_db():
        stmt = select(Scope)
        scopes = (await session.execute(stmt)).scalars().all()
        print(scopes)
        return gr.Dropdown(
            label="⛳️ Select Homework",
            choices=[s.name for s in scopes],
            interactive=True,
        )


async def update_question_dropdown_and_description(scope_name: str) -> gr.Dropdown:
    if not scope_name:
        raise ValueError("scope_name is required")
    print(scope_name)
    async for session in get_db():
        stmt = select(Question).where(Question.scope.has(name=scope_name))
        questions = (await session.execute(stmt)).scalars().all()
        print(questions)
        first_question = questions[0] if questions else None
        first_description = None
        if first_question:
            first_description = first_question.description
        return gr.Dropdown(
            label="📸 Select Question",
            value=questions[0].name if questions else None,
            choices=[q.name for q in questions],
            interactive=True,
        ), gr.Markdown(first_description or "No question found")


async def get_submissions(page_size: int, page_number: int) -> list[Submission]:
    async for session in get_db():
        stmt = (
            select(Submission)
            .order_by(Submission.created_at.desc())
            .offset(page_size * page_number)
            .limit(page_size)
        )
        return (await session.execute(stmt)).scalars().all()


async def get_self_submissions(user_id: int, page_size: int, page_number: int) -> list[Submission]:
    async for session in get_db():
        stmt = (
            select(Submission)
            .where(Submission.user_id == user_id)
            .order_by(Submission.created_at.desc())
            .offset(page_size * page_number)
            .limit(page_size)
        )
        return (await session.execute(stmt)).scalars().all()

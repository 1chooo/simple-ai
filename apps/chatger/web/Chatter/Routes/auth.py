from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from Chatter.Database.connection import get_db
from Chatter.Database.models import User
from Chatter.Utils.Auth import get_password_hash, verify_password
from Chatter.Utils.Build import ADMIN_PATH, JUDGE_PATH

__all__ = ["router"]

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(
    username: Annotated[str, Form()],  # 表單用户名
    password: Annotated[str, Form()],  # 表單密碼
    request: Request,  # 請求對象
    db_session: AsyncSession = Depends(get_db),  # DB session
) -> RedirectResponse:
    stmt = select(User).where(User.username == username)
    user = (await db_session.execute(stmt)).scalars().first()
    if user and verify_password(password, user.password):
        request.session["user"] = user.id
        request.session["is_admin"] = username == "admin"
        if username == "admin":
            return RedirectResponse(url=ADMIN_PATH, status_code=status.HTTP_303_SEE_OTHER)
        return RedirectResponse(url=JUDGE_PATH, status_code=status.HTTP_303_SEE_OTHER)
    return RedirectResponse(
        url="/?msg=Invalid username or password", status_code=status.HTTP_303_SEE_OTHER
    )


@router.post("/register")
async def register(
    username: Annotated[str, Form()],  # 表單用户名
    password: Annotated[str, Form()],  # 表單密碼
    db_session: AsyncSession = Depends(get_db),  # DB session
) -> RedirectResponse:
    stmt = select(User).where(User.username == username)
    user = (await db_session.execute(stmt)).scalars().first()
    if user:
        return RedirectResponse(
            url="/?msg=Username already exists", status_code=status.HTTP_303_SEE_OTHER
        )
    user = User(username=username, password=get_password_hash(password))
    db_session.add(user)
    await db_session.commit()
    return RedirectResponse(
        url="/?msg=Registered successfully", status_code=status.HTTP_303_SEE_OTHER
    )


# 登出路由
@router.get("/logout")
async def logout(request: Request) -> RedirectResponse:
    request.session.clear()  # 清除 Session 數據
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)  # 重定向到首頁

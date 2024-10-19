# # -*- coding: utf-8 -*-
# """
# Create Date: 2023/10/18
# Author: @1chooo (Hugo ChunHo Lin)
# Version: v0.0.1
# """
import os

import google.generativeai as genai
from Chatter.ChatBot.model_scheduling import schdule
# 從環境變數讀取 API 金鑰
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY 環境變數未設置")


async def respond(
    message,
    chat_history,
    *args,
    **kwargs,
):
    genai.configure(api_key=API_KEY)

    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]
    prompt = []

    # 模型回應函式 (model_response)
    def model_response(text):
        data = {
            "role": "model",  # 指定角色為模型 (model)
            "parts": [{"text": f"{text}"}],  # 文字內容包含在 "text" 欄位
        }
        return data

    # 使用者輸入函式 (user_word)
    def user_word(text):
        data = {
            "role": "user",  # 指定角色為使用者 (user)
            "parts": [{"text": f"{text}"}],  # 文字內容包含在 "text" 欄位
        }
        return data

    # 對話歷史初始化
    def init_dialog(sentence):
        for i in sentence:
            user_input = user_word(i[0])
            model_output = model_response(i[1])
            prompt.append(user_input)
            prompt.append(model_output)

    init_dialog(chat_history)
    
    question_type = await schdule(message)
    user_input = user_word(message)
    prompt.append(user_input)

    print(question_type)
    try:
        if question_type == 'hard':  # 複雜問題使用複雜模型
            print("1.5pro")
            model = genai.GenerativeModel(
                model_name="gemini-1.5-pro",
                generation_config=generation_config,
                safety_settings=safety_settings,
            )
        elif question_type == 'easy':
            print("1.5flash")
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config=generation_config,
                safety_settings=safety_settings,
            )
        else:
            print("1.0pro")
            model = genai.GenerativeModel(
                model_name="gemini-1.0-pro",
                generation_config=generation_config,
                safety_settings=safety_settings,
            )
        response = model.generate_content(prompt)
    except:
        print("exception 1.0pro")
        model = genai.GenerativeModel(
                model_name="gemini-1.0-pro",
                generation_config=generation_config,
                safety_settings=safety_settings,
            )
        response = model.generate_content(prompt)


    model_output = model_response(response.text)
    prompt.append(model_output)

    return response.text

import google.generativeai as genai

from Chatter.ChatBot.load_creds import load_creds


async def code_advice(message):
    creds = load_creds()

    genai.configure(credentials=creds)

    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]
    prompt_parts = [
        "請回答錯誤類別",
        "input: " + message,
        "output: ",
    ]
    model = genai.GenerativeModel(
        model_name="tunedModels/code-error-55a8dpf0zb5b",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    response = model.generate_content(prompt_parts)
    print(prompt_parts, response)
    return response.text

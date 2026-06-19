from ai_engine import ask_ai
import os

def generate_app(task):

    prompt = f"""
你是一个Kivy开发者，请生成一个完整Android App：

需求：{task}

要求：
- 必须是Kivy代码
- 必须包含main.py
- 必须可运行
- 不要解释，只输出代码
"""

    code = ask_ai(prompt)

    with open("main.py", "w") as f:
        f.write(code)

    return "APP生成完成"

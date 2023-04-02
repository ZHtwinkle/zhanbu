from flask import Flask, render_template, request
import openai

# 加载环境变量，获取OpenAI API密钥
openai.api_key = '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'
# 设置占卜的模型ID和引擎参数
model_id = "tarot"
engine = "davinci"

def fortune_telling_post():
    zodiac = "处女座"
    age = ""
    question = request.form['question']

    # 根据用户提出的问题，调用OpenAI API获取回答
    prompt = f"{zodiac}座，{age}岁，问：{question}"
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 从API的回答结果中提取生成的文本并返回给用户
    answer = response.choices[0].text.strip()


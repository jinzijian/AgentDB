import configparser
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.llms import OpenAI
from langchain.schema import HumanMessage

# 创建配置解析器
config = configparser.ConfigParser()

# 读取配置文件
config.read('./config/config.ini')

def call_gpt4(config, prompt, model_name="gpt-4-1106-preview", temperature=0.1, max_tokens=2000):
    api_key = config['openai']['api_key']
    chat_model = ChatOpenAI(model=model_name, openai_api_key=api_key, temperature=temperature,max_tokens=max_tokens)
    return chat_model.predict(prompt)

def main():
    # 设置测试参数
    # 创建配置解析器
    config = configparser.ConfigParser()

    # 读取配置文件
    config.read('./config/config.ini')
    model_name = "gpt-4-1106-preview"
    prompt = "请解释机器学习是什么。"

    # 调用函数
    try:
        response_text = call_gpt4(config, prompt)
        print(response_text)
    except AssertionError as e:
        print(f"测试失败：{e}")
    except Exception as e:
        # 捕获其他可能的异常
        print(f"测试时出现异常：{e}")

if __name__ == '__main__':
    main()
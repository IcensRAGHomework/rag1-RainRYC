import json
import traceback

from model_configurations import get_model_configuration

from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate


gpt_chat_version = 'gpt-4o'
gpt_config = get_model_configuration(gpt_chat_version)

holidayJsonFormat = '{{"Result": [{{"date": "yyyy-MM-dd", "name": "節日名稱"}}, {{"date": "yyyy-MM-dd", "name": "節日名稱"}}]}}'

def generate_hw01(question):
    llm = AzureChatOpenAI(
            model=gpt_config['model_name'],
            deployment_name=gpt_config['deployment_name'],
            openai_api_key=gpt_config['api_key'],
            openai_api_version=gpt_config['api_version'],
            azure_endpoint=gpt_config['api_base'],
            temperature=gpt_config['temperature']
    )
    promptTemplate = ChatPromptTemplate.from_messages([
        ('system', '你是一位專門回答在特定國家的某個月份有哪些節假日的專家'),
        ('system', f'回答的所有節日，並用繁體中文回答節日名稱，答案請用此 JSON 格式呈現:{holidayJsonFormat}'),
        ('human', '{input}')
    ])
    response = llm.invoke(promptTemplate.format_prompt(input=question).to_messages())
    return json.dumps(JsonOutputParser().invoke(response),
            indent=4,
            ensure_ascii=False)
    
def generate_hw02(question):
    pass
    
def generate_hw03(question2, question3):
    pass
    
def generate_hw04(question):
    pass
    
def demo(question):
    llm = AzureChatOpenAI(
            model=gpt_config['model_name'],
            deployment_name=gpt_config['deployment_name'],
            openai_api_key=gpt_config['api_key'],
            openai_api_version=gpt_config['api_version'],
            azure_endpoint=gpt_config['api_base'],
            temperature=gpt_config['temperature']
    )
    message = HumanMessage(
            content=[
                {"type": "text", "text": question},
            ]
    )
    response = llm.invoke([message])
    
    return response

#print(generate_hw01("2025年台灣1月紀念日有哪些？"))

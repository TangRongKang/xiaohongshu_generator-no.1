#避免过度的文字与代码在一起，分为另外一个文件
from prompt_template import system_template_text,user_template_text
#导入ChatOpenAI模型
from langchain_openai import ChatOpenAI
#导入langchain中的Pydantic输出解析器
from langchain.output_parsers import PydanticOutputParser
#从langchain 中导入ChatPromptTemplate
from langchain.prompts import ChatPromptTemplate
#导入对数据类型的定义
from xiaohongshu_model import Xiaohongshu

def generate_xiaohongshu(theme,open_ai_key):
    #提示模板
    prompt = ChatPromptTemplate.from_messages([
        ("system",system_template_text),
        ("user",user_template_text)
    ])
    #创建模型;使用课程密钥需要额外提供openai_api_base参数
    model = ChatOpenAI(model= "gpt-3.5-turbo",api_key = open_ai_key,openai_api_base="https://api.aigc369.com/v1" )
    #需要定义解析AI返回结果的输出解析器；获取JSON格式输出可以用PydanticOutputParser
    #输出解析器：定义理想解析出的数据类型，新建一个专门放数据模式的文件
    output_parser = PydanticOutputParser(pydantic_object= Xiaohongshu)
    #将提示模板prompt\模型Model\输出解析器output_parser链起来
    chain = prompt | model | output_parser
    #触发这个链调用invoke方法，参数就是提示模板里变量的键值对
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme":theme
    })
    return result

#print(generate_xiaohongshu("大模型","sk-2kMZkaS7hkySCft2Ea0e61Dc3e4641D2A47e1f1cD36886Fa"))

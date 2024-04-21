#Xiaohongshu这个类要继承BaseModel;后面会用到Feild函数给BaseModel里的属性提供额外的校验
from langchain_core.pydantic_v1 import BaseModel,Field
#list等复合类型从typing库中引入
from typing import List
class Xiaohongshu(BaseModel):
    titles:List[str] = Field(description="小红书的5个标题",min_items=5,max_items=5)
    content:str = Field(description="小红书的正文内容")
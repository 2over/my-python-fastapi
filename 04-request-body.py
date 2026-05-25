from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated
import uvicorn


class Item(BaseModel):
    """
    创建数据模型，把数据模型声明为继承BaseModel的类
    和查询参数一样，如果没有默认值就是必填属性
    """

    name: str = Field(description="商品名称")
    # 字符串类型约束长度要用max_length,int类型要用le、ge
    # 类型可以是str或None, 默认值是None
    description: str | None = Field(description="商品描述", max_length=100)
    price: float = Field(description="商品价格, 价格必须再0以上5000以下", ge=0, le=5000)
    tax: float | None = None


app = FastAPI()


# 使用与声明路径和查询参数相同的方式声明请求体，把请求体添加至路径操作
@app.post("/items")
async def create_item(item: Item):
    print(item)
    item_dict = item.model_dump() # 将对象字段转变为字典
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
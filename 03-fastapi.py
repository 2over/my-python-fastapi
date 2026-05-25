# from fastapi import FastAPI
# import uvicorn
#
# # 1.创建对象
# app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)


from enum import Enum
import uvicorn
from fastapi import FastAPI, Path, Query
from typing import Annotated


class ModelName(str, Enum):
    English = "英语"
    Chinese = "中文"
    French = "法语"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.English:
        return {"model_name": model_name, "message": "这是英文"}
    if model_name.value == "中文":
        return {"model_name": model_name, "message": "这是中文"}

    return {"model_name": model_name, "message": "这是法语"}


@app.get("/users/{id}")
async def get_user(
        id: Annotated[int, Path(description="用户id")]):
    return {"id": id, "message": f"这是用户id为{id}的人"}


fake_item_db = [{"item_name": "苹果"}, {"item_name": "香蕉"},
                {"item_name": "橙子"}, {"item_name": "笔记本电脑"},
                {"item_name": "无线鼠标"}, {"item_name": "蓝牙耳机"},
                {"item_name": "纯棉T恤"}, {"item_name": "休闲裤"}]


@app.get("/items/")
async def read_item(skip: int = 0,
                    limit: Annotated[int, Query(description="条数")] = 5):
    return fake_item_db[skip:skip + limit]


if __name__ == "__main__":
    uvicorn.run(app)
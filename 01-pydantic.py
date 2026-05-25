from pydantic import BaseModel



class User(BaseModel):
    name : str = "Coffee" # 如果有默认值就代表不是必填参数
    age: int

 

user = User(age="asdsada")

print(user)
from pydantic import BaseModel

BaseModel;

class NewStudent(BaseModel):
    name:str
    age:int
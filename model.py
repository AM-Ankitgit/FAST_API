from pydantic import BaseModel



class NewStudent(BaseModel):
    name:str
    age:int


class demoStudent(BaseModel):
    name:str
    age:int
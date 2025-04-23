from fastapi import FastAPI
from model import NewStudent

app  = FastAPI(title="CRUD Operation",description="this simple CRUD opeartion apis")


student = {
    1:{'name':'annu',
       'age':12
       }
    }




@app.get("/")
def home():
    return "welcome to home pages"

@app.get("/getdetails")
def getdetails():
    return student


# get name of the student by id

@app.get("/name/{stud_id}")
def get_name(stud_id:int):
    if stud_id not in student:
        return "this information not exit"
    
    name = student.get((stud_id)).get('name')
    return name


@app.post("/addStudent")
def add_student(stud: NewStudent):
    if not student:  # Check if database is empty
        id_ = 1
    else:
        id_ = max(student.keys()) + 1
    
    # Update database
    student[id_] = stud.model_dump()  # Convert Pydantic model to dictionary

    return {"id": id_, **student[id_]}


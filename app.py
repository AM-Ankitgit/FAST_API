from fastapi import FastAPI

app = FastAPI(title="this demo",description="this provide the detail apis")

student = {
    1:{'name':'annu',
       'age':12
       }
    }


@app.get("/")
def get_hellow():
    return "hello"

# @app.get("/detail/{id_std}")
@app.get("/name/{stud_id}")
def get_student_id(stud_id):
    return student.get(int(stud_id))



from model import demoStudent

@app.post("/update")
def update_detail(details:demoStudent):
    if student:
        id_ = max(student.keys())+1
        student[id_] = details.model_dump()
    else:
        id_=1
        student[id_] = details.model_dump()
    return {"id":id_,**student}


@app.put("/updateAll")
def get_update_all(details:demoStudent):
    return {"id":1,**student}

@app.patch("/updatePartial")
def get_partial_update(details:demoStudent):
    details.age=12
    return  details.model_dump()

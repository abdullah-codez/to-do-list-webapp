from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

task = {
    1: {"title":"Groceries", "description":"Eggs and Milk"}
}

class Task(BaseModel):
    title: str
    description: str

class EditedTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

@app.post("/post-task/{id}")
def post_task(id : int, new_task : Task):
    if id in task:
        return "ERROR: The Task already Exists...."
    task[id] = new_task.model_dump() #converts model instance to python dictionary
    return "Success!"

@app.get("/get-tasks")
def get_all():
    return task

  # Bug HERE PARTIAL UPDATE TO BE IMPLETED USING PATCH NOT PUT
  # put for complete update
@app.patch("/edit-task/{id}")
def edit_task(id:int,  new_task:EditedTask):
    if id not in task:
        return "No such task exists"
    
    if new_task.title is not None:
        task[id]["title"] = new_task.title

    if new_task.description is not None:
        task[id]["description"] = new_task.description

    return "Updated successfully"

@app.put("/complete-change/{id}")
def complete_ch(id:int, new_task:Task):
    if id not in task:
        return "No such task exists"
    task[id] = {
        "title": new_task.title,
        "description": new_task.description 
    }

@app.delete("/del-task/{id}")
def del_task(id:int):
    if id not in task:
        return "No such task exists"
    del task[id]
    return "Task deleted successfully"

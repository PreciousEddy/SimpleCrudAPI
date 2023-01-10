from fastapi import FastAPI
import mysql.connector
from fastapi.openapi.models import Response
from pydantic import BaseModel
from task import Task


mydb = mysql.connector.connect(host="localhost",username="root",password="",database="todo")

mycursor = mydb.cursor()


app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome to the To-do List API"}

tasks = [

        {"To_do":"",
        "Project_name":"",
        "state":"",
        "author_id":0},

         {"To_do":"Build",
         "Project_name":"Pushing a ACR",
          "state":"active",
          "author_id":114},

          {"To_do":"Push",
         "Project_name":"commiting the recent update",
          "state":"Done",
          "author_id":115},

          {"To_do":"Pull",
         "Project_name":"Pull the recent update",
          "state":"Done",
          "author_id":116},
          

          {"To_do":"Push to Repositories",
         "Project_name":"Updating Repositories",
          "state":"Done",
          "author_id":117},
          
          
          ]


#get all tasks
@app.get("/all_tasks")
def get_tasks():
    sql = "SELECT * FROM tasks"
    mycursor.execute(sql)
    tasks = mycursor.fetchall()
    return {"message":" All Task listed below📝"},tasks


#get single task
@app.get("/task/{task_id}")
def get_task(task_id:int):
    sql = "SELECT * FROM tasks WHERE task_id = %s"
    val = (task_id,)
    mycursor.execute(sql,val)
    task = mycursor.fetchall
    return {"message":" Here's the requested Task🔎"},tasks[0]


#get task by name
@app.get("/task_by_name/{task_name}")
def get_task_name(task_name:str):
    sql = "SELECT * FROM tasks WHERE To_do, project_name = %s"
    val = (To_do,)
    mycursor.execute(sql,val)
    movie = mycursor.fetchall()
    return {"message":" Here you go!!🔎"},tasks[0]




#Create a task
@app.post("/create_task")
def create_task(task:Task):
    sql = "INSERT INTO tasks(To_do,project_name,state,author_id) VALUES(%s,%s,%s,%s)"
    val = (task.To_do, task.project_name, task.state, task.author_id)
    mycursor.execute(sql,val)
    mydb.commit()
    return {"message":"New task created ⚒️👷"}, task


#update a task
@app.post("/update_task")
def update_task(task_id:int,task:Task):
    sql = "UPDATE tasks SET To_do =%s, project_name =%s, state =%s, author_id =%s WHERE id = %s"
    val =  (task.To_do, task.project_name, task.state, task.author_id)
    mycursor.execute(sql,val)
    mydb.commit()
    return {"message":" Tasks updated👌"}, task


#delete task
@app.delete("/task/{task_id}")
def delete_task(task_id:int):
    sql = "DELETE FROM tasks WHERE id = %s"
    val = (task_id,)
    mycursor.execute(sql,val)
    mydb.commit()
    return {"message":"Task has been deleted sucessfully👍"} 

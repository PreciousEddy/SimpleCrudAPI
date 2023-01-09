from fastapi import FastAPI
import mysql.connector


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
@app.get("/tasks")
def get_tasks():
    return tasks


#get single task
@app.get("/task/{task_id}")
def get_task(task_id:int):
    return tasks[task_id]


#delete task
@app.delete("/task/{task_id}")
def delete_task(task_id:int):
    tasks.pop(task)

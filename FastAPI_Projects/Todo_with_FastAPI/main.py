from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome to the To-do List API"}

tasks = [{"To_do":"Build","Project_name":"Pushing a ACR","state":"active","author_id":114}]

@app.get("/tasks")
def get_tasks():
    return tasks
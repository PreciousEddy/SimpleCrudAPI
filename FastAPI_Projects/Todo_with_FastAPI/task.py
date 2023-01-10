from pydantic import BaseModel

class Task(BaseModel):
    To_do: str
    project_name: str
    state: str
    author_id: int

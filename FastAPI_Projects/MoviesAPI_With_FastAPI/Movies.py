from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    title: str
    Year:int
    storyline: Optional[str] = None
from pydantic import BaseModel
from typing import Optional

class File_dto(BaseModel):
    filename: str
    id: Optional[str] = None
    url: Optional[str] = None
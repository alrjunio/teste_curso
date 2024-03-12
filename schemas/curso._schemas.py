import string
from typing import Optional
from pydantic import BaseModel as SCBaseModel


class CursoSchemas(SCBaseModel):
    id: Optional[int]
    titulo: string
    aulas: int
    horas: int


class Config: 
    orm_mode = True

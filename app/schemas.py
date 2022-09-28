from lib2to3.pgen2.token import OP
from operator import truediv
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


T = TypeVar('T')

class BookSchema(BaseModel):
    id: Optional[int]=None
    title: Optional[int]=None
    description: Optional[str]=None

    class Configs:
        orm_mode = True

class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
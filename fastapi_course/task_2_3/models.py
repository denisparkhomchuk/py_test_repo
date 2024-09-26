from typing import Union

from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int
    age: int
    is_adult: Union[bool, None]

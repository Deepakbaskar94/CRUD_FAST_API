# Schema class
from typing import Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    movie_name: str
    director: str
    geners: str
    cast: str


class MovieAdd(MovieBase):
    movie_id: int
    # Optional[str] is just a shorthand or alias for Union[str, None].
    streaming_platform: Optional[str] = None
    membership_required: bool

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class Movie(MovieAdd):
    id: int

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class UpdateMovie(BaseModel):
    # Optional[str] is just a shorthand or alias for Union[str, None].
    streaming_platform: Optional[str] = None
    membership_required: bool

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True

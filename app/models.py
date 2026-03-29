from pydantic import BaseModel, Field
from typing import Optional

class BookSchema(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    year: int = Field(..., gt=1400, lt=2027)
    genre: str = Field(...)
    is_read: bool = Field(default=False)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "year": 1925,
                "genre": "Classic Literature",
                "is_read": False
            }
        }

class UpdateBookModel(BaseModel):
    title: Optional[str]
    author: Optional[str]
    year: Optional[int]
    genre: Optional[str]
    is_read: Optional[bool]